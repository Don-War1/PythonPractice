class Student:
    def __init__(self,name,email,mobile,branch):
        self.name = name
        self.email = email
        self.mobile = mobile
        self.branch = branch

for i in range(int(input("Enter the no.of students: "))):
    S = Student(input("Enter name: "),input("Enter email: "),int(input("Enter mobile no: ")),input("Enter branch: "))
    print(S.__dict__)
    delattr(S, 'name')
    print(S.__dict__)