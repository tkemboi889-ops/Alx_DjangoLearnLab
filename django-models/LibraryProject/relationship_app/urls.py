from django.urls import path
from . import views
from .views import LibraryDetailView, LibrarylistView

urlpatterns = [
    # Function-based view for listing all books
    path('books/', views.list_books, name='list-books'),

    # Class-based DetailView for a specific library
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),

    # Class-based ListView for all libraries
    path('libraries/', LibrarylistView.as_view(), name='library-list'),
]


