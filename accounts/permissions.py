from rest_framework.permissions import BasePermission


class IsAuthenticated(BasePermission):
    """
    Allow access only to authenticated users.
    """

    message = "Authentication required."

    def has_permission(self, request, view):
        return bool(
            request.user and
            request.user.is_authenticated
        )