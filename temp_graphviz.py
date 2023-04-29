import ast
from graphviz import Digraph

code = "a=3"

def analyze_code(code):
    tree = ast.parse(code)
    graph = Digraph()

    def visit(node):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                graph.node(target.id, label=target.id)
                graph.edge(target.id, visit(node.value))
        elif isinstance(node, ast.Expr):
            return visit(node.value)
        elif isinstance(node, ast.BinOp):
            left = visit(node.left)
            right = visit(node.right)
            op = type(node.op).__name__
            op_node = '_'.join([op, str(node.lineno), str(node.col_offset)])
            graph.node(op_node, label=op)
            graph.edge(left, op_node)
            graph.edge(right, op_node)
            return op_node
        elif isinstance(node, ast.Name):
            return node.id
        elif isinstance(node, ast.Constant):
            return str(node.value)
        else:
            raise Exception('No visitor method for ' + node.__class__.__name__)

    for stmt in tree.body:
        visit(stmt)

    return graph
