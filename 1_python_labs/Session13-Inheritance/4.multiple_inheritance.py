class A:
    a,b=10,20

    def am1(self):
        print("this is m1 method from class A")
        print(self.a + self.b)

class B:
    x,y = 30,40

    def am1(self):
        print("this is m1 override method from class B")
        print(self.x + self.y)

    def bm2(self,i,j):
        print("this is bm2 method from class B")
        if i>j:
            print("subtraction with class B local variables")
            print(i-j)
        else:
            print("subtraction with class B local variables")
            print(j-i)

    def bm3(self):
        print("multiplication with parent class A class variables")
        print(self.a * self.b)

    def get_parent_class_var(self):
        print("multiplication with parent class A class variables")
        return super().a , super().b


class C(B,A):
    s, t = 22, 44

    ''' In inheritance scenario if both parent class has same method name,and if child class object called the method, 
     then method of class mentioned first in parenthesis while declaring inheritance ll get called, 
     e.g here am1 method of class B get called'''

    # def am1(self):
    #     print("this is am1 override method from class C")
    #     super().am1()
    #     #print(self.s + self.t)

    def bm2(self,p,q):
        print("this is m2 method from class C")
        if p>q:
            print("subtraction with class C local variables")
            print(p-q)
        else:
            print("subtraction with class C local variables")
            print(q-p)

    def bm3(self):
        print("multiplication with parent class A class variables")
        print(self.a * self.b)

    def get_parent_class_var(self):
        print("this is get_parent_class_var method from class C")
        return super().a , super().b

print("---------- Class C Object Calling Methods ---------- ")
cobj = C()
cobj.am1() # calling grand-parent class A method using C class object
cobj.bm2(25,35) # calling parent class B override method using C class object
parent_var = cobj.get_parent_class_var() # calling parent class B override method using C class object
print(type(parent_var), parent_var)