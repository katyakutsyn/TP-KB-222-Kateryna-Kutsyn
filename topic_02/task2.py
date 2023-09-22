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
    print("1. Add = '+'")
    print("2. Subtract = '-'")
    print("3. Multiply = '*'")
    print("4. Divide = '/'")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "5":
        print("Exiting...")
        break

    if choice not in ("1", "2", "3", "4"):
        print("Invalid choice")
        continue

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if choice == "1":
        result = add(a, b)
    elif choice == "2":
        result = subtract(a, b)
    elif choice == "3":
        result = multiply(a, b)
    elif choice == "4":
        result = divide(a, b)

    print("Result:", result)
