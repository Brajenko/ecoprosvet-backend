from rest_framework import serializers
from .models import Video, VideoFile

from places.serializers import PlaceSerializer
from events.serializers import EventSerializer


class VideoFileSerializer(serializers.ModelSerializer):
    filepond = serializers.FileField()

    class Meta:
        model = VideoFile
        fields = ['id', 'filepond']


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['id', 'title', 'description', 'place', 'event', 'videofile']



class VideoWithVideoFileSerializer(serializers.ModelSerializer):
    videofile = VideoFileSerializer()
    place = PlaceSerializer()
    event = EventSerializer()

    class Meta:
        model = Video
        fields = ['id', 'title', 'description', 'place', 'event', 'videofile']

