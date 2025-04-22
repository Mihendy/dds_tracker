from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView

from app.internal.forms.transaction import TransactionForm
from app.internal.models.transaction import Transaction


class TransactionListView(ListView):
    model = Transaction
    template_name = 'transactions/list.html'
    context_object_name = 'transactions'


class TransactionCreateView(CreateView):
    model = Transaction
    form_class = TransactionForm
    template_name = 'transactions/create.html'
    success_url = reverse_lazy('transaction_list')


class TransactionUpdateView(UpdateView):
    model = Transaction
    form_class = TransactionForm
    template_name = 'transactions/edit.html'
    success_url = reverse_lazy('transaction_list')
