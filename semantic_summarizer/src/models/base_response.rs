use serde::Serialize;

#[derive(Serialize)]
pub struct BaseResponse {
    success: bool,
    message: String
}