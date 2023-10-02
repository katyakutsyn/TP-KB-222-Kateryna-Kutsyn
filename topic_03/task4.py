my_list = ["h", "r", "w"]

while True:
    new_value = input("New value (or 'Q' to exit): ")

    if new_value == 'Q':
        break

    insert_index = 0

    for elem in my_list:
        if new_value > elem:
            insert_index += 1

    my_list.insert(insert_index, new_value)

    print("Result:", my_list)
