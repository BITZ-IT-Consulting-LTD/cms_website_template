import json
from rest_framework import serializers
from .models import Partner, PartnerPhone, PartnerEmail


class PartnerContactMixin:
    """
    Shared read logic for the extra phone/email child models, used by both
    the full PartnerSerializer and the lightweight PartnerListSerializer so
    the public partner listing also exposes every number/address, not just
    the primary Partner.phone/Partner.email.
    """

    def get_phone_numbers(self, obj):
        """Return the partner's phone numbers as a list of strings."""
        numbers = [p.phone for p in obj.phones.all() if p.phone]
        if numbers:
            return numbers
        if obj.phone:
            return [obj.phone]
        return []

    def get_email_addresses(self, obj):
        """Return the partner's email addresses as a list of strings."""
        addresses = [e.email for e in obj.emails.all() if e.email]
        if addresses:
            return addresses
        if obj.email:
            return [obj.email]
        return []

    def get_logo_url(self, obj):
        """Return relative URL for logo (frontend proxy handles it)"""
        if obj.logo:
            try:
                return obj.logo.url
            except (ValueError, AttributeError):
                return None
        return None

    def get_logo_thumbnail_url(self, obj):
        """
        Small derivative of `logo`, generated on save. Falls back to the
        full-resolution logo for rows saved before derivatives existed, or
        when Pillow couldn't decode the source.
        """
        if obj.logo_thumbnail:
            try:
                return obj.logo_thumbnail.url
            except (ValueError, AttributeError):
                pass
        return self.get_logo_url(obj)


class PartnerSerializer(PartnerContactMixin, serializers.ModelSerializer):
    """Serializer for Partner model"""
    logo_url = serializers.SerializerMethodField()
    logo_thumbnail_url = serializers.SerializerMethodField()
    phone_numbers = serializers.SerializerMethodField()
    email_addresses = serializers.SerializerMethodField()

    class Meta:
        model = Partner
        fields = [
            'id', 'name', 'slug', 'description', 'partner_type',
            'logo', 'logo_url', 'logo_thumbnail_url', 'website_url', 'email', 'email_addresses',
            'phone', 'phone_numbers', 'order',
            'is_active', 'is_featured', 'created_at', 'updated_at'
        ]
        read_only_fields = ['slug', 'created_at', 'updated_at', 'logo_url', 'logo_thumbnail_url']

    def _extract_email_addresses(self):
        """
        `email_addresses` is sent by the admin over multipart form data, so it
        can arrive as a JSON-encoded string, or as a real list (e.g. from a
        JSON client/tests). Tolerate both; return None if the field wasn't
        sent at all so existing single-`email` writes keep working untouched.
        """
        raw = self.initial_data.get('email_addresses') if hasattr(self, 'initial_data') else None
        if raw is None:
            return None
        if isinstance(raw, str):
            try:
                raw = json.loads(raw)
            except (ValueError, TypeError):
                return None
        if not isinstance(raw, list):
            return None
        return [str(address).strip() for address in raw if str(address).strip()]

    def _sync_email_addresses(self, partner, addresses):
        if addresses is None:
            return
        partner.emails.all().delete()
        for index, address in enumerate(addresses):
            PartnerEmail.objects.create(partner=partner, email=address, order=index)
        # Keep the primary Partner.email field in sync for backward compatibility.
        partner.email = addresses[0] if addresses else ''
        partner.save(update_fields=['email'])

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
        email_addresses = self._extract_email_addresses()
        partner = super().create(validated_data)
        self._sync_phone_numbers(partner, phone_numbers)
        self._sync_email_addresses(partner, email_addresses)
        return partner

    def update(self, instance, validated_data):
        phone_numbers = self._extract_phone_numbers()
        email_addresses = self._extract_email_addresses()
        partner = super().update(instance, validated_data)
        self._sync_phone_numbers(partner, phone_numbers)
        self._sync_email_addresses(partner, email_addresses)
        return partner


class PartnerListSerializer(PartnerContactMixin, serializers.ModelSerializer):
    """Simplified serializer for listing partners"""
    logo_url = serializers.SerializerMethodField()
    logo_thumbnail_url = serializers.SerializerMethodField()
    phone_numbers = serializers.SerializerMethodField()
    email_addresses = serializers.SerializerMethodField()

    class Meta:
        model = Partner
        fields = [
            'id', 'name', 'slug', 'logo', 'logo_url', 'logo_thumbnail_url', 'website_url',
            'partner_type', 'is_featured', 'phone', 'phone_numbers', 'email', 'email_addresses'
        ]
