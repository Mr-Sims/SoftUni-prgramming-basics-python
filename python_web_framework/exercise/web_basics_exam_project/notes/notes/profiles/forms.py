import os
from os.path import join

from django import forms
from django.conf import settings

from notes.common.utils import get_profile
from notes.profiles.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class EditProfileForm(ProfileForm):
    def save(self, commit=True):
        profile = get_profile()
        if commit:
            image_path = join(settings.MEDIA_ROOT, str(profile.image))
            os.remove(image_path)
        return super().save(commit)