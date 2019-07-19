from rest_framework import permissions


class IsUser(permissions.BasePermission):
    """
    Custom permission to allow only authenticated user to put, post and patch , the get is allowed for everyone
    """
    def has_permission(self, request, view):
        if request.method in ['POST', 'PATCH', 'PUT']:
            if request.user.is_anonymous:
                return False
            return True
        return True
