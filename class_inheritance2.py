class Vehicle:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

class Car(Vehicle):
    def __init__(self, brand, color, wheels):
        self.wheels = wheels
        super().__init__(brand, color)

    def car_info(self):
        print(f"This is a {self.color} {self.brand} with {self.wheels} wheels.")

my_car = Car(brand="Ford", color="Black", wheels = 4)
print(my_car)
print(dir(my_car))
my_car.car_info()
