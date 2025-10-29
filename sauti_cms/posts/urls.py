from django.urls import path
from .views import (
    PostListCreateView, PostDetailView,
    CategoryListView, CategoryDetailView, TagListView
)

app_name = 'posts'

urlpatterns = [
    # Categories and Tags (must come before slug patterns)
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('tags/', TagListView.as_view(), name='tag-list'),
    
    # Posts
    path('', PostListCreateView.as_view(), name='post-list'),
    path('<slug:slug>/', PostDetailView.as_view(), name='post-detail'),
]
