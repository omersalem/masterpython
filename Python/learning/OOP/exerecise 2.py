

class book:
        def __init__(self, title, author, year):
            self.title = title
            self.author = author
            self.year = year
            self.available = True
        
        def info(self):
            print(f'Title: {self.title}, Author: {self.author}, Year: {self.year}, Available: {self.available}')

class library:
        def __init__(self):
        
             
              self.books = [] # we used self so the variable books is available in all the methods of the class library
              # and this variable will belong to the class object created from the class library
            
        
        def add_book(self,book):
              self.books.append(book) #so here we used self.books to refer to the books variable in the class library

        def list_books(self,title):
                for book in self.books:
                    if book.title == title:
                          if book.available:
                                print(f'{book.title} is available.')
                                book.info()
                          else:
                                print(f'{book.title} is not available.')
                
        def borrow_book(self, title):
                for book in self.books:
                    if book.title == title:
                        if book.available:
                            book.available = False
                            print(f'You have borrowed {book.title}.')
                        else:
                            print(f'{book.title} is not available.')
        def return_book(self, title):
                for book in self.books:
                    if book.title == title:
                        if not book.available:
                            book.available = True
                            print(f'You have returned {book.title}.')
                        else:
                            print(f'{book.title} was not borrowed.')
        def search_book(self, title):
                for book in self.books:
                    if book.title == title:
                        print(f'{book.title} is available.')
                        book.info()
                        return
                print(f'{title} not found in the library.')


book1 = book('The Great Gatsby', 'F. Scott Fitzgerald', 1925)
book2 = book('To Kill a Mockingbird', 'Harper Lee', 1960)
book3 = book('1984', 'George Orwell', 1949)
lib= library()
lib.add_book(book1)
lib.add_book(book2)
lib.add_book(book3)
lib.list_books('The Great Gatsby')
lib.borrow_book('The Great Gatsby')
lib.return_book('The Great Gatsby')
lib.borrow_book('The Great Gatsby')
lib.search_book('The Great Gatsdfdfby')


        


              