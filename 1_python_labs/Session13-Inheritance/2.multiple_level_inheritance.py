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


class C(B):
    s, t = 22, 44

    def m2(self,p,q):
        print("this is m2 override method from class C")
        if p>q:
            print("subtraction with class C local variables")
            print(p-q)
        else:
            print("subtraction with class C local variables")
            print(q-p)
        print("addition with class C class variables")
        print(self.s + self.t)
        print("multiplication with parent class B class variables")
        print(self.x * self.y)

    def get_parent_class_var(self):
        print("this is get_parent_class_var override method from class C")
        return super().x , super().y

print("---------- Class B Object Calling Methods ---------- ")
bobj = B()
bobj.m1() # calling parent class method using child class object
bobj.m2(25,35)
parent_var = bobj.get_parent_class_var()
print(type(parent_var), parent_var)

print("---------- Class C Object Calling Methods ---------- ")
cobj = C()
cobj.m1() # calling grand-parent class A method using C class object
cobj.m2(25,35) # calling parent class B override method using C class object
parent_var = cobj.get_parent_class_var() # calling parent class B override method using C class object
print(type(parent_var), parent_var)