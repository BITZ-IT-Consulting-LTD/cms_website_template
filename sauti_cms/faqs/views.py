from rest_framework import generics, filters, status
from rest_framework.response import Response
from .models import FAQ, FAQCategory
from .serializers import (
    FAQSerializer, FAQCreateUpdateSerializer, FAQCategorySerializer
)
from posts.views import IsEditorOrReadOnly


class FAQCategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET /api/faqs/categories/<id>/ - Get category
    PUT/PATCH /api/faqs/categories/<id>/ - Update category (Editors/Admins only)
    DELETE /api/faqs/categories/<id>/ - Delete category (Editors/Admins only)
    """
    queryset = FAQCategory.objects.all()
    serializer_class = FAQCategorySerializer
    permission_classes = [IsEditorOrReadOnly]


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
        
        # Only show active and published FAQs to public
        if not self.request.user.is_authenticated or not self.request.user.is_editor:
            queryset = queryset.filter(is_active=True, status=FAQ.Status.PUBLISHED)
        else:
            # Editors can filter by status
            status = self.request.query_params.get('status')
            if status:
                queryset = queryset.filter(status=status)
        
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

    def perform_create(self, serializer):
        serializer.save(
            created_by=self.request.user,
            last_updated_by=self.request.user
        )

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        instance = serializer.instance
        output = FAQSerializer(instance, context=self.get_serializer_context()).data
        headers = self.get_success_headers(serializer.data)
        return Response(output, status=status.HTTP_201_CREATED, headers=headers)


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

    def perform_update(self, serializer):
        serializer.save(last_updated_by=self.request.user)


class FAQCategoryListView(generics.ListCreateAPIView):
    """
    GET /api/faqs/categories/ - List categories
    POST /api/faqs/categories/ - Create category (Editors/Admins only)
    """
    queryset = FAQCategory.objects.all()
    serializer_class = FAQCategorySerializer
    permission_classes = [IsEditorOrReadOnly]
