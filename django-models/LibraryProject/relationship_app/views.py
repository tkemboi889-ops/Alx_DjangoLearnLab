from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from django.shortcuts import render
from .models import Book
from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Library
from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Library
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseForbidden


def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'


class LibrarylistView(ListView):
    model = Library
    template_name = 'relationship_app/library_detail.html'



class SignupView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration.html"


class UserLoginView(LoginView):
    template_name = 'login.html'


class UserLogoutView(LogoutView):
    template_name = 'logout.html'

    

# Helper tests
def is_admin(user):
 return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'


def is_librarian(user):
 return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'


def is_member(user):
 return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'


# Admin view (file name: admin_view)

@user_passes_test(is_admin)
@login_required
def admin_view(request):
# Returns a page for Admin users only
  return render(request, 'admin_view.html', {
'user': request.user,
})


# Librarian view (file name: librarian_view)
@login_required
@user_passes_test(is_librarian)
def librarian_view(request):
 return render(request, 'librarian_view.html', {
'user': request.user,
})


# Member view (file name: member_view)
@login_required
@user_passes_test(is_member)
def member_view(request):
 return render(request, 'member_view.html', {
'user': request.user,
})

@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        description = request.POST.get('description')
        Book.objects.create(title=title, author=author, description=description)
        return redirect('book-list')
    return render(request, 'relationship_app/add_book.html')

@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.description = request.POST.get('description')
        book.save()
        return redirect('book-list')
    return render(request, 'relationship_app/edit_book.html', {'book': book})

@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('book-list')
    return render(request, 'relationship_app/delete_book.html', {'book': book})
