from django.urls import path
from .views import PostListView,PostDetailView,PostDeleteView,PostCreateView,PostUpdateView


urlpatterns = [
    # LIST all posts
    path('posts/', PostListView.as_view(), name='post_list'),

    # CREATE a new post
    path('posts/new/', PostCreateView.as_view(), name='post_create'),

    # DETAIL: Single post view
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail'),

    # UPDATE: Edit a post
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),

    # DELETE: Delete a post
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
]


