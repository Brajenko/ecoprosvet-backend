from rest_framework import serializers
from .models import Request

class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = ['id', 'user', 'event', 'as_volunteer', 'created_at']

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user if request else None
        return Request.objects.create(user=user, **validated_data)
