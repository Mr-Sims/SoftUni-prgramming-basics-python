from django.urls import path

from .views import create, index

urlpatterns = [
    path('', index, name="index"),
    path('create/', create, name="create"),



    # path('test/', test_view, name='test view'),


]
