# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import (
#     EventRetrieveView, EventUpdateDestroyView, AvailableEventsRetrieveView,
#     EventsCreateView, AvailableEventsListView, EventImagesCreateView, EventRequestsViewSet
# )

# router = DefaultRouter()
# router.register(r'', EventRequestsViewSet, basename='event-requests')

# urlpatterns = [
#     path('<int:pk>/', EventRetrieveView.as_view(), name='event-retrieve'),
#     path('available/', AvailableEventsListView.as_view(), name='available-events-list'),
#     path('available/<int:pk>/', AvailableEventsRetrieveView.as_view(), name='available-events-retrieve'),
#     path('', EventsCreateView.as_view(), name='events-create'),
#     path('<int:pk>/', EventUpdateDestroyView.as_view(), name='event-update-destroy'),
#     path('images/', EventImagesCreateView.as_view(), name='event-images-create'),
#     path('', include(router.urls)),
# ]

# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import EventViewSet

# router = DefaultRouter()
# router.register(r'', EventViewSet, basename='events')

# urlpatterns = [
#     path('', include(router.urls)),
#     path('available/', EventViewSet.as_view({'get': 'list_available_events'}), name='available-events-list'),
#     path('available/<int:pk>/', EventViewSet.as_view({'get': 'retrieve_available_event'}), name='available-events-retrieve'),
#     path('<int:pk>/requests/', EventViewSet.as_view({'get': 'list_requests', 'post': 'create_request'}), name='event-requests'),
#     path('images/', EventViewSet.as_view({'post': 'create_image'}), name='event-images-create'),
# ]


from django.urls import path
from .views import EventViewSet

event_list = EventViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

event_detail = EventViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

available_events_list = EventViewSet.as_view({
    'get': 'list_available_events'
})

available_event_detail = EventViewSet.as_view({
    'get': 'retrieve_available_event'
})

event_requests = EventViewSet.as_view({
    'get': 'list_requests',
    'post': 'create_request'
})

create_image = EventViewSet.as_view({
    'post': 'create_image'
})

urlpatterns = [
    path('', event_list, name='events-list'),
    path('<int:pk>/', event_detail, name='event-detail'),
    path('available/', available_events_list, name='available-events-list'),
    path('available/<int:pk>/', available_event_detail, name='available-events-retrieve'),
    path('<int:pk>/requests/', event_requests, name='event-requests'),
    path('images/', create_image, name='event-images-create'),
]
