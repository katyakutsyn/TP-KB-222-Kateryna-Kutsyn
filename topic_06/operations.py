def get_int_or_float_value(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Введіть дійсне число.")

def get_operation():
    while True:
        operation = input("Оберіть операцію (+, -, *, /): ")
        if operation in ['+', '-', '*', '/']:
            return operation
        else:
            print("Неправильна операція. Спробуйте ще раз.")
