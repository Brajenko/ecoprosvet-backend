from django.urls import path

from .views import EventRetrieveUpdateDestroyView, AvailableEventsRetrieveView, EventsListCreateView, AvailableEventsListView, EventImagesCreateView

urlpatterns = [
    path('available/', AvailableEventsListView.as_view()),
    path('available/<int:pk>/', AvailableEventsRetrieveView.as_view()),
    path('', EventsListCreateView.as_view()),
    path('<int:pk>/', EventRetrieveUpdateDestroyView.as_view()),
    path('images/', EventImagesCreateView.as_view()),
]
