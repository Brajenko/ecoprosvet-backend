from django.urls import path
from .views import OrganizationsSearchView
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import (
    OrganizationsSearchView,
    OrganizationCreateView,
    OrganizationUpdateView,
    OrganizationRetrieveView,
    OrganizationDocumentCreateApi
)


urlpatterns = [
    path('search/', OrganizationsSearchView.as_view(), name='organizations-search'),
    path('create/', OrganizationCreateView.as_view(), name='organization-create'),
    path('update/', OrganizationUpdateView.as_view(), name='organization-update'),
    path('retrieve/', OrganizationRetrieveView.as_view(), name='organization-retrieve'),
    path('documents/', OrganizationDocumentCreateApi.as_view(), name='organization-documents-create'),
]