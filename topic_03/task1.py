while True:
    try:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        operation = input("Enter the operation (+, -, *, /) or 'Q' to quit: ")

        if operation == 'Q':
            print("Program terminated.")
            break

        if operation not in ('+', '-', '*', '/'):
            print("Invalid operation. Please try again.")
            continue

        if operation == '+':
            result = a + b
        elif operation == '-':
            result = a - b
        elif operation == '*':
            result = a * b
        elif operation == '/':
            if b == 0:
                print("Division by zero is not allowed.")
                continue
            result = a / b

        print("Result: ", result)

    except ValueError:
        print("Invalid input. Please try again.")

