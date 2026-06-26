class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def __add__(self, other):
        return BankAccount(self.balance + other.balance)

    def __str__(self):
        return (self.balance)

account1 = BankAccount(5000)
account2 = BankAccount(10000)

total = account1 + account2

print(total)
