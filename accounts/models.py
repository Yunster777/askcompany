from django.conf import settings
from django.db import models
from django.urls import reverse


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    address = models.CharField(max_length=100, blank=True)
    zipcode = models.CharField(max_length=6, blank=True)

    def get_absolute_url(self):
        return reverse("accounts:profile")
