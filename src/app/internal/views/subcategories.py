from django.contrib import messages
from django.db.models import ProtectedError
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView

from app.internal.forms.subcategory import SubcategoryForm
from app.internal.models.category import Category
from app.internal.models.subcategory import Subcategory


class SubcategoryCreateView(CreateView):
    model = Subcategory
    form_class = SubcategoryForm
    template_name = 'subcategories/create.html'
    success_url = reverse_lazy('directory_tree')

    def get_form(self, form_class=None):
        """Устанавливаю disabled для поля category, если оно передано в GET запросе"""
        form = super().get_form(form_class)
        category_id = self.request.GET.get('category')
        if category_id:
            form.initial['category'] = category_id
            form.fields['category'].disabled = True
        return form

    def form_valid(self, form):
        """Перегружаю метод form_valid, чтобы установить категорию, т.к. она не передается в форме"""
        category_id = self.request.GET.get('category')
        if category_id:
            try:
                form.instance.category = Category.objects.get(pk=category_id)
            except Category.DoesNotExist:
                pass
        return super().form_valid(form)


class SubcategoryUpdateView(UpdateView):
    model = Subcategory
    form_class = SubcategoryForm
    template_name = 'subcategories/edit.html'
    success_url = reverse_lazy('directory_tree')


class SubcategoryDeleteView(DeleteView):
    model = Subcategory
    success_url = reverse_lazy('directory_tree')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        try:
            return super().post(request, *args, **kwargs)
        except ProtectedError:
            messages.error(
                request,
                f"Невозможно удалить подкатегорию, так как она используется. "
                f"<a href='{reverse_lazy('transaction_list')}?subcategory={self.object.pk}' class='alert-link'>Посмотреть записи</a>."
            )
            return redirect('directory_tree')
