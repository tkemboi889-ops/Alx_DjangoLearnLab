from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from .models import Notification
from .serializers import NotificationSerializer, NotificationMarkReadSerializer
from .pagination import StandardResultsPagination 

class NotificationListView(generics.ListAPIView):
    """
    Lists the current user's notifications.
    Filters for unread notifications if 'unread' query param is set.
    """
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = StandardResultsPagination # Reuse pagination

    def get_queryset(self):
        queryset = Notification.objects.filter(recipient=self.request.user)
        
        # Optional: Filter by unread status
        unread_only = self.request.query_params.get('unread', 'false').lower() == 'true'
        if unread_only:
            queryset = queryset.filter(is_read=False)
            
        return queryset.select_related('actor').order_by('-timestamp')


class NotificationMarkReadView(generics.GenericAPIView):
    """
    Allows users to mark notifications as read, either individually or all at once.
    """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = NotificationMarkReadSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = request.user
        mark_all = serializer.validated_data.get('mark_all')
        notification_ids = serializer.validated_data.get('notification_ids')
        
        # Filter queryset to notifications belonging to the user
        queryset = Notification.objects.filter(recipient=user, is_read=False)
        
        if mark_all:
            # Mark all unread notifications as read
            count = queryset.update(is_read=True)
            return Response(
                {"detail": f"Marked {count} notifications as read."},
                status=status.HTTP_200_OK
            )
        
        elif notification_ids:
            # Mark specific notifications as read
            count = queryset.filter(id__in=notification_ids).update(is_read=True)
            return Response(
                {"detail": f"Marked {count} selected notifications as read."},
                status=status.HTTP_200_OK
            )

        return Response(
            {"detail": "No notifications marked. Specify 'mark_all' or 'notification_ids'."},
            status=status.HTTP_400_BAD_REQUEST
        )