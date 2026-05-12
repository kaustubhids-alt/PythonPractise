number1=int(input("Enter 1st number: "))
number2=int(input("Enter 2nd number: "))
number3=int(input("Enter 3rd number: "))

if number1>number2 and number1>number3:
 print(f"1st number is Greatest {number1}")

elif number2>number3 and number2>number1:
 print(f"2nd number is Greatest {number2}")

else:
 print(f"3rd number is Greatest {number3}")