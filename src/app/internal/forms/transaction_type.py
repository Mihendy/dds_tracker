from django import forms

from app.internal.models.transaction_type import TransactionType


class TransactionTypeForm(forms.ModelForm):
    class Meta:
        model = TransactionType
        fields = '__all__'
        labels = {
            'name': 'Название',
        }
