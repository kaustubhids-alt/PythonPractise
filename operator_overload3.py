class Temperature:
    def __init__(self, temp):
        self.temp = temp

        def __lt__(self, other):
            return self.temp < other.temp

        def __gt__(self, other):
            return self.temp > other.temp

    
        def __eq__(self, other):
            return self.temp == other.temp

temp_1 = Temperature(25)
temp_2 = Temperature(30)

print(temp_1 > temp_2)
print(temp_1 > temp_2)
print(temp_1 == temp_2)