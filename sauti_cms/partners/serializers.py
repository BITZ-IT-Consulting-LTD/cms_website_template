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
        """Return relative URL for logo (frontend proxy handles it)"""
        if obj.logo:
            try:
                return obj.logo.url
            except (ValueError, AttributeError):
                return None
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
        """Return relative URL for logo (frontend proxy handles it)"""
        if obj.logo:
            try:
                return obj.logo.url
            except (ValueError, AttributeError):
                return None
        return None
