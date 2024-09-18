from rest_framework import serializers

from .models import Place, PlacesImage


class PlacesImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()
    class Meta:
        model = PlacesImage
        fields = ('id', 'image', )


class PlaceSerializer(serializers.ModelSerializer):
    images = PlacesImageSerializer(many=True, read_only=True)

    class Meta:
        model = Place
        fields = ('id', 'name', 'description', 'images', 'address', 'lat', 'lon',)
    
    def create(self, validated_data):
        validated_data['creator'] = self.context['request'].user
        images = validated_data.pop('uploaded_images')
        place = super().create(validated_data)

        for image in images:
            PlacesImage.objects.create(place=place, image=image)

        return place
