class BankAccount:

    Bank_Name = "SBI"

    def __init__(self, name, number, age, birthday, balance):
        self.name = name
        self.number = number
        self.age = age
        self.birthday = birthday
        self.balance = balance

    def show_info(self):
        print(self.name, self.number, self.age, self.balance)
        
    def deposit(self, amount):
        if amount < 0:
            print("Invalid Amount")
        self.balance += amount
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Invalid Amount")
        self.balance -= amount
Abhishek = BankAccount("Abhishek", 1234567890, 24, "2408", 1000)

Bank_Account = []
while True:

    print ("""
    A: Creating a New Account
    B: Checking Bank details
    C: Deposit
    D: Withdrawal
    """)
    a = input("Enter your choice: ")

    match a:
        case "A":
            name = input("Enter your Name: ")
            number = input("Enter your mobile number: ")
            age = input("Enter your Age: ")
            birthday = input("Enter your Birthdate: ")


            Bank_Account.append(
                BankAccount(name, number, age, birthday, 500)
            )

        case"B":
            number = input("Enter your mobile number: ")
            account = ""
            for x in Bank_Account:
                if x.number == number:
                    account = x
                if account:
                    account.show_info()
                else:
                    print("Bank Account not found")

        case"C":
            number = input("Enter your mobile number: ")
            account = ""
            for x in Bank_Account:
                if x.number == number:
                    account = x
                amount = int(input("Enter the amount: "))
                if account:
                    account.deposit(amount)
                else:
                    print("Bank Account not found")

        case"D":
            number = input("Enter your mobile number: ")
            account = ""
            for x in Bank_Account:
                if x.number == number:
                    account = x
                amount = int(input("Enter the amount: "))
                if account:
                    account.withdraw(amount)
                else:
                    print("Bank Account not found")
                    

