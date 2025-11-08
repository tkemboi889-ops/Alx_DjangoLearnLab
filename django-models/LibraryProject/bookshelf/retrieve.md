from bookshelf.models import Book
books = Book.objects.get()
for b in books:
    print(b.id, b.title, b.author, b.publication_year)
# Expected Output:
# 1 1984 George Orwell 1949
