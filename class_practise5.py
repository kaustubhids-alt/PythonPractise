class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

Manager = Manager("Shubman", 10000, "Manager")

print(Manager.name)
print(Manager.salary)
print(Manager.department)
