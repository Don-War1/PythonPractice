class Sample:
    def __init__(self):
        print("Object created...")

    def wish(self,name):
        print(f"Hello {name}")

    def __del__(self):
        print("Object destroyed...")

S = Sample()
s_name = input("Enter your name: ")
for i in range(int(input("Enter the frequency: "))):
    S.wish(s_name)