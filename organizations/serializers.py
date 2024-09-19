from rest_framework import serializers

from .models import Organization, OrganizationDocument

class OrganizationsSearch(serializers.Serializer):
    search = serializers.CharField(max_length=255)


class OrganizationFromSearchSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    inn = serializers.CharField(max_length=10)
    kpp = serializers.CharField(max_length=9)
    ogrn = serializers.CharField(max_length=13)


class OrganizationDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationDocument
        fields = ['id', 'filepond']


class OrganizationSerializer(serializers.ModelSerializer):
    documents = OrganizationDocumentSerializer(many=True, read_only=True)

    class Meta:
        model = Organization
        fields = ['id', 'name', 'inn', 'kpp', 'ogrn', 'documents']


class OrganizationWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ['id', 'name', 'inn', 'kpp', 'ogrn', 'documents']
