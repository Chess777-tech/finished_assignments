class School:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.students = []
        self.teachers = []

    def add_student(self, student):
        self.students.append(student)
        print(f"{student} has been added to {self.name}.")

    def remove_student(self, student):
        if student in self.students:
            self.students.remove(student)
            print(f"{student} has been removed from {self.name}.")
        else:
            print(f"{student} is not enrolled in {self.name}.")

    def add_teacher(self, teacher):
        self.teachers.append(teacher)
        print(f"{teacher} has been added to {self.name}.")

    def remove_teacher(self, teacher):
        if teacher in self.teachers:
            self.teachers.remove(teacher)
            print(f"{teacher} has been removed from {self.name}.")
        else:
            print(f"{teacher} is not employed by {self.name}.")

# Example usage:
my_school = School("Example School", "123 Main St")
my_school.add_student("John Smith") # John Smith has been added to Example School.
my_school.add_teacher("Jane Doe") # Jane Doe has been added to Example School.
my_school.remove_student("John Doe") # John Doe is not enrolled in Example School.
my_school.remove_teacher("John Smith") 