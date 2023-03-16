class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True

class Borrower:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.books = []

    def borrow_book(self, book):
        if book.available:
            book.available = False
            self.books.append(book)
            print(f"{self.name} borrowed {book.title}.")
        else:
            print(f"Sorry, {book.title} is not available for borriwnig")

    def add_borrow(self,borrower):
        self.add_borrow.append(borrower)
    
    def remove_borrower(self,borrower):
        if borrower in self.borrower:
            self.borrwers.remove(borrower)
        else:
            print(f"{borrower.name} is not a registered borrower.")

    def search_books(self,search_term):
        results = []
        for book in self.books:
            if search_term in book.title or search_term in book.author or search_term in book.isbn:
                results.append(book)
        return results

    def sort_books(self,key):
        if key == "title":
            self.book.sort(key=lambda book: book.title)
        elif key == "author":
            self.book.sort(key=lambda book: book.author)

    def reserve_book(self,book,borrower):
        if book.available:
            borrower.borrow_book(book)
        else:
            print(f"{book.title} is already reserved by another customer")
        
    def display_books(self):
        for book in self.books:
            print(f"{book.title} by {book.author}, ISBN: {book.isbn}, Availavle: {book.availavle}")
        