# todos.urls.py
from django.urls import path

from todos_app.todos.views import index, create_todo, update, delete_todo

# from todos_app.todos.views import create_todo, change_todo_state

urlpatterns = [
    path('', index, name='index'),
    path('create/ ', create_todo, name='create_todo'),
    path('update/<int:pk>', update, name='update'),
    path('delete/<int:pk>', delete_todo, name='delete'),

]
