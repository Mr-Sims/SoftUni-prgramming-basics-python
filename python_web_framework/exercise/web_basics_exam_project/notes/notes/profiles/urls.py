from django.urls import path

from notes.profiles.views import profile_details, edit_profile, create_profile, delete_profile

urlpatterns = (

    path('profile/', profile_details, name='profile details'),
    path('create-profile/', create_profile, name='create profile'),
    path('edit-profile', edit_profile, name='edit profile'),
    path('delete-profile', delete_profile, name='delete profile'),

)