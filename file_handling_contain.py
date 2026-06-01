file=open("india_jaipur.txt", "r")

for line in file.readlines():
    if not("India" in line or "india" in line):
        print(line)
file.close()