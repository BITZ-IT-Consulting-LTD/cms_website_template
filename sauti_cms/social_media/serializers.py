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
    class Meta:
        model = ContactInformation
        fields = [
            'id',
            'primary_email',
            'support_email',
            'primary_phone',
            'whatsapp_number',
            'office_address',
            'facebook_url',
            'twitter_url',
            'instagram_url',
            'linkedin_url',
            'youtube_url',
            'tiktok_url',
            'working_hours',
            'updated_at'
        ]
