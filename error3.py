try:
    my_list = [10, 20]
    a= int(input("Enter an index: "))
    print(my_list[a])
except (IndexError, ValueError) as error:
    print(f"Error Found: {error}")