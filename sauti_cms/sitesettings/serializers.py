from rest_framework import serializers
from .models import SiteSetting

class SiteSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteSetting
        fields = '__all__'
        read_only_fields = ('last_updated',)
