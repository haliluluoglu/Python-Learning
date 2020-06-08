class Student:
    school="YTU,BM"
    def __init__(self,name,student_number):
        self.name=name
        self.student_number=student_number
    def info(self):
        print("Student name: ", self.name, "Student number: ", self.student_number)

    class Laptop:
        def __init__(self,brand,cpu,ram):
            self.brand=brand
            self.cpu=cpu
            self.ram=ram
        def info(self):
            print("Brand", self.brand, "Cpu", self.cpu, "Ram", self.ram)


student1=Student("Halil", 12345)
laptop1=Student.Laptop("Lenovo", "i9", 16)

student1.info()
laptop1.info()


