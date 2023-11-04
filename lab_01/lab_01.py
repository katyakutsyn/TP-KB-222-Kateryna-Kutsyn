

student_list = [
    {"name": "Bob", "phone": "0631234567", "email": "aboba", "group": "A"},
    {"name": "Emma", "phone": "0631234567", "email": "emmomus", "group": "B"},
    {"name": "Jon", "phone": "0631234567", "email": "jonsonuk", "group": "C"},
    {"name": "Zak", "phone": "0631234567", "email": "zakodirovan", "group": "A"},
    {"name": "Alice", "phone": "0631234567", "email": "alcoholik", "group": "B"},
    {"name": "Eve", "phone": "0631234567", "email": "evening", "group": "A"},
    {"name": "Mike", "phone": "0631234567", "email": "mikelandjelo", "group": "C"},
    {"name": "Charlie", "phone": "0631234567", "email": "charkavodki", "group": "B"},
    {"name": "David", "phone": "0631234567", "email": "davay", "group": "A"},
    {"name": "Sarah", "phone": "0631234567", "email": "sarakonozka", "group": "C"},
]

def print_all_students():
    for student in student_list:
        print(f"Name: {student['name']}, Phone: {student['phone']}, Email: {student['email']}, Group: {student['group']}")

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
    print_all_students()

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
        print_all_students()

def edit_student():
    name_to_edit = input("Please enter the name of the student to edit: ")

    for student in student_list:
        if student["name"] == name_to_edit:
            print(f"Editing student: {student['name']}")
      
            new_name = input(f"Enter new name ({student['name']}): ")
            new_phone = input(f"Enter new phone ({student['phone']}): ")
            new_email = input(f"Enter new email ({student['email']}): ")
            new_group = input(f"Enter new group ({student['group']}): ")
           
            student["name"] = new_name
            student["phone"] = new_phone
            student["email"] = new_email
            student["group"] = new_group
            print(f"Student '{name_to_edit}' has been updated")
            print_all_students()
            return

    print(f"Student '{name_to_edit}' not found")

def main():
    while True:
        choice = input("Please specify the action [C create, D delete, E edit, P print, Q exit]: ")
        if choice.upper() == "C":
            print("Creating a new student:")
            add_new_student()
        elif choice.upper() == "D":
            print("Deleting a student:")
            delete_student()
        elif choice.upper() == "E":
            print("Editing a student:")
            edit_student()
        elif choice.upper() == "P":
            print("Printing the student list:")
            print_all_students()
        elif choice.upper() == "Q":
            print("Dosviduli")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
