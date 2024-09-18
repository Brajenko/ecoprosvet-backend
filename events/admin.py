from django.contrib import admin
from .models import Event, EventImage

class EventImageInline(admin.TabularInline):
    model = EventImage

class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_time', 'end_time', 'organizer', 'place', 'created_at')
    search_fields = ('name', 'organizer__username', 'place__name')
    list_filter = ('start_time', 'end_time', 'organizer', 'place')
    inlines = [EventImageInline]

admin.site.register(Event, EventAdmin)
