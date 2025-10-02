from rest_framework import generics, filters
from .models import FAQ, FAQCategory
from .serializers import (
    FAQSerializer, FAQCreateUpdateSerializer, FAQCategorySerializer
)
from posts.views import IsEditorOrReadOnly


class FAQListCreateView(generics.ListCreateAPIView):
    """
    GET /api/faqs/ - List all active FAQs
    POST /api/faqs/ - Create FAQ (Editors/Admins only)
    """
    permission_classes = [IsEditorOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['question', 'answer']
    ordering_fields = ['order', 'created_at']
    ordering = ['category', 'order']
    
    def get_queryset(self):
        queryset = FAQ.objects.select_related('category')
        
        # Only show active FAQs to public
        if not self.request.user.is_authenticated or not self.request.user.is_editor:
            queryset = queryset.filter(is_active=True)
        
        # Filter by category
        category = self.request.query_params.get('category')
        if category:
            queryset = queryset.filter(category__slug=category)
        
        # Filter by language
        language = self.request.query_params.get('language')
        if language:
            queryset = queryset.filter(language=language)
        
        return queryset
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return FAQCreateUpdateSerializer
        return FAQSerializer


class FAQDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET /api/faqs/<id>/ - Get FAQ detail
    PUT/PATCH /api/faqs/<id>/ - Update FAQ (Editors/Admins only)
    DELETE /api/faqs/<id>/ - Delete FAQ (Admins only)
    """
    queryset = FAQ.objects.select_related('category')
    permission_classes = [IsEditorOrReadOnly]
    
    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return FAQCreateUpdateSerializer
        return FAQSerializer
    
    def retrieve(self, request, *args, **kwargs):
        from rest_framework.response import Response
        instance = self.get_object()
        # Increment view count
        instance.views_count += 1
        instance.save(update_fields=['views_count'])
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class FAQCategoryListView(generics.ListCreateAPIView):
    """
    GET /api/faqs/categories/ - List categories
    POST /api/faqs/categories/ - Create category (Editors/Admins only)
    """
    queryset = FAQCategory.objects.all()
    serializer_class = FAQCategorySerializer
    permission_classes = [IsEditorOrReadOnly]
