class GST:
    tax = 15
    def __init__(self, name):
        self.name = name
milk = GST(name="Amul")
bread = GST(name="Lotus")

print(f"{milk.name} has {milk.tax} rate.")
print(f"{bread.name} has {bread.tax} rate.")

GST.tax = 5

print(f"\n{milk.name} has {milk.tax} rate.")
print(f"{bread.name} has {bread.tax} rate.")
