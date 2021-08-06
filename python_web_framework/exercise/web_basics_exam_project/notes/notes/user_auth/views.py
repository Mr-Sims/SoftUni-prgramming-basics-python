from django.contrib.auth import logout, login
from django.shortcuts import render, redirect

from notes.user_auth.forms import RegisterForm, LoginForm


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()

    context = {
        'form': form,
    }
    return render(request, 'user_auth/register.html', context)


def log_in(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.user
            login(request, user)
            return redirect('home')
    else:
        form = LoginForm()

    context = {
        'form': form,
    }
    return render(request, 'user_auth/log_in.html', context)



def log_out(request):
    logout(request)
    return redirect('home')

