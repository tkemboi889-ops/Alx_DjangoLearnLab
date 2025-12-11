from .models import Notification
from django.contrib.contenttypes.models import ContentType
#notification utility system
def create_notification(recipient, actor, verb, target):
    """
    Creates a Notification instance.
    - target must be a Django model instance (Post, User, Comment, etc.)
    """
    
    # Get the ContentType object for the target instance
    content_type = ContentType.objects.get_for_model(target)
    
    Notification.objects.create(
        recipient=recipient,
        actor=actor,
        verb=verb,
        content_type=content_type,
        object_id=target.pk,
        target=target
    )