import os
from os.path import join

from django import forms
from django.conf import settings
from django.contrib.auth import get_user_model


from petstagram.core.forms import BootstrapFormMixin
from petstagram.pets.models import Pet

UserModel = get_user_model()

class PetForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Pet
        exclude = ('user',)


class EditPetForm(PetForm):

    # put new image and delete the old. Does not work through the django admin
    # def save(self, commit=True):
    #     db_pet = Pet.objects.get(pk=self.instance.id)
    #     if commit:
    #         image_path = join(settings.MEDIA_ROOT, str(db_pet.image))
    #         os.remove(image_path)
    #     return super().save(commit)


    class Meta:
        model = Pet
        fields = '__all__'
        widgets = {
            'type': forms.TextInput(
                attrs={
                    'readonly': 'readonly'
                }
            )
        }


