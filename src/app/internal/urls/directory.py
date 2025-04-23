from django.urls import path

from app.internal.views.directory import DirectoryTreeView

urlpatterns = [
    path('', DirectoryTreeView.as_view(), name='directory_tree'),
]
