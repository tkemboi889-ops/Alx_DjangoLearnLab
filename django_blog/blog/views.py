
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import PostForm
from .models import Post
#implementation of user authentication
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterForm
from .forms import UpdateUserForm
from django.shortcuts import get_object_or_404, redirect
from .models import Post, Comment
from .forms import CommentForm


# User Registration View
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Account created successfully!")
            return redirect("profile")
    else:
        form = RegisterForm()
    return render(request, "register.html", {"form": form})


# User Profile View
@login_required
def profile(request):
    if request.method == "POST":
        form = UpdateUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect("profile")
    else:
        form = UpdateUserForm(instance=request.user)

    return render(request, "profile.html", {"form": form})

#comment views crud operaations


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "comments/add_comment.html"

    def form_valid(self, form):
        post = get_object_or_404(Post, pk=self.kwargs['post_id'])
        form.instance.post = post
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.kwargs['post_id']})
    
class CommentUpdateView(UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'comments/edit_comment.html'

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.post_id})

    def dispatch(self, request, *args, **kwargs):
        comment = self.get_object()
        if comment.author != request.user:
            return redirect('post_detail', pk=comment.post.id)
        return super().dispatch(request, *args, **kwargs)


class CommentDeleteView(DeleteView):
    model = Comment
    template_name = 'comments/delete_comment.html'

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.post_id})

    def dispatch(self, request, *args, **kwargs):
        comment = self.get_object()
        if comment.author != request.user:
            return redirect('post_detail', pk=comment.post.id)
        return super().dispatch(request, *args, **kwargs)

#implementing search functionality
from django.db.models import Q

def search_posts(request):
    query = request.GET.get('q')
    results = []

    if query:
        results = Post.objects.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(tags__name__icontains=query)
        ).distinct()

    return render(request, "search_results.html", {"results": results, "query": query})
#view for tagging filtering
def posts_by_tag(request, tag):
    posts = Post.objects.filter(tags__name=tag)
    return render(request, "posts_by_tag.html", {"posts": posts, "tag": tag})


# LISTING ALL POSTS
class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"   # corrected
    context_object_name = "posts"
    ordering = ['-published_date']


# DISPLAYING DETAILS FOR EACH POST
class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"   # corrected
    context_object_name = "post"


# CREATING A NEW POST
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "blog/post_create.html"   # corrected
    fields = ['title', 'content']  # required

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# UPDATING A POST
class PostUpdateView(LoginRequiredMixin, UpdateView,UserPassesTestMixin):
    model = Post
    template_name = "blog/post_update.html"   # corrected
    fields = ['title', 'content']
def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
def test_func(self):
        post = self.get_object()
        return self.request.user == post.author  # only author can edit


# DELETING A POST
class PostDeleteView(LoginRequiredMixin, DeleteView,UserPassesTestMixin):
    model = Post
    template_name = "blog/post_delete.html"   # corrected
    success_url = reverse_lazy('post_list')  # required redirect after delete
def test_func(self):
        post = self.get_object()
        return self.request.user == post.author  # only author can delete