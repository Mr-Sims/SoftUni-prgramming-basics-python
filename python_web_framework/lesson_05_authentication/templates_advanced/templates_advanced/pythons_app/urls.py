from django.urls import path

from .views import create, index, sign_in, sign_out

urlpatterns = [
    path('', index, name="index"),
    path('create/', create, name="create"),
    path('sign-in/', sign_in, name='sign in'),
    path('sign-out/', sign_out, name='sign out'),


    # path('test/', test_view, name='test view'),


]
