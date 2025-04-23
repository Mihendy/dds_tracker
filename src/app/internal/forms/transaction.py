from django import forms

from app.internal.models.category import Category
from app.internal.models.status import Status
from app.internal.models.subcategory import Subcategory
from app.internal.models.transaction import Transaction
from app.internal.models.transaction_type import TransactionType


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = '__all__'
        labels = {
            'created_at': 'Дата',
            'status': 'Статус',
            'type': 'Тип',
            'category': 'Категория',
            'subcategory': 'Подкатегория',
            'amount': 'Сумма',
            'comment': 'Комментарий',
        }


class TransactionFilterForm(forms.Form):
    """Форма для фильтрации транзакций"""
    created_at__gte = forms.DateField(required=False, widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    created_at__lte = forms.DateField(required=False, widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    status = forms.ModelChoiceField(queryset=Status.objects.all(), required=False, empty_label="----", widget=forms.Select(attrs={'class': 'form-select'}))
    type = forms.ModelChoiceField(queryset=TransactionType.objects.all(), required=False, empty_label="----", widget=forms.Select(attrs={'class': 'form-select'}))
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=False, empty_label="----", widget=forms.Select(attrs={'class': 'form-select'}))
    subcategory = forms.ModelChoiceField(queryset=Subcategory.objects.all(), required=False, empty_label="----", widget=forms.Select(attrs={'class': 'form-select'}))
