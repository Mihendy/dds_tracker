from django.contrib import messages
from django.db.models import ProtectedError
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView

from app.internal.forms.transaction_type import TransactionTypeForm
from app.internal.models.transaction_type import TransactionType


class TransactionTypeCreateView(CreateView):
    model = TransactionType
    form_class = TransactionTypeForm
    template_name = 'transaction_type/create.html'
    success_url = reverse_lazy('directory_tree')


class TransactionTypeUpdateView(UpdateView):
    model = TransactionType
    form_class = TransactionTypeForm
    template_name = 'transaction_type/edit.html'
    success_url = reverse_lazy('directory_tree')


class TransactionTypeDeleteView(DeleteView):
    model = TransactionType
    success_url = reverse_lazy('directory_tree')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        try:
            return super().post(request, *args, **kwargs)
        except ProtectedError:
            messages.error(
                request,
                f"Невозможно удалить тип, так как он используется. "
                f"<a href='{reverse_lazy('transaction_list')}?type={self.object.pk}' class='alert-link'>Посмотреть записи</a>."
            )
            return redirect('directory_tree')
