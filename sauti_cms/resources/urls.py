from django.urls import path
from .views import (
    ResourceListCreateView, ResourceDetailView, ResourceCategoryListView
)

app_name = 'resources'

urlpatterns = [
    path('', ResourceListCreateView.as_view(), name='resource-list'),
    path('categories/', ResourceCategoryListView.as_view(), name='category-list'),
    path('<slug:slug>/', ResourceDetailView.as_view(), name='resource-detail'),
]
