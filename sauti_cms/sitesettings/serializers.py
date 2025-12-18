from rest_framework import serializers
from .models import SiteSetting, GlobalSettings

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
