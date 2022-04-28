class Student(object):
    def __init__(self, name, age, gender, level, grades = None):
        self.name = name
        self.age = age
        self.gender = gender
        self.level = level
        self.grades = grades or {}

    def setgrade(self, course, grade):
        self.grades[course] = grade

    def getgrade(self, course):
        return self.grades[course]

    def getgpa(self):
        return sum(self.grades.values()) / len(self.grades)


john = Student("John", 12, "male", 6, {"math": 3.3})
jane = Student("Jane", 12, "female", 6, {"math": 3.5})

print(john.getgpa())
print(jane.getgpa())