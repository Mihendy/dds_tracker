from django.shortcuts import render
from django.views import View

from app.internal.models.status import Status
from app.internal.models.transaction_type import TransactionType


class DirectoryTreeView(View):
    def get(self, request):
        statuses = Status.objects.all()

        transaction_types = TransactionType.objects.prefetch_related(
            'categories__subcategories'
        ).all()

        context = {
            'statuses': statuses,
            'transaction_types': transaction_types,
        }

        return render(request, 'directory/tree.html', context)
