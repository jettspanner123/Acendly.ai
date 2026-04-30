#!/bin/bash

BASE_URL="/Users/jettspanner123/RustDevelopment/acendly-nexus-runtime/SourceCode"

APPS=("Rider" "RustRover" "PyCharm")

for app in "${APPS[@]}"; do
    if ! osascript -e "id of application \"$app\"" &>/dev/null; then
        echo "🚫 Bro, '$app' isn't even installed on this machine. Fix that first, then come back."
        exit 1
    fi
done

open -a "Rider" "$BASE_URL/coordinator"
echo "✅ Rider opened with coordinator project."

open -a "RustRover" "$BASE_URL/semantic_summarizer"
echo "✅ RustRover opened with semantic_summarizer project."

open -a "PyCharm" "$BASE_URL/vector_embedder"
echo "✅ PyCharm opened with vector_embedder project."
