class Car:
    def __init__(self, value):
        self._value = value
    
    def _show_value(self):
        print(self._value)

class Toyota(Car):
    def display(self):
        self._show_value()

obj = Toyota(10)
obj.display()