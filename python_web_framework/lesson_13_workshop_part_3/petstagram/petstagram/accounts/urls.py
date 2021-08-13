from django.urls import path

from petstagram.accounts.views import login_user, logout_user, register_user, profile_details, RegisterView, \
    ProfileDetailsView, LoginUserView, LoginUserViewTrue

urlpatterns = (
    path('login/', LoginUserViewTrue.as_view(), name='log in user'),
    path('logout/', logout_user, name='log out user'),
    path('register/', RegisterView.as_view(), name='register user'),
    path('profile/', ProfileDetailsView.as_view(), name='profile details'),
)
