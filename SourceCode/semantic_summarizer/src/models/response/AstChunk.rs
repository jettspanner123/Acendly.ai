use serde::Serialize;

#[derive(Serialize, Debug, Clone)]
#[serde(rename_all = "lowercase")]
pub enum AstChunkType {
    Function,
    Class,
    Statement,
    Expression,
}

#[derive(Serialize, Debug, Clone)]
pub struct AstChunk {
    pub id: String,

    #[serde(rename = "type")]
    pub chunk_type: AstChunkType,

    #[serde(skip_serializing_if = "Option::is_none")]
    pub name: Option<String>,

    /// Human-readable description of what this chunk does, used for embedding
    pub text: String,

    pub ast_node_id: String,
}
