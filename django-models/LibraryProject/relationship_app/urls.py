from django.urls import path
from .views import list_books
from .views import LibraryDetailView,LibrarylistView

urlpatterns = [
    # Function-based view for listing all books
    path('books/', list_books, name='list-books'),

    # Class-based DetailView for a specific library
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),

    # Class-based ListView for all libraries
    path('libraries/', LibrarylistView.as_view(), name='library-list'),
]
#login  the user
from django.contrib.auth.views import LoginView
from django.urls import path

urlpatterns = [
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
]
#logout the user
from django.contrib.auth.views import LogoutView
from django.urls import path

urlpatterns = [
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
]


from . import views
urlpatterns[
path('signup/', views.register, name='register') 
 ]


