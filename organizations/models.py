from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

from django.contrib.auth import get_user_model

UserModel = get_user_model()

class Organization(models.Model):
    name = models.CharField(max_length=255)
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE)
    inn = models.CharField(max_length=10)
    kpp = models.CharField(max_length=9)
    ogrn = models.CharField(max_length=13)

    def __str__(self):
        return self.name


class OrganizationDocument(models.Model):
    organization = models.ForeignKey(Organization, related_name='documents', on_delete=models.CASCADE, blank=True, null=True)
    filepond = models.FileField(upload_to='organization_documents')

    def __str__(self):
        return f"Document"
