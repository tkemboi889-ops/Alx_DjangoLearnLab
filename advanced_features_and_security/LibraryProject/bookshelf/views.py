
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponseForbidden, HttpResponse 
from django.db.models import Q
from .models import Book
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy # Used for success_url

class SignUpView(CreateView):
    # 1. Specify the form to use (built-in UserCreationForm)
    form_class = UserCreationForm
    
    # 2. Specify the template for the form
    template_name = 'registration/signup.html'
    
    # 3. Specify where to redirect the user upon successful form submission
    # We use reverse_lazy because the URLconf is not loaded when Django loads this file.
    success_url = reverse_lazy('login') 
    
    # NOTE: If you are using a CUSTOM UserCreationForm (that inherits from the built-in one), 
    # the logic is the same.

# your_app/views.py



def book_search(request):
    """
    Safely handles user search input using the Django ORM to prevent SQL Injection.
    """
    # User input is retrieved safely via request.GET.get()
    query = request.GET.get('q', '') 

    if query:
        # The ORM parameterizes the 'query' variable, treating it as data, not code.
        # This completely nullifies SQL injection risk.
        books = Book.objects.filter(
            # Validate input implicitly by using ORM lookups (like icontains)
            Q(title__icontains=query) | Q(author__icontains=query)
        ).distinct()
    else:
        books = Book.objects.none()

    return render(request, 'your_app/search_results.html', {'books': books, 'query': query})





@login_required 
# --- CHANGE 2: Use 'core.can_view_book' permission ---
@permission_required('core.can_view_book', raise_exception=True)
# --- CHANGE 3: Rename function to book_list ---
def books(request): 
    """Users must have the 'can_view_book' permission to access this list."""
    # --- CHANGE 4: Query Book model and pass to template ---
    booklist = Books.objects.all() 
    return render(request,  {'booklist': booklist})

# --- View Single Book (Requires can_view_book) ---
@login_required
@permission_required('core.can_view_book', raise_exception=True)
# --- CHANGE 5: Rename function to book_detail ---
def books_detail(request, pk): 
    # --- CHANGE 6: Get Book object ---
    book = get_object_or_404(Books, pk=pk) 
    return render(request, 'core/book_detail.html', {'book': book})

# --- Create Book (Requires can_create_book) ---
@login_required
# --- CHANGE 7: Use 'core.can_create_book' permission ---
@permission_required('core.can_create_book', raise_exception=True)
# --- CHANGE 8: Rename function to book_create ---
def books_create(request):
    """Only Editors and Admins should be able to reach this view."""
    if request.method == 'POST':
        # ... actual creation logic using BookForm
        pass 
        
    return HttpResponse('Book Creation Form (Permission Check Passed)')


# --- Edit Book (Requires can_edit_book) ---
@login_required
# --- CHANGE 9: Use 'core.can_edit_book' permission ---
@permission_required('core.can_edit_book', raise_exception=True)
# --- CHANGE 10: Rename function to book_edit ---
def books_edit(request, pk):
    """Only Editors and Admins should be able to edit."""
    # --- CHANGE 11: Get Book object ---
    book = get_object_or_404(Books, pk=pk) 
    if request.method == 'POST':
        # ... actual edit logic using BookForm and book instance
        pass 
        
    return HttpResponse(f'Book Edit Form for "{book.title}" (Permission Check Passed)')


# --- Delete Book (Requires can_delete_book) ---
@login_required
# --- CHANGE 12: Use 'core.can_delete_book' permission ---
@permission_required('core.can_delete_book', raise_exception=True)
# --- CHANGE 13: Rename function to book_delete ---
def books_delete(request, pk):
    """Typically only Admins should have this permission."""
    # --- CHANGE 14: Get Book object ---
    book = get_object_or_404(Books, pk=pk) 
    if request.method == 'POST':
        book.delete()
        # --- CHANGE 15: Redirect to book_list ---
        return redirect('book_list') 
        
    return HttpResponse(f'Book Delete Confirmation for "{book.title}" (Permission Check Passed)')