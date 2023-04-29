import ast
import os
import sys
from graphviz import Digraph


def visualize_code_execution(code):
    graph = Digraph('Execution Flow', filename='execution_flow.gv')
    graph.attr(rankdir='LR')
    node_id = 0

    # Add initial node
    graph.node(str(node_id), 'Start', shape='oval')
    node_id += 1

    # Parse the code into an abstract syntax tree
    code_ast = ast.parse(code)

    # Traverse the abstract syntax tree and add nodes for each line of code
    for node in ast.walk(code_ast):
        if isinstance(node, ast.AST):
            if hasattr(node, 'lineno'):
                source_code = f'{node.lineno}: {ast.dump(node)}'
                graph.node(str(node_id), source_code, shape='box')
                graph.edge(str(node_id - 1), str(node_id))
                node_id += 1

    # Add final node
    graph.node(str(node_id), 'End', shape='oval')
    graph.edge(str(node_id - 1), str(node_id))

    # Save the graph to a file and open it
    graph.render(view=True)


if __name__ == '__main__':
    code_to_visualize = """
    x = 1
    y = 2
    z = x + y
    print(z)
    """
    visualize_code_execution(code_to_visualize)
