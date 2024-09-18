from typing import Iterable
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), unique=True)
    birthday = models.DateField(null=True, blank=True)
    is_organizer = models.BooleanField(default=False)
    organization_name = models.CharField(max_length=100, null=True, blank=True)
    organization_description = models.TextField(null=True, blank=True)
    organization_inn = models.CharField(max_length=10, null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def clean(self):
        if self.is_organizer:
            if not self.organization_name:
                raise ValidationError("Organization name is required")
            if not self.organization_description:
                raise ValidationError("Organization description is required")
            if not self.organization_inn:
                raise ValidationError("Organization INN is required")
        return super().clean()

    def save(self, *args, **kwargs) -> None:
        self.full_clean()
        return super().save(*args, **kwargs)
