class Dog:
    species : "Golden retriver"

    def eat(self):
        self.b = 10
        print(f"I am hungry!")

    def bark(self):
        print(self.b)
        print(f"woof woof!")

a = Dog()
a.eat()
a.bark()

    
