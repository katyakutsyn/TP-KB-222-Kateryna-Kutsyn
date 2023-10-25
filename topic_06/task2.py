students = [
    {"name": "Alina", "grade": 69},
    {"name": "Bohdan", "grade": 92},
    {"name": "Emelia", "grade": 77},
    {"name": "Andriy", "grade": 10}
]
def add_student(name, grade):
    new_student = {"name": name, "grade": grade}
    students.append(new_student)
    students.sort(key=lambda x: x["name"])

while True:
    print("Поточний список студентв:")
    for student in students:
        print(f"Ім'я: {student['name']}, Оцінка: {student['grade']}")
    name = input("Введіть імя нового студента (або 'q' для виходу): ")
    if name.lower() == 'q':
        break

    try:
        grade = int(input("Введіть оцінку нового студента: "))
        add_student(name, grade)
    except ValueError:
        print("Некоректне значення оцінки. У вас ще є спроба, а може і ні.")

sorted_by_name = sorted(students, key=lambda x: x["name"])
print("Список відсортований за ім'ям:")
for student in sorted_by_name:
    print(f"Ім'я: {student['name']}, Оцінка: {student['grade']}")

sorted_by_grade = sorted(students, key=lambda x: x["grade"])
print("список відсортований за оцінкою:")
for student in sorted_by_grade:
    print(f"Ім'я: {student['name']}, Оцінка: {student['grade']}")
