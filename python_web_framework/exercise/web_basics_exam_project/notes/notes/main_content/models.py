from django.db import models


class Note(models.Model):
    title = models.CharField(
        max_length=30,
    )

    image = models.ImageField(upload_to='notes')

    content = models.TextField()