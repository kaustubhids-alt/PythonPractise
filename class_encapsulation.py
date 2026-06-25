class Vehicle:
    def __init__(self, type, color):
        self.__type = type 
        self.__color = color

    def get_info(self):
        print(f"This is a {self.__type} of {self.__color} color.")
class Car(Vehicle):

    def __init__(self, brand, color, battery_level):
        super().__init__(brand, color)
        self.__battery_level = battery_level

    def get_info(self):
        print(f"Color: {self._Vehicle__color}, Battery: {self.__battery_level}%")

a = Car("Tata", 10000, 95)
print(a._Vehicle__color)

my_Vehicle = Vehicle("Car", "White")
my_car = Car("Toyota", "Gray", 90)

my_Vehicle.get_info()
my_car.get_info()