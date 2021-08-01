from django.urls import path

from notes.profiles.views import create_profile, profile_details, delete_profile, edit_profile

urlpatterns = (
    path('create_profile/', create_profile, name='create profile'),
    path('profile/', profile_details, name='profile details'),
    path('delete_profile/', delete_profile, name='delete profile'),
    path('edit_profile/', edit_profile, name='edit_profile'),
)