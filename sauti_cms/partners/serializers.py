from rest_framework import serializers
from .models import Partner


class PartnerSerializer(serializers.ModelSerializer):
    """Serializer for Partner model"""
    
    class Meta:
        model = Partner
        fields = [
            'id', 'name', 'slug', 'description', 'partner_type',
            'logo', 'website_url', 'email', 'phone', 'order',
            'is_active', 'is_featured', 'created_at', 'updated_at'
        ]
        read_only_fields = ['slug', 'created_at', 'updated_at']


class PartnerListSerializer(serializers.ModelSerializer):
    """Simplified serializer for listing partners"""
    
    class Meta:
        model = Partner
        fields = [
            'id', 'name', 'slug', 'logo', 'website_url',
            'partner_type', 'is_featured'
        ]
