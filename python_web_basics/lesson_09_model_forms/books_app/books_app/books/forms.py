from django import forms

from books_app.books.models import Book


# class BookForm(forms.ModelForm):
#     class Meta:
#         model = Book
#         fields = '__all__'
#

# # one widget for all fields
# class BootstrapFormMixin:
#     def _init_bootstrap(self):
#         for (_, field) in self.fields.items():
#             field.widget.attrs = {
#                 'class': 'form-control',
#             }
#
#
# class BookForm(forms.ModelForm, BootstrapFormMixin):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self._init_bootstrap()
#
#     class Meta:
#         model = Book
#         fields = '__all__'
#


###################################################


# # widget per each field
class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'pages': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'author': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 5
                }
            )
        }
