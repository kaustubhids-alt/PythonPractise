try:
    a = int(input("Enter A number: "))
except:
    print("Type conversion error.")
else:
    print("No error")
finally:
    print("runs anyway")