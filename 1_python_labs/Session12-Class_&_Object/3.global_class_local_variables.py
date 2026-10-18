''' the 3 types of variables in python - global, class, local variables
global variable
- usually created outside class & can be accessed anywhere in class i.e. inside/outside functions & methods
- considering global variable declared already then it can be ...
    - called inside function/method using ---> globals()['var_name']
    - modified inside function/method using --->  global var_name, & assigning value in next line
- considering global variable not declared already then it can be ...
    - declared inside function/method using ---> globals var_name
class variable
- created inside class & can be accessed anywhere inside class i.e. inside/outside class methods
- can be accessed inside class method using 'self' keyword i.e. self.var_name
local variable
- created inside function / class method
- can be accessed only inside function / class method '''

a, b = 50, 60 # global variables having same name as class & local variables
x, y = 30, 40 # global variables

class MyClass:
    a, b = 20, 25 # class variable

    def print_variable_values(self,a,b):
        # to print values of local variables
        print(f'values of a, b local variables are - {a}, {b}')
        # to print values of class variables
        print(f'values of a, b class variables are - {self.a}, {self.b}')
        # to print values of global variables
        print(f'values of x, y global variables are - {x}, {y}')
        # to print values of global variables having same var_name as class / local variables
        print(f'values of a, b global variables are - {globals()['a']}, {globals()['b']}')


mc = MyClass()
mc.print_variable_values(5,15)