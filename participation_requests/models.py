from django.db import models

from django.contrib.auth import get_user_model

CustomUser = get_user_model()

class Request(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    event = models.ForeignKey('events.Event', on_delete=models.CASCADE)
    as_volunteer = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
