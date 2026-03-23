from fastapi import Request
from stores.RootApplicationStore import RootApplicationStore

APPLICATION = RootApplicationStore.APPLICATION
TARGET_PATH = "/embedding"

class EmbeddingEventMiddleware:
    @staticmethod
    @APPLICATION.middleware("http")
    async def log_embedding_events(request: Request, call_next):
        if request.url.path.startswith(TARGET_PATH):
            pass
