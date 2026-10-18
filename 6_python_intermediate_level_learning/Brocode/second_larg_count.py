x = [1,2,1,3,1,3,5,4,5,5,5,5,5,5,5,5,5,1,6,6,6,6,6,6,6,6,3,3,3,3,3,3,3,3,3,3,3,3]

from collections import Counter

x_count = dict(Counter(x))
x_count_values = list(x_count.values())
x_count_values.sort()
x_count_values.pop()
x_count_values_2nd_max_count = max(x_count_values)

for key, value in x_count.items():
    if value == x_count_values_2nd_max_count:
        print (f"second large count is {key} : {value}")