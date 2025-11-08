
from django.shortcuts import render
from .models import Book

def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


from django.shortcuts import render
from django.views.generic .detail import DetailView
from .models import Library

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'

from django.shortcuts import render
from django.views.generic import ListView
from .models import Library

class LibrarylistView(ListView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    

