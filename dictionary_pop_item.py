grades = {"math": 90, "science": 85}
grades["music"] = 99
print(f"Before popitem: {grades}")
popped_item_pair = grades.popitem()
print(f"Popped item pair: {popped_item_pair}, After popitem: {grades}")