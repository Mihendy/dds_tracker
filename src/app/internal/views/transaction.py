from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, ListView, UpdateView

from app.internal.forms.transaction import TransactionFilterForm, TransactionForm
from app.internal.models.category import Category
from app.internal.models.subcategory import Subcategory
from app.internal.models.transaction import Transaction


class TransactionListView(ListView):
    model = Transaction
    template_name = 'transactions/list.html'
    context_object_name = 'transactions'

    def get_context_data(self, **kwargs):
        """Передача формы фильтрации в контекст"""
        context = super().get_context_data(**kwargs)

        form = TransactionFilterForm(self.request.GET)

        if form.is_valid():
            transactions = Transaction.objects.all()

            if form.cleaned_data.get('created_at__gte'):
                transactions = transactions.filter(created_at__gte=form.cleaned_data['created_at__gte'])
            if form.cleaned_data.get('created_at__lte'):
                transactions = transactions.filter(created_at__lte=form.cleaned_data['created_at__lte'])
            if form.cleaned_data.get('status'):
                transactions = transactions.filter(status=form.cleaned_data['status'])
            if form.cleaned_data.get('type'):
                transactions = transactions.filter(type=form.cleaned_data['type'])
            if form.cleaned_data.get('category'):
                transactions = transactions.filter(category=form.cleaned_data['category'])
            if form.cleaned_data.get('subcategory'):
                transactions = transactions.filter(subcategory=form.cleaned_data['subcategory'])

            context['transactions'] = transactions

        context['form'] = form
        return context


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


class TransactionDeleteView(View):
    """Удаление транзакции (ответ на AJAX запрос)"""
    def delete(self, request, pk):
        transaction = get_object_or_404(Transaction, pk=pk)
        transaction.delete()
        return JsonResponse({'success': True})


class GetCategoriesByTransactionTypeView(View):
    """Получение категорий и подкатегорий по типу транзакции (ответ на AJAX запрос)"""

    def get(self, request, transaction_type_pk):
        categories = Category.objects.filter(transaction_type__pk=transaction_type_pk)
        subcategories = Subcategory.objects.filter(category__transaction_type__pk=transaction_type_pk)

        categories_data = [{'pk': category.pk, 'name': str(category)} for category in categories]
        subcategories_data = [{'pk': subcategory.pk, 'name': str(subcategory)} for subcategory in subcategories]

        return JsonResponse({
            'categories': categories_data,
            'subcategories': subcategories_data
        })
