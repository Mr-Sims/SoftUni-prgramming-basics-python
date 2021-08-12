from django.urls import path

from petstagram.accounts.views import login_user, logout_user, register_user, profile_details, RegisterView, \
    ProfileDetailView

urlpatterns = (
    path('login/', login_user, name='log in user'),
    path('logout/', logout_user, name='log out user'),
    path('register/', RegisterView.as_view(), name='register user'),
    path('profile/', ProfileDetailView.as_view(), name='profile details'),
)
