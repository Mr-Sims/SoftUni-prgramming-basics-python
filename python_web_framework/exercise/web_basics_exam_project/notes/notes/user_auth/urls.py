from django.urls import path

from notes.user_auth.views import register, log_in, log_out, RegisterUserView, LogInView

urlpatterns = (
    path('register/', RegisterUserView.as_view(), name='register'),
    path('log-in/', LogInView.as_view(), name='log in'),
    path('log-out/', log_out, name='log out'),
)