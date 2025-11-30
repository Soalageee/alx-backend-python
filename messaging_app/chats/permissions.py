from rest_framework import permissions
from rest_framework.permissions import BasePermission, SAFE_METHODS


# class IsOwner(permissions.BasePermission):
#     """
#     Custom permission to only allow owners of an object to view or edit it.
#     """

#     def has_object_permission(self, request, view, obj):
#         # obj.user is the owner of the object
#         # request.user is the logged-in user
#         return obj.user == request.user


class IsParticipantOfConversation(BasePermission):
    """
    Allow only authenticated users who are participants of a conversation
    to send, view, update and delete messages.
    """

    def has_permission(self, request, view):
        # Must be authenticated
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        """
        Restrict access to only conversation participants.
        """

        # GET, HEAD, OPTIONS are safe -- still must be participant
        if request.method in SAFE_METHODS:
            return self._is_participant(request, obj)

        # PUT, PATCH, DELETE (unsafe methods) — stricter check
        if request.method in ["PUT", "PATCH", "DELETE"]:
            return self._is_participant(request, obj)

        # POST for sending messages — must be participant
        if request.method == "POST":
            return self._is_participant(request, obj)

        return False

    def _is_participant(self, request, obj):
        # Message → conversation.participants
        if hasattr(obj, "conversation"):
            return request.user in obj.conversation.participants.all()

        # Conversation → participants
        if hasattr(obj, "participants"):
            return request.user in obj.participants.all()

        return False

