class A:
    def m1(self):
        print("  Hey Siri")
class B(A):
    def m2(self):
        print("  OK Google")

a,b = A(), B()
print("Class A")
a.m1()
print("Class B")
b.m1()
b.m2()