i=2
number=int(input("Enter the Number: "))

while i<number:
 if number%i==0:
  print(i)
  break
 i+=1

if i==number:
 print("It is a Prime Number")