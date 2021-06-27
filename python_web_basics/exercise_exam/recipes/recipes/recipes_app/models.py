from django.core.exceptions import ValidationError
from django.db import models


def validation_comma_separator(value):
    if ', ' not in value:
        raise ValidationError('Ingredients need to be separated by ", "')


class Recipe(models.Model):

    title = models.CharField(
        max_length=30
    )
    image_url = models.URLField()

    description = models.TextField()

    ingredients = models.CharField(
        max_length=250,
        validators=(validation_comma_separator,)

    )

    time = models.IntegerField()
