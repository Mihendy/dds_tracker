from django.contrib import admin

from app.internal.models.category import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'transaction_type')
    search_fields = ('name',)
    list_filter = ('transaction_type',)
