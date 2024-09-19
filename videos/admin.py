from django.contrib import admin
from .models import VideoFile, Video

@admin.register(VideoFile)
class VideoFileAdmin(admin.ModelAdmin):
    list_display = ('id', 'filepond')
    search_fields = ('filepond',)
    list_filter = ('filepond',)

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'place', 'event', 'videofile', 'created_at')
    search_fields = ('title', 'description')
    list_filter = ('place', 'event', 'created_at')
    raw_id_fields = ('place', 'event', 'videofile')

# Register your models here if not using the @admin.register decorator
# admin.site.register(VideoFile, VideoFileAdmin)
# admin.site.register(Video, VideoAdmin)