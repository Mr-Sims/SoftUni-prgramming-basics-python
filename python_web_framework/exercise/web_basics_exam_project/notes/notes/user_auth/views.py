from django.contrib.auth import logout, login, get_user_model
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from notes.user_auth.forms import RegisterForm, LoginForm


UserModel = get_user_model()


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


class RegisterUserView(CreateView):
    template_name = 'user_auth/register.html'
    model = UserModel
    success_url = reverse_lazy('home')
    form_class = RegisterForm


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


class LogInView(LoginView):
    template_name = 'user_auth/log_in.html'
    form_class = LoginForm

    def get_success_url(self):
        return reverse_lazy('home')


def log_out(request):
    logout(request)
    return redirect('home')

