from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import SiteSetting, GlobalSettings, OrganizationProfile
from .serializers import SiteSettingSerializer, GlobalSettingsSerializer, OrganizationProfileSerializer

# DEPRECATED: This viewset is deprecated and will be removed in a future version.
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


class GlobalSettingsView(APIView):
    """
    API endpoint to manage global site settings.
    Provides GET and PUT methods for the singleton GlobalSettings object.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        try:
            settings, created = GlobalSettings.objects.get_or_create()
            serializer = GlobalSettingsSerializer(settings)
            return Response(serializer.data)
        except Exception as e:
            import logging
            logger = logging.getLogger(__name__)
            logger.error(f"Error in GlobalSettingsView.get: {e}", exc_info=True)
            return Response(
                {"detail": "An error occurred while fetching settings."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def put(self, request, *args, **kwargs):
        settings, created = GlobalSettings.objects.get_or_create()
        serializer = GlobalSettingsSerializer(settings, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrganizationProfileView(APIView):
    """
    API endpoint to manage organization profile.
    Provides GET and PUT methods for the singleton OrganizationProfile object.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        profile, created = OrganizationProfile.objects.get_or_create()
        serializer = OrganizationProfileSerializer(profile, context={'request': request})
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        profile, created = OrganizationProfile.objects.get_or_create()
        serializer = OrganizationProfileSerializer(profile, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
