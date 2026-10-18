from abc import ABC, abstractmethod

class Shape():

    def __init__(self, type, color):
        self.type = type
        self.color = color

    @abstractmethod
    def get_area():
        pass


class Circle(Shape):

    def __init__(self, type, color,radius):
        super().__init__(type, color)
        self.radius = radius

    def get_area(self):
        return (3.14 * self.radius ** 2)
    

class Square(Shape):

    def __init__(self, type, color, width):
        super().__init__(type, color)
        self.width = width

    def get_area(self):
        return (self.width ** 2)
    

shapes = [Circle('circle', 'blue', 3),Square('sqare', 'green', 5)]

for shape in shapes:
    print(f" The {shape.color} {shape.type} having area - {shape.get_area()} cm^2")