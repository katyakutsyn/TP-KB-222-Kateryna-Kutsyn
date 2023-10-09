
student_list = [
    {"name": "Bob", "phone": "0631234567", "email": "bob@example.com", "group": "A"},
    {"name": "Emma", "phone": "0631234567", "email": "emma@example.com", "group": "B"},
    {"name": "Jon", "phone": "0631234567", "email": "jon@example.com", "group": "C"},
    {"name": "Zak", "phone": "0631234567", "email": "zak@example.com", "group": "A"}
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

def edit_student():
    name_to_edit = input("Please enter the name of the student to edit: ")

   
    for student in student_list:
        if student["name"] == name_to_edit:
            print(f"Editing student: {student['name']}")
            
            new_name = input("Enter new name: ")
            
            
            
            student_list.remove(student)
           
            student["name"] = new_name
           
           
            insert_position = 0
            for existing_student in student_list:
                if new_name > existing_student["name"]:
                    insert_position += 1
                else:
                    break
            student_list.insert(insert_position, student)
           
            print(f"Student '{name_to_edit}' has been updated with new name: {new_name}")
            return

   
    print(f"Student '{name_to_edit}' not found")

def main():
    while True:
        choice = input("Please specify the action [C create, D delete, E edit, P print, Q exit]: ")
        if choice.upper() == "C":
            print("Creating a new student:")
            add_new_student()
            print_all_students()
        elif choice.upper() == "D":
            print("Deleting a student:")
            delete_student()
            print_all_students()
        elif choice.upper() == "E":
            print("Editing a student:")
            edit_student()
            print_all_students()
        elif choice.upper() == "P":
            print("Printing the student list:")
            print_all_students()
        elif choice.upper() == "Q":
            print("Dosvidos")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
