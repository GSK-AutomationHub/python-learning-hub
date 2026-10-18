""" python decorator is function which add wrapper to original function and customized it"""

def new_decorator(original_func):
    def wrapper_function():
        print("the code to run before original function")
        original_func()
        print("the code to run after original function")
    return wrapper_function


def my_func():
    print(" I want to be decorated !!")

# decorated_function = new_decorator(my_func)
# decorated_function()

# another way for calling decorated function is
@new_decorator
def my_func2():
    print(" I want to be decorated !!")

my_func2()