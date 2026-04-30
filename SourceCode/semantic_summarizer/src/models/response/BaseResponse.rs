use serde::Serialize;

#[derive(Serialize, Debug)]
pub struct BaseResponse {
    pub success: bool,
    pub message: String,
}