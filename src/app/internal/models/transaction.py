from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from app.internal.models.category import Category
from app.internal.models.status import Status
from app.internal.models.subcategory import Subcategory
from app.internal.models.transaction_type import TransactionType


class Transaction(models.Model):
    """Модель для транзакций, движений денежных средств"""
    created_at = models.DateField(default=timezone.now)

    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    type = models.ForeignKey(TransactionType, on_delete=models.PROTECT)

    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.PROTECT)

    amount = models.DecimalField(max_digits=12, decimal_places=2)
    comment = models.TextField(blank=True)

    def clean(self):
        """Проверка на соответствие категории и подкатегории"""
        if self.category.transaction_type != self.type:
            raise ValidationError(
                _("Category does not match the selected transaction type.")
            )
        if self.subcategory.category != self.category:
            raise ValidationError(
                _("Subcategory does not match the selected category.")
            )
