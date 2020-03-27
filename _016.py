class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__hello = 1
    
    def getInfo(self):
        return "Person { name : %s, age : %d } " % (self.name, self.age)

class Student(Person):
    def __init__(self, name, age, studentID):
        self.name = name
        self.age = age
        self.studentID = studentID
    
    def getInfo(self):
        return "Student { name : %s, age : %d, studentID : %d }" % (self.name, self.age, self.studentID)

class Teacher(Person):
    def __init__(self, name, age, teacherID):
        self.name = name
        self.age = age
        self.teacherID = teacherID
    
    def getInfo(self):
        return "Teacher { name : %s, age : %d, teacherID : %d }" % (self.name, self.age, self.teacherID)

p = Person('Coalery', 19)
print(p.getInfo())

s = Student('Hello', 17, 10101)
print(s.getInfo())

t = Teacher('Teacher', 27, 12)
print(t.getInfo())