from rest_framework import serializers
from .models import SiteContent, CoreValue, Contact, ProtectionApproach, TeamMember

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
        """Return full URL for image field, Docker-proxy-aware"""
        if obj.image:
            try:
                image_url = obj.image.url
            except (ValueError, AttributeError):
                return None

            request = self.context.get('request')
            if request:
                host = request.META.get('HTTP_X_FORWARDED_HOST', request.get_host())
                scheme = request.META.get('HTTP_X_FORWARDED_PROTO', request.scheme)
                if host == 'backend':
                    host = 'localhost:8080'
                    scheme = 'http'
                return f"{scheme}://{host}{image_url}"
            return f"http://localhost:8080{image_url}" if image_url else None
        return None
