class Dog:
    species = "Golden Retriever"

    def __init__(self, name="tom", age=2):
        self.dog_name = name
        self.age = age
        self.is_hungry = True

    def bark(self):
        print(f"{self.dog_name} says woof!")

    def eat(self):
        if self.is_hungry:
            print(f"{self.dog_name} is eating...")
            self.is_hungry = False
        else:
            print(f"{self.dog_name} is not hungry right now.")
            self.is_hungry = True

my_dog = Dog()
my_dog.bark()
my_dog.eat()