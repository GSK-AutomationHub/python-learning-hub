""" Python supports both structure & object-oriented concepts
OOPs concepts in python - classes, objects, inheritance, polymorphism
class
- blueprint, logical entity, does not acquire space in memory
- class is collection of variable (attribute) & methods (behavior)
objects
- instance of class, physical entity, acquires space in memory
- each object is independent & carries copy of class's attribute & methods
function vs method
- function - block of code when created outside class & called independently
- method - when any function created inside class the its method & has default 'self' args """

def func():
    print("independent function")

class MyClass:
    def m1(self):
        print("MyClass method")

    def display(self,name):
        print(name)

func() # function call

mc1 = MyClass() # object of class MyClass stored in variable mc1
mc2 = MyClass() # object of class MyClass stored in variable mc2

mc1.m1() # class method call using class object
mc1.display('anant')

mc2.m1() # class method call using class object
mc2.display('anand')