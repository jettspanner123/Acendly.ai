pub struct AstConstants;

impl AstConstants {
    /// Schema version for the AST transfer payload
    pub const SCHEMA_VERSION: &'static str = "1.0.0";

    /// Route for the AST parse endpoint
    pub const PARSE_ROUTE: &'static str = "/ast/parse";
}
