
class Cube:

    def __init__(self,number):
        self.number = number

    def gen_cube(self):
        return self.number ** 3

c = Cube(3)

print(c)
print(c.gen_cube)
print(c.gen_cube())

d = c
print(d)
print(d.gen_cube)
print(d.gen_cube())

print(c, d)
print(c.gen_cube)
print(d.gen_cube)
print(id(c))
print(id(d))