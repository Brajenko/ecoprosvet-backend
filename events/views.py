import datetime as dt

from rest_framework import viewsets
from rest_framework import generics

from .models import Event, EventImage
from .serializers import EventSerializer, EventImageSerializer
from users.permissions import IsOrganizer


class EventsListCreateView(generics.ListCreateAPIView):
    serializer_class = EventSerializer
    permission_classes = [IsOrganizer]

    def get_queryset(self):
        return Event.objects.filter(organizer=self.request.user)

class EventRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EventSerializer
    permission_classes = [IsOrganizer]

    def get_queryset(self):
        return Event.objects.filter(organizer=self.request.user)

class AvailableEventsListView(generics.ListAPIView):
    queryset = Event.objects.filter(end_time__gte=dt.datetime.now()).order_by('?')
    serializer_class = EventSerializer

class AvailableEventsRetrieveView(generics.RetrieveAPIView):
    queryset = Event.objects.filter(end_time__gte=dt.datetime.now())
    serializer_class = EventSerializer

class EventImagesCreateView(generics.CreateAPIView):
    queryset = EventImage.objects.all()
    serializer_class = EventImageSerializer
    permission_classes = [IsOrganizer]
