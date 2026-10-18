# python function can return multiple values, the values returned in tuple format

def get_largest(x, y):
    if x > y:
        return x, y
    else:
        return y, x


result = get_largest(25, 45)
print(type(result))
print(result)

a, b = result  # unpacking of tuple
print(f'a = {a}, b = {b}')

(i, j) = result  # another way of unpacking of tuple
print(f'i = {i}, j = {j}')
