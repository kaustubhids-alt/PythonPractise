class Vehicle:
    def __init__(self, brand, color):
        self.__brand = brand

    def __show_brand(self):
        print(self.__brand)

    def public_method(self):
        self.__show_brand

    def _show_color(self):
        print(self.color)

class Car(Vehicle):
    def display(self):
        self._show_color()

obj = Car("Toyota")
obj.__show_brand()
print(obj.__brand)

obj = Car("White")
obj.display()
print(obj._color)


    