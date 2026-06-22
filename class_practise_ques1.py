class Programmer:
    company = "Microsoft"

    def __init__(self, name, id, location):
        self.name = name
        self.id = id
        self.location = location

    def get_info(self):
        print({self.name})
        print({self.id})
        print({self.location})

p1 = Programmer("Rahul", 1234, "Jaipur")
p2 = Programmer("Rohit", 1245, "Delhi")

p1.get_info()
print()
p2.get_info()