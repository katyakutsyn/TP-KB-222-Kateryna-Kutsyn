import csv

def load_data(file_name):
    student_list = []
    with open(file_name, encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            student_list.append({
                "name": row["name"],
                "phone": row["phone"],
                "age": row["age"],
                "email": row["email"]
            })
    return student_list

def save_data(file_name, student_list):
    try:
        with open(file_name, "w", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["name", "phone", "age", "email"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(student_list)
        print("Data has been saved to the CSV file.")
    except IOError as e:
        print(f"Error saving data to {file_name}: {e}")

def print_all_list(student_list):
    for student in student_list:
        str_for_print = f"Student name is {student['name']}, Age is {student['age']}, Phone is {student['phone']}, Email is {student['email']}"
        print(str_for_print)

def add_new_element(student_list):
    name = input("Please enter student name: ")
    age = int(input("Please enter student age: "))
    phone = input("Please enter student phone: ")
    email = input("Please enter student email: ")
    new_student = {"name": name, "phone": phone, "age": age, "email": email}

    student_list.append(new_student)
    student_list.sort(key=lambda student: student["name"])
    print("New element has been added")

def delete_element(student_list):
    name = input("Please enter name to be deleted: ")
    for student in student_list:
        if name == student["name"]:
            student_list.remove(student)
            print("Element has been deleted")
            break
    else:
        print("Element was not found")

def update_element(student_list):
    name = input("Please enter name to be updated: ")
    for student in student_list:
        if name == student["name"]:
            student["name"] = input("Enter new name: ")
            student["age"] = input("Enter new age: ")
            student["phone"] = input("Enter new phone: ")
            student["email"] = input("Enter new email: ")
            student_list.sort(key=lambda student: student["name"])
            print("Element has been updated")
            break
    else:
        print("Student not found")

def main():
    file_name = input("Enter the CSV file name (e.g., lab2.csv): ")
    student_list = load_data(file_name)

    while True:
        choice = input("Please specify the action [C create, U update, D delete, S save, P print, Q exit]: ")
        if choice.upper() == "C":
            print("New element will be created:")
            add_new_element(student_list)
        elif choice.upper() == "U":
            print("Existing element will be updated")
            update_element(student_list)
        elif choice.upper() == "D":
            print("Element will be deleted")
            delete_element(student_list)
        elif choice.upper() == "P":
            print("List will be printed")
            print_all_list(student_list)
        elif choice.upper() == "S":
            save_data(file_name, student_list)
        elif choice.upper() == "Q":
            print("Dosviduli")
            break
        else:
            print("Dosviduli")

if __name__ == "__main__":
    main()
