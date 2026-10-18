
numbers = [3,5,7,9,12]

def gen_cube(num_itr):
    for num in numbers:
        yield num ** 3

cube = gen_cube(numbers)
print(next(cube))
print(next(cube))
print(next(cube))

# for cube in gen_cube(numbers):
#     print(cube)