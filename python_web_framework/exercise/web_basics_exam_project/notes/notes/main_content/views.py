from django.shortcuts import render, redirect

from notes.common.utils import get_profile
from notes.main_content.forms import CreateNoteForm, EditNoteForm, DeleteNoteForm
from notes.main_content.models import Note


def home(request):
    profile = get_profile()
    if not profile:
        return redirect('create profile')
    notes = Note.objects.all
    context = {
        'notes': notes
    }
    return render(request, 'profile/home-with-profile.html', context)


def create_note(request):
    if request.method == "POST":
        form = CreateNoteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreateNoteForm()
    context = {
        'form': form
    }
    return render(request, 'notes/note-create.html', context)


def edit_note(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == "POST":
        form = EditNoteForm(request.POST, request.FILES, instance=note)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EditNoteForm(instance=note)
    context = {
        'note': note,
        'form': form
    }
    return render(request, 'notes/note-edit.html', context)


def delete_note(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == "POST":
        note.delete()
        return redirect('home')
    else:
        form = DeleteNoteForm(instance=note)
    context = {
        'note': note,
        'form': form
    }
    return render(request, 'notes/note-delete.html', context)


def note_details(request, pk):
    note = Note.objects.get(pk=pk)
    context = {
        'note': note
    }
    return render(request, 'notes/note-details.html', context)


