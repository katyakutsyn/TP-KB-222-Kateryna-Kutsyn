import csv
import sys

student_list = []
def load_students_from_csv(filename):
    global student_list
    try:
        with open(filename, newline='') as file:
            reader = csv.DictReader(file)
            student_list = [row for row in reader]
        print("Students loaded from CSV.")
    except FileNotFoundError:
        print(f"File '{filename}' not found. No students loaded.")
def save_students_to_csv(filename):
    try:
        with open(filename, 'w', newline='') as file:
            fieldnames = student_list[0].keys() if student_list else []
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(student_list)
        print("Students saved to CSV.")
    except Exception as e:
        print(f"Error saving students to CSV: {e}")

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
def delete_student():
    name = input("Please enter name to be deleted: ")
    students_to_delete = [student for student in student_list if student['name'] == name]  
    if students_to_delete:
        for student in students_to_delete:
            student_list.remove(student)
            print(f"Student '{student['name']}' has been deleted")
    else:
        print("Student not found")
def edit_student():
    name_to_edit = input("Please enter the name of the student to edit:")
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



            student_list.sort(key=lambda x: x['name'])
            print("Student list has been sorted by name.")
            return

    print(f"Student '{name_to_edit}' not found")

def main():
    while True:
        choice = input("Please specify the action [C create, D delete, E edit, P print, L load, S save, Q exit]: ")
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
        elif choice.upper() == "L":
            filename = input("Please enter the CSV filename to load: ")
            load_students_from_csv(filename)
        elif choice.upper() == "S":
            filename = input("Please enter the CSV filename to save: ")
            save_students_to_csv(filename)
        elif choice.upper() == "Q":
            print("Dosviduli")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
