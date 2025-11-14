import os
import django

# Django setup
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookshelf.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian


#  Get all books by a specific author
def get_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)
    print(f"Books by {author_name}:")
    for book in books:
        print(f" - {book.title}")


#  List all books in a library
def list_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    print(f"Books in {library_name}:")
    for book in books:
        print(f" - {book.title}")


#  Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = Librarian.objects.get(library=library)
    print(f"Librarian for {library_name}: {librarian.name}")


if __name__ == "__main__":
    # Example calls — use names that exist in your database
    get_books_by_author("J.K. Rowling")
    list_books_in_library("Central Library")
    get_librarian_for_library("Central Library")
