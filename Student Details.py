class Student:
    def __init__(self,name,rollno,email):
        self.name = name
        self.rollno = rollno
        self.email = email

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Roll No: {self.rollno}")
        print(f"Email ID: {self.email}")

S = Student("s1","123","ex@gmail.com")
S.display_details()