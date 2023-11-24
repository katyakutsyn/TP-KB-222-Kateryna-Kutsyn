
class StudentList:
    def __init__(self):
        self.student_list = []

    def add_student(self, student):
        self.student_list.append(student)

    def delete_student(self, name):
        for student in self.student_list:
            if name == student.name:
                self.student_list.remove(student)
                return True
        return False

    def update_student(self, name, new_student):
        for student in self.student_list:
            if name == student.name:
                student.name = new_student.name
                student.age = new_student.age
                student.phone = new_student.phone
                student.email = new_student.email
                return True
        return False

    def get_all_students(self):
        return self.student_list
