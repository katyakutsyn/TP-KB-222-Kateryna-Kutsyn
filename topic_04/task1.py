

import sys

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        if b == 0:
            raise ZeroDivisionError("Division by zero is not allowed")
        return a / b
    except ZeroDivisionError as e:
        print("Error:", e)
        return None

def getInt(prompt):
    while True:
        try:
            num = int(input(prompt))
            return num
        except ValueError:
            print("Invalid input. Please enter an integer.")

while True:
    print("Choose operation:")
    print("1. Add = '+' ")
    print("2. Subtract = '-' ")
    print("3. Multiply = '*' ")
    print("4. Divide = '/' ")
    print("5. Exit = 'Q'")
    print("6. Get Integer = 'get_int'")

    operation = input('Enter operation sign: ')

    if operation == "Q":
        print("GG goodbye")
        break

    elif operation == "get_int":
        num = getInt("Enter an integer: ")
        print("You entered:", num)
    else:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        result = None

        try:
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

        except Exception as e:
            print("Error:", e)


