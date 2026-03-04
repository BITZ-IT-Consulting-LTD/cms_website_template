from rest_framework import serializers
from .models import SocialPost, SocialMediaChannels, ContactInformation
from django.core.files.base import ContentFile
import requests
import os

class SocialPostSerializer(serializers.ModelSerializer):
    thumbnail_url = serializers.URLField(write_only=True, required=False, allow_blank=True)

    class Meta:
        model = SocialPost
        fields = '__all__'

    def create(self, validated_data):
        thumbnail_url = validated_data.pop('thumbnail_url', None)

        if thumbnail_url:
            try:
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
                }
                response = requests.get(thumbnail_url, headers=headers, timeout=10)
                response.raise_for_status()

                filename = os.path.basename(thumbnail_url.split("?")[0])
                if not filename:
                    filename = "default.jpg"

                validated_data['image'] = ContentFile(response.content, name=filename)

            except Exception as e:
                print(f"Could not download image from {thumbnail_url}. Error: {e}")

        return super().create(validated_data)





class ContactInformationSerializer(serializers.ModelSerializer):
    primary_email = serializers.SerializerMethodField()
    support_email = serializers.SerializerMethodField()
    primary_phone = serializers.SerializerMethodField()
    whatsapp_number = serializers.SerializerMethodField()
    office_address = serializers.SerializerMethodField()
    working_hours = serializers.SerializerMethodField()
    facebook_url = serializers.SerializerMethodField()
    twitter_url = serializers.SerializerMethodField()
    instagram_url = serializers.SerializerMethodField()
    linkedin_url = serializers.SerializerMethodField()
    youtube_url = serializers.SerializerMethodField()
    tiktok_url = serializers.SerializerMethodField()

    class Meta:
        model = ContactInformation
        fields = [
            'id', 'primary_email', 'support_email', 'primary_phone',
            'whatsapp_number', 'office_address', 'facebook_url',
            'twitter_url', 'instagram_url', 'linkedin_url',
            'youtube_url', 'tiktok_url', 'working_hours', 'updated_at'
        ]

    def _get_global_settings(self):
        from sitesettings.models import GlobalSettings
        return GlobalSettings.objects.first()

    def get_primary_email(self, obj):
        gs = self._get_global_settings()
        return gs.contact_email_info if gs and gs.contact_email_info else obj.primary_email

    def get_support_email(self, obj):
        gs = self._get_global_settings()
        return gs.contact_email_sautichl if gs and gs.contact_email_sautichl else obj.support_email

    def get_primary_phone(self, obj):
        gs = self._get_global_settings()
        return gs.contact_phone_main if gs and gs.contact_phone_main else obj.primary_phone

    def get_whatsapp_number(self, obj):
        gs = self._get_global_settings()
        return gs.social_whatsapp if gs and gs.social_whatsapp else obj.whatsapp_number

    def get_office_address(self, obj):
        gs = self._get_global_settings()
        return gs.office_address if gs and gs.office_address else obj.office_address

    def get_working_hours(self, obj):
        gs = self._get_global_settings()
        return gs.operating_hours_text if gs and gs.operating_hours_text else obj.working_hours

    def get_facebook_url(self, obj):
        gs = self._get_global_settings()
        return gs.social_facebook if gs and gs.social_facebook else obj.facebook_url

    def get_twitter_url(self, obj):
        gs = self._get_global_settings()
        return gs.social_twitter if gs and gs.social_twitter else obj.twitter_url

    def get_instagram_url(self, obj):
        gs = self._get_global_settings()
        return gs.social_instagram if gs and gs.social_instagram else obj.instagram_url

    def get_linkedin_url(self, obj):
        gs = self._get_global_settings()
        return gs.social_linkedin if gs and gs.social_linkedin else obj.linkedin_url

    def get_youtube_url(self, obj):
        gs = self._get_global_settings()
        return gs.social_youtube if gs and gs.social_youtube else obj.youtube_url

    def get_tiktok_url(self, obj):
        gs = self._get_global_settings()
        return gs.social_tiktok if gs and gs.social_tiktok else obj.tiktok_url


class SocialMediaChannelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMediaChannels
        fields = '__all__'
