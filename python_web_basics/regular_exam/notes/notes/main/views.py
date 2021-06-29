
from django.shortcuts import render, redirect

from notes.common.utils import get_profile
from notes.main.forms import ProfileForm, CreateNoteForm, EditNoteForm, DeleteNoteForm
from notes.main.models import Note


def home(request):
    profile = get_profile()
    if not profile:
        return redirect('create profile')
    notes = Note.objects.all
    context = {
        'notes': notes
    }
    return render(request, 'home-with-profile.html', context)


def create_profile(request):
    # if someone tries to type directly 127.0.0.1:8000/create_profile/ and there already is a profile created,
    # this would redirect him back to 'home'. Otherwise nothing would stop him from creating other profiles
    profile = get_profile()
    if profile:
        return redirect('home')

    #profile-create form bellow
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProfileForm()
    context = {
        'form': form
    }
    return render(request, 'home-no-profile.html', context)


def profile_details(request):
    profile = get_profile()
    notes = Note.objects.all()
    notes_count = len(notes)
    context = {
        'notes_count': notes_count,
        'profile': profile,
    }
    return render(request, 'profile.html', context)


def delete_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        profile.delete()
        Note.objects.all().delete()
        return redirect('home')


def create_note(request):
    if request.method == "POST":
        form = CreateNoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreateNoteForm()
    context = {
        'form': form
    }
    return render(request, 'note-create.html', context)


def edit_note(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == "POST":
        form = EditNoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EditNoteForm(instance=note)
    context = {
        'note': note,
        'form': form
    }
    return render(request, 'note-edit.html', context)


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
    return render(request, 'note-delete.html', context)


def note_details(request, pk):
    note = Note.objects.get(pk=pk)
    context = {
        'note': note
    }
    return render(request, 'note-details.html', context)
