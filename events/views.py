# import datetime as dt

# from rest_framework import viewsets
# from rest_framework import generics, permissions, views, mixins

# from .models import Event, EventImage, Request
# from .serializers import CreateUpdateEventSerializer, EventImageSerializer, EventSerializer, RequestSerializer
# from users.permissions import IsOrganizer

# from events.permissions import IsEventOrganizer

# from rest_framework.decorators import action
# from rest_framework.response import Response


# class EventsCreateView(generics.CreateAPIView):
#     serializer_class = CreateUpdateEventSerializer
#     permission_classes = [IsOrganizer]

#     def get_queryset(self):
#         return Event.objects.filter(organizer=self.request.user)
    
# class EventsListView(generics.ListAPIView):
#     serializer_class = EventSerializer
#     permission_classes = [IsOrganizer]

#     def get_queryset(self):
#         return Event.objects.filter(organizer=self.request.user)
    

# class EventUpdateDestroyView(mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
#     serializer_class = CreateUpdateEventSerializer
#     permission_classes = [IsOrganizer]
    
#     def get_queryset(self):
#         return Event.objects.filter(organizer=self.request.user)

# class EventRetrieveView(generics.RetrieveAPIView):
#     serializer_class = EventSerializer
#     permission_classes = [IsOrganizer]
    
#     def get_queryset(self):
#         return Event.objects.filter(organizer=self.request.user)


# class AvailableEventsListView(generics.ListAPIView):
#     queryset = Event.objects.filter(end_time__gte=dt.datetime.now()).order_by('?')
#     serializer_class = EventSerializer

# class AvailableEventsRetrieveView(generics.RetrieveAPIView):
#     queryset = Event.objects.filter(end_time__gte=dt.datetime.now())
#     serializer_class = EventSerializer

# class EventImagesCreateView(generics.CreateAPIView):
#     queryset = EventImage.objects.all()
#     serializer_class = EventImageSerializer
#     permission_classes = [IsOrganizer]

# class EventRequestsViewSet(viewsets.ModelViewSet):
#     permission_classes = [permissions.IsAuthenticated]
#     serializer_class = RequestSerializer

#     def get_queryset(self, event_id):
#         return Request.objects.filter(event_id=event_id)

#     @action(detail=True, methods=['get'], permission_classes=[IsEventOrganizer])
#     def list_requests(self, request, pk=None):
#         event_id = pk
#         queryset = self.get_queryset(event_id)
#         serializer = RequestSerializer(queryset, many=True)
#         return Response(serializer.data)

#     @action(detail=True, methods=['post'])
#     def create_request(self, request, pk=None):
#         event_id = pk
#         serializer = RequestSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(user=request.user, event_id=event_id)
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)

import datetime as dt
from rest_framework import permissions, generics
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from drf_spectacular.utils import extend_schema

from .models import Event, EventImage, Request
from .serializers import CreateUpdateEventSerializer, EventImageSerializer, EventSerializer, RequestSerializer
from users.permissions import IsOrganizer
from events.permissions import IsEventOrganizer

class EventViewSet(viewsets.ModelViewSet):
    def get_permissions(self):
        if self.action in ['create', 'update', 'destroy', 'create_image']:
            permission_classes = [IsOrganizer]
        elif self.action in ['list_requests', 'create_request']:
            permission_classes = [permissions.IsAuthenticated]
        elif self.action in ['list', 'retrieve']:
            permission_classes = [IsOrganizer]
        else:
            permission_classes = []
        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        if self.action in ['create', 'update']:
            return CreateUpdateEventSerializer
        elif self.action == 'create_image':
            return EventImageSerializer
        elif self.action in ['list', 'retrieve', 'list_available_events', 'retrieve_available_event']:
            return EventSerializer
        elif self.action in ['list_requests', 'create_request']:
            return RequestSerializer
        return EventSerializer

    def get_queryset(self):
        if self.action in ['list', 'retrieve', 'update', 'destroy']:
            return Event.objects.filter(organizer=self.request.user)
        elif self.action in ['list_available_events', 'retrieve_available_event']:
            return Event.objects.filter(end_time__gte=dt.datetime.now())
        elif self.action in ['list_requests']:
            event_id = self.kwargs.get('pk')
            if not event_id:
                raise PermissionDenied("Event ID is required")
            return Request.objects.filter(event_id=event_id)
        return Event.objects.none()

    def perform_create(self, serializer):
        serializer.save(organizer=self.request.user)

    def perform_destroy(self, instance):
        instance.delete()

    @extend_schema(operation_id="api_events_available_list")
    @action(detail=False, methods=['get'])
    def list_available_events(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def retrieve_available_event(self, request, pk=None):
        queryset = self.get_queryset()
        event = generics.get_object_or_404(queryset, pk=pk)
        serializer = self.get_serializer(event)
        return Response(serializer.data)

    @action(detail=False, methods=['post'])
    def create_image(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    @action(detail=True, methods=['get'], permission_classes=[IsEventOrganizer])
    def list_requests(self, request, pk=None):
        event_id = pk
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def create_request(self, request, pk=None):
        event_id = pk
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(event_id=event_id)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
