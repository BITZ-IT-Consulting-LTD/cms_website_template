from django.urls import path
from .views import (
    VideoListCreateView, VideoDetailView, VideoCategoryListView, VideoCategoryDetailView
)

urlpatterns = [
    # Video categories
    path('categories/', VideoCategoryListView.as_view(), name='video-category-list'),
    path('categories/<int:pk>/', VideoCategoryDetailView.as_view(), name='video-category-detail'),
    
    # Videos
    path('', VideoListCreateView.as_view(), name='video-list'),
    path('<slug:slug>/', VideoDetailView.as_view(), name='video-detail'),
]
