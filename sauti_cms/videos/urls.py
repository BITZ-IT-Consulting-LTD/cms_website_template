from django.urls import path
from .views import (
    VideoListCreateView, VideoDetailView, VideoCategoryListView
)

urlpatterns = [
    # Video categories
    path('categories/', VideoCategoryListView.as_view(), name='video-category-list'),
    
    # Videos
    path('', VideoListCreateView.as_view(), name='video-list'),
    path('<slug:slug>/', VideoDetailView.as_view(), name='video-detail'),
]
