
class Circle:

    # CLASS OBJECT ATTRIBUTE SET TO PRIVATE
    __pi = 3.14

    def __init__(self,radius:float = 1):
        # USER DEFINED ATTRIBUTE SET TO PRIVATE
        assert radius > 0, "negative or zero radius value not allowed"
        self.__radius = radius

    @property
    def get_pi_value(self):
        return Circle.__pi

    @property
    def radius_value(self):
        return self.__radius

    @radius_value.setter
    def radius_value(self,new_radius:float):
        assert new_radius > 0, "negative or zero radius value not allowed"
        self.__radius = new_radius

    def get_circumference(self):
        circumference = self.__radius * Circle.__pi * 2
        return round(circumference,2)

    def get_circle_area(self):
        return Circle.__pi * pow(self.__radius,2)

    def get_nth_size_of_area(self, size, customized=None):
        customized_size_area = self.get_circle_area()/size
        return round(customized_size_area,2)

my_circle = Circle(5)

print("CLASS OBJECT ATTRIBUTE i.e. pi value is {}" .format(my_circle.get_pi_value))

print("USER DEFINED ATTRIBUTE i.e. radius for circle is {}" .format(my_circle.radius_value))

print("circumference of the circle is {}" .format(my_circle.get_circumference()))

print("area of the circle is {}" .format(my_circle.get_circle_area()))

print("customized circle area size {}" .format(my_circle.get_nth_size_of_area(3)))

my_circle.radius_value = 2.5

print("USER DEFINED ATTRIBUTE i.e. radius for circle is {}" .format(my_circle.radius_value))

