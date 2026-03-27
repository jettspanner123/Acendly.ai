

struct ServerConstants {
    pub server_port: i16,
    pub server_host: String,
    pub thread_flavour: String,
}

impl ServerConstants {

    pub fn new() -> Self {
        Self {
            server_port: 8080,
            server_host: "localhost".to_string(),
            thread_flavour: "current_thread".to_string()
        }
    }

    pub fn get_host() -> String {
        ServerConstants::new().server_host
    }

    pub fn get_port() -> i16 {
        ServerConstants::new().server_port
    }

    pub fn get_server_url() -> String {
        let var = ServerConstants::new();
        format!("{}:{}", var.server_host, var.server_port).to_string()
    }
}