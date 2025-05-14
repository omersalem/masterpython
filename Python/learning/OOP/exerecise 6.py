class Book:
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies

    def show_info(self):
        print(f"Title: {self.title}, Author: {self.author}, Copies Available: {self.copies}")
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):  # book is an instance of Book
        self.books.append(book)

    def show_books(self):
        if not self.books:
            print("No books available.")
            return
        for book in self.books:
            book.show_info()

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and book.copies > 0:
                book.copies -= 1
                print(f"You borrowed '{book.title}'.")
                return
            elif book.title.lower() == title.lower():
                print(f"'{book.title}' is currently unavailable.")
                return
        print(f"Book '{title}' not found in the library.")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                book.copies += 1
                print(f"You returned '{book.title}'.")
                return
        print(f"Book '{title}' does not belong to this library.")
