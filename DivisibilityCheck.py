number=int(input("Enter any Number: "))

if number%3==0:
 if number%5==0:
  print("Divisible by both 3 and 5")
 else:
  print("Divisible by 3")

elif number%5==0:
 if number%3==0:
  print("Divisible by both 3 and 5")
 else:
  print("Divisible by 5")

else:
 print("Not divisible by 3 or 5")