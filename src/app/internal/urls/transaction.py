from django.urls import path

from app.internal.views.transaction import TransactionCreateView, TransactionListView, TransactionUpdateView

urlpatterns = [
    path('', TransactionListView.as_view(), name='transaction_list'),
    path('create/', TransactionCreateView.as_view(), name='transaction_create'),
    path('edit/<int:pk>/', TransactionUpdateView.as_view(), name='transaction_update'),
]
