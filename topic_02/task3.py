def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Division by zero is not allowed"
    return a / b

while True:
    print("Choose operation:")
    print("1. Add = '+' ")
    print("2. Subtract = '-' ")
    print("3. Multiply = '*' ")
    print("4. Divide = '/' ")
    print("5. Exit = ']'")
     
    operation = input('Enter operation sign: ')
    
    if operation == "]":
        print("Leaving...")
        break
    
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    result = None

    if operation == '+':
        result = add(a, b)
    elif operation == '-':
        result = subtract(a, b)
    elif operation == '*':
        result = multiply(a, b)
    elif operation == '/':
        result = divide(a, b)
    elif operation == ']':
        print(' ')
    else:
        print("Invalid operation")
        continue

    if result is not None:
        print("Result:", result)
