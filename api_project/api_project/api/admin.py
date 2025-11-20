from django.contrib import admin
from .models import Book
# Register your models here.
class Bookadmin(admin.ModelAdmin):
    list_display=("title","author")
admin.site.register(Book,Bookadmin)