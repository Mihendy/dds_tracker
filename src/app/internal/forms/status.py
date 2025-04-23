from django import forms

from app.internal.models.status import Status


class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = '__all__'
        labels = {
            'name': 'Название',
        }
