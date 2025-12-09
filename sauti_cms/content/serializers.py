from rest_framework import serializers
from .models import SiteContent

class SiteContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteContent
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')
