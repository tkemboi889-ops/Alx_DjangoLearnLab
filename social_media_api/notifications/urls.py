from django.urls import path
from .views import NotificationListView, NotificationMarkReadView

urlpatterns = [
    # Route for listing notifications (with optional ?unread=true filtering)
    path('notifications/', NotificationListView.as_view(), name='notification-list'),
    
    # Route for marking notifications as read
    path('notifications/read/', NotificationMarkReadView.as_view(), name='notification-mark-read'),
]