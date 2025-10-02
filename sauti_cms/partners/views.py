from rest_framework import generics
from .models import Partner
from .serializers import PartnerSerializer, PartnerListSerializer
from posts.views import IsEditorOrReadOnly


class PartnerListCreateView(generics.ListCreateAPIView):
    """
    GET /api/partners/ - List all active partners
    POST /api/partners/ - Create partner (Editors/Admins only)
    """
    permission_classes = [IsEditorOrReadOnly]
    
    def get_queryset(self):
        queryset = Partner.objects.filter(is_active=True)
        
        # Filter by featured
        is_featured = self.request.query_params.get('featured')
        if is_featured:
            queryset = queryset.filter(is_featured=True)
        
        return queryset
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PartnerListSerializer
        return PartnerSerializer


class PartnerDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET /api/partners/<slug>/ - Get partner detail
    PUT/PATCH /api/partners/<slug>/ - Update partner (Editors/Admins only)
    DELETE /api/partners/<slug>/ - Delete partner (Admins only)
    """
    queryset = Partner.objects.all()
    lookup_field = 'slug'
    serializer_class = PartnerSerializer
    permission_classes = [IsEditorOrReadOnly]
