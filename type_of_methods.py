
class Student:
    school="YTÜ"

    def __init__(self,name,age,student_number):
        self.name=name
        self.age=age
        self.student_number=student_number

    def get_name(self):
        return self.name
    def set_name(self,value):
        self.name=value
    def get_age(self):
        return self.age
    def get_age(self,value):
        self.age=value
    def get_student_number(self):
        return self.student_number
    def get_student_number(self,value):
        self.student_number=value

    @classmethod
    def modify_school(cls):
        return (cls.school) + ("+CE")

    @staticmethod
    def info():
        print("This is a static method.")

student1=Student("Halil",21,1234)
student2=Student("Ibrahim",19,1235)

print(student1.get_name())
student1.set_name("Ibo")
print("Name of student1 has changed to: {}".format(student1.get_name()))

Student.modify_school()
print(student2.school)

Student.info()






