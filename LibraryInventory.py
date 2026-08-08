class Book:
    def __init__(self, title, author, available=True):
        self.title = title
        self.author = author
        self.available = available

class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
#Lambda functions to search  
    def search_by_title(self, title):
        search_title = lambda book: book.title.lower() == title.lower()
        return list(filter(search_title, self.books))
    
    def search_by_author(self, author):
        search_author = lambda book: book.author.lower() == author.lower()
        return list(filter(search_author, self.books))
    
    def update_availability(self, title, available):
        update_book = lambda book: setattr(book, 'available', available) if book.title.lower() == title.lower() else None
        list(map(update_book, self.books))

#Creating books
book1 = Book("How to cook eggs", "Taran Anderson")
book2 = Book("How to bake cakes", "Taran Anderson")
book3 = Book("How to fly a plane", "Joel Edwards")

#Instance of the Library class
library = Library()

#Add books to the library
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

#Functions to search by parameters
def search_books_by_title(library):
    title = input("Enter a book title to search: ")
    print(f"Books with title '{title}':")
    for book in library.search_by_title(title):
        print(f"- {book.title} by {book.author}")


def search_books_by_author(library):
    author = input("Enter an author to search: ")
    print(f"Books by author '{author}':")
    for book in library.search_by_author(author):
        print(f"- {book.title} by {book.author}")
        
#Update book availability
library.update_availability("How to bake cakes", False)

#Check updated availability
def check_book_availability(library):
    title = input("Enter a book title to check availability: ")

    print(f"\nAvailability of '{title}':")
    results = library.search_by_title(title)

    if not results:
        print("- No books found with that title.")
    else:
        for book in results:
            print(f"- {book.title} is {'available' if book.available else 'not available'}")


search_books_by_title(library)
search_books_by_author(library)
check_book_availability(library)
