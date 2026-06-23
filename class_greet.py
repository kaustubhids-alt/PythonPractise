class Test:
    a = 5 

    @staticmethod
    def greet():
        print("Hello!")

obj = Test()

print("Before:", obj.a)

obj.a = 0

print("After:", obj.a)
print("Class attribute still:", Test.a)


Test.greet()  
obj.greet()