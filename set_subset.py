set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}
set3 = {34, 32, 24}
set4 = {12, 54, 20}

print(set1)
print(set2)
print(set3)
print(set4)

print(f"Is {set1} subset of {set2}? {set1.issubset(set2)}")

print(f"Is {set2} superset of {set1}? {set2.issuperset(set1)}")