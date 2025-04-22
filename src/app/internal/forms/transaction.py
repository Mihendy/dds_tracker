from django import forms

from app.internal.models.transaction import Transaction


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
