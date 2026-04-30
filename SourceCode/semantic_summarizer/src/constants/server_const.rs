pub struct ServerConstants;

impl ServerConstants {
    pub const PORT: u16 = 8080;
    pub const HOST: &'static str = "localhost";

    pub fn get_server_url() -> String {
        format!("{}:{}", Self::HOST, Self::PORT)
    }
}
