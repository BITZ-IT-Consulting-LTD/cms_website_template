from rest_framework import serializers
from .models import SiteSetting, GlobalSettings, OrganizationProfile

# DEPRECATED: This serializer is deprecated and will be removed in a future version.
class SiteSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteSetting
        fields = '__all__'
        read_only_fields = ('last_updated',)


class GlobalSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = GlobalSettings
        fields = '__all__'

class OrganizationProfileSerializer(serializers.ModelSerializer):
    logo_url = serializers.SerializerMethodField()
    favicon_url = serializers.SerializerMethodField()
    team_photo_url = serializers.SerializerMethodField()

    class Meta:
        model = OrganizationProfile
        fields = '__all__'
        read_only_fields = ('last_updated', 'logo_url', 'favicon_url', 'team_photo_url')

    def _build_absolute_url(self, image_field):
        """Helper to build absolute URL for image fields"""
        if not image_field:
            return None

        try:
            image_url = image_field.url
        except (ValueError, AttributeError):
            return None

        # Check if already absolute
        if image_url.startswith('http://') or image_url.startswith('https://'):
            return image_url

        request = self.context.get('request')
        if request:
            host = request.META.get('HTTP_X_FORWARDED_HOST', request.get_host())
            scheme = request.META.get('HTTP_X_FORWARDED_PROTO', request.scheme)
            if host == 'backend':
                host = 'localhost:8080'
                scheme = 'http'
            return f"{scheme}://{host}{image_url}"

        return f"http://localhost:8080{image_url}" if image_url else None

    def get_logo_url(self, obj):
        """Return full URL for organization logo"""
        return self._build_absolute_url(obj.logo)

    def get_favicon_url(self, obj):
        """Return full URL for organization favicon"""
        return self._build_absolute_url(obj.favicon)

    def get_team_photo_url(self, obj):
        """Return full URL for organization team photo"""
        return self._build_absolute_url(obj.team_photo)
