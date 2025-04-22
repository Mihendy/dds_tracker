from django.contrib import admin

from app.internal.models.transaction_type import TransactionType


@admin.register(TransactionType)
class TransactionTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
