mod abstract_syntax_tree;
mod summarizer;

use std::env;
use std::fs;

fn main() {
    let args: Vec<String> = env::args().collect();
    if args.len() < 2 {
        eprintln!("Usage: {} <file_path>", args[0]);
        std::process::exit(1);
    }

    let file_path = &args[1];
    let content = match fs::read_to_string(file_path) {
        Ok(c) => c,
        Err(e) => {
            eprintln!("Error reading file {}: {}", file_path, e);
            std::process::exit(1);
        }
    };

    let source_bytes = content.as_bytes();

    // 1. Convert raw code to AST
    let tree = abstract_syntax_tree::parse_to_ast(&content);

    // 2. Print AST
    println!("Abstract Syntax Tree for: {}", file_path);
    println!("========================================");
    abstract_syntax_tree::print_ast(&tree, source_bytes);
    println!("\n");

    // 3. Convert AST to Semantic Summary
    let summary = summarizer::generate_summary(tree.root_node(), source_bytes);

    // 4. Print Semantic Summary
    println!("Semantic Summary for: {}", file_path);
    println!("========================================");
    println!("{}", summary);
}
