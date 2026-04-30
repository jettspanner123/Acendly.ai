use crate::services::ast_service::ASTService;
pub struct ASTController {
    ast_service: ASTService,
}

impl ASTController {
    pub fn new(ast_service: ASTService) -> Self {
        Self {
            ast_service
        }
    }
}

