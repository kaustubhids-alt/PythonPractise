a = 5
b = 10
print(a,b)
c = a
a = b
b = c
print(a,b)

print("\nusing tuple unpacking")
a=10
b=20
print(a,b)
a,b= b,a
print(a,b)