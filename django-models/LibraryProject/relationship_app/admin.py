from django.contrib import admin
from .models import Book, Library,Librarian,Author

admin.site.register(Book)
admin.site.register(Library)
admin.site.register(Author)
admin.site.register(Librarian)
