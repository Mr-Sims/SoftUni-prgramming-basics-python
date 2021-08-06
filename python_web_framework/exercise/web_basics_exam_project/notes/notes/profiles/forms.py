import os
from os.path import join

from django import forms
from django.conf import settings

from notes.profiles.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)


class EditProfileForm(ProfileForm):

    def save(self, commit=True):
        profile = Profile.objects.get(pk=self.instance.user_id)
        if commit:
            image_path = join(settings.MEDIA_ROOT, str(profile.image))
            os.remove(image_path)
        return super().save(commit)


class DeleteProfileForm(ProfileForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'