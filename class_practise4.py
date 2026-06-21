class Vehicle:
    def start(self):
        print("Start")

class Car(Vehicle):
    def start(self):
        print("Car is starting")

a = Car()
a.start()