import ast

code = """
a = 3
b = 4
c = a + b
print(c)
"""

tree = ast.parse(code)
print(ast.dump(tree))
import ast

code = """
a = 3
b = 4
c = a + b
print(c)
"""

tree = ast.parse(code)
print(ast.dump(tree))
