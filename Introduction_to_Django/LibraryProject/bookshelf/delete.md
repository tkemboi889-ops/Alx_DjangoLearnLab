book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
Book.objects.all()
# Expected Output:
# <QuerySet []>  (means no books exist)
