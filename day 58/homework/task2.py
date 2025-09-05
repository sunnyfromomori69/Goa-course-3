class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def check_pass(self):
        return self.grade >= 50


s1 = Student("Alice", 75)
s2 = Student("Bob", 40)

print(s1.name, "passed?", s1.check_pass())  
print(s2.name, "passed?", s2.check_pass())  