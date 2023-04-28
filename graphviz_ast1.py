import ast
from graphviz import Digraph

# Define the Python code snippet to visualize
code = """
a = 3
b = 4
c = add(a, b)
print(c)
"""

# Parse the code into an Abstract Syntax Tree (AST)
tree = ast.parse(code)

# Create a Graphviz Digraph object
dot = Digraph()

# Define a function to recursively traverse the AST and create nodes and edges
def visit(node):
    if isinstance(node, ast.Assign):
        for target in node.targets:
            dot.node(target.id, label=target.id)
            dot.edge(target.id, visit(node.value))
        return target.id
    elif isinstance(node, ast.BinOp):
        dot.node(str(node.lineno), label=type(node).__name__)
        left = visit(node.left)
        right = visit(node.right)
        if left and right:
            dot.edge(left, str(node.lineno))
            dot.edge(right, str(node.lineno))
        return str(node.lineno)
    elif isinstance(node, ast.Name):
        dot.node(node.id, label=node.id)
        return node.id
    elif isinstance(node, ast.Num):
        dot.node(str(node.n), label=str(node.n))
        return str(node.n)
    elif isinstance(node, ast.Expr):
        return visit(node.value)
    elif isinstance(node, ast.Module):
        for stmt in node.body:
            visit(stmt)
    elif isinstance(node, ast.Call):
        func_name = visit(node.func)
        for arg in node.args:
            arg_name = visit(arg)
            dot.edge(arg_name, func_name)
        return func_name
    else:
        raise Exception('No visitor method for ' + node.__class__.__name__)

# Traverse the AST and create nodes and edges
visit(tree)

# Render the graph as a PDF file
dot.render('ast_graph', format='pdf')
