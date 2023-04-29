from graphviz import Digraph
import ast

# def my_function(x, y):
#     z = x + y
#     return z

code = """
def my_function(x, y):
    z = x + y
    return z
"""

tree = ast.parse(code)
print(tree)



# You can now traverse the AST to extract information about the function
