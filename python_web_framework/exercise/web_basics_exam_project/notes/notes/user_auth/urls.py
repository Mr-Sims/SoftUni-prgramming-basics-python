from django.urls import path

from notes.user_auth.views import register, log_in, log_out

urlpatterns = (
    path('register/', register, name='register'),
    path('log-in/', log_in, name='log in'),
    path('log-out/', log_out, name='log out'),
)