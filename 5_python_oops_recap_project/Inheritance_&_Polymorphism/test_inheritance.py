from abc import ABC, abstractmethod


class Animal(ABC):

    def __init__(self,name):
        self.name = name
        print("New Animal Created with name {}" .format(self.name))

    @abstractmethod
    def speak(self):
        pass


class Dog(Animal):

    def __init__(self,name):
        Animal.__init__(self,name)

    def speak(self):
        return "Woof!!"


class Cat(Animal):

    def __init__(self, name):
        Animal.__init__(self, name)

    def speak(self):
        return "Meow!!"


catty = Cat('catty')
doggy = Dog('Doggy')
for pet in [catty, doggy]:
    print(pet.speak())