from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    """
    Custom permission to allow only owners of a message to view or edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Check if the logged-in user is the sender of the message
        return obj.sender == request.user
