
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponseForbidden, HttpResponse
from .models import Article # Assume ArticleForm is defined elsewhere for simplicity

# --- View all Articles (Requires can_view_article) ---
@login_required 
@permission_required('core.can_view_article', raise_exception=True)
def article_list(request):
    """Users must have the 'can_view_article' permission to access this list."""
    articles = Article.objects.all()
    # raise_exception=True automatically translates to a 403 Forbidden page 
    # if the user lacks the permission.
    return render(request, 'core/article_list.html', {'articles': articles})

# --- View Single Article (Also requires can_view_article) ---
@login_required
@permission_required('core.can_view_article', raise_exception=True)
def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'core/article_detail.html', {'article': article})

# --- Create Article (Requires can_create_article) ---
@login_required
@permission_required('core.can_create_article', raise_exception=True)
def article_create(request):
    """Only Editors and Admins should be able to reach this view."""
    if request.method == 'POST':
        
        pass # Placeholder for actual creation logic
    
    return HttpResponse('Article Creation Form (Permission Check Passed)')


# --- Edit Article (Requires can_edit_article) ---
@login_required
@permission_required('core.can_edit_article', raise_exception=True)
def article_edit(request, pk):
    """Only Editors and Admins should be able to edit."""
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        
    
     return HttpResponse(f'Article Edit Form for "{article.title}" (Permission Check Passed)')


# --- Delete Article (Requires can_delete_article) ---
@login_required
@permission_required('core.can_delete_article', raise_exception=True)
def article_delete(request, pk):
    """Typically only Admins should have this permission."""
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('article_list')
        
    return HttpResponse(f'Article Delete Confirmation for "{article.title}" (Permission Check Passed)')