from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator

# validator for the presence of a certain char
from todos_app.todos.models import Todo
from todos_app.todos.models.todo import Person


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


## Django Model Form
class CreateTodoForm2(forms.ModelForm):
    class Meta:
        model = Todo
        # fields = '__all__'
        # fields = ('text','state', 'description', 'owner')
        exclude = ('categories',)
        widgets = {
            'owner': forms.RadioSelect(),
            'text': forms.TextInput(

                attrs={
                    'class': 'form-control',
                    'placeholder': 'task name'

                }
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'task description',
                    'rows': 3
                }
            )

        }

    # # Validators that seem to work for what they do, but they mess up other functions and I can`t figure out how to fix that

    # def clean(self):
    #     owner = self.cleaned_data['owner']
    #     if owner.todo_set.count() > 2:
    #         raise ValidationError(f'{owner.name} cannot have more than 2 todos')

    # def clean_text(self):
    #     validate_dot(self.cleaned_data['text'])


## Normal Django form
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
            attrs={
                'class': 'my-text-area',
                'rows': 3,
            }
        ),

    )

    bots_catcher = forms.CharField(
        widget=forms.HiddenInput(),
        required=False,
        validators=[
            # validate_bot_catcher_empty
        ]

    )

    def clean_bots_catcher(self):
        value = self.cleaned_data['bots_catcher']
        validate_bot_catcher_empty(value)


class UpdateTodoForm(CreateTodoForm):
    state = forms.BooleanField()
