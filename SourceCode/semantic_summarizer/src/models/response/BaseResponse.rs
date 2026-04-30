use serde::Serialize;

#[derive(Serialize, Debug)]
struct BaseResponse {
    success: bool,
    message: String
}