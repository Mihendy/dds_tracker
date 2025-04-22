from django.db import models

from app.internal.models.category import Category


class Subcategory(models.Model):
    """Модель для подкатегорий транзакций"""
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')

    class Meta:
        unique_together = ('name', 'category')  # уникальность в рамках категории
        verbose_name_plural = 'Subcategories'

    def __str__(self):
        return f"{self.category} > {self.name}"
