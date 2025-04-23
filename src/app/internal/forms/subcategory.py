from django import forms

from app.internal.models.subcategory import Subcategory


class SubcategoryForm(forms.ModelForm):
    class Meta:
        model = Subcategory
        fields = '__all__'
        labels = {
            'name': 'Название',
            'category': 'Категория',
        }
