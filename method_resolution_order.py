class A:
    def __init__(self):
        print("Class A init function")

    def feature1(self):
        print("Class A feature1 function")

class B:
    def __init__(self):
        print("Class B init function")
    def feature1(self):
        print("Class B feature1 function")

class C(A,B):
    def __init__(self):
        super().__init__()
        print("Class C init function")

class_c_object=C()