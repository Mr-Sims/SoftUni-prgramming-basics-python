from django.urls import path

from . import views
from .views import PythonCreateView

urlpatterns = [
    #path('', views.index, name="index"),
    path('', views.IndexView.as_view(), name='index'),
    # path('create/', views.create, name="create"),
    path('create/', PythonCreateView.as_view(), name='create'),


    # path('test/', test_view, name='test view'),


]
