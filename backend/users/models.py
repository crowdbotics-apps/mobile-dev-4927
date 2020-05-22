from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    name = models.CharField(null=True, blank=True, max_length=255,)
    jhgkjhgkjhgkjhgkjg = models.BigIntegerField(null=True, blank=True,)
    jzhgfhsfkjghrf = models.BigIntegerField(null=True, blank=True,)
    jhgsafakd = models.BigIntegerField(null=True, blank=True,)
    jhghjgfw = models.ManyToManyField(
        "home.HomePage", blank=True, related_name="user_jhghjgfw",
    )

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})
