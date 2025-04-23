from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

from app.internal.views.transaction import TransactionListView

urlpatterns = [
    path('', RedirectView.as_view(url='/transactions/')),
    path('admin/', admin.site.urls),
    path('transactions/', include('app.internal.urls.transaction')),
    path('directories/', include('app.internal.urls.directory')),
    path('statuses/', include('app.internal.urls.status')),
    path('subcategories/', include('app.internal.urls.subcategory')),
    path('transaction_types/', include('app.internal.urls.transaction_type')),
    path('categories/', include('app.internal.urls.category')),
]
