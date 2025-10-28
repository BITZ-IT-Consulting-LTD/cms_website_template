from rest_framework import generics, permissions, filters
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from .models import Video, VideoCategory
from .serializers import (
    VideoSerializer, VideoListSerializer, VideoCategorySerializer
)


class IsEditorOrReadOnly(permissions.BasePermission):
    """Custom permission: Only editors/admins can create/edit, others read-only"""
    
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.is_editor


class VideoCategoryListView(generics.ListAPIView):
    """List all video categories"""
    queryset = VideoCategory.objects.all()
    serializer_class = VideoCategorySerializer
    permission_classes = [permissions.AllowAny]


class VideoListCreateView(generics.ListCreateAPIView):
    """List and create videos"""
    queryset = Video.objects.select_related('category', 'author').all()
    permission_classes = [IsEditorOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'description']
    ordering_fields = ['created_at', 'published_at', 'views_count', 'title']
    ordering = ['-published_at', '-created_at']
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return VideoListSerializer
        return VideoSerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        
        # Filter by featured videos
        if self.request.query_params.get('featured') == 'true':
            queryset = queryset.filter(is_featured=True)
        
        # Filter by status
        status = self.request.query_params.get('status')
        if status:
            queryset = queryset.filter(status__iexact=status)
        
        # Limit results
        limit = self.request.query_params.get('limit')
        if limit:
            try:
                queryset = queryset[:int(limit)]
            except ValueError:
                pass
        
        return queryset
    
    def perform_create(self, serializer):
        # Set author to current user
        serializer.save(author=self.request.user)


class VideoDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve, update, or delete a video"""
    queryset = Video.objects.select_related('category', 'author').all()
    serializer_class = VideoSerializer
    permission_classes = [IsEditorOrReadOnly]
    lookup_field = 'slug'
    
    def get_queryset(self):
        return Video.objects.select_related('category', 'author').all()
    
    def perform_update(self, serializer):
        # Only allow author or admin to update
        video = self.get_object()
        if video.author != self.request.user and not self.request.user.is_staff:
            raise PermissionDenied("You can only edit your own videos")
        serializer.save()
    
    def perform_destroy(self, instance):
        # Only allow author or admin to delete
        if instance.author != self.request.user and not self.request.user.is_staff:
            raise PermissionDenied("You can only delete your own videos")
        instance.delete()
