def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        raise ValueError("ZeroDivisionError occurs")
    return a / b

def get_number(prompt):
    while True:
        try:
            x = float(input(prompt))
            return x
        except ValueError:
            print("Invalid input, please try again.")

while True:
    print("Choose operation:")
    print("1. Add = '+' ")
    print("2. Subtract = '-' ")
    print("3. Multiply = '*' ")
    print("4. Divide = '/' ")
    print("5. Exit = 'Q'")
    
    choice = input("Enter operation sign:: ")
    
    if choice == "Q" :
        print("goodbye")
        break
    
    if choice in ('+', '-', '*', '/'):
        
        first_number = get_number("Enter the first number: ")
        second_number = get_number("Enter the second number: ")

        try:
            if choice == '+':
                result = addition(first_number, second_number)
            elif choice == '-':
                result = subtraction(first_number, second_number)
            elif choice == '*':
                result = multiplication(first_number, second_number)
            elif choice == '/':
                result = division(first_number, second_number)

            print("Result:", result)
        except ValueError as e:
            print("Error:", e)

