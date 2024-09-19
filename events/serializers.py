from rest_framework import serializers

from .models import Event, EventImage, Request
from places.serializers import PlaceSerializer

class CreateUpdateEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'name', 'description', 'images', 'start_time', 'end_time', 'place', 'volunteers_needed', 'questions')

    def create(self, validated_data):
        validated_data['organizer'] = self.context['request'].user
        images = validated_data.pop('images')
        event = Event.objects.create(**validated_data)

        for image_id in images:
            event.images.add(image_id) # type: ignore

        return event
    

class EventImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventImage
        fields = ('id', 'filepond', )


class EventSerializer(serializers.ModelSerializer):
    images = EventImageSerializer(many=True, read_only=True)
    place = PlaceSerializer()

    class Meta:
        model = Event
        fields = ('id', 'name', 'description', 'images', 'start_time', 'end_time', 'place', 'volunteers_needed', 'questions')


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = ['id', 'as_volunteer', 'user', 'answers']
        read_only_fields = ('user', )

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user if request else None
        return Request.objects.create(user=user, **validated_data)


class RequestReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = ['id', 'event', 'as_volunteer', 'user', 'answers']
        read_only_fields = ['user']
