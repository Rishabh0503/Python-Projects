class Library:
    def __init__(self,listOfBooks):
        self.books = listOfBooks

    def displayAvailableBooks(self):
        print("Books present n this library are: ")
        for book in self.books:
            print("*",book)

    def borrowBook(self,bookName):
        if bookName in self.books:
            print(f"You have been issued the book named {bookName.upper()}")
            self.books.remove(bookName)
            return True
            print()
        else:
            print(f"Sorry the book name {bookName.upper()} is not available.")
            return False
            print()

    def returnBook(self,bookName):
        self.books.append(bookName)
        print(f"Thanks for returning the book named {bookName.upper()}")

class Student:
    def requestBook(self):
        self.book = input("Enter the name of book you want to borrow: ")
        return self.book

    def returnBook(self):
        self.book = input("Enter the name of the book you want to return: ")
        return self.book


if __name__ == "__main__":
    centralibrary = Library (["Data structure and algorithm","Atomic Habit","IKIGAI","Lord Of Rings","Da Vinci Code" ])
    student = Student()
    # centralibrary.displayAvailableBooks()
    while True:
        greetMsg = """\t**** WELCOME TO CENTRAL LIBRARY **** \t
        Choose an Option: 
        1. Listing all the books 
        2. Request a book
        3. Return a book
        4. Exit the library
        """
        print(greetMsg)
        print()
        choice = int(input("Enter your choice: "))
        if choice == 1:
            centralibrary.displayAvailableBooks()
        elif choice == 2:
            centralibrary.borrowBook(student.requestBook())
        elif choice == 3:
           centralibrary.returnBook(student.returnBook())
        elif choice == 4:
            print("Thanks for choosing CENTRAL LIBRARY !!!!")
            quit()
        else:
            print("Invalid option. Kindly select the mentioned options.")


        
