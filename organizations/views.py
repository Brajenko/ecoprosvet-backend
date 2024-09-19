from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import OrganizationsSearch, OrganizationFromSearchSerializer

from drf_spectacular.utils import extend_schema, OpenApiParameter

from .serializers import OrganizationSerializer, OrganizationWriteSerializer
from .models import Organization

from rest_framework import viewsets, permissions

from users.permissions import IsOrganizer

from django.conf import settings

import dadata
from rest_framework.generics import CreateAPIView
from .models import OrganizationDocument
from .serializers import OrganizationDocumentSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action

class OrganizationsSearchView(APIView):
    @extend_schema(
        responses={200: OrganizationFromSearchSerializer(many=True)},
        parameters=[
            OpenApiParameter(name='search_term', type=str, location=OpenApiParameter.QUERY, required=True),
        ]
    )
    def get(self, request, *args, **kwargs):
        search_term = request.query_params.get('search_term', '')
        if not search_term:
            return Response({"detail": "Search term is required."}, status=status.HTTP_400_BAD_REQUEST)
        with dadata.Dadata(settings.DADATA_API_KEY, settings.DADATA_SECRET_KEY) as dadata_client:
            results = dadata_client.suggest("party", search_term)[5:]
        clear_results = [{'name': res['value'], 'inn': res['data']['inn'], 'kpp': res['data']['kpp'], 'ogrn': res['data']['ogrn']} for res in results]
        return Response(clear_results, status=status.HTTP_200_OK)


class OrganizationCreateView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        request=OrganizationWriteSerializer,
        responses={201: OrganizationSerializer}
    )
    def post(self, request, *args, **kwargs):
        serializer = OrganizationWriteSerializer(data=request.data)
        if serializer.is_valid():
            organization = serializer.save(user=request.user)
            return Response(OrganizationSerializer(organization).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrganizationUpdateView(APIView):
    permission_classes = [IsAuthenticated, IsOrganizer]

    @extend_schema(
        request=OrganizationWriteSerializer,
        responses={200: OrganizationSerializer}
    )
    def put(self, request, *args, **kwargs):
        try:
            organization = Organization.objects.get(user=request.user)
        except Organization.DoesNotExist:
            return Response({"detail": "Organization not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = OrganizationWriteSerializer(organization, data=request.data, partial=True)
        if serializer.is_valid():
            organization = serializer.save()
            return Response(OrganizationSerializer(organization).data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrganizationRetrieveView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        responses={200: OrganizationSerializer}
    )
    def get(self, request, *args, **kwargs):
        try:
            organization = Organization.objects.get(user=request.user)
        except Organization.DoesNotExist:
            return Response({"detail": "Organization not found."}, status=status.HTTP_404_NOT_FOUND)

        return Response(OrganizationSerializer(organization).data, status=status.HTTP_200_OK)


class OrganizationDocumentCreateApi(CreateAPIView):
    queryset = OrganizationDocument.objects.all()
    serializer_class = OrganizationDocumentSerializer
    permission_classes = [IsAuthenticated]

