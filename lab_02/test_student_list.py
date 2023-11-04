from lab_02 import add_new_student, save_students_to_csv

def test_add_new_student():
    student_list = []
    initial_length = len(student_list)

    add_new_student(student_list, "Alice", "1234567890", "alicka", "A")

    assert len(student_list) == initial_length + 1
    assert student_list[-1] == {
        "name": "Alice",
        "phone": "1234567890",
        "email": "alicka",
        "group": "A"
    }
    
    # Тут ви додаєте код для збереження у CSV після додавання студента
    save_students_to_csv('students.csv', student_list)

    # Додайте інші тестові випадки за необхідності

   

