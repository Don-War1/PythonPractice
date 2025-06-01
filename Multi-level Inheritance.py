class A:
    def m1(self):
        print("   Hey Siri")
class B(A):
    def m2(self):
        print("   OK Google")
class C(B):
    def m3(self):
        print("   Hey Bixby")
class D(C):
    def m4(self):
        print("   Hey Cortana")

a,b,c,d = A(), B(), C(), D()
print("Class A")
a.m1()
print("Class B")
b.m1()
b.m2()
print("Class C")
c.m1()
c.m2()
c.m3()
print("Class D")
d.m1()
d.m2()
d.m3()
d.m4()