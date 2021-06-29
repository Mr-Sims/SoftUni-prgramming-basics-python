from django.urls import path

from notes.main.views import home, create_profile, profile_details, delete_profile, create_note, edit_note, delete_note, \
    note_details

urlpatterns = [
    path('', home, name='home'),
    path('create_profile/', create_profile, name='create profile'),
    path('profile/', profile_details, name='profile details'),
    path('delete_profile/', delete_profile, name='delete profile'),

    path('add/', create_note, name='create note'),
    path('edit/<int:pk>', edit_note, name='edit note'),
    path('delete/<int:pk>', delete_note, name='delete note'),
    path('details/<int:pk>', note_details, name='note details')
]