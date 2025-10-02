from rest_framework import generics, filters
from .models import Resource, ResourceCategory
from .serializers import (
    ResourceListSerializer, ResourceDetailSerializer,
    ResourceCreateUpdateSerializer, ResourceCategorySerializer
)
from posts.views import IsEditorOrReadOnly


class ResourceListCreateView(generics.ListCreateAPIView):
    """
    GET /api/resources/ - List all resources
    POST /api/resources/ - Create resource (Editors/Admins only)
    """
    queryset = Resource.objects.select_related('category')
    permission_classes = [IsEditorOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'description']
    ordering_fields = ['published_at', 'download_count']
    ordering = ['-published_at']
    
    def get_queryset(self):
        queryset = super().get_queryset()
        
        # Filter by category
        category = self.request.query_params.get('category')
        if category:
            queryset = queryset.filter(category__slug=category)
        
        # Filter by language
        language = self.request.query_params.get('language')
        if language:
            queryset = queryset.filter(language=language)
        
        # Filter by featured
        is_featured = self.request.query_params.get('featured')
        if is_featured:
            queryset = queryset.filter(is_featured=True)
        
        return queryset
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ResourceCreateUpdateSerializer
        return ResourceListSerializer


class ResourceDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET /api/resources/<slug>/ - Get resource detail
    PUT/PATCH /api/resources/<slug>/ - Update resource (Editors/Admins only)
    DELETE /api/resources/<slug>/ - Delete resource (Admins only)
    """
    queryset = Resource.objects.select_related('category')
    lookup_field = 'slug'
    permission_classes = [IsEditorOrReadOnly]
    
    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return ResourceCreateUpdateSerializer
        return ResourceDetailSerializer
    
    def retrieve(self, request, *args, **kwargs):
        from rest_framework.response import Response
        instance = self.get_object()
        # Increment download count
        instance.download_count += 1
        instance.save(update_fields=['download_count'])
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class ResourceCategoryListView(generics.ListCreateAPIView):
    """
    GET /api/resources/categories/ - List categories
    POST /api/resources/categories/ - Create category (Editors/Admins only)
    """
    queryset = ResourceCategory.objects.all()
    serializer_class = ResourceCategorySerializer
    permission_classes = [IsEditorOrReadOnly]
