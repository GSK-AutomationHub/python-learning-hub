'''
method vs constructor
- method can take any name, constructor name is fixed i.e. def __init__(self)
- both method & constructor can take arguments
- method can return value/s, constructor can not return anything
- method can be invoked using class object, constructor get auto invoked during obj creation
'''

class MyClass:

    def __init__(self,name):
        print('constructor called')
        print(f'hello {name}')

    def m1(self,name):
        print(f'method called')
        print(f'how are you doing, {name}?')

    @staticmethod
    def greetings(self,msg):
        print('static method called')
        print(msg)

mc = MyClass('Ganesh')
mc.m1('Ganesh')

MyClass.greetings('hi','Welcome to world of python prog')

class Emp:

    def __init__(self,eid,ename,esal):
        print("in the default constructor")
        self.eid = eid
        self.ename = ename
        self.esal = esal

    def __str__(self):
        print("in the string constructor")
        print("# str constructor prints only string data")
        print("# f-string or text.format() can be used to return type cast data")
         # return id
        # return salary
        return f' {self.ename} , {str(self.eid)}, {str(self.esal)}'

    def display(self):
        print("in the instance display method")
        print(self.eid, self.ename, self.esal)


e1=Emp('eid-003', 'vijay',150000)
e1.display()
print(e1) # to call string constructor we need to print object of class