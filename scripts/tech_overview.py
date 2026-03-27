#!/usr/bin/env python3
"""
Script to scan project folders and print detected technologies, languages, frameworks, and libraries using rich.
"""
import os
import re
from pathlib import Path
from rich.console import Console
from rich.table import Table

FOLDERS = [
    "../coordinator",
    "../semantic_summarizer",
    "../vector_embedder"
]

console = Console()

def detect_dotnet(folder):
    csproj_files = list(Path(folder).glob("*.csproj"))
    if csproj_files:
        return {
            "Language": "C#",
            "Framework": ".NET",
            "Project File": csproj_files[0].name
        }
    return {}

def detect_python(folder):
    req = Path(folder) / "requirements.txt"
    if req.exists():
        with open(req) as f:
            libs = [line.strip() for line in f if line.strip() and not line.startswith("#")]
        return {
            "Language": "Python",
            "Framework": "(varies)",
            "Libraries": ", ".join(libs)
        }
    # Check for .py files as fallback
    py_files = list(Path(folder).rglob("*.py"))
    if py_files:
        return {
            "Language": "Python",
            "Framework": "(unknown)",
            "Libraries": "(unknown)"
        }
    return {}

def detect_rust(folder):
    toml = Path(folder) / "Cargo.toml"
    if toml.exists():
        with open(toml) as f:
            content = f.read()
        pkgs = re.findall(r"[\w-]+ = \"[\w\d\.-]+\"", content)
        pkgs = [p.split(" = ")[0] for p in pkgs]
        return {
            "Language": "Rust",
            "Framework": "Cargo",
            "Libraries": ", ".join(pkgs)
        }
    # Check for .rs files as fallback
    rs_files = list(Path(folder).rglob("*.rs"))
    if rs_files:
        return {
            "Language": "Rust",
            "Framework": "(unknown)",
            "Libraries": "(unknown)"
        }
    return {}

def scan_folder(folder):
    info = {}
    info.update(detect_dotnet(folder))
    info.update(detect_python(folder))
    info.update(detect_rust(folder))
    return info

def main():
    table = Table(title="Project Technology Overview")
    table.add_column("Folder", style="cyan", no_wrap=True)
    table.add_column("Language", style="magenta")
    table.add_column("Framework", style="green")
    table.add_column("Libraries / Details", style="yellow")
    for folder in FOLDERS:
        abs_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), folder))
        info = scan_folder(abs_folder)
        table.add_row(
            os.path.basename(abs_folder),
            info.get("Language", "-"),
            info.get("Framework", "-"),
            info.get("Libraries", info.get("Project File", "-"))
        )
    console.print(table)

if __name__ == "__main__":
    main()

