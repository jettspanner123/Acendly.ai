use serde::Deserialize;

#[derive(Deserialize, Debug)]
pub struct AstParseRequest {
    pub source_code: String,
    pub language: String,
}
