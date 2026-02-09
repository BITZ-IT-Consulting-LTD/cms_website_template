from rest_framework import serializers
from .models import Partner


class PartnerSerializer(serializers.ModelSerializer):
    """Serializer for Partner model"""
    logo_url = serializers.SerializerMethodField()

    class Meta:
        model = Partner
        fields = [
            'id', 'name', 'slug', 'description', 'partner_type',
            'logo', 'logo_url', 'website_url', 'email', 'phone', 'order',
            'is_active', 'is_featured', 'created_at', 'updated_at'
        ]
        read_only_fields = ['slug', 'created_at', 'updated_at', 'logo_url']

    def get_logo_url(self, obj):
        """Return full URL for logo, Docker-proxy-aware"""
        if obj.logo:
            try:
                logo_url = obj.logo.url
            except (ValueError, AttributeError):
                return None

            request = self.context.get('request')
            if request:
                host = request.META.get('HTTP_X_FORWARDED_HOST', request.get_host())
                scheme = request.META.get('HTTP_X_FORWARDED_PROTO', request.scheme)
                if host == 'backend':
                    host = 'localhost:8080'
                    scheme = 'http'
                return f"{scheme}://{host}{logo_url}"
            return f"http://localhost:8080{logo_url}" if logo_url else None
        return None


class PartnerListSerializer(serializers.ModelSerializer):
    """Simplified serializer for listing partners"""
    logo_url = serializers.SerializerMethodField()

    class Meta:
        model = Partner
        fields = [
            'id', 'name', 'slug', 'logo', 'logo_url', 'website_url',
            'partner_type', 'is_featured'
        ]

    def get_logo_url(self, obj):
        """Return full URL for logo, Docker-proxy-aware"""
        if obj.logo:
            try:
                logo_url = obj.logo.url
            except (ValueError, AttributeError):
                return None

            request = self.context.get('request')
            if request:
                host = request.META.get('HTTP_X_FORWARDED_HOST', request.get_host())
                scheme = request.META.get('HTTP_X_FORWARDED_PROTO', request.scheme)
                if host == 'backend':
                    host = 'localhost:8080'
                    scheme = 'http'
                return f"{scheme}://{host}{logo_url}"
            return f"http://localhost:8080{logo_url}" if logo_url else None
        return None
