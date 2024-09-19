from django.urls import path
from .views import VideoListCreateView, VideoFileCreateView

urlpatterns = [
    path('', VideoListCreateView.as_view(), name='video-list-create'),
    path('videofile/', VideoFileCreateView.as_view(), name='video-file-create'),
]
