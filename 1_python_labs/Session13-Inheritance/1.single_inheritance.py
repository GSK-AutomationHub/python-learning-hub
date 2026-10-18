class A:
    a,b=10,20

    def m1(self):
        print("this is m1 method from class A")
        print(self.a + self.b)

class B(A):
    x,y = 30,40

    def m2(self,i,j):
        print("this is m2 method from class B")
        if i>j:
            print("subtraction with class B local variables")
            print(i-j)
        else:
            print("subtraction with class B local variables")
            print(j-i)
        print("addition with class B class variables")
        print(self.x + self.y)
        print("multiplication with parent class A class variables")
        print(self.a * self.b)

    def get_parent_class_var(self):
        return super().a , super().b

bobj = B()

bobj.m1() # calling parent class method using child class object

bobj.m2(25,35)

parent_var = bobj.get_parent_class_var()
print(type(parent_var), parent_var)