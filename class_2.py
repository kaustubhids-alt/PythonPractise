class Dog:
    species = "GS"

    def __init__(self, age=24):
        self.age = age
        print("Object")

    def eat(self):
        print(f"I m hungry")

    def bark(self):
        print(self.age)
        print(f"woof woof")

a = Dog(2)
a.bark()