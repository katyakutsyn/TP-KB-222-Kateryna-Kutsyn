
from Student import Student
from StudentList import StudentList
from Utils import FileUtils

def main():
    file_name = input("Enter the CSV file name (e.g., lab3.csv): ")
    student_list = FileUtils.load_data(file_name)
    group = StudentList()
    group.student_list = student_list

    while True:
        choice = input("Please specify the action [C create, U update, D delete, S save, P print, Q exit]: ")
        if choice.upper() == "C":
            print("New element will be created:")
            name = input("Please enter student name: ")
            age = int(input("Please enter student age: "))
            phone = input("Please enter student phone: ")
            email = input("Please enter student email: ")
            new_student = Student(name, phone, age, email)
            group.add_student(new_student)
        elif choice.upper() == "U":
            print("Existing element will be updated")
            name = input("Please enter name to be updated: ")
            new_name = input("Enter new name: ")
            new_age = int(input("Enter new age: "))
            new_phone = input("Enter new phone: ")
            new_email = input("Enter new email: ")
            updated_student = Student(new_name, new_phone, new_age, new_email)
            updated = group.update_student(name, updated_student)
            if not updated:
                print("Student not found")
        elif choice.upper() == "D":
            print("Element will be deleted")
            name = input("Please enter name to be deleted: ")
            deleted = group.delete_student(name)
            if not deleted:
                print("Student not found")
        elif choice.upper() == "P":
            print("List will be printed")
            all_students = group.get_all_students()
            for student in all_students:
                str_for_print = f"Student name is {student.name}, Age is {student.age}, Phone is {student.phone}, Email is {student.email}"
                print(str_for_print)
        elif choice.upper() == "S":
            FileUtils.save_data(file_name, group.student_list)
        elif choice.upper() == "Q":
            print("Dosviduli")
            break
        else:
            print("Dosviduli")

if __name__ == "__main__":
    main()
