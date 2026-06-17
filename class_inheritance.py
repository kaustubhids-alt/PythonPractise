class Vehicle:

    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def display_info(self):
        print(f"Brand: {self.brand}, Color: {self.color}")

class Car( Vehicle ):

    def wheels(self):
        print("Car has 4 wheels")

class Bike( Vehicle ):

    def wheels(self):
        print("Bike has 2 wheels")

my_car = Car("Toyota", "White")
print(my_car.brand)
print(my_car.color)

my_bike = Bike("Honda", "Black")
print(my_bike.brand)
print(my_bike.color)