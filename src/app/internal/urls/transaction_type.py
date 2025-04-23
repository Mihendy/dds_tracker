from django.urls import path

from app.internal.views.transaction_type import (
    TransactionTypeCreateView,
    TransactionTypeDeleteView,
    TransactionTypeUpdateView,
)

urlpatterns = [
    path('create/', TransactionTypeCreateView.as_view(), name='transaction_type_create'),
    path('<int:pk>/edit/', TransactionTypeUpdateView.as_view(), name='transaction_type_update'),
    path('<int:pk>/delete/', TransactionTypeDeleteView.as_view(), name='transaction_type_delete'),
]
