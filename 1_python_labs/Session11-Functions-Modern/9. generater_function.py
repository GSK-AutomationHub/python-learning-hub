"""
function make use of 'yield' keyword and act as iterator
it could have multiple yield statements
function returns value insequence one at a time
it uses next(itr) to print value return by function
"""

def sample_gen(x):
    print(type(x))
    if type(x) == int:
        for i in range(x):
            yield i
    elif type(x) == list:
        for i in range(len(x)):
            yield x[i]

x = [9,16,25,36,49]
sg = sample_gen(x)
print(next(sg))
print(next(sg))
print(next(sg))

for i in sample_gen(10):
    print(i)
