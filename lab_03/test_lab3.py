import unittest
from Student import Student
from StudentList import StudentList

class TestStudentList(unittest.TestCase):
    def setUp(self):
        self.student_list = StudentList()

    def test_student_list_initialization(self):
        self.assertEqual(len(self.student_list.get_all_students()), 0)

    def test_student_list_add_student(self):
        student = Student("John", "1234567890", 20, "john@example.com")
        self.student_list.add_student(student)
        students = self.student_list.get_all_students()
        self.assertEqual(len(students), 1)
        self.assertIn(student, students)

    def test_student_list_delete_student(self):
        student = Student("John", "1234567890", 20, "john@example.com")
        self.student_list.add_student(student)
        self.student_list.delete_student("John")
        self.assertEqual(len(self.student_list.get_all_students()), 0)

if __name__ == '__main__':
    unittest.main()
