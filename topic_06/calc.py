import functions
import operations
import logging

logging.basicConfig(filename='calculator.log', level=logging.INFO, format='%(asctime)s - %(message)s')
while True:
    a = operations.get_int_or_float_value("Введіть перше число: ")
    b = operations.get_int_or_float_value("Введіть друге число: ")
    operation = operations.get_operation()
    if operation == '+':
        result = functions.add(a, b)
        logging.info(f"Додавання: {a} + {b} = {result}")
    elif operation == '-':
        result = functions.sub(a, b)
        logging.info(f"Віднімання: {a} - {b} = {result}")
    elif operation == '*':
        result = functions.mul(a, b)
        logging.info(f"Множення: {a} * {b} = {result}")
    elif operation == '/':
        result = functions.div(a, b)
        logging.info(f"Ділення: {a} / {b} = {result}")
    print(f"Результат: {result}")
    repeat = input("Бажаєте продовжити (yep/no)? ").lower()
    if repeat != 'yep':
        break

logging.shutdown()
