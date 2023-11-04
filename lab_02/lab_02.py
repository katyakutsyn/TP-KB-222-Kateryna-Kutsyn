import csv

def load_students_from_csv(filename, student_list):
    try:
        with open(filename, newline='') as file:
            reader = csv.DictReader(file)
            student_list.extend(row for row in reader)
        print("Students loaded from CSV.")
    except FileNotFoundError:
        print(f"File '{filename}' not found. No students loaded.")

def save_students_to_csv(filename, student_list):
    try:
        with open(filename, 'w', newline='') as file:
            fieldnames = student_list[0].keys() if student_list else []
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(sorted(student_list, key=lambda x: x['name']))
        print("Students saved to CSV.")
    except Exception as e:
        print(f"Error saving students to CSV: {e}")

def print_all_students(student_list):
    for student in student_list:
        print(f"Name: {student['name']}, Phone: {student['phone']}, Email: {student['email']}, Group: {student['group']}")

def add_new_student(student_list, name, phone, email, group):
    new_student = {"name": name, "phone": phone, "email": email, "group": group}

    student_list.append(new_student)
    student_list.sort(key=lambda x: x['name'])
    print("New student has been added and the student list has been sorted.")

def delete_student(student_list, name):
    students_to_delete = [student for student in student_list if student['name'] == name]
    if students_to_delete:
        for student in students_to_delete:
            student_list.remove(student)
            print(f"Student '{student['name']}' has been deleted.")
    else:
        print("Student not found.")

def edit_student(student_list, name_to_edit):
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
            student_list.sort(key=lambda x: x['name'])
            print(f"Student '{name_to_edit}' has been updated, and the student list has been sorted.")
            return
    print(f"Student '{name_to_edit}' not found.")

def main():
    student_list = []

    while True:
        choice = input("Please specify the action [C create, D delete, E edit, P print, L load, S save, Q exit]: ")
        if choice.upper() == "C":
            print("Creating a new student:")
            add_new_student(student_list, input("Please enter student name: "), input("Please enter student phone: "), input("Please enter student email: "), input("Please enter student group: "))
        elif choice.upper() == "D":
            print("Deleting a student:")
            delete_student(student_list, input("Please enter name to be deleted: "))
        elif choice.upper() == "E":
            print("Editing a student:")
            edit_student(student_list, input("Please enter the name of the student to edit: "))
        elif choice.upper() == "P":
            print("Printing the student list:")
            print_all_students(student_list)
        elif choice.upper() == "L":
            filename = input("Please enter the CSV filename to load: ")
            load_students_from_csv(filename, student_list)
        elif choice.upper() == "S":
            filename = input("Please enter the CSV filename to save: ")
            save_students_to_csv(filename, student_list)
        elif choice.upper() == "Q":
            print("Dosviduli")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()





