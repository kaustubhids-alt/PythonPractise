num = 20
print (True if num > 10 else False)

a = int(input("\nEnter a number: "))

print ("divisible by both" if a % 3 == 0 and a % 5 == 0 else "divisible by 3" if a % 3 == 0 else "divisible by 5" if a % 5 == 0 else "divisible by none")