from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.company.owner == self.request.user
        # return super().has_object_permission(request, view, obj)
