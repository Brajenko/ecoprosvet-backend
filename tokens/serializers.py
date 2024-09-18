from rest_framework import serializers


class YandexAuthSerializer(serializers.Serializer):
    ya_token = serializers.CharField()
