def test( number1, number2 ):
    print(f"Sum of numbers are {number1 + number2}")
    return number2 + number1
    print(f"Mul of numbers are {number1 * number2}")
print(test(13, 23))

def test( number1, number2 ):
    print(f"\nSum of numbers are {number1 + number2}")
    print(f"Mul of numbers are {number1 * number2}")
    return number2 * number1
print(test(13, 23))