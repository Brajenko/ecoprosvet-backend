from django.db import models

from django.contrib.auth import get_user_model

UserModel = get_user_model()

class Place(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    lon = models.DecimalField(max_digits=9, decimal_places=6)
    address = models.CharField(max_length=100)
    creator = models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class PlacesImage(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='places/images')

    def __str__(self):
        return self.image.url
