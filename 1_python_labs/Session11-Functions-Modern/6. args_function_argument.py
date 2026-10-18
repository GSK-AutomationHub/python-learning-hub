"""
• *args can be used as dynamic function parameter to pass any no of positional arguments to the function

• Similarly if any function takes multiple arguments then that can be passed to function using *args list

• Function using *args if have return statement, then returns type is always Tuple

"""

def sample_one(*args):
    print(type(args))
    for i in args:
        print(i, end="   ")
    print()

sample_one("orange", "red", "white", "blue", "green")
sample_one(12, 14, 15, 17, 21, 24)

print("---------------------------------------------------------------")
def sample_two(a, b, c, d, e):
    print(type(args))
    sum =  a + b + c + d + e
    return a, b, c, d, e, sum

args = [3, 5, 7, 9, 12]

result = sample_two(*args)
print(type(result), result)