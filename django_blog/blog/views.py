
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import LoginRequiredMixin,UserPassesTestMixin
from .forms import PostForm
from .models import Post

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