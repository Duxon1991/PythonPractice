class Person:
    def __init__(self,name,sex,profession):
        self.name = name
        self.sex = sex
        self.profession = profession

    def show(self):
        print("Hi my name is ", self.name, ", my sex is ", self.sex,"and I work as ", self.profession)

    def work(self):
        print("I'm a ", self.sex, "working as a ", self.profession)

class Student:
    my_School = "Roydon School"

    def __init__(self,name,age):

        self.name = name
        self.age = age

    def show(self):
        print("Student: ",self.name, ", Age: ", self.age, "School: ", self.my_School)

    def change_name(self, new_name):
        self.name = new_name

    def change_school(cls, new_school):
        cls.my_School = new_school

s1 = Student("Michael",29)

print(Student.my_School)
print(s1.name, s1.age)

Student.my_School = "st Andrews School"

s1.change_name("Emma")
s1.change_school("Presdales")

print(Student.my_School)
print(s1.name, s1.age)

s1.show()

Michael = Person("Michael","Male","Systems Analyst")

Michael.show()
Michael.work()
