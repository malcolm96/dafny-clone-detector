# Dafny Program Analyzer

This project is a Python application that analyzes Dafny programs for similarity in their components. It uses the ANTLR4 parser generator to parse Dafny source code and analyze the resulting parse tree.

Please be aware that this program is currently in the early stages of development, and its accuracy may vary. The grammar file is included in the repository, and you are welcome to modify it for improved coherence.

## Features

- Collects components (methods, functions, classes) in the parse tree
- Generates a canonical form of a subtree by anonymizing the names
- Compares two subtrees for similarity
- Analyzes similarity between components in the program

## Requirements

- Python 3
- ANTLR4 Python runtime

## Usage

1. Clone the repository:

```bash
git clone https://github.com/malcolm96/dafny-program-analyzer.git
cd dafny-program-analyzer

