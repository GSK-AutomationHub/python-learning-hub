class Car:

    category = 'premium'

    def __init__(self, brand, color, model):
        self.brand = brand
        self.color = color
        self.model = model

    
    def get_car_info(self):
        print(f"It's {self.color} {self.brand} of {Car.category} category - {self.model} model")


car1 = Car('ferari', 'blue', 2024)
car1.get_car_info()

car2 = Car('breeza', 'white', 2025)
car2.get_car_info()