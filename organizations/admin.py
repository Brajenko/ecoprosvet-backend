from django.contrib import admin
from .models import Organization, OrganizationDocument

class OrganizationDocumentInline(admin.TabularInline):
    model = OrganizationDocument
    extra = 3

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'inn', 'kpp', 'ogrn')
    search_fields = ('name', 'inn', 'ogrn')
    list_filter = ('user',)
    inlines = [OrganizationDocumentInline]
