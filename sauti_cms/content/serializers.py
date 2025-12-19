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
    class Meta:
        model = TeamMember
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')
