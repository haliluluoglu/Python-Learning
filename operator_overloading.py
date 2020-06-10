class Student:
    def __init__(self,mark1,mark2):
        self.mark1=mark1
        self.mark2=mark2
    def __add__(self, other):
        sum1=self.mark1+other.mark1
        sum2=self.mark1+other.mark2
        total=Student(sum1,sum2)
        return total
    def __sub__(self, other):
        sub1=self.mark1-other.mark1
        sub2=self.mark2-other.mark2
        substraction=Student(sub1,sub2)
        return substraction
    def __mul__(self, other):
        mul1=self.mark1*other.mark1
        mul2=self.mark2*other.mark2
        multiplication=Student(mul1,mul2)
        return multiplication
    def __ge__(self, other):
        sum1=self.mark1+self.mark2
        sum2=other.mark1+other.mark2
        if sum1==sum2:
            return True
        else:
            return False

    def __gt__(self, other):
        sum1=self.mark1+self.mark2
        sum2=other.mark1+other.mark2
        if sum1>sum2:
            return True
        else:
            return False

student1=Student(90,75)
student2=Student(90,70)

total=student1+student2
print("Totals of mark1 {} and mark2 {}".format(total.mark1, total.mark2))

if student1>student2:
    print("Student1 has marks greater than student2")
elif(student1<student2):
    print("Student2 has marks greater than student1")
else:
    print("The marks are equal for both students")

