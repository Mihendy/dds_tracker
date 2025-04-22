from django.db import models

from app.internal.models.transaction_type import TransactionType


class Category(models.Model):
    name = models.CharField(max_length=100)
    transaction_type = models.ForeignKey(TransactionType, on_delete=models.PROTECT, related_name='categories')

    class Meta:
        unique_together = ('name', 'transaction_type')  # уникальность в рамках типа, но название может повторяться
        verbose_name_plural = 'Categories'

    def __str__(self):
        return f"{self.transaction_type.name} > {self.name}"
