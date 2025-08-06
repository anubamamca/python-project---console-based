
class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
        self.is_available = True            # Availability status (default: available)

    def __str__(self):
        return f"Title : {self.title} \n Author : {self.author} \n Available : {'Yes' if self.is_available else 'No'}"

class Library:
    def __init__(self):
        self.books = []                     # List to store book objects
    def add_book(self,book):
        self.books.append(book)             # Add a book to the library's collection
    def display_books(self):                # Display all books in the library
        if self.books:
            print("Books available in the library:")
            for book in self.books:
                print(book)                 # Uses the __str__ method of Book class
        else:
            print("No books are availalbe in the library")
    def lend_book(self,title):
        for book in self.books:
            if book.title == title:
                if book.is_available:
                    book.is_available = False
                    print(f"You have borrowed '{book.title}'.Enjoy Reading!")
                else:
                    print(f"Sorry, '{book.title}' is currently not available")
                return
        print("Book not found in the Library.")
    def return_book(self,title):
        for book in self.books:
            if book.title == title:
                book.is_available = True
                print(f"Thank you for returning '{book.title}'.")
                return
        print("Book is not found in the library.")
    def display_options(self):               # Display menu options to the user
        print("\nOptions: ")
        print("1. Display All Books")
        print("2. Borrow a Book")
        print("3. Return a Book")
        print("4. Exit")

library = Library()
book1 = Book("Python Programming","Raman")
book2 = Book("Mastering Java","John")
book3 = Book("Learn Web Designing","Sam")
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
# Infinite loop to keep the program running until the user exits
while True:
    library.display_options()
    choice = input("Enter your Choice: ")
    if choice == '1':
        library.display_books()
    elif choice == '2':
        title = input("Enter the Title of the Book:")
        library.lend_book(title)
    elif choice == '3':
        title = input("Enter the Title of the Book:")
        library.return_book(title)
    elif choice == '4':
        print("Exiting the Library. Thank you!!!")
        exit()
    else:
        print("Invalid Choice. Please select a Valid Option")    # Invalid input handling
