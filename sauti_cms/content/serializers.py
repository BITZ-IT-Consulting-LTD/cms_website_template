from rest_framework import serializers
from .models import SiteContent, CoreValue, Contact, ProtectionApproach, TeamMember, WhoWeAreImage, OperationsImage

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
    class Meta:
        model = Contact
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')


class ProtectionApproachSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProtectionApproach
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')


class TeamMemberSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False, allow_null=True)
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = TeamMember
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at', 'image_url')

    def get_image_url(self, obj):
        """Return relative URL for image field (frontend proxy handles it)"""
        if obj.image:
            try:
                return obj.image.url
            except (ValueError, AttributeError):
                return None
        return None


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
