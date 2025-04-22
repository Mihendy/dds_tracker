from django.contrib import admin

from app.internal.models.transaction import Transaction


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'status', 'type', 'category', 'subcategory', 'amount', 'comment')
    search_fields = ('type__name', 'category__name', 'subcategory__name', 'comment')
    list_filter = ('created_at', 'status', 'type', 'category', 'subcategory')
