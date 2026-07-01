a = {"virat":87, "rohit":100, "aryan": 15, "abhishek":75, "ishan":72, "manas": 8, "shubman":84 }
print("Passed: ",{ i:a[i] for i in a if a[i] >= 33 })
print("Failed: ",{ i:a[i] for i in a if a[i] < 33 })




