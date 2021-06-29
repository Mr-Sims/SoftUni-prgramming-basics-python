from django.contrib import admin

from notes.main.models import Profile, Note


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['first_name']


class NoteAdmin(admin.ModelAdmin):
    list_display = ['title']


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Note, NoteAdmin)
