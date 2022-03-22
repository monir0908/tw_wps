from rest_framework.permissions import BasePermission


class IsSuperUser(BasePermission):
    message = "You are not a not superuser; You won't be able to perform this task."
    def has_permission(self, request, view):
        return request.user.is_superuser

