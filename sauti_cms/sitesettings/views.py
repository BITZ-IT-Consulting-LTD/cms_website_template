from rest_framework import viewsets, permissions
from .models import SiteSetting
from .serializers import SiteSettingSerializer

class SiteSettingViewSet(viewsets.ModelViewSet):
    queryset = SiteSetting.objects.all()
    serializer_class = SiteSettingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] # Allow read for all, write for authenticated
    lookup_field = 'key' # Allow lookup by key

    def get_queryset(self):
        queryset = super().get_queryset()
        page = self.request.query_params.get('page', None)
        if page is not None:
            queryset = queryset.filter(page=page)
        return queryset

    def get_permissions(self):
        """
        Allow public read access, but require authentication for write access.
        Explicitly allow OPTIONS for preflight requests.
        """
        if self.action in ['list', 'retrieve', 'options']:
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]
