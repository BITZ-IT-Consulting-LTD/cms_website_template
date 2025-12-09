from rest_framework import viewsets, permissions
from .models import SiteContent
from .serializers import SiteContentSerializer

class SiteContentViewSet(viewsets.ModelViewSet):
    queryset = SiteContent.objects.all()
    serializer_class = SiteContentSerializer
    lookup_field = 'key'
    pagination_class = None  # Disable pagination to return all content for admin filtering

    def get_permissions(self):
        """
        Allow public read access, but require authentication for write access.
        """
        if self.action in ['list', 'retrieve']:
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]
