

# Create your views here.
from rest_framework import viewsets, permissions
from django.shortcuts import get_object_or_404
from django.contrib.contenttypes.models import ContentType
from .models import Post, Comment,Like
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import PostSerializer
from .pagination import StandardResultsPagination 
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from notifications.utils import create_notification



#implementing feed functionality
class createUserFeedView(generics.ListAPIView):
    """
    Returns a list of posts from all users that the current user is following,
    ordered by creation date (most recent first).
    """
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = StandardResultsPagination
    
    def get_queryset(self):
        # 1. Get the list of users the current user follows (following is a ManyToMany field)
        following_users = self.request.user.following.all()
        
        # 2. Filter posts to include only those authored by the followed users.
    
        queryset = Post.objects.filter(
            author__in=following_users
        ).order_by('created_at')
        
        return queryset

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        # Automatically assign the logged-in user as the author
        serializer.save(author=self.request.user)
    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def like(self, request, pk=None):
        # 1. Use get_object_or_404 as requested
        post = get_object_or_404(Post, pk=pk)
        user = request.user

        # 2. Use get_or_create as requested
        like_created = Like.objects.get_or_create(user=user, post=post)

        if not like_created:
            # The object already existed, meaning the user already liked it
            return Response(
                {"detail": "Post already liked."},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # 3. Generate Notification using direct Notification.objects.create as requested
        if user != post.author:
            # Get content type for the post target
            content_type = ContentType.objects.get_for_model(post)
            
            notification= notification.objects.create( # <--- Notification.objects.create is used here
                recipient=post.author,
                actor=user,
                verb='liked',
                content_type=content_type,
                object_id=post.pk,
                target=post
            )

        return Response(
            {"detail": "Post liked successfully."},
            status=status.HTTP_200_OK
        )


    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def unlike(self, request, pk=None):
        # Use get_object_or_404 here too for consistency
        post = get_object_or_404(Post, pk=pk) 
        user = request.user
        
        # Try to find and delete the Like object
        like_query = Like.objects.filter(post=post, user=user)
        
        if like_query.exists():
            like_query.delete()
            return Response(
                {"detail": "Post unliked successfully."},
                status=status.HTTP_200_OK
            )
        
        return Response(
            {"detail": "Post was not previously liked by this user."},
            status=status.HTTP_400_BAD_REQUEST
        )

#coment model
class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_queryset(self):
        # Filtering comments by post dynamically if needed
        return Comment.objects.all().order_by('-created_at')

    def perform_create(self, serializer):
        # Automatically attach the logged-in user as the author
        serializer.save(author=self.request.user)
# NEW: Generate Notification (if user comments on someone else's post)
        if self.request.user != Post.author:
            create_notification(
                recipient=Post.author,
                actor=self.request.user,
                verb='commented on',
                target=Post
            )