
import ast

def nunu(a,b):
    c=a+b
    return c
tree = ast.parse("def greet(name):\n    return name")

print(tree)