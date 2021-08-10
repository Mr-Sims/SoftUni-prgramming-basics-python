from django import forms
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError

UserModel = get_user_model()


class RegisterForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('email',)


class LoginForm(AuthenticationForm): # AuthenticationForm instead of forms.Form
    user = None

    # email = forms.EmailField()
    # password = forms.CharField(
    #     widget=forms.PasswordInput(),
    # )

    def clean_password(self):
        super().clean() # <= added becasue of the CBV
        self.user = authenticate(
            email=self.cleaned_data['username'],
            password = self.cleaned_data['password'],
        )
        if not self.user:
            raise ValidationError('Email and/or password incorrect.')

    def save(self):
        return self.user