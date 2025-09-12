class Student:
    count = 0

    def __init__(self, name, grade, student_id):
        self.name = name
        self._grade = grade
        self.__id = student_id
        Student.count += 1

    @classmethod
    def get_count(cls):
        return cls.count

    def get_id(self):
        return self.__id


s1 = Student("Nika", 90, 101)
s2 = Student("Ana", 85, 102)

print("Total students:", Student.get_count())
print("Student 1 ID:", s1.get_id())
print("Student 2 Grade:", s2._grade)