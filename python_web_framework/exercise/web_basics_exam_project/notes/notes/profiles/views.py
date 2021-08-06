from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from notes.main_content.models import Note
from notes.profiles.forms import ProfileForm, EditProfileForm, DeleteProfileForm
from notes.profiles.models import Profile

UserModel = get_user_model()


@login_required
def profile_details(request):
    profile = Profile.objects.get(pk=request.user.id)
    notes_by_user = Note.objects.filter(user_id=request.user.id)
    notes_count = len(notes_by_user)
    context = {
        'profile': profile,
        'notes': notes_by_user,
        'notes_count': notes_count,
    }
    return render(request, 'profile/profile.html', context)

@login_required
def create_profile(request):
    profile = Profile.objects.get(pk=request.user.id)
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile details')
    else:
        form = ProfileForm(instance=profile)
    context = {
        'profile': profile,
        'form': form
    }
    return render(request, 'profile/edit-profile.html', context)


@login_required
def edit_profile(request):
    profile = Profile.objects.get(pk=request.user.id)
    if request.method == "POST":
        form = EditProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile details')
    else:
        form = EditProfileForm(instance=profile)

    context = {
        'profile': profile,
        'form': form
    }
    return render(request, 'profile/edit-profile.html', context)


def delete_profile(request):
    profile = Profile.objects.get(pk=request.user.id)
    user = UserModel.objects.get(pk=request.user.id)
    notes_by_user = Note.objects.filter(user_id=request.user.id)
    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, instance=profile)
        notes_by_user.delete()
        profile.delete()
        user.delete()
        return redirect('home')
    else:
        form = DeleteProfileForm(instance=profile)
    context = {
        'form': form,
        'profile': profile,
        'user': user,
        'notes': notes_by_user,
    }
    return render(request, 'profile/delete_profile.html', context)
