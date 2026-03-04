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


class SocialMediaChannelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMediaChannels
        fields = ['id', 'channel_1_url', 'channel_2_url', 'channel_3_url', 'channel_4_url', 'updated_at']

    def create(self, validated_data):
        # Handle thumbnail_url if provided
        thumbnail_url = validated_data.pop('thumbnail_url', None)

        if thumbnail_url and not validated_data.get('image'):
            try:
                # Download the image from the URL
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                }
                response = requests.get(thumbnail_url, headers=headers, timeout=10)
                response.raise_for_status()

                # Get filename from URL or generate one
                filename = os.path.basename(thumbnail_url.split('?')[0])
                if not filename or '.' not in filename:
                    filename = f'social_post_{validated_data.get("platform", "image")}.jpg'

                # Save the image to the model
                validated_data['image'] = ContentFile(response.content, name=filename)
            except Exception as e:
                # If downloading fails, continue without image
                print(f'Failed to download thumbnail: {str(e)}')

        return super().create(validated_data)

    def update(self, instance, validated_data):
        # Handle thumbnail_url if provided
        thumbnail_url = validated_data.pop('thumbnail_url', None)

        if thumbnail_url and not validated_data.get('image'):
            try:
                # Download the image from the URL
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                }
                response = requests.get(thumbnail_url, headers=headers, timeout=10)
                response.raise_for_status()

                # Get filename from URL or generate one
                filename = os.path.basename(thumbnail_url.split('?')[0])
                if not filename or '.' not in filename:
                    filename = f'social_post_{validated_data.get("platform", instance.platform)}.jpg'

                # Save the image to the model
                validated_data['image'] = ContentFile(response.content, name=filename)
            except Exception as e:
                # If downloading fails, continue without image
                print(f'Failed to download thumbnail: {str(e)}')

        return super().update(instance, validated_data)


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
