# core/permissions.py
from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit/delete it.
    Assumes model instances have an `owner` or `user` attribute pointing to a User.
    """

    def has_object_permission(self, request, view, obj):
        # Read-only for any request
        if request.method in permissions.SAFE_METHODS:
            return True

        # If object has 'owner' attribute
        owner = getattr(obj, "owner", None) or getattr(obj, "user", None) or getattr(obj, "athlete", None)
        if owner is None:
            # fallback: allow superusers/staff to edit
            return request.user.is_staff
        return owner == request.user or request.user.is_staff
