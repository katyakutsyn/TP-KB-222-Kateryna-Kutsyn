
student_list = [
    {"name": "Katya", "phone": "0631234567", "email": "Katya@example.com", "group": "A"},
    {"name": "Carlicci", "phone": "0641234567", "email": "Carlicci@example.com", "group": "B"},
    {"name": "Santa", "phone": "0651234567", "email": "Santa@example.com", "group": "C"},
    {"name": "Puffendui", "phone": "0661234567", "email": "Puffendui@example.com", "group": "A"}
]

def print_all_students():
    for student in student_list:
        print(f"Name: {student['name']}, Phone: {student['phone']}, Email: {student['email']}, Group: {student['group']}")
    return

def add_new_student():
    name = input("Please enter student name: ")
    phone = input("Please enter student phone: ")
    email = input("Please enter student email: ")
    group = input("Please enter student group: ")

    new_student = {"name": name, "phone": phone, "email": email, "group": group}

    insert_position = 0
    for student in student_list:
        if name > student["name"]:
            insert_position += 1
        else:
            break

    student_list.insert(insert_position, new_student)
    print("New student has been added")
    return

def delete_student():
    name = input("Please enter name to be deleted: ")
    delete_position = -1
    for student in student_list:
        if name == student["name"]:
            delete_position = student_list.index(student)
            break
    if delete_position == -1:
        print("Student not found")
    else:
        del student_list[delete_position]
        print(f"Student '{name}' has been deleted")
    return

def main():
    while True:
        choice = input("Please specify the action [C create, D delete, P print, Q exit]: ")
        if choice.upper() == "C":
            print("Creating a new student:")
            add_new_student()
            print_all_students()
        elif choice.upper() == "D":
            print("Deleting a student:")
            delete_student()
            print_all_students()
        elif choice.upper() == "P":
            print("Printing the student list:")
            print_all_students()
        elif choice.upper() == "Q":
            print("Goodbye GG")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
