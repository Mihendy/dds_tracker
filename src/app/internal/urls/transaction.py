from django.urls import path

from app.internal.views.transaction import (
    GetCategoriesByTransactionTypeView,
    TransactionCreateView,
    TransactionDeleteView,
    TransactionListView,
    TransactionUpdateView,
)

urlpatterns = [
    path('', TransactionListView.as_view(), name='transaction_list'),
    path('create/', TransactionCreateView.as_view(), name='transaction_create'),
    path('<int:pk>/edit/', TransactionUpdateView.as_view(), name='transaction_update'),
    path('<int:pk>/delete/', TransactionDeleteView.as_view(), name='transaction_delete'),
    path('get_categories_by_type/<int:transaction_type_pk>/', GetCategoriesByTransactionTypeView.as_view(),
         name='get_categories_by_type'),
]
