class Student:
    def __init__(self, student_id, name, age, major):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.major = major

    def update_details(self, name=None, age=None, major=None):
        if name:
            self.name = name
        if age:
            self.age = age
        if major:
            self.major = major

    def display(self):
        print(f"ID: {self.student_id}, Name: {self.name}, Age: {self.age}, Major: {self.major}")


class StudentRepository:
    def __init__(self):
        self.students = {}

    def add_student(self, student):
        self.students[student.student_id] = student

    def remove_student(self, student_id):
        if student_id in self.students:
            del self.students[student_id]

    def get_student(self, student_id):
        return self.students.get(student_id)

    def get_all_students(self):
        return self.students.values()


class StudentManagementSystem:
    def __init__(self, repository):
        self.repository = repository

    def add_student(self, student_id, name, age, major):
        student = Student(student_id, name, age, major)
        self.repository.add_student(student)

    def delete_student(self, student_id):
        self.repository.remove_student(student_id)

    def update_student_info(self, student_id, name=None, age=None, major=None):
        student = self.repository.get_student(student_id)
        if student:
            student.update_details(name, age, major)

    def show_all_students(self):
        for student in self.repository.get_all_students():
            student.display()


# Example Usage
repository = StudentRepository()
system = StudentManagementSystem(repository)

system.add_student(1, "John Doe", 20, "Computer Science")
system.add_student(2, "Jane Smith", 22, "Mathematics")
system.show_all_students()
system.update_student_info(1, name="Johnathan Doe")
system.show_all_students()
system.delete_student(2)
system.show_all_students()
