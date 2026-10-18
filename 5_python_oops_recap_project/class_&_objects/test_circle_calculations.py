
class Circle:

    # CLASS OBJECT ATTRIBUTE
    pi = 3.14

    def __init__(self,radius = 1):
        # USER DEFINED ATTRIBUTE
        self.radius = radius

    def get_circumference(self):
        circumference = self.radius * Circle.pi * 2
        return round(circumference,2)

    def get_circle_area(self):
        return Circle.pi * pow(self.radius,2)

    def get_nth_size_of_area(self, size, customized=None):
        customized_size_area = self.get_circle_area()/size
        return round(customized_size_area,2)

my_circle = Circle(5)

print("CLASS OBJECT ATTRIBUTE i.e. pi value is {}" .format(Circle.pi))

print("USER DEFINED ATTRIBUTE i.e. radius for circle is {}" .format(my_circle.radius))

print("circumference of the circle is {}" .format(my_circle.get_circumference()))

print("area of the circle is {}" .format(my_circle.get_circle_area()))

print("customized circle area size {}" .format(my_circle.get_nth_size_of_area(3)))