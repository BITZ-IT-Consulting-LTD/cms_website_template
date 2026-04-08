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
    # About hero image URLs
    about_hero_image_1_url = serializers.SerializerMethodField()
    about_hero_image_2_url = serializers.SerializerMethodField()
    about_hero_image_3_url = serializers.SerializerMethodField()
    about_hero_image_4_url = serializers.SerializerMethodField()
    about_hero_image_5_url = serializers.SerializerMethodField()
    about_hero_image_6_url = serializers.SerializerMethodField()
    about_hero_image_7_url = serializers.SerializerMethodField()
    about_hero_image_8_url = serializers.SerializerMethodField()

    class Meta:
        model = OrganizationProfile
        fields = '__all__'
        read_only_fields = ('last_updated', 'logo_url', 'favicon_url', 'team_photo_url',
                           'about_hero_image_1_url', 'about_hero_image_2_url', 'about_hero_image_3_url',
                           'about_hero_image_4_url', 'about_hero_image_5_url', 'about_hero_image_6_url',
                           'about_hero_image_7_url', 'about_hero_image_8_url')

    def _build_absolute_url(self, image_field):
        """Return relative URL for image fields (frontend proxy handles it)"""
        if not image_field:
            return None

        try:
            image_url = image_field.url
        except (ValueError, AttributeError):
            return None

        # Check if already absolute
        if image_url.startswith('http://') or image_url.startswith('https://'):
            return image_url

        # Return relative URL - frontend proxy will handle /sauti/media/
        return image_url

    def get_logo_url(self, obj):
        """Return full URL for organization logo"""
        return self._build_absolute_url(obj.logo)

    def get_favicon_url(self, obj):
        """Return full URL for organization favicon"""
        return self._build_absolute_url(obj.favicon)

    def get_team_photo_url(self, obj):
        """Return full URL for organization team photo"""
        return self._build_absolute_url(obj.team_photo)

    def get_about_hero_image_1_url(self, obj):
        """Return full URL for About hero image 1 (left column, top)"""
        return self._build_absolute_url(obj.about_hero_image_1)

    def get_about_hero_image_2_url(self, obj):
        """Return full URL for About hero image 2 (left column, middle)"""
        return self._build_absolute_url(obj.about_hero_image_2)

    def get_about_hero_image_3_url(self, obj):
        """Return full URL for About hero image 3 (left column, bottom)"""
        return self._build_absolute_url(obj.about_hero_image_3)

    def get_about_hero_image_4_url(self, obj):
        """Return full URL for About hero image 4 (center, top-right)"""
        return self._build_absolute_url(obj.about_hero_image_4)

    def get_about_hero_image_5_url(self, obj):
        """Return full URL for About hero image 5 (center, bottom-left)"""
        return self._build_absolute_url(obj.about_hero_image_5)

    def get_about_hero_image_6_url(self, obj):
        """Return full URL for About hero image 6 (center, bottom-right)"""
        return self._build_absolute_url(obj.about_hero_image_6)

    def get_about_hero_image_7_url(self, obj):
        """Return full URL for About hero image 7 (right column, top)"""
        return self._build_absolute_url(obj.about_hero_image_7)

    def get_about_hero_image_8_url(self, obj):
        """Return full URL for About hero image 8 (right column, middle)"""
        return self._build_absolute_url(obj.about_hero_image_8)
