import csv

list = [
    {"name": "Bob", "phone": "0631234567", "age": 20, "email": "bob@gmail.com"},
    {"name": "Emma", "phone": "0631234567", "age": 22, "email": "emma@gmail.com"},
    {"name": "Jon", "phone": "0631234567", "age": 21, "email": "jon@gmail.com"},
    {"name": "Zak", "phone": "0631234567", "age": 19, "email": "zak@gmail.com"}
]

def save_to_csv(student_list, filename):
    try:
        with open(filename, "w", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["name", "age", "phone", "email"]
            csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
            csvwriter.writeheader()
            csvwriter.writerows(student_list)
        print("Data has been saved to the CSV file.")
    except IOError as e:
        print(f"Error saving data to {filename}: {e}")

def printAllList():
    for student in list:
        strForPrint = f"Student name is {student['name']}, Age is {student['age']}, Phone is {student['phone']}, Email is {student['email']}"
        print(strForPrint)

def addNewElement():
    name = input("Please enter student name: ")
    age = int(input("Please enter student age: "))
    phone = input("Please enter student phone: ")
    email = input("Please enter student email: ")
    new_student = {"name": name, "phone": phone, "age": age, "email": email}

    list.append(new_student)
    list.sort(key=lambda student: student["name"])
    print("New element has been added")

def deleteElement():
    name = input("Please enter name to be deleted: ")
    for student in list:
        if name == student["name"]:
            list.remove(student)
            print("Element has been deleted")
            break
    else:
        print("Element was not found")

def updateElement():
    name = input("Please enter name to be updated: ")
    for student in list:
        if name == student["name"]:
            student["name"] = input("Enter new name: ")
            student["age"] = input("Enter new age: ")
            student["phone"] = input("Enter new phone: ")
            student["email"] = input("Enter new email: ")
            list.sort(key=lambda student: student["name"])
            print("Element has been updated")
            break
    else:
        print("Student not found")

def main():
    while True:
        choice = input("Please specify the action [C create, U update, D delete, S save, P print, Q exit]: ")
        if choice.upper() == "C":
            print("New element will be created:")
            addNewElement()
        elif choice.upper() == "U":
            print("Existing element will be updated")
            updateElement()
        elif choice.upper() == "D":
            print("Element will be deleted")
            deleteElement()
        elif choice.upper() == "P":
            print("List will be printed")
            printAllList()
        elif choice.upper() == "S":
            file_name = input("Enter the CSV file name (e.g., lab2.csv) to save data to: ")
            if not file_name.endswith(".csv"):
                file_name += ".csv"  
            save_to_csv(list, file_name) 
        elif choice.upper() == "Q":
            print("Dosviduli")
            break
        else:
            print("Dosviduli")

if __name__ == "__main__":
    main()