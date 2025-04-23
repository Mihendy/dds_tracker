from django.urls import path

from app.internal.views.categories import CategoryCreateView, CategoryDeleteView, CategoryUpdateView

urlpatterns = [
    path('create/', CategoryCreateView.as_view(), name='category_create'),
    path('<int:pk>/edit/', CategoryUpdateView.as_view(), name='category_update'),
    path('statuses/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category_delete'),
]
