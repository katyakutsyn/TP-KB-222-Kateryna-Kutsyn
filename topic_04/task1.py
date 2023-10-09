import sys

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError :
        print("ZeroDivisionError occurs")
        return None


while True:
    print("Choose operation:")
    print("1. Add = '+' ")
    print("2. Subtract = '-' ")
    print("3. Multiply = '*' ")
    print("4. Divide = '/' ")
    print("5. Exit = 'Q'")

    operation = input('Enter operation sign: ')

    if operation == "Q":
        print("Goodbye")
        break

    try:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))

        result = None

        if operation == '+':
            result = add(a, b)
        elif operation == '-':
            result = subtract(a, b)
        elif operation == '*':
            result = multiply(a, b)
        elif operation == '/':
            result = divide(a, b)
        else:
            print("Invalid operation")
            continue

        if result is not None:
            print("Result:", result)

    except ValueError:
        print("Invalid input. Please enter a valid number.")


