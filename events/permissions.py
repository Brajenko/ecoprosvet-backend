from .models import Event
from rest_framework import permissions


class IsEventOrganizer(permissions.BasePermission):
    def has_permission(self, request, view):
        event_id = view.kwargs.get('event_id')
        if not event_id:
            return False
        try:
            event = Event.objects.get(id=event_id)
        except Event.DoesNotExist:
            return False
        return event.organizer == request.user