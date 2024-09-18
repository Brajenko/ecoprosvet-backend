from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from .models import Request, Event
from .serializers import RequestSerializer

from users.permissions import IsOrganizer

class RequestCreateView(generics.CreateAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
    permission_classes = [permissions.IsAuthenticated]


class RequestListView(generics.ListAPIView):
    serializer_class = RequestSerializer
    permission_classes = [IsOrganizer]

    def get_queryset(self):
        event_id = self.kwargs.get('event_id')
        if not event_id:
            raise PermissionDenied("Event ID is required")
        return Request.objects.filter(event_id=event_id)