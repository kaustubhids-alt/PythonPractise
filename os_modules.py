import os

a = os.listdir()
# print(a)
for x in a:
    if x.startswith("function"):
        print(x)

for y in a:
    if y.endswith("py"):
        print(y)
