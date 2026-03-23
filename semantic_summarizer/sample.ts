
type ID = string;

interface User {
  id: ID;
  name: string;
  email: string;
  roles: Role[];
  metadata: Record<string, unknown>;
}

interface Role {
  name: string;
  permissions: Permission[];
}

interface Permission {
  resource: string;
  action: "read" | "write" | "delete";
}

interface Repository<T> {
  findById(id: ID): Promise<T | null>;
  save(entity: T): Promise<void>;
  delete(id: ID): Promise<void>;
}

class InMemoryRepository<T extends { id: ID }> implements Repository<T> {
  private store = new Map<ID, T>();

  async findById(id: ID): Promise<T | null> {
    return this.store.get(id) ?? null;
  }

  async save(entity: T): Promise<void> {
    this.store.set(entity.id, entity);
  }

  async delete(id: ID): Promise<void> {
    this.store.delete(id);
  }
}

class UserService {
  constructor(private repo: Repository<User>) {}

  async create(user: User): Promise<void> {
    await this.repo.save(user);
  }

  async getUserPermissions(userId: ID): Promise<Set<string>> {
    const user = await this.repo.findById(userId);
    if (!user) throw new Error("User not found");

    const permissions = new Set<string>();

    for (const role of user.roles) {
      for (const perm of role.permissions) {
        permissions.add(`${perm.resource}:${perm.action}`);
      }
    }

    return permissions;
  }

  async hasPermission(userId: ID, resource: string, action: string): Promise<boolean> {
    const perms = await this.getUserPermissions(userId);
    return perms.has(`${resource}:${action}`);
  }
}

type Event =
  | { type: "USER_CREATED"; payload: User }
  | { type: "USER_DELETED"; payload: { id: ID } }
  | { type: "USER_UPDATED"; payload: User };

class EventBus {
  private handlers: { [K in Event["type"]]?: ((event: Extract<Event, { type: K }>) => void)[] } = {};

  subscribe<K extends Event["type"]>(
    type: K,
    handler: (event: Extract<Event, { type: K }>) => void
  ): void {
    if (!this.handlers[type]) {
      this.handlers[type] = [];
    }
    this.handlers[type]!.push(handler as any);
  }

  publish(event: Event): void {
    const handlers = this.handlers[event.type];
    if (handlers) {
      for (const handler of handlers) {
        handler(event as any);
      }
    }
  }
}

class Cache<K, V> {
  private cache = new Map<K, { value: V; expiresAt: number }>();

  constructor(private ttl: number) {}

  set(key: K, value: V): void {
    this.cache.set(key, {
      value,
      expiresAt: Date.now() + this.ttl,
    });
  }

  get(key: K): V | null {
    const entry = this.cache.get(key);
    if (!entry) return null;

    if (Date.now() > entry.expiresAt) {
      this.cache.delete(key);
      return null;
    }

    return entry.value;
  }
}

class AuthService {
  constructor(private userService: UserService, private cache: Cache<ID, Set<string>>) {}

  async authorize(userId: ID, resource: string, action: string): Promise<boolean> {
    let perms = this.cache.get(userId);

    if (!perms) {
      perms = await this.userService.getUserPermissions(userId);
      this.cache.set(userId, perms);
    }

    return perms.has(`${resource}:${action}`);
  }
}

const repo = new InMemoryRepository<User>();
const userService = new UserService(repo);
const cache = new Cache<ID, Set<string>>(5000);
const authService = new AuthService(userService, cache);
const eventBus = new EventBus();

eventBus.subscribe("USER_CREATED", async (event) => {
  await userService.create(event.payload);
});

eventBus.subscribe("USER_DELETED", async (event) => {
  await repo.delete(event.payload.id);
});

(async () => {
  const user: User = {
    id: "1",
    name: "Alice",
    email: "alice@example.com",
    metadata: {},
    roles: [
      {
        name: "admin",
        permissions: [
          { resource: "file", action: "read" },
          { resource: "file", action: "write" },
          { resource: "user", action: "delete" },
        ],
      },
    ],
  };

  eventBus.publish({ type: "USER_CREATED", payload: user });

  const canWrite = await authService.authorize("1", "file", "write");
  const canDelete = await authService.authorize("1", "user", "delete");

  console.log(canWrite, canDelete);
})();