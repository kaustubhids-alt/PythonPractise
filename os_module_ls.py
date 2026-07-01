import os

while True:
    a = input("-->")
    if a == "ls":
        print(os.listdir())

    elif a == "lsfolder":
        for x in os.listdir():
            if os.path.isdir(x):
                print(x)

    elif a == "lsfiles":
        for x in os.listdir():
            if os.path.isfile(x):
                print(x)

    elif a == "exit":
        break

    else:
        print("Invalid Command")