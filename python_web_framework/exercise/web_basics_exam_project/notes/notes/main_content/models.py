from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class Note(models.Model):
    title = models.CharField(
        max_length=30,
    )

    image = models.ImageField(upload_to='notes')

    content = models.TextField()

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )