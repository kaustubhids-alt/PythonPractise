my_set = {10, 20, 30, 40, 50}
print(f"Original set: {my_set}")

my_set.remove(20)
print(f"{my_set}")

my_set.discard(90)
print(f"\nAfter discard(90): {my_set}")