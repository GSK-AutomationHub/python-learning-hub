"""
function which do not have any name, it uses lambda keyword before parameters
it can take any no of arguments, but it can have only one expression
It uses : to separate function param & expressions
lambda function do not use return keyword as return happens implicitly on function call
"""

result = lambda x, y, z : (x * y) + z

print(result(3,5, 9))

colors = ["orange", "red", "white", "blue", "green"]

print("--------------- approach-1 ----------------------")
# Using a for loop with a lambda function to print each item
for color in colors:
  (lambda x: print(x))(color)

print("--------------- approach-2 ----------------------")
# Equivalent using map (more common for applying a function to each element)
list(map(lambda x: print(x), colors))