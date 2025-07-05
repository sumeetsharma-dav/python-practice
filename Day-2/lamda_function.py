"""
Lambda Functions : Useful for small one-line functions
Syntax:
lambda arguments: expression
Anonymous (no name) functions
"""
# Lets create a simpe add lambda fucntion
add = lambda a,b : a + b
print(add(5,5))
# Square
square = lambda a : a*a
print(square(8))
contains_a = lambda s : "a" in s
print(contains_a("pple"))
# Last character
last_char = lambda s: s[-1]
print(last_char("hello"))

# Return maximum of two numbers
r_max = lambda a,b: max(a,b)
print(r_max(5,10))
