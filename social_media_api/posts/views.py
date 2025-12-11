

# Create your views here.
from rest_framework import viewsets, permissions

from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsOwnerOrReadOnly


from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Post
from .serializers import PostSerializer
from .pagination import StandardResultsPagination 

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
        # Order by created_at descending (newest first).
        queryset = Post.objects.filter(
            author__in=following_users
        ).order_by('-created_date')
        
        return queryset

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        # Automatically assign the logged-in user as the author
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_queryset(self):
        # Filtering comments by post dynamically if needed
        return Comment.objects.all().order_by('-created_at')

    def perform_create(self, serializer):
        # Automatically attach the logged-in user as the author
        serializer.save(author=self.request.user)

