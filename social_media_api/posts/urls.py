from django.urls import path
from views import PostViewSet,CommentViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import routers
from .views import PostViewSet, CommentViewSet,UserFeedView

# Base router for Posts
router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')

# Nested router for Comments (nested under Posts)
# This creates URLs like: /posts/{post_pk}/comments/
posts_router = routers.NestedSimpleRouter(router, r'posts', lookup='post')
posts_router.register(r'comments', CommentViewSet, basename='post-comment')


urlpatterns = [
    # Top-level URLs: /posts/ and /posts/{pk}/
    path('', include(router.urls)),
    path('feed/', UserFeedView.as_view(), name='user-feed'),
    path('', include(posts_router.urls)),
]