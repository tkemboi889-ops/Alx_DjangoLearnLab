from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book
# Expected Output:
# <Book: 1984 by George Orwell>
from bookshelf.models import Book
books = Book.objects.all()
for b in books:
    print(b.id, b.title, b.author, b.publication_year)
# Expected Output:
# 1 1984 George Orwell 1949
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
print(book.title)
# Expected Output:
# Nineteen Eighty-Four
from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
Book.objects.all()
# Expected Output:
# <QuerySet []>  (means no books exist)
