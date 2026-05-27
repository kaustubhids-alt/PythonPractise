dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

dict1.update(dict2)
print(f"After update: {dict1}")

dict2.update(dict1)
print(dict2)
