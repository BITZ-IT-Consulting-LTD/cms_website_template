from rest_framework import generics, permissions, filters
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from .models import Post, Category, Tag
from .serializers import (
    PostListSerializer, PostDetailSerializer, PostCreateUpdateSerializer,
    CategorySerializer, TagSerializer
)


class IsEditorOrReadOnly(permissions.BasePermission):
    """Custom permission: Only editors/admins/authors can create/edit, others read-only"""

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        # Allow authenticated users with author role or higher (AUTHOR, EDITOR, ADMIN)
        return request.user.is_authenticated and request.user.is_author


class IsAdminOrReadOnly(permissions.BasePermission):
    """Custom permission: Only admins can delete"""
    
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.method == 'DELETE':
            return request.user.is_authenticated and request.user.is_admin
        return request.user.is_authenticated


class PostListCreateView(generics.ListCreateAPIView):
    """
    GET /api/posts/ - List all published posts (or all for authenticated editors)
    POST /api/posts/ - Create new post (Editors/Admins only)
    """
    permission_classes = [IsEditorOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'content', 'excerpt']
    ordering_fields = ['published_at', 'created_at', 'views_count']
    ordering = ['-published_at']
    
    def get_queryset(self):
        queryset = Post.objects.select_related('author', 'category').prefetch_related('tags')
        
        # Public users see only published posts
        if not self.request.user.is_authenticated or not self.request.user.is_editor:
            queryset = queryset.filter(status=Post.Status.PUBLISHED)
        
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
        
        # Filter by status
        status = self.request.query_params.get('status')
        if status:
            queryset = queryset.filter(status=status)
        
        return queryset
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return PostCreateUpdateSerializer
        return PostListSerializer
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET /api/posts/<slug>/ - Get post detail
    PUT/PATCH /api/posts/<slug>/ - Update post (Editors/Admins only)
    DELETE /api/posts/<slug>/ - Delete post (Admins only)
    """
    lookup_field = 'slug'
    permission_classes = [IsEditorOrReadOnly]
    
    def get_queryset(self):
        queryset = Post.objects.select_related('author', 'category').prefetch_related('tags')
        
        # Public users see only published posts
        if not self.request.user.is_authenticated or not self.request.user.is_editor:
            queryset = queryset.filter(status=Post.Status.PUBLISHED)
        
        return queryset
    
    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return PostCreateUpdateSerializer
        return PostDetailSerializer
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        # Increment view count
        instance.views_count += 1
        instance.save(update_fields=['views_count'])
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class CategoryListView(generics.ListCreateAPIView):
    """
    GET /api/posts/categories/ - List categories
    POST /api/posts/categories/ - Create category (Editors/Admins only)
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsEditorOrReadOnly]


class TagListView(generics.ListCreateAPIView):
    """
    GET /api/posts/tags/ - List tags
    POST /api/posts/tags/ - Create tag (Editors/Admins only)
    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsEditorOrReadOnly]
