file = open("india_jaipur.txt","r")
data = file.read()
vowels = "aeiouAEIOU"
count = 0

for ch in data:
    if ch in vowels:
        count +=1
print("\n Total Vowels in text : ", count)