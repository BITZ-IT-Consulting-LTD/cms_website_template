import json
from rest_framework import serializers
from .models import SiteContent, CoreValue, Contact, ContactValue, ProtectionApproach, TeamMember, WhoWeAreImage, OperationsImage

class SiteContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteContent
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')


class CoreValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoreValue
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')


class ContactSerializer(serializers.ModelSerializer):
    extra_values = serializers.SerializerMethodField()

    class Meta:
        model = Contact
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')

    def get_extra_values(self, obj):
        """Return this contact's additional values as a list of strings."""
        return [v.value for v in obj.extra_values.all() if v.value]

    def _extract_extra_values(self):
        """
        `extra_values` is sent by the admin as plain JSON, but tolerate a
        JSON-encoded string too for safety. Returns None if the field wasn't
        sent at all, so existing single-`value` writes keep working untouched.
        """
        raw = self.initial_data.get('extra_values') if hasattr(self, 'initial_data') else None
        if raw is None:
            return None
        if isinstance(raw, str):
            try:
                raw = json.loads(raw)
            except (ValueError, TypeError):
                return None
        if not isinstance(raw, list):
            return None
        return [str(value).strip() for value in raw if str(value).strip()]

    def _sync_extra_values(self, contact, values):
        if values is None:
            return
        contact.extra_values.all().delete()
        for index, value in enumerate(values):
            ContactValue.objects.create(contact=contact, value=value, order=index)

    def create(self, validated_data):
        extra_values = self._extract_extra_values()
        contact = super().create(validated_data)
        self._sync_extra_values(contact, extra_values)
        return contact

    def update(self, instance, validated_data):
        extra_values = self._extract_extra_values()
        contact = super().update(instance, validated_data)
        self._sync_extra_values(contact, extra_values)
        return contact


class ProtectionApproachSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProtectionApproach
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')


class TeamMemberSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False, allow_null=True)
    image_url = serializers.SerializerMethodField()
    image_thumbnail_url = serializers.SerializerMethodField()

    class Meta:
        model = TeamMember
        fields = '__all__'
        # `image_thumbnail` is a raw model field pulled in by fields = '__all__';
        # it is populated server-side on save (see TeamMember.save()) and must
        # never be writable directly, so it's forced read-only alongside the
        # computed _url fields.
        read_only_fields = ('created_at', 'updated_at', 'image_url', 'image_thumbnail', 'image_thumbnail_url')

    def get_image_url(self, obj):
        """Return relative URL for image field (frontend proxy handles it)"""
        if obj.image:
            try:
                return obj.image.url
            except (ValueError, AttributeError):
                return None
        return None

    def get_image_thumbnail_url(self, obj):
        """
        Small derivative of `image`, generated on save. Falls back to the
        full-resolution image for rows saved before derivatives existed, or
        when Pillow couldn't decode the source.
        """
        if obj.image_thumbnail:
            try:
                return obj.image_thumbnail.url
            except (ValueError, AttributeError):
                pass
        return self.get_image_url(obj)


class WhoWeAreImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=True)
    image_url = serializers.SerializerMethodField()
    position_display = serializers.SerializerMethodField()

    class Meta:
        model = WhoWeAreImage
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at', 'image_url', 'position_display')

    def get_position_display(self, obj):
        return obj.get_position_display()

    def get_image_url(self, obj):
        """Return relative URL for image field (frontend proxy handles it)"""
        if obj.image:
            try:
                return obj.image.url
            except (ValueError, AttributeError):
                return None
        return None


class OperationsImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=True)
    image_url = serializers.SerializerMethodField()
    position_display = serializers.SerializerMethodField()

    class Meta:
        model = OperationsImage
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at', 'image_url', 'position_display')

    def get_position_display(self, obj):
        return obj.get_position_display()

    def get_image_url(self, obj):
        """Return relative URL for image field (frontend proxy handles it)"""
        if obj.image:
            try:
                return obj.image.url
            except (ValueError, AttributeError):
                return None
        return None
