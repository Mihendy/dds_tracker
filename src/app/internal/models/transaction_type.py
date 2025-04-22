from django.db import models


class TransactionType(models.Model):
    """Модель для типов транзакций"""
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
