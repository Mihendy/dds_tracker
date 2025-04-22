from django.db import models


class Status(models.Model):
    """Модель для статусов транзакций"""
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name_plural = "Statuses"

    def __str__(self):
        return self.name
