import functions
import operations

while True:
    a = operations.get_int_or_float_value("Введіть перше число: ")
    b = operations.get_int_or_float_value("Введіть друге число: ")
    operation = operations.get_operation()

    if operation == '+':
        result = functions.add(a, b)
    elif operation == '-':
        result = functions.sub(a, b)
    elif operation == '*':
        result = functions.mul(a, b)
    elif operation == '/':
        result = functions.div(a, b)

    print(f"Результат: {result}")

    repeat = input("Бажаєте продовжити (yep/no)? ").lower()
    if repeat != 'yep':
        break
