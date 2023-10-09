
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("ZeroDivisionError occurs")
    return a / b

while True:
    print("Choose operation:")
    print("1. Add = '+' ")
    print("2. Subtract = '-' ")
    print("3. Multiply = '*' ")
    print("4. Divide = '/' ")
    print("5. Exit = 'Q'")

    operation = input('Enter operation sign: ')

    if operation == 'Q':
        print("Goodbye")
        break

    if operation not in ('+', '-', '*', '/'):
        print("Goodbye 2.0")
        continue

    try:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))

        result = None

        if operation == '+':
            result = add(a, b)
        elif operation == '-':
            result = sub(a, b)
        elif operation == '*':
            result = multiply(a, b)
        elif operation == '/':
            try:
                result = divide(a, b)
            except ValueError as e:
                print(f"Error: {e}")
                continue

        print("Result:", result)
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
