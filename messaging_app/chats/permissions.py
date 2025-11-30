from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to view or edit it.
    """

    def has_object_permission(self, request, view, obj):
        # obj.user is the owner of the object
        # request.user is the logged-in user
        return obj.user == request.user