from django.contrib import admin
from .models import Place, PlacesImage

class PlacesImageAdmin(admin.TabularInline):
    model = PlacesImage

class PlaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'creator', 'created_at')
    search_fields = ('name', 'address', 'creator__username')
    list_filter = ('created_at', 'creator')

    inlines = [PlacesImageAdmin, ]

admin.site.register(Place, PlaceAdmin)