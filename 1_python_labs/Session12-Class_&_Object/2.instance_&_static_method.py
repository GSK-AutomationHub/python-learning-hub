""" instance vs static method
instance method
- method get copied for each new class instance during object creation
- so each object has its own copy of method
- method need to call using class object
- no param need to pass against 'self' args during instance method call

Static method
- created using @staticmethod
- static method is common for all class objects (shared class property)
- so no object specific copy created of static method
- * param need to pass against 'self' args during static method call  """

class MyClass:
    def m1(self):
        print("MyClass method")

    def display(self,name):
        print(name)

    @staticmethod
    def greeting(self):
        print('welcome to python world!')


mc1 = MyClass() # object of class MyClass stored in variable mc1
mc2 = MyClass() # object of class MyClass stored in variable mc2

# instance method call using class objects,
# no param need to pass against 'self' args during instance method call
mc1.m1()
mc2.display('anant')

# static method call using class name,
# param need to pass against 'self' args during static method call
MyClass.greeting('Hello')