import os
from os.path import join

from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models

# validation method(the complex one)
# def is_positive(value):
#     if value <= 0:
#         raise ValidationError


class Pet(models.Model):
    TYPE_CHOICE_DOG = 'dog'
    TYPE_CHOICE_CAT = 'cat'
    TYPE_CHOICE_PARROT = 'parrot'

    TYPE_CHOICES = (
        (TYPE_CHOICE_DOG, 'Dog'),
        (TYPE_CHOICE_CAT, 'Cat'),
        (TYPE_CHOICE_PARROT, 'Parrot')
    )

    type = models.CharField(
        max_length=6,
        choices=TYPE_CHOICES
        )
    name = models.CharField(
        max_length=6,
        )
    age = models.PositiveIntegerField()
    # age = models.IntegerField(
    #     null=False,
    #     blank=False,
    #     validators=[
    #         models.Min(1)
    #     ]
    # )
    description = models.TextField()
    #image_url = models.URLField()
    image = models.ImageField(
        upload_to='pets',
    )

    # def save(self, force_insert=False, force_update=False, using=None,
    #          update_fields=None):
    #     db_pet = Pet.objects.get(pk=self.id)
    #     image_path = join(settings.MEDIA_ROOT, str(db_pet.image))
    #     os.remove(image_path)
    #     return super().save(
    #         force_insert=force_insert,
    #         force_update=force_update,
    #         using=using,
    #         update_fields=update_fields
    #     )


class Like(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)