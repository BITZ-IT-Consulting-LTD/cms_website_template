from rest_framework import serializers
from .models import SiteContent, CoreValue

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
