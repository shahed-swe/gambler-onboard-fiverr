from django.contrib.auth.models import AnonymousUser

from rest_framework import permissions
from rest_framework.permissions import BasePermission


class IsAnonymous(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        if request.method == 'OPTIONS':
            return True
        return isinstance(request.user, AnonymousUser)


class IsAuthenticated(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        if request.method == 'OPTIONS':
            return True
        return super(IsAuthenticated, self).has_permission(request, view)


class AllowStaff(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if isinstance(user, AnonymousUser):
            return False

        if user.is_superuser and user.is_admin:
            return True

        return False  # TODO: change to is staff


class AllowAdmin(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if isinstance(user, AnonymousUser):
            return False

        if user.is_superuser and user.is_admin:
            return True

        return False  # TODO: change to is admin


class NotBanned(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if isinstance(user, AnonymousUser):
            return False

        return not user.is_banned()
