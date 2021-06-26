from django import forms
from django.core.exceptions import ValidationError

from expenses_tracker.core.profile_utils import get_profile
from expenses_tracker.expenses.models import Expense


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = '__all__'

    def clean_price(self):
        profile = get_profile()
        expenses = Expense.objects.all()
        budget = profile.budget
        budget_left = budget - sum(e.price for e in expenses)
        price = float(self.cleaned_data['price'])
        if budget_left < price:
             raise ValidationError('Not enough budget')
        return price

class CreateExpenseForm(ExpenseForm):
    pass


class EditExpenseForm(ExpenseForm):
    pass


class DeleteExpenseForm(ExpenseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'

