class Point:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return Point(self.a + other.a, self.b + other.b)

    def __str__(self):
        return f"({self.a}, {self.b})"

point_1 = Point(11,22)
point_2 = Point(44,55)

point_3 = point_1 + point_2

print(point_3)