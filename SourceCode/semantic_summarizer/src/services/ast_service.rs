use crate::helpers::ASTServiceHelper::{build_ast_node, extract_chunks, parse_to_ast};
use crate::models::request::AstParseRequest::AstParseRequest;
use crate::models::response::AstParseResponse::{AstParseResponse, AstTransferPayload};
use crate::constants::ast_const::AstConstants;

pub struct ASTService {}

impl ASTService {
    pub fn new() -> Self {
        Self {}
    }

    pub fn parse(&self, request: AstParseRequest) -> AstParseResponse {
        let tree = parse_to_ast(&request.source_code);

        if tree.root_node().has_error() {
            return AstParseResponse {
                success: false,
                message: "Source code contains syntax errors and could not be fully parsed.".to_string(),
                summary: None,
            };
        }

        let source_bytes = request.source_code.as_bytes();
        let ast_node = build_ast_node(&tree, source_bytes);
        let chunks = extract_chunks(&ast_node);

        let payload = AstTransferPayload {
            language: request.language,
            version: AstConstants::SCHEMA_VERSION.to_string(),
            ast: ast_node,
            chunks,
        };

        AstParseResponse {
            success: true,
            message: "AST parsed successfully.".to_string(),
            summary: Some(payload),
        }
    }
}
