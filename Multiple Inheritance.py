class A:
    def m1(self):
        print("   Hey Siri")
class B:
    def m2(self):
        print("   OK Google")
class C(A,B):
    def m3(self):
        print("   Hey Bixby")

a,b,c = A(), B(), C()
print("Class A")
a.m1()
print("Class B")
b.m2()
print("Class C")
c.m1()
c.m2()
c.m3()