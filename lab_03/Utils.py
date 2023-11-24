
import csv
from Student import Student  
class FileUtils:
    @staticmethod
    def load_data(file_name):
        student_list = []
        with open(file_name, encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                student = Student(row["name"], row["phone"], row["age"], row["email"])
                student_list.append(student)
        return student_list

    @staticmethod
    def save_data(file_name, student_list):
        try:
            with open(file_name, "w", newline="", encoding="utf-8") as csvfile:
                fieldnames = ["name", "phone", "age", "email"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for student in student_list:
                    writer.writerow({
                        "name": student.name,
                        "phone": student.phone,
                        "age": student.age,
                        "email": student.email
                    })
            print("Data has been saved to the CSV file.")
        except IOError as e:
            print(f"Error saving data to {file_name}: {e}")
