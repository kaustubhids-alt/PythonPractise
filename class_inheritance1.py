class Vehicle:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
        print("Vehicle called.")

class Car(Vehicle):
    def __init__(self, num_wheels):
        self.num_wheels = num_wheels
        print("Car called.")
        super().__init__("Toyota", "White")

    def car_info(self):
        print(f"This is a {self.color} colour {self.brand} having {self.num_wheels} wheels.")


my_car = Car(4)
print(my_car.num_wheels)
my_car.car_info()