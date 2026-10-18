"""
map is in-build function with python
it takes two arguments - user defined function and iterable
map applies user defined function on each element in iterable (could be list, tuple, dict)
and returns new iterable
"""

import math

def find_sqaure_root(x):
    if type(x) == int:
        return int(math.sqrt(x))
    elif type(x) == list:
        for i in x:
            return int(math.sqrt(x[i]))


num_list = [9,16,25,36,49]

sqrt_list = list(map(find_sqaure_root,num_list))
print(sqrt_list)

random_num_sqrt_tuple = tuple(map(find_sqaure_root,(181,225,364,789)))
print(random_num_sqrt_tuple)