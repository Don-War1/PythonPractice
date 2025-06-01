class Library:
    def __init__(self,bookslist):
        print("Welcome to Library")
        self.bookslist = bookslist
        self.borrowlist = {}

    def displaybooks(self):
        print("Available Books:")
        for b in self.bookslist:
            print(f"---{b}")

    def borrowbooks(self,bn,u):
        if bn in self.bookslist:
            self.borrowlist[bn] = u
            self.bookslist.remove(bn)
            print("Order placed successfully...")
        elif bn in self.borrowlist:
            print(f"{bn} book is currently available with {self.borrowlist[bn]}")
        else:
            print("Book not available at library..")

    def returnbook(self,bn,u):
        self.bookslist.append(bn)
        self.borrowlist.__delitem__(bn)
        print(f"{u} returned the book - {bn}")

l = Library(input().split())
while True:
    print("1: Available Books","2: Borrow book", "3: Return book", "4: Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        l.displaybooks()
    elif choice == 2:
        l.borrowbooks(input("Enter book name: "),input("Enter user name: "))
    elif choice == 3:
        l.returnbook(input("Enter book name: "),input("Enter user name: "))
    elif choice == 4:
        print("Thanks for visiting our library :)")
        break