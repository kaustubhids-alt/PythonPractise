import math

class Calculator:
    
    def square(self, num):
        return num ** 2
    
    def cube(self, num):
        return num ** 3
    
    def square_root(self, num):
        return math.sqrt(num)

calc = Calculator()

print("Square:", calc.square(4))       
print("Cube:", calc.cube(3))           
print("Square Root:", calc.square_root(25))