


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

while True:
    print("Choose operation:")
    print("1. Addition = '+' ")
    print("2. Subtraction = '-' ")
    print("3. Multiplication = '*' ")
    print("4. Division = '/' ")
    print("5. Exit = 'Q'")
    
    operation = input('Enter operation sign: ')

    if operation == "Q":
        print("gg goddbye")
        break
    else:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))

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
