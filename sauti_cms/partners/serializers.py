import json
from rest_framework import serializers
from .models import Partner, PartnerPhone


class PartnerSerializer(serializers.ModelSerializer):
    """Serializer for Partner model"""
    logo_url = serializers.SerializerMethodField()
    phone_numbers = serializers.SerializerMethodField()

    class Meta:
        model = Partner
        fields = [
            'id', 'name', 'slug', 'description', 'partner_type',
            'logo', 'logo_url', 'website_url', 'email', 'phone', 'phone_numbers', 'order',
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

    def get_phone_numbers(self, obj):
        """Return the partner's phone numbers as a list of strings."""
        numbers = [p.phone for p in obj.phones.all() if p.phone]
        if numbers:
            return numbers
        if obj.phone:
            return [obj.phone]
        return []

    def _extract_phone_numbers(self):
        """
        `phone_numbers` is sent by the admin over multipart form data, so it can
        arrive as a JSON-encoded string, or as a real list (e.g. from a JSON
        client/tests). Tolerate both; return None if the field wasn't sent at
        all so existing single-`phone` writes keep working untouched.
        """
        raw = self.initial_data.get('phone_numbers') if hasattr(self, 'initial_data') else None
        if raw is None:
            return None
        if isinstance(raw, str):
            try:
                raw = json.loads(raw)
            except (ValueError, TypeError):
                return None
        if not isinstance(raw, list):
            return None
        return [str(number).strip() for number in raw if str(number).strip()]

    def _sync_phone_numbers(self, partner, numbers):
        if numbers is None:
            return
        partner.phones.all().delete()
        for index, number in enumerate(numbers):
            PartnerPhone.objects.create(partner=partner, phone=number, order=index)
        # Keep the primary Partner.phone field in sync for backward compatibility.
        partner.phone = numbers[0] if numbers else ''
        partner.save(update_fields=['phone'])

    def create(self, validated_data):
        phone_numbers = self._extract_phone_numbers()
        partner = super().create(validated_data)
        self._sync_phone_numbers(partner, phone_numbers)
        return partner

    def update(self, instance, validated_data):
        phone_numbers = self._extract_phone_numbers()
        partner = super().update(instance, validated_data)
        self._sync_phone_numbers(partner, phone_numbers)
        return partner


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
