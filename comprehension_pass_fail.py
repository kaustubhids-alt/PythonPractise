marks = [13, 45, 23, 56, 90, 53, 24]

print("Passed Students:",[a for a in marks if a >= 33])
print("Failed Students:",[a for a in marks if a < 33])
print(["Pass" if a >= 33 else "Fail" for a in marks])