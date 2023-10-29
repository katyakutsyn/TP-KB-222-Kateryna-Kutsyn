class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
students = [
    Student("Maximka", 12),
    Student("Bohdanckik", 21),
    Student("Alinochka", 96),
    Student("Katrusik", 69)
]
sorted_students = sorted(students, key=lambda student: student.name)

for student in sorted_students:
    print(f"Name: {student.name}, AGe: {student.age}")
