from rest_framework import permissions

class IsOrganizer(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_organizer


class IsCreator(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.creator == request.user
