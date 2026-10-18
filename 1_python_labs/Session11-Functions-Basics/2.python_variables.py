''' There are two types of variable in python - global & local variables
global variable
- usually created outside function
- scope is global, i.e. can be accessed inside, outside function within class

local variable
- created inside function
- scope is local, i.e. only can be accessed inside function
'''

print("# Example1 - global, local variable illustration")
x = 100  # global variable

def func():
    y = 50  # local variable
    print(f'from inside function- x={x}, y={y}')  # global variable can be accessed inside function

func()
print(f'global variable {x} can also printed outside function')
try:
    print(y)
except Exception as e:
    print('error message for local variable when printed outside function is- ', e)

print("-----------------------------------------------------------------------------")

print("# Example2 - global variable can be modified inside function")
x = 100  # global variable

def func():
    global x  # to address global variable inside function before editing,
    x = 200   # assigning new value, Note- global x = 200 is Invalid expression in python
    y = 50  # local variable
    print(f'from inside function- x={x}, y={y}')  # global variable can be accessed inside function

print(f'global variable {x} before function call - prints origianl value')
func()
print(f'global variable {x} after function call - prints modified value')

print("-----------------------------------------------------------------------------")

print("# Example3 - global variable can also be declared inside function")
print("no global variable defined outside function")
def func():
    global x  # to declare global variable inside function,
    x = 500   # assigned value, Note- global x = 500 is Invalid expression in python
    y = 50  # local variable
    print(f'from inside function- x={x}, y={y}')  # global variable can be accessed inside function

func()
print(f'global variable {x} after function call - prints defined global value')
