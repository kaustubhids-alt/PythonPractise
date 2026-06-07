def add_pos_num():
    add = 0
    while True:
        a = int(input("Enter A number: "))
        if a > 0:
            add += a
        else:
            return add

a = add_pos_num()
print(a)