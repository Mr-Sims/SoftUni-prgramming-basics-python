from django.urls import path

from notes.main_content.views import home, NoteUpdateView, NoteDetailView, delete_note, NoteCreateView, HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),

    path('add/', NoteCreateView.as_view(), name='create note'),
    path('edit/<int:pk>', NoteUpdateView.as_view(), name='edit note'),
    path('delete/<int:pk>', delete_note, name='delete note'),
    path('details/<int:pk>', NoteDetailView.as_view(), name='note details'),
]