from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """
    A custom permission class to control access based on ownership.
    """
    def has_permission(self, request, view):
        """
        Check if the requesting user has permission to perform the
        action on the entire viewset.

        Args:
        request (HttpRequest): The HTTP request object.
        view (View): The viewset object.

        Returns:
        bool: True if the user has permission to perform the action,
        False otherwise.
        """
        if view.action == 'list':
            return False
        return True

    def has_object_permission(self, request, view, obj):
        """
        Check if the requesting user has permission to perform the
        action on a specific object.

        Args:
        request (HttpRequest): The HTTP request object.
        view (View): The viewset object.
        obj (object): The object being accessed.

        Returns:
        bool: True if the user has permission to perform the action
        on the object, False otherwise.
        """
        return obj.owner == request.user
