# Write a Program to create a class by name
# Students, and initialize attributes like name, age, and grade
# while creating an object.

class Students:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade


pawan = Students("Pawan Kumar", 21, 12)
print(pawan.name)

