
from rest_framework import generics,status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
from .models import CustomUser
from .serializers import RegisterSerializer
from rest_framework.permissions.IsAuthenticated
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from notifications.utils import create_notification
# Register new user
class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

# Login and return token
class LoginView(generics.GenericAPIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)
        if not user:
            return Response({"error": "Invalid credentials"}, status=400)

        token = Token.objects.get_or_create(user=user)
        return Response({"token": token.key})
    
#follow management views

User = get_user_model()

class FollowUserView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        # The user being followed
        user_to_follow = get_object_or_404(User, pk=user_id)
        current_user = request.user

        if current_user == user_to_follow:
            return Response(
                {"detail": "You cannot follow yourself."},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Add the relationship
        current_user.following.add(user_to_follow)
        # NEW: Generate Notification
        create_notification(
            recipient=user_to_follow,
            actor=current_user,
            verb='followed',
            target=user_to_follow # Target is the user object itself
        )
        return Response(
            {"detail": f"You are now following {user_to_follow.username}."},
            status=status.HTTP_200_OK
        )

class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        # The user being unfollowed
        user_to_unfollow = get_object_or_404(User, pk=user_id)
        current_user = request.user
        
        # Remove the relationship
        if current_user.following.filter(pk=user_id).exists():
            current_user.following.remove(user_to_unfollow)
            return Response(
                {"detail": f"You have unfollowed {user_to_unfollow.username}."},
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"detail": "You were not following this user."},
                status=status.HTTP_400_BAD_REQUEST
            )

