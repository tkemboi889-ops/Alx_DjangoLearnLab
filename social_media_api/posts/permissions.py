from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwnerOrReadOnly(BasePermission):
    """
    Allow read permissions for anyone.
    Write permissions only for the owner.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True  # Anyone can GET

        return obj.author == request.user  # Only owner can EDIT/DELETE
