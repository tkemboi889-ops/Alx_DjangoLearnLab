from django.urls import path
from .views import PostListView,PostDetailView,PostDeleteView,PostCreateView,PostUpdateView
from django.contrib.auth import views as auth_views
from . import views
from .views import add_comment, CommentUpdateView, CommentDeleteView,CommentCreateView

urlpatterns = [
    # LIST all posts
    path('post/', PostListView.as_view(), name='post_list'),

    # CREATE a new post
    path('post/new/', PostCreateView.as_view(), name='post_create'),

    # DETAIL: Single post view
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),

    # UPDATE: Edit a post
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),

    # DELETE: Delete a post
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
        path('login/', auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name="logout.html"), name="logout"),
    path('register/', views.register, name="register"),
    path('profile/', views.profile, name="profile"),
    path('posts/<int:post_id>/comments/add/', add_comment, name='add_comment'),
    path('Comments/<int:pk>/update/', CommentUpdateView.as_view(), name='update_comment'),
    path('Comments/<int:pk>/delete/', CommentDeleteView.as_view(), name='delete_comment'),
    path('post/<int:pk>/comment/new/', CommentCreateView.as_view(), name='create_comment'),
]


