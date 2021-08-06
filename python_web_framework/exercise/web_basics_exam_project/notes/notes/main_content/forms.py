import os
from os.path import join

from django import forms
from django.conf import settings

from notes.main_content.models import Note


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        exclude = ('user',)


class CreateNoteForm(NoteForm):
    pass


class EditNoteForm(NoteForm):
    def save(self, commit=True):
        db_note = Note.objects.get(pk=self.instance.id)
        if commit:
            image_path = join(settings.MEDIA_ROOT, str(db_note.image))
            os.remove(image_path)
        return super().save(commit)


class DeleteNoteForm(NoteForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
