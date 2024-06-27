import re
import antlr4
import argparse
from antlr4.tree.Tree import ParseTreeWalker, ParseTreeListener
from dafny_grammar.dafnyParser import dafnyParser
from dafny_grammar.dafnyLexer import dafnyLexer
import difflib


# Listener class to collect components in the tree
class ComponentListener(ParseTreeListener):
    def __init__(self):
        self.methods = []
        self.functions = []
        self.classes = []

    # Override the enter methods for method, function and class declarations
    def enterMethodDecl(self, ctx):
        method_name_child = ctx.methodSignatureDecl().getChild(1)
        if isinstance(method_name_child, dafnyParser.IdentifierContext):
            method_name = method_name_child.getText()
        elif isinstance(method_name_child, dafnyParser.UpperIdentifierContext):
            method_name = method_name_child.getText()
        else:
            method_name = "unknown"
        self.methods.append((method_name, ctx))

    def enterFunctionDecl(self, ctx):
        function_name = ctx.functionSignatureDecl().getChild(1).getText()
        self.functions.append((function_name, ctx))

    def enterClassDecl(self, ctx):
        class_name = ctx.getChild(1).getText()
        self.classes.append((class_name, ctx))

    def get_components(self):
        return {
            "method": self.methods,
            "function": self.functions,
            "class": self.classes,
        }


# Function to get the components in the tree
def get_components(tree):
    listener = ComponentListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
    return listener.get_components()


# Function to collect identifiers in the tree
def collect_identifiers(tree):
    identifier_mapping = {}
    current_var = 1
    current_func = 1
    current_meth = 1
    current_class = 1

    keywords = {"var", "function", "class", "method"}

    # Helper function to determine the type of upper identifier
    def determine_upper_identifier_type(node):
        parent = node.parentCtx
        if isinstance(parent, dafnyParser.MethodDeclContext):
            return "method"
        elif isinstance(parent, dafnyParser.FunctionDeclContext):
            return "function"
        elif isinstance(parent, dafnyParser.ClassDeclContext):
            return "class"
        return None

    # Helper function to collect identifiers
    def collect(node):
        nonlocal current_var, current_func, current_meth, current_class
        if isinstance(node, antlr4.tree.Tree.TerminalNodeImpl):
            text = node.getText()
            if re.match(r'^[a-zA-Z_][a-zA-Z_0-9]*$', text) and text not in keywords:
                if isinstance(node.parentCtx, dafnyParser.IdentifierContext):
                    if text not in identifier_mapping:
                        identifier_mapping[text] = {'type': 'variable', 'anonymized': f'var{current_var}'}
                        current_var += 1
                elif isinstance(node.parentCtx, dafnyParser.UpperIdentifierContext):
                    identifier_type = determine_upper_identifier_type(node.parentCtx)
                    if identifier_type == "method":
                        if text not in identifier_mapping:
                            identifier_mapping[text] = {'type': 'method', 'anonymized': f'method{current_meth}'}
                            current_meth += 1
                    elif identifier_type == "function":
                        if text not in identifier_mapping:
                            identifier_mapping[text] = {'type': 'function', 'anonymized': f'func{current_func}'}
                            current_func += 1
                    elif identifier_type == "class":
                        if text not in identifier_mapping:
                            identifier_mapping[text] = {'type': 'class', 'anonymized': f'class{current_class}'}
                            current_class += 1
        else:
            # check if NoneType to prevent error
            if node.children is None:
                return
            for child in node.children:
                collect(child)

    collect(tree)
    return identifier_mapping


# Function to anonymize the names in the tree
def anonymize_names(tree, identifier_mapping):
    # Helper function to replace identifiers
    def replace_identifiers(node):
        if isinstance(node, antlr4.tree.Tree.TerminalNodeImpl):
            text = node.getText()
            if text in identifier_mapping:
                node.symbol.text = identifier_mapping[text]['anonymized']
        else:
            # check if NoneType to prevent error
            if node.children is None:
                return
            for child in node.children:
                replace_identifiers(child)

    replace_identifiers(tree)
    return tree


# Function to generate the canonical form of a subtree
def generate_canonical_form(subtree):
    identifier_mapping = collect_identifiers(subtree)
    anonymized_tree = anonymize_names(subtree, identifier_mapping)
    return anonymized_tree.toStringTree(), identifier_mapping


# Function to normalize the whitespace in the canonical form
def normalize_whitespace(canonical_form):
    return re.sub(r'\s+', '', canonical_form)


# Function to compare two subtrees
def compare_subtrees(subtree1, subtree2):
    canonical_form1, mapping1 = generate_canonical_form(subtree1)
    canonical_form2, mapping2 = generate_canonical_form(subtree2)

    # print("\nNormalized canonical form of tree 1:")
    # print(canonical_form1)
    # print("\n\nNormalized canonical form of tree 2:")
    # print(canonical_form2)

    matcher = difflib.SequenceMatcher(None, canonical_form1, canonical_form2)
    return matcher.ratio(), mapping1, mapping2


# Function to analyze similarity between components in the program
def analyze_similarity(components):
    if components is None:
        print("No components found in the program.")
        return

    for component_type, subtrees in components.items():
        if subtrees is None:
            print(f"No {component_type}s found in the program.")
            continue

        print(f"\nAnalyzing {component_type}...")

        # Collect the names and subtrees separately
        names = [name for name, _ in subtrees]
        trees = [subtree for _, subtree in subtrees]

        for i in range(len(trees)):
            for j in range(i + 1, len(trees)):
                subtree1 = trees[i]
                subtree2 = trees[j]
                similarity_score, mapping1, mapping2 = compare_subtrees(subtree1, subtree2)
                if similarity_score > 0:
                    print(
                        f"\n\nSimilarity score between {component_type} '{names[i]}' and {component_type} '{names[j]}' : {similarity_score}")


# Function to print the tree structure
def print_tree(node, indent=""):
    if isinstance(node, antlr4.tree.Tree.TerminalNodeImpl):
        print(indent + node.getText())
    else:
        print(indent + dafnyParser.ruleNames[node.getRuleIndex()])
        for child in node.children:
            print_tree(child, indent + "  ")


# Main function to run the program
def main():
    parser = argparse.ArgumentParser(description='Analyze similarity in Dafny programs.')
    parser.add_argument('file_path', type=str, help='Path to the Dafny source file')
    args = parser.parse_args()

    input_stream = antlr4.FileStream(args.file_path)
    lexer = dafnyLexer(input_stream)
    stream = antlr4.CommonTokenStream(lexer)
    parser = dafnyParser(stream)
    tree = parser.program()

    # print the tree structure
    # print_tree(tree)

    components = get_components(tree)

    if components is not None:
        for component_type, subtrees in components.items():
            print(f"\n {component_type}s:")
            for name, subtree in subtrees:
                print(f"{name}")

    analyze_similarity(components)


# Run the main function if the script is run directly
if __name__ == "__main__":
    main()
