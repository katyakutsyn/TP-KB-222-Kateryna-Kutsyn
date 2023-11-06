

list = [
    {"name": "Bob", "phone": "0631234567", "age": 20, "email": "bob@gmail.com"},
    {"name": "Emma", "phone": "0631234567", "age": 22, "email": "emma@gmail.com"},
    {"name": "Jon", "phone": "0631234567", "age": 21, "email": "jon@gmail.com"},
    {"name": "Zak", "phone": "0631234567", "age": 19, "email": "zak@gmail.com"}
]

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
    
    insert_position = 0
    for student in list:
        if name > student["name"]:
            insert_position += 1
        else:
            break

    list.insert(insert_position, new_student)
    print("New element has been added")

def deleteElement():
    name = input("Please enter name to be deleted: ")
    deletePosition = -1
    for student in list:
        if name == student["name"]:
            deletePosition = list.index(student)
            break
    if deletePosition == -1:
        print("Element was not found")
    else:
        del list[deletePosition]
        print("Element has been deleted")

def updateElement():
    name = input("Please enter name to be updated: ")
    for index, student in enumerate(list):
        if name == student["name"]:
            new_name = input("Enter new name: ")
            new_age = input("Enter new age: ")
            new_phone = input("Enter new phone: ")
            new_email = input("Enter new email: ")
            newElement = {"name": new_name, "age": new_age, "phone": new_phone, "email": new_email}

            del list[index]
            insertPos = 0
            for pos, elem in enumerate(list):
                if new_name > elem["name"]:
                    insertPos = pos + 1
                else:
                    break
            list.insert(insertPos, newElement)
            print("Element has been updated")
            break
    else:
        print("Student not found")

def main():
    while True:
        choice = input("Please specify the action [C create, U update, D delete, P print, Q exit]: ")
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
        elif choice.upper() == "Q":
            print("Exit")
            break
        else:
            print("Dosviduli")

if __name__ == "__main__":
    main()
