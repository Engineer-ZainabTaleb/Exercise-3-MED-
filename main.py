
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.is_checked_out = False

    def checkout(self):
        self.is_checked_out = True

    def return_book(self):
        self.is_checked_out = False

    def __str__(self):
        return f"{self.year} by {self.author} - {self.title} (Checked out: {self.is_checked_out})"


class Library:
    def __init__(self):
        self.collection = []

    def add_book(self, book):
        self.collection.append(book)

    def list_books(self):
        if not self.collection:
            print("The library is empty.")
            return

        for book in self.collection:
            print(book)

    def find_book(self, title):
        for book in self.collection:
            if book.title.lower() == title.lower():
                return book

        return None



library = Library()

book1 = Book("1984", "George Orwell", 1949)
book2 = Book("The Hobbit", "J.R.R. Tolkien", 1937)
book3 = Book("Animal Farm", "George Orwell", 1945)


library.add_book(book1)
library.add_book(book2)
library.add_book(book3)


print("=== All Books ===")
library.list_books()

print("\n=== Checking Out a Book ===")
book1.checkout()
print(book1)
print("\n=== Returning the Book ===")
book1.return_book()
print(book1)
print("\n=== Searching for a Book ===")
found_book = library.find_book("the hobbit")

if found_book:
    print("Book found:", found_book)
else:
    print("Book not found.")
