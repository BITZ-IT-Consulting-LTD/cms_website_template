from rest_framework import serializers
from sitesettings.models import GlobalSettings


class GetHelpServiceSerializer(serializers.Serializer):
    """
    Serializer for Get Help services from GlobalSettings.
    Maps GlobalSettings fields to the format expected by the frontend.
    """
    key = serializers.CharField()
    title = serializers.CharField()
    intro_text = serializers.CharField()
    icon = serializers.CharField()
    scope_items = serializers.ListField(child=serializers.CharField(), required=False)
    steps = serializers.ListField(required=False)


class GetHelpServicesListSerializer(serializers.Serializer):
    """
    Serializer for listing all Get Help services.
    """
    services = GetHelpServiceSerializer(many=True)
    section_title = serializers.CharField()
    section_description = serializers.CharField()
