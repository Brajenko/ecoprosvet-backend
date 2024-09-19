from django.db import models
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError

from django.db.models.signals import post_save
from django.dispatch import receiver
import ffmpeg
import os

import subprocess

class VideoFile(models.Model):
    filepond = models.FileField(upload_to='videos', max_length=255, validators=[FileExtensionValidator(allowed_extensions=['mp4', 'avi', 'mov', 'wmv', 'flv', 'webm'])])

    def __str__(self):
        return self.filepond.name


class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    place = models.ForeignKey('places.Place', on_delete=models.CASCADE, null=True, blank=True)
    event = models.ForeignKey('events.Event', on_delete=models.CASCADE, null=True, blank=True)
    videofile = models.OneToOneField(VideoFile, on_delete=models.CASCADE, related_name='video')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def clean(self):
        if bool(self.place) == bool(self.event):
            raise ValidationError('One (and only one) of "place" or "event" must be filled.')

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
    
    

@receiver(post_save, sender=VideoFile)
def convert_video_to_webm(sender, instance: VideoFile, **kwargs):
    post_save.disconnect(convert_video_to_webm, sender=sender)
    if instance.filepond:
        input_file_path = instance.filepond.path
        input_file_name = instance.filepond.name
        if not input_file_path.endswith('.mp4'):
            output_file_path = os.path.splitext(input_file_path)[0] + '.mp4'
            output_file_name = os.path.splitext(input_file_name)[0] + '.mp4'
            print(input_file_name, input_file_path)
            print(output_file_name, output_file_path)

            subprocess.Popen(['ffmpeg', '-i', input_file_path, output_file_path])

            instance.filepond.name = output_file_name
            instance.filepond.close()
            instance.save()
    post_save.connect(convert_video_to_webm, sender=sender)
