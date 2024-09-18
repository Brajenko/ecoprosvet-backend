from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    place = models.ForeignKey('places.Place', on_delete=models.CASCADE, null=True, blank=True)
    event = models.ForeignKey('events.Event', on_delete=models.CASCADE, null=True, blank=True)
    video = models.FileField(upload_to='videos')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
