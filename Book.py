class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True

    # Getter methods
    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_isbn(self):
        return self.isbn

    def is_available(self):
        return self.available

    # Setter methods
    def set_title(self, title):
        self.title = title

    def set_author(self, author):
        self.author = author

    def set_isbn(self, isbn):
        self.isbn = isbn

    def set_available(self, available):
        self.available = available

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.get_title()}' added to the library.")

    def borrow_book(self, isbn):
        for book in self.books:
            if book.get_isbn() == isbn:
                if book.is_available():
                    book.set_available(False)
                    print(f"Book '{book.get_title()}' has been borrowed.")
                    return
                else:
                    print(f"Book '{book.get_title()}' is already borrowed.")
                    return
        print(f"No book with ISBN {isbn} found in the library.")

    def return_book(self, isbn):
        for book in self.books:
            if book.get_isbn() == isbn:
                if not book.is_available():
                    book.set_available(True)
                    print(f"Book '{book.get_title()}' has been returned.")
                    return
                else:
                    print(f"Book '{book.get_title()}' was not borrowed.")
                    return
        print(f"No book with ISBN {isbn} found in the library.")

    def display_available_books(self):
        available_books = [book for book in self.books if book.is_available()]
        if available_books:
            print("Available books in the library:")
            for book in available_books:
                print(f"Title: {book.get_title()}, Author: {book.get_author()}, ISBN: {book.get_isbn()}")
        else:
            print("No books are currently available in the library.")

# Main class to demonstrate functionality
def main():
    library = Library()

    # Add some books to the library
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "1234567890")
    book2 = Book("To Kill a Mockingbird", "Harper Lee", "0987654321")
    book3 = Book("1984", "George Orwell", "1122334455")

    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    # Display available books
    library.display_available_books()

    # Borrow a book
    library.borrow_book("1234567890")

    # Display available books
    library.display_available_books()

    # Try to borrow the same book again
    library.borrow_book("1234567890")

    # Return a book
    library.return_book("1234567890")

    # Display available books
    library.display_available_books()

    # Try to return a book that was not borrowed
    library.return_book("1234567890")

    # Borrow a book that does not exist
    library.borrow_book("0000000000")

    # Return a book that does not exist
    library.return_book("0000000000")

if __name__ == "__main__":
    main()
