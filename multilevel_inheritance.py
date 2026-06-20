class Parent_A:
    def method_A(self):
        print("Parent A")

    def test(self):
        print("Test A")

class Parent_B(Parent_A):
    def method_B(self):
        print("Parent B")

    def test(self):
        print("Test B")

class Child_C(Parent_B):
    def method_C(self):
        print("Parent C")

    def test(self):
        Parent_A.test(self)
        Parent_B.test(self)
        print("Test C")

child_obj = Child_C()

print(child_obj.method_A())
print(child_obj.method_B())
print(child_obj.method_C())
print(child_obj.test())