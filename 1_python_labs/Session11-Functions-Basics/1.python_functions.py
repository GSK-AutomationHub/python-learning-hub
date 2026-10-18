'''
python function syntax -
def function_name():
    function statements

Step1 - function declaration
step2 - function call / invoking the function
'''

print("# Example1 - functions that does not take any args & not return any value")

# function definition
def greetings():
    print("Hello there...")

# function call
greetings()

print("# Example2 - functions that takes the args but do not return any value")

# function definition
def greetings(greetmsg):
    print(greetmsg)

# function call
greetings('welcome to India !')

print("# Example3 - functions that does not take any args but returns the value")

# function definition
def get_pi_value():
    return 3.14

# function call
pi = get_pi_value()
print(pi)

print("# Example3 - functions that takes args & returns the value")

# function definition
def addition(num1, num2):
    return num1 + num2

# function call
sum =addition(15,6)
print(sum)