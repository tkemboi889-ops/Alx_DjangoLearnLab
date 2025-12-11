#notification serialzier 
from rest_framework import serializers
from .models import Notification
from django.contrib.auth import get_user_model

User = get_user_model()

# Simple serializer for the actor/user who caused the notification
class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')

class NotificationSerializer(serializers.ModelSerializer):
    # Use the ContentType to dynamically represent the target object
    target_type = serializers.CharField(source='content_type.model', read_only=True)
    actor = ActorSerializer(read_only=True)
    
    class Meta:
        model = Notification
        fields = [
            'id', 'recipient', 'actor', 'verb', 
            'target_type', 'object_id', 'timestamp', 'is_read'
        ]
        read_only_fields = ['recipient', 'actor', 'verb', 'target_type', 'object_id', 'timestamp']


class NotificationMarkReadSerializer(serializers.Serializer):
    """
    Serializer used solely for marking one or all notifications as read.
    """
    mark_all = serializers.BooleanField(required=False, default=False, write_only=True)
    notification_ids = serializers.ListField(
        child=serializers.IntegerField(), 
        required=False, 
        write_only=True
    )