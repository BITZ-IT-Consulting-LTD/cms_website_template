from django.urls import path
from .views import (
    PostListCreateView, PostDetailView,
    CategoryListView, TagListView
)

app_name = 'posts'

urlpatterns = [
    # Posts
    path('', PostListCreateView.as_view(), name='post-list'),
    path('<slug:slug>/', PostDetailView.as_view(), name='post-detail'),
    
    # Categories and Tags
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('tags/', TagListView.as_view(), name='tag-list'),
]
