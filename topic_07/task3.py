class Calculator:
    def __init__(self, log_file):
        self._operand1 = 0
        self._operand2 = 0
        self.log_file = log_file
    @property
    def operand1(self):
        return self._operand1
    @operand1.setter
    def operand1(self, value):
        self._operand1 = value
    @property
    def operand2(self):
        return self._operand2
    @operand2.setter
    def operand2(self, value):
        self._operand2 = value
        
        
    def add(self):
        result = self.operand1 + self.operand2
        self._log("Addition", result)
        return result
    def subtract(self):
        result = self.operand1 - self.operand2
        self._log("Subtraction", result)
        return result
    def multiply(self):
        result = self.operand1 * self.operand2
        self._log("Multiplication", result)
        return result
    def divide(self):
        if self.operand2 == 0:
            result = "Error: Division by zero"
            self._log("Division", result)
            return result
        result = self.operand1 / self.operand2
        self._log("Division", result)
        return result
    
    def _log(self, operation, result):
        with open(self.log_file, "a") as log:
            log.write(f"{operation}: operand1={self.operand1}, operand2={self.operand2}, result={result}\n")
def main():
    log_file = "calс_log.txt"
    calc = Calculator(log_file)
    while True:
        print("Operations:")
        print("1. Set Operand 1")
        print("2. Set Operand 2")
        print("3. Addition")
        print("4. Subtraction")
        print("5. Multiplication")
        print("6. Division")
        print("Q. Quit")
        choice = input("Choose an operation (1/2/3/4/5/6/Q): ")
        if choice == 'Q':
            print("допобаченя")
            break
        if choice == '1':
            operand = float(input("Enter Operand 1: "))
            calc.operand1 = operand
        elif choice == '2':
            operand = float(input("Enter Operand 2: "))
            calc.operand2 = operand
        elif choice == '3':
            result = calc.add()
            print("Result:", result)
        elif choice == '4':
            result = calc.subtract()
            print("Result:", result)
        elif choice == '5':
            result = calc.multiply()
            print("Result:", result)
        elif choice == '6':
            result = calc.divide()
            print("Result:", result)
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()
