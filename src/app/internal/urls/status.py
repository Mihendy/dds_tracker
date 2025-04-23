from django.urls import path

from app.internal.views.status import StatusCreateView, StatusDeleteView, StatusUpdateView

urlpatterns = [
    path('create/', StatusCreateView.as_view(), name='status_create'),
    path('<int:pk>/edit/', StatusUpdateView.as_view(), name='status_update'),
    path('<int:pk>/delete/', StatusDeleteView.as_view(), name='status_delete'),
]
