from django.contrib import messages
from django.db.models import ProtectedError
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView

from app.internal.forms.category import CategoryForm
from app.internal.models.category import Category
from app.internal.models.transaction_type import TransactionType


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'categories/create.html'
    success_url = reverse_lazy('directory_tree')

    def get_initial(self):
        """Устанавливаю начальное значение для поля type, если оно передано в GET запросе (query)"""
        initial = super().get_initial()
        type_id = self.request.GET.get('type')
        if type_id:
            try:
                initial['type'] = TransactionType.objects.get(pk=type_id)
            except TransactionType.DoesNotExist:
                pass
        return initial

    def get_form(self, form_class=None):
        """Устанавливаю disabled для поля type, если оно передано в GET запросе"""
        form = super().get_form(form_class)
        type_id = self.request.GET.get('type')
        if type_id:
            form.initial['transaction_type'] = type_id
            form.fields['transaction_type'].disabled = True
        return form

    def form_valid(self, form):
        type_id = self.request.GET.get('type')
        # Перегружаю метод form_valid, чтобы установить тип транзакции, т.к. она не передается в форме
        if type_id:
            try:
                form.instance.transaction_type = TransactionType.objects.get(pk=type_id)
            except TransactionType.DoesNotExist:
                pass
        return super().form_valid(form)


class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'categories/edit.html'
    success_url = reverse_lazy('directory_tree')


class CategoryDeleteView(DeleteView):
    model = Category
    success_url = reverse_lazy('directory_tree')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        try:
            return super().post(request, *args, **kwargs)
        except ProtectedError:
            messages.error(
                request,
                f"Невозможно удалить подкатегорию, так как она используется. "
                f"<a href='{reverse_lazy('transaction_list')}?category={self.object.pk}' class='alert-link'>Посмотреть записи</a>."
            )
            return redirect('directory_tree')
