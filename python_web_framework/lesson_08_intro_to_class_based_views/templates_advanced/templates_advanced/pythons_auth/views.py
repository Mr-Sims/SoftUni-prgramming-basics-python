from django.contrib.auth import login, logout, get_user_model
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from templates_advanced.pythons_auth.forms import SignInForm, SignUpForm

UserModel = get_user_model()

## FuncBased View
def sign_up(request):
    if request.POST:
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sign in')
    else:
        form = SignUpForm()
    context = {
        'form': form,
    }
    return render(request, 'auth/sign-up.html', context)


def sign_in(request):
    if request.method == "POST":
        form = SignInForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = SignInForm()
    context = {
        'form': form,
    }
    return render(request, 'auth/sign-in.html', context)


def sign_out(request):
    logout(request)
    return redirect('index')


## Class-Based View
class SignUpView(CreateView):
    template_name = 'auth/sign-up.html'
    model = UserModel
    form_class = SignUpForm
    success_url = reverse_lazy('index')


class SignInView(LoginView):
    template_name = 'auth/sign-in.html'
    form_class = SignInForm

    def get_success_url(self):
        return reverse_lazy('index')