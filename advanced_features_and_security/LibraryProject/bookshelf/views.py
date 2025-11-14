
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponseForbidden, HttpResponse
# --- CHANGE 1: Import the Book model instead of Article ---
from .models import Book 

# --- View all Books (The booklist) (Requires can_view_book) ---
@login_required 
# --- CHANGE 2: Use 'core.can_view_book' permission ---
@permission_required('core.can_view_book', raise_exception=True)
# --- CHANGE 3: Rename function to book_list ---
def book_list(request): 
    """Users must have the 'can_view_book' permission to access this list."""
    # --- CHANGE 4: Query Book model and pass to template ---
    booklist = Book.objects.all() 
    return render(request, 'core/book_list.html', {'booklist': booklist})

# --- View Single Book (Requires can_view_book) ---
@login_required
@permission_required('core.can_view_book', raise_exception=True)
# --- CHANGE 5: Rename function to book_detail ---
def book_detail(request, pk): 
    # --- CHANGE 6: Get Book object ---
    book = get_object_or_404(Book, pk=pk) 
    return render(request, 'core/book_detail.html', {'book': book})

# --- Create Book (Requires can_create_book) ---
@login_required
# --- CHANGE 7: Use 'core.can_create_book' permission ---
@permission_required('core.can_create_book', raise_exception=True)
# --- CHANGE 8: Rename function to book_create ---
def book_create(request):
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
def book_edit(request, pk):
    """Only Editors and Admins should be able to edit."""
    # --- CHANGE 11: Get Book object ---
    book = get_object_or_404(Book, pk=pk) 
    if request.method == 'POST':
        # ... actual edit logic using BookForm and book instance
        pass 
        
    return HttpResponse(f'Book Edit Form for "{book.title}" (Permission Check Passed)')


# --- Delete Book (Requires can_delete_book) ---
@login_required
# --- CHANGE 12: Use 'core.can_delete_book' permission ---
@permission_required('core.can_delete_book', raise_exception=True)
# --- CHANGE 13: Rename function to book_delete ---
def book_delete(request, pk):
    """Typically only Admins should have this permission."""
    # --- CHANGE 14: Get Book object ---
    book = get_object_or_404(Book, pk=pk) 
    if request.method == 'POST':
        book.delete()
        # --- CHANGE 15: Redirect to book_list ---
        return redirect('book_list') 
        
    return HttpResponse(f'Book Delete Confirmation for "{book.title}" (Permission Check Passed)')