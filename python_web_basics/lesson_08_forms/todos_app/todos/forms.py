from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator


# validator for the presence of a certain char
def validate_dot(value):
    if '.' in value:
        raise forms.ValidationError('\'.\' is present in value')


# validator for minimum length of input
def validate_min_length(min_length):
    def validate(value):
        if len(value) < min_length:
            raise forms.ValidationError(f'Length must be at least {min_length} characters')
    return validate


def validate_bot_catcher_empty(value):
    if value:
        raise ValidationError('You are a bot')


class CreateTodoForm(forms.Form):
    text = forms.CharField(
        max_length=30,
        validators=[
            validate_dot,
            validate_min_length(3),
        ],
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )

    description = forms.CharField(
        validators=[
            validate_dot,
            validate_min_length(5)
        ],
        widget=forms.Textarea(
            attrs= {
                'class': 'my-text-area',
                'rows': 3,
            }
        ),

    )

    bots_catcher = forms.CharField(
        widget=forms.HiddenInput(),
        required=False,
        validators=[
            #validate_bot_catcher_empty
        ]

    )

    def clean_bot_catcher(self):
        value = self.cleaned_data['bots_catcher']
        validate_bot_catcher_empty(value)

class UpdateTodoForm(CreateTodoForm):
    state = forms.BooleanField()