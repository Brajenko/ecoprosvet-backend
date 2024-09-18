from rest_framework import serializers

from .models import Event, EventImage

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'name', 'description', 'images', 'start_time', 'end_time', 'place')

    def create(self, validated_data):
        validated_data['organizer'] = self.context['request'].user
        images = validated_data.pop('images')
        event = Event.objects.create(**validated_data)

        for image_id in images:
            image = EventImage.filter(id=image_id).first()
            event.images.add(
                image
            )

        return event

class EventImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventImage
        fields = ('id', 'image', )
