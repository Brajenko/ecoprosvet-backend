from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView

from .serializers import VideoSerializer, VideoFileSerializer, VideoWithVideoFileSerializer

from .models import Video


class VideoFileCreateView(CreateAPIView):
    serializer_class = VideoFileSerializer


class VideoListCreateView(ListCreateAPIView):
    queryset = Video.objects.all().order_by('?')
    serializer_class = VideoSerializer
    page_size = 5
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return VideoWithVideoFileSerializer
        return super().get_serializer_class()
