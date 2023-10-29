class Calculator:
    def add(self, x, y):
        return x + y
    def subtract(self, x, y):
        return x - y
    def multiply(self, x, y):
        return x * y
    def divide(self, x, y):
        if y == 0:
            return "EROR!!!! Division by zero"
        return x / y

def main():
    calc = Calculator()
    while True:
        print("Operations:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("Q. Quit")       
        choice = input("Choose an operation (1/2/3/4/5): ")
        if choice == 'Q':
            print("Orividerchi!")
            break
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if choice == '1':
            print("Result:", calc.add(num1, num2))
        elif choice == '2':
            print("Result:", calc.subtract(num1, num2))
        elif choice == '3':
            print("Result:", calc.multiply(num1, num2))
        elif choice == '4':
            print("Result:", calc.divide(num1, num2))
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()

