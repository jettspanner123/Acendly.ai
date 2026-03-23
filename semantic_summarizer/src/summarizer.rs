use tree_sitter::Node;

pub fn generate_summary(root_node: Node, source: &[u8]) -> String {
    let mut summary = String::new();
    extract_semantics(root_node, source, false, &mut summary);
    summary
}

fn extract_semantics(node: Node, source: &[u8], inside_class: bool, summary: &mut String) {
    let kind = node.kind();
    
    let mut is_class_context = inside_class;
    let mut should_print = false;
    let mut prefix = "";

    match kind {
        "comment" => {
            should_print = true;
        }
        // Identifies major structural blocks like classes and interfaces
        "class_declaration" | "interface_declaration" | "function_declaration" | "type_alias_declaration" => {
            should_print = true;
            if kind == "class_declaration" || kind == "interface_declaration" {
                is_class_context = true;
            }
        }
        // Identifies internal members for classed/interfaces
        "method_definition" | "method_signature" | "public_field_definition" | "property_signature" => {
            should_print = true;
            prefix = "  - ";
        }
        _ => {}
    }

    if should_print {
        if let Ok(text) = node.utf8_text(source) {
            // Comments can be multiline, append as is
            if kind == "comment" {
                summary.push_str(text);
                summary.push('\n');
            } else {
                // Otherwise only grab the signature part (typically first line)
                if let Some(first_line) = text.lines().next() {
                    let mut sig = first_line.trim_end();
                    // Strip trailing braces
                    if sig.ends_with('{') {
                        sig = sig[..sig.len()-1].trim_end();
                    }
                    summary.push_str(prefix);
                    summary.push_str(sig);
                    summary.push('\n');
                }
            }
        }
        
        // For structured blocks, recurse explicitly to pull out member fields
        if kind != "comment" {
            let mut cursor = node.walk();
            for child in node.children(&mut cursor) {
                if kind == "class_declaration" || kind == "interface_declaration" {
                    extract_semantics(child, source, is_class_context, summary);
                }
            }
        }
    } else {
        // Continue searching AST if no match found at this layer
        let mut cursor = node.walk();
        for child in node.children(&mut cursor) {
            extract_semantics(child, source, is_class_context, summary);
        }
    }
}
