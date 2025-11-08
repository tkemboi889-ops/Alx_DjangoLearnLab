from django.urls import path
from .views import list_books
from .import LibraryDetailView,LibrarylistView

urlpatterns = [
    # Function-based view for listing all books
    path('books/', list_books, name='list-books'),

    # Class-based DetailView for a specific library
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),

    # Class-based ListView for all libraries
    path('libraries/', LibrarylistView.as_view(), name='library-list'),
]


