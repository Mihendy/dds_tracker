from django.urls import path

from app.internal.views.subcategories import SubcategoryCreateView, SubcategoryDeleteView, SubcategoryUpdateView

urlpatterns = [
    path('create/', SubcategoryCreateView.as_view(), name='subcategory_create'),
    path('<int:pk>/edit/', SubcategoryUpdateView.as_view(), name='subcategory_update'),
    path('statuses/<int:pk>/delete/', SubcategoryDeleteView.as_view(), name='subcategory_delete'),
]
