
class Student:

    def __init__(self,name,grade):
        self.name = name
        self.grade = grade

    def get_grade(self):
        return self.grade

class Course:

    def __init__(self,name,max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_students(self,student):
        if len(self.students)< self.max_students:
            self.students.append(student)
            return True        
        return False

    def get_avg_grade(self):
        total = 0
        for student in self.students:
            total+= student.get_grade()

        return total/len(self.students)

s1 =  Student("John",69)
s2 = Student("Tom",75)
s3 = Student("Max",67)

course = Course("Science" , 2)
course.add_students(s1)
print(course.add_students(s2))

print(course.add_students(s3))

print(course.get_avg_grade())