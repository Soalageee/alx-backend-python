from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to view or edit it.
    """

    def has_object_permission(self, request, view, obj):
        # obj.user is the owner of the object
        # request.user is the logged-in user
        return obj.user == request.user


from rest_framework.permissions import BasePermission

class IsParticipantOfConversation(BasePermission):
    """
    Only participants of a conversation can view, edit, or delete messages.
    """

    def has_permission(self, request, view):
        # Only allow access if user is logged in
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        """
        Check if the logged-in user is a participant of the conversation.
        'obj' can be a Message or Conversation object
        """
        # If obj is a Message, check its conversation participants
        if hasattr(obj, 'conversation'):
            return request.user in obj.conversation.participants.all()
        
        # If obj is a Conversation, check its participants directly
        if hasattr(obj, 'participants'):
            return request.user in obj.participants.all()
        
        return False
