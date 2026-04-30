use serde::Serialize;

#[derive(Serialize, Debug, Clone)]
pub struct SourcePosition {
    pub line: usize,
    pub column: usize,
}

#[derive(Serialize, Debug, Clone)]
pub struct SourceLocation {
    pub start: SourcePosition,
    pub end: SourcePosition,
}

#[derive(Serialize, Debug, Clone)]
pub struct AstNode {
    pub id: String,

    #[serde(rename = "type")]
    pub node_type: String,

    #[serde(skip_serializing_if = "Option::is_none")]
    pub name: Option<String>,

    #[serde(skip_serializing_if = "Option::is_none")]
    pub operator: Option<String>,

    #[serde(skip_serializing_if = "Option::is_none")]
    pub value: Option<String>,

    #[serde(skip_serializing_if = "Option::is_none")]
    pub children: Option<Vec<AstNode>>,

    #[serde(skip_serializing_if = "Option::is_none")]
    pub loc: Option<SourceLocation>,

    #[serde(skip_serializing_if = "Option::is_none")]
    pub parent_id: Option<String>,
}
