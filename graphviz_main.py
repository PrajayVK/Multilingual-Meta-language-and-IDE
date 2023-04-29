from graphviz import Digraph
import ast

class AstGraphVisualizer(ast.NodeVisitor):
    def __init__(self):
        self.graph = Digraph()
        self.parent = None

    def visit(self, node):
        # Get node name and label
        node_name = str(id(node))
        node_label = node.__class__.__name__

        # Add node to graph
        self.graph.node(node_name, node_label)

        # Add edge from parent node, if applicable
        if self.parent is not None:
            self.graph.edge(str(id(self.parent)), node_name)

        # Set current node as parent for next visit
        self.parent = node

        # Call the visit method of the superclass to visit child nodes
        super().visit(node)

    def view(self):
        return self.graph.view()

code = """
def complex_function(a, b, c):
    x = a * b
    y = b * c
    if x > y:
        z = a + b + c
    else:
        z = a - b - c
    return z
"""

tree = ast.parse(code)
visualizer = AstGraphVisualizer()
visualizer.visit(tree)
visualizer.view()
