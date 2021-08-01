from django.shortcuts import render, redirect

from notes.common.utils import get_profile
from notes.main_content.models import Note
from notes.profiles.forms import ProfileForm, EditProfileForm


def create_profile(request):
    # if someone tries to type directly 127.0.0.1:8000/create_profile/ and there already is a profile created,
    # this would redirect him back to 'home'. Otherwise nothing would stop him from creating other profiles
    profile = get_profile()
    if profile:
        return redirect('home')

    #profile-create form bellow
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProfileForm()
    context = {
        'form': form
    }
    return render(request, 'profile/home-no-profile.html', context)


def profile_details(request):
    profile = get_profile()
    notes = Note.objects.all()
    notes_count = len(notes)
    context = {
        'notes_count': notes_count,
        'profile': profile,
    }
    return render(request, 'profile/profile.html', context)


def edit_profile(request):
    profile = get_profile()
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        profile = get_profile()
        form = EditProfileForm(instance=profile)
    context = {
        'profile': profile,
        'form': form
    }
    return render(request, 'profile/edit-profile.html', context)


def delete_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        profile.delete()
        Note.objects.all().delete()
        return redirect('home')
