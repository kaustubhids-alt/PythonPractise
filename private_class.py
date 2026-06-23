class Car:
    def __init__(self, value):
        self.__value = value

    def __show_value(self):
        print(self.__value)

    def public_method(self):
        self.__show_value()

obj = Car(10)

obj.public_method()