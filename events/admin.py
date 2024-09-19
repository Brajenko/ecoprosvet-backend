from django.contrib import admin
from .models import Event, EventImage
from import_export import resources
from import_export.admin import ExportMixin

class EventImageInline(admin.TabularInline):
    model = EventImage

class EventResource(resources.ModelResource):
    class Meta:
        model = Event

class EventAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = EventResource
    list_display = ('name', 'start_time', 'end_time', 'organizer', 'place', 'created_at')
    search_fields = ('name', 'organizer__username', 'place__name')
    list_filter = ('start_time', 'end_time', 'organizer', 'place')
    inlines = [EventImageInline]

admin.site.register(Event, EventAdmin)
