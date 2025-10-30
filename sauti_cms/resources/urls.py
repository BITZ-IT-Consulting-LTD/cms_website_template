from django.urls import path
from .views import (
    ResourceListCreateView, ResourceDetailView,
    ResourceCategoryListView, ResourceCategoryDetailView
)

app_name = 'resources'

urlpatterns = [
    path('', ResourceListCreateView.as_view(), name='resource-list'),
    path('categories/', ResourceCategoryListView.as_view(), name='category-list'),
    path('categories/<int:pk>/', ResourceCategoryDetailView.as_view(), name='category-detail'),
    path('<slug:slug>/', ResourceDetailView.as_view(), name='resource-detail'),
]
