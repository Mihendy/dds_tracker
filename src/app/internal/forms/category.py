from django import forms

from app.internal.models.category import Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        labels = {
            'name': 'Название',
            'transaction_type': 'Тип транзакции',
        }
