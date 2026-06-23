class Test:
    a = 5  

obj = Test()
print("Before change:")
print("Class attribute:", Test.a)
print("Object attribute:", obj.a)

obj.a = 0
print("\nAfter change:")
print("Class attribute:", Test.a)
print("Object attribute:", obj.a)