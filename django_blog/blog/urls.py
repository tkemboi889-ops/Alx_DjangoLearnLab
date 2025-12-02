from django.urls import path
from .views import PostListView,PostDetailView,PostDeleteView,PostCreateView,PostUpdateView


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
]


