from django.contrib import messages
from django.db.models import ProtectedError
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView

from app.internal.forms.status import StatusForm
from app.internal.models.status import Status


class StatusCreateView(CreateView):
    model = Status
    form_class = StatusForm
    template_name = 'statuses/create.html'
    success_url = reverse_lazy('directory_tree')


class StatusUpdateView(UpdateView):
    model = Status
    form_class = StatusForm
    template_name = 'statuses/edit.html'
    success_url = reverse_lazy('directory_tree')


class StatusDeleteView(DeleteView):
    model = Status
    success_url = reverse_lazy('directory_tree')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        try:
            return super().post(request, *args, **kwargs)
        except ProtectedError:
            messages.error(
                request,
                f"Невозможно удалить статус, так как он используется. "
                f"<a href='{reverse_lazy('transaction_list')}?status={self.object.pk}' class='alert-link'>Посмотреть записи</a>."
            )
            return redirect('directory_tree')
