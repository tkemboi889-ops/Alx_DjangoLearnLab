from django.contrib.auth.views import LoginView
from django.urls import path
from .views import LibraryDetailView
#login  the user
from django.urls import path
#logout the user
from django.contrib.auth.views import LogoutView
from . import views



urlpatterns =[
    # Function-based view for listing all books
    path('books/',views.list_books, name='list-books'),

    # Class-based DetailView for a specific library
    path('library/<int:pk>/',views. LibraryDetailView.as_view(), name='library-detail'),

    # Class-based ListView for all libraries
    path('libraries/',views. LibrarylistView.as_view(), name='library-list'),
    path('logout/',views. LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('signup/', views.register, name='register'),
    path('admin-area/', views.admin_view, name='admin_view'),
    path('librarian-area/', views.librarian_view, name='librarian_view'),
    path('member-area/', views.member_view, name='member_view'),
    path('books/add/', views.add_book, name='add-book'),
    path('books/<int:book_id>/edit/', views.edit_book, name='edit-book'),
    path('books/<int:book_id>/delete/', views.delete_book, name='delete-book'),

   path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
]











