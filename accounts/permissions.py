from rest_framework.permissions import BasePermission
from setup.models import MenuRole


class IsPermission(BasePermission):

    message = "You do not have permission to access this menu."

    def has_permission(self, request, view):

        if not request.user.is_authenticated:
            self.message = "Please login first."
            return False

        menu = getattr(view, "permission_menu", None)

        permission = MenuRole.objects.filter(
            role=request.user.role,
            menu=menu
        ).first()

        if not permission:
            self.message = f"No permission assigned for '{menu}' menu."
            return False

        method_permissions = {
            "GET": (permission.is_view, "View permission denied."),
            "POST": (permission.is_add, "Add permission denied."),
            "PUT": (permission.is_edit, "Edit permission denied."),
            "PATCH": (permission.is_edit, "Edit permission denied."),
            "DELETE": (permission.is_delete, "Delete permission denied."),
        }

        allowed, msg = method_permissions.get(
            request.method,
            (False, "Method not allowed.")
        )

        self.message = msg
        return allowed