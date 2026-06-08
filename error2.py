a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))
try:
    print( a / b)
except ValueError:
    print("Enter only integers")
except ZeroDivisionError:
    print("A number can't be divided 0")
