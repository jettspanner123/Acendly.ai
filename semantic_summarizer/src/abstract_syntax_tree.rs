use tree_sitter::{Node, Parser, Tree};

pub fn parse_to_ast(content: &str) -> Tree {
    let mut parser = Parser::new();
    let language = tree_sitter_typescript::LANGUAGE_TYPESCRIPT.into();
    parser.set_language(&language).expect("Error loading TypeScript grammar");

    parser.parse(content, None).expect("Error parsing file")
}

pub fn print_ast(tree: &Tree, source: &[u8]) {
    let root_node = tree.root_node();
    walk_and_print_ast(root_node, source, 0);
}

fn walk_and_print_ast(node: Node, source: &[u8], depth: usize) {
    let indent = "  ".repeat(depth);
    let kind = node.kind();
    
    // If it's a leaf node, print its contents
    if node.child_count() == 0 {
        if let Ok(text) = node.utf8_text(source) {
            let short_text = text.lines().next().unwrap_or("").trim();
            println!("{}{} => {:?}", indent, kind, short_text);
        } else {
            println!("{}{}", indent, kind);
        }
    } else {
        println!("{}{}", indent, kind);
        let mut cursor = node.walk();
        for child in node.children(&mut cursor) {
            // is_named filters out punctuation such as '{', '}'
            if child.is_named() {
                walk_and_print_ast(child, source, depth + 1);
            }
        }
    }
}
