class Employee:
    def setName(self,name):
        self.name = name

    def setID(self,id):
        self.id = id

    def setSalary(self,salary):
        self.salary = salary

    def getName(self):
        return self.name

    def getID(self):
        return self.id

    def getSalary(self):
        return self.salary

l = []
for i in range(int(input("Enter the no.of employees: "))):
    E = Employee()
    E.setName(input("Enter name: "))
    E.setID(input("Enter ID: "))
    E.setSalary(float(input("Enter Salary: ")))
    l.append(E)
print()
count = 1
for emp in l:
    print(f"Employee-{count} details")
    print("-"*15)
    print(f"Name: {emp.getName()}")
    print(f"ID: {emp.getID()}")
    print(f"Salary: {emp.getSalary()}")
    print("-" * 15)
    print()
    count += 1