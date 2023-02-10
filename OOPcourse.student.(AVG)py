class Student():

    def __init__(self, fname, age, grade):
        self.fname = fname
        self.age = age 
        self.grade = grade # 0 - 100 

    def get_grade(self):
        return self.grade
    
class Course():

    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True 
        return False
    
    def get_avg_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        return value / len(self.students)

s1 = Student("Colby", 22, 97)
s2 = Student("charles", 49, 100)
s3 = Student("mackey", 76, 37)

course = Course("Computer Science", 3)
course.add_student(s1)
course.add_student(s2)
course.add_student(s3)
print(course.get_avg_grade())
