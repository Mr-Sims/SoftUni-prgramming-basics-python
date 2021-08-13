from django.contrib.auth import logout, login, get_user_model, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView

from petstagram.accounts.forms import LoginForm, ProfileForm, LoginFormTrue
from petstagram.accounts.forms import RegisterForm
from petstagram.accounts.models import Profile
from petstagram.core.forms import BootstrapFormViewMixin
from petstagram.pets.models import Pet

UserModel = get_user_model()


class RegisterView(CreateView, BootstrapFormViewMixin):
    model = UserModel
    template_name = 'accounts/signup.html'
    form_class = RegisterForm
    success_url = reverse_lazy('landing page')

    # in order for us to login the user after he has registered, we use this
    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result


# variant 1 for profile view/update
class ProfileDetailsView(LoginRequiredMixin, BootstrapFormViewMixin, FormView):
    template_name = 'accounts/user_profile.html'
    form_class = ProfileForm
    success_url = reverse_lazy('profile details')
    object = None

    def get(self, request, *args, **kwargs):
        self.object = Profile.objects.get(pk=request.user.id)
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = Profile.objects.get(pk=request.user.id)
        return super().post(request, *args, **kwargs)

    # to set and update profile pic
    def form_valid(self, form):
        profile = self.object
        profile.profile_image = form.cleaned_data['profile_image']
        profile.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pets'] = Pet.objects.filter(user_id=self.request.user.id)
        context['profile'] = Profile.objects.get(user_id=self.request.user.id)
        return context


# custom CBV Login View
class LoginUserView(FormView, BootstrapFormViewMixin):
    template_name = 'accounts/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('landing page')

    def form_valid(self, form):
        user = authenticate(
            email=form.cleaned_data['email'],
            password=form.cleaned_data['password'],
        )
        if not user:
            raise ValidationError('Email and/or password incorrect')
        login(self.request, user)
        return super(). form_valid(form)



class LoginUserViewTrue(LoginView, BootstrapFormViewMixin):
    form_class = LoginFormTrue
    success_url = reverse_lazy('landing page')
    template_name = 'accounts/login.html'



def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid:
            user = form.save()
            login(request, user)
            return redirect('landing page')
    else:
        form = RegisterForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('landing page')
    else:
        form = LoginForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


def logout_user(request):
    logout(request)
    return redirect('landing page')


@login_required
def profile_details(request):
    profile = Profile.objects.get(pk=request.user.id)
    if request.method == "POST":
        form = ProfileForm(
            request.POST,
            request.FILES,
            instance=profile,
        )
        if form.is_valid():
            form.save()
            return redirect('profile details')
    else:
        form = ProfileForm(instance=profile)
    user_pets = Pet.objects.filter(user_id=request.user.id)
    context = {
        'form': form,
        'pets': user_pets,
        'profile': profile,
    }
    return render(request, 'accounts/user_profile.html', context)
