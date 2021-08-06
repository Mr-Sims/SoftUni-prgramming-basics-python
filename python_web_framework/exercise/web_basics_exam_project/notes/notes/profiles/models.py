from django.db import models
from django.contrib.auth import get_user_model

from notes.user_auth.models import NotesUser

UserModel = get_user_model()


class Profile(models.Model):
    first_name = models.CharField(
        max_length=20,
        blank=True
    )

    last_name = models.CharField(
        max_length=20,
        blank=True
    )

    age = models.IntegerField(
        blank=True,
        null=True,
    )

    image = models.ImageField(
        upload_to='profile',
        blank=True,
    )

    user = models.OneToOneField(
        NotesUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )


from notes.user_auth.signals import *