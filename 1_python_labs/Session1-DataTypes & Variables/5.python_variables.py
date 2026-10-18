# multiple variable assignment in single line
x, y, z = 'Aditya', 100, ['software developer', 'infosys', 'pune-hinjewadi']
print(x, y, z)

# assigning single value to multiple variables
# a,b,c = 10000 ---> incorrect way of multiple variable assignment with single value
a = b = c = 100000 # this is correct way
print(a, b, c)

# variable reassignment
p = 100
print(p)
p = 'test passed'
print(p)

# variable exchange / swapping
i, j = 100, 300
print(i, j)
i, j = j, i  # variable value swapping
print(i, j)
