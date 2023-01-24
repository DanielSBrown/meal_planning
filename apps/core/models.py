from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .mixins import TimeStampedModelMixin


class User(AbstractUser, TimeStampedModelMixin):
    """Default user for meal_planning backend."""

    #: First and last name do not cover name patterns around the globe
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    first_name = models.CharField(blank=True, null=True, max_length=255)
    last_name = models.CharField(blank=True, null=True, max_length=255)
    email = models.EmailField(unique=True)
