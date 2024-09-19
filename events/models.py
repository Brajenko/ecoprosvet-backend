from django.db import models
from django.contrib.postgres.fields import ArrayField


from django.contrib.auth import get_user_model

UserModel = get_user_model()

class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    organizer = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    volunteers_needed = models.IntegerField(default=0)
    questions = ArrayField(models.CharField(max_length=200), blank=True, default=list)
    place = models.ForeignKey('places.Place', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class EventImage(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='images', blank=True, null=True)
    filepond = models.ImageField(upload_to='events/images')

    def __str__(self):
        return self.filepond.url


class Request(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    event = models.ForeignKey('events.Event', on_delete=models.CASCADE)
    answers = ArrayField(models.CharField(max_length=200), blank=True, default=list)
    as_volunteer = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

