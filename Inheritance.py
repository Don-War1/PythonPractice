class A:
    def m1(self):
        print("Hey Siri")
class B(A):
    def m2(self):
        print("OK Google")
class C(A):
    def m3(self):
        print("Hey Bixby")
class D(B,C):
    def m4(self):
        print("Hey Cortana")

d = D()
d.m2()
d.m3()
d.m4()