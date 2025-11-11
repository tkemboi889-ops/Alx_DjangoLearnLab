from django.urls import path
from .views import list_books
from .views import LibraryDetailView,LibrarylistView
#login  the user
from django.contrib.auth.views import LoginView
from django.urls import path
#logout the user
from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views
from django.urls import path


urlpatterns =[
    # Function-based view for listing all books
    path('books/', list_books, name='list-books'),

    # Class-based DetailView for a specific library
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),

    # Class-based ListView for all libraries
    path('libraries/', LibrarylistView.as_view(), name='library-list'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path'signup/', views.register, name='register',
    path('admin-area/', views.admin_view, name='admin_view'),
    path('librarian-area/', views.librarian_view, name='librarian_view'),
    path('member-area/', views.member_view, name='member_view'),

   path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
]











