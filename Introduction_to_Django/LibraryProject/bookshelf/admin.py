from django.contrib import admin

# Register your models here.
from.models import Book
# Create a custom admin class
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # show these fields in list view
    search_fields = ('title', 'author')  # allow searching by title or author
    list_filter = ('publication_year',)  # add a filter by publication year

# Register the model with the custom admin
admin.site.register(Book, BookAdmin)