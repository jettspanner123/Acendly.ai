use axum::{extract::State, routing::post, Json, Router};
use std::sync::Arc;

use crate::constants::ast_const::AstConstants;
use crate::models::request::AstParseRequest::AstParseRequest;
use crate::models::response::AstParseResponse::AstParseResponse;
use crate::services::ast_service::ASTService;

/// Shared application state holding the service instance.
pub struct AppState {
    pub ast_service: ASTService,
}

/// Build and return the AST router.
pub fn ast_router(state: Arc<AppState>) -> Router {
    Router::new()
        .route(AstConstants::PARSE_ROUTE, post(parse_handler))
        .with_state(state)
}

/// POST /ast/parse
/// Accepts source code and returns a structured AST with semantic chunks.
async fn parse_handler(
    State(state): State<Arc<AppState>>,
    Json(request): Json<AstParseRequest>,
) -> Json<AstParseResponse> {
    let response = state.ast_service.parse(request);
    Json(response)
}
