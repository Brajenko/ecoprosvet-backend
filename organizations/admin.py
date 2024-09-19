from django.contrib import admin
from .models import Organization, OrganizationDocument
import csv
from django.http import HttpResponse
from import_export import resources
from import_export.admin import ExportMixin

class OrganizationDocumentInline(admin.TabularInline):
    model = OrganizationDocument
    extra = 3

# @admin.register(Organization)
# class OrganizationAdmin(admin.ModelAdmin):
#     list_display = ('name', 'user', 'inn', 'kpp', 'ogrn')
#     search_fields = ('name', 'inn', 'ogrn')
#     list_filter = ('user',)
#     inlines = [OrganizationDocumentInline]
class OrganizationResource(resources.ModelResource):
    class Meta:
        model = Organization

@admin.register(Organization)
class OrganizationAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = OrganizationResource
    list_display = ('name', 'user', 'inn', 'kpp', 'ogrn')
    search_fields = ('name', 'inn', 'ogrn')
    list_filter = ('user',)
    inlines = [OrganizationDocumentInline]