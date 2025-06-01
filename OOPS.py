class ATM:
    atm_name = "SBI"
    def __init__(self):
        self.pin = 1234
        self.balance = 10000.0
        self.count = 0

    def checkuser(self,pin):
        if self.pin == pin:
            print("Valid User")
            self.atm_op()
        else:
            print("Invalid User")
            self.count += 1
            if self.count<3:
                pin = int(input("Enter the PIN: "))
                self.checkuser(pin)
            else:
                print("Your ATM has been blocked, kindly visit the nerest branch")

    def deposit(self,amt):
        self.balance += amt
        print(f"{amt} has been credited to your account")
        print(f"Account balance: {self.balance}")

    def withdrawal(self,amt):
        if amt<=self.balance and amt%100 == 0:
           self.balance -= amt
           print(f"{amt} has been debited from your account")
           print(f"Account balance: {self.balance}")
        else:
            print("Transaction failed, please try again")

    def checkbalance(self):
        print(f"Account balance: {self.balance}")

    def atm_op(self):
        while True:
            print("-"*20)
            print("1:Deposit", "2:Withdrawal", "3:Balance", "4:Exit", sep="\n")
            choice = int(input())
            if choice==1:
                amt = int(input("Enter the amount: "))
                self.deposit(amt)
            elif choice==2:
                amt = int(input("Enter the amount: "))
                self.withdrawal(amt)
            elif choice==3:
                self.checkbalance()
            elif choice == 4:
                print(f"Thanks for visiting {self.atm_name} bank...")
                break

A = ATM()
A.checkuser(int(input("Enter the PIN: ")))