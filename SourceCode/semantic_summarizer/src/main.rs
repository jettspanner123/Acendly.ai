mod controllers;
mod services;
mod constants;
mod models;
mod helpers;

use std::sync::Arc;
use axum::Router;

use controllers::ast_controller::{ast_router, AppState};
use constants::server_const::ServerConstants;
use services::ast_service::ASTService;

#[tokio::main(flavor = "current_thread")]
async fn main() {
    let state = Arc::new(AppState {
        ast_service: ASTService::new(),
    });

    let app: Router = ast_router(state);

    let addr = ServerConstants::get_server_url();
    println!("🚀 semantic_summarizer running on http://{}", addr);

    let listener = tokio::net::TcpListener::bind(&addr)
        .await
        .expect("Failed to bind to address");

    axum::serve(listener, app.into_make_service())
        .await
        .expect("Server error");
}
