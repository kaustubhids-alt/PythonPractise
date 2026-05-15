password="admin1234"
attempts=0

while attempts<3:
 Pass=input("Enter the Password: ")


 if Pass==password:
  print("Password accepted!")
  break 
 else:
  attempts=attempts+1
  print("Try Again!")
  
if attempts==3:
 print("Account Locked")