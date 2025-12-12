from rest_framework import viewsets, filters, status
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from .models import SocialPost, SocialMediaChannels, ContactInformation
from .serializers import SocialPostSerializer, SocialMediaChannelsSerializer, ContactInformationSerializer
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

class SocialPostViewSet(viewsets.ModelViewSet):
    queryset = SocialPost.objects.filter(is_active=True)
    serializer_class = SocialPostSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['platform', 'handle', 'content']
    ordering_fields = ['posted_at', 'order']
    ordering = ['-posted_at']  # Default to most recent posts first

    def get_queryset(self):
        queryset = super().get_queryset()
        platform = self.request.query_params.get('platform', None)
        if platform:
            queryset = queryset.filter(platform__iexact=platform)
        return queryset.order_by('-posted_at')  # Ensure latest posts first

    @action(detail=False, methods=['post'], url_path='fetch-metadata')
    def fetch_metadata(self, request):
        """
        Fetch OpenGraph metadata from a social media post URL
        """
        url = request.data.get('url')

        if not url:
            return Response(
                {'error': 'URL is required'},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            # Set headers to mimic a browser
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }

            # Fetch the URL
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()

            # Parse HTML
            soup = BeautifulSoup(response.content, 'html.parser')

            # Extract OpenGraph metadata
            metadata = {
                'title': None,
                'description': None,
                'image': None,
                'video': None,
            }

            # Try OpenGraph tags first
            og_title = soup.find('meta', property='og:title')
            og_description = soup.find('meta', property='og:description')
            og_image = soup.find('meta', property='og:image')
            og_video = soup.find('meta', property='og:video')

            if og_title:
                metadata['title'] = og_title.get('content')
            if og_description:
                metadata['description'] = og_description.get('content')
            if og_image:
                metadata['image'] = og_image.get('content')
            if og_video:
                metadata['video'] = og_video.get('content')

            # Fallback to Twitter Card tags
            if not metadata['title']:
                twitter_title = soup.find('meta', attrs={'name': 'twitter:title'})
                if twitter_title:
                    metadata['title'] = twitter_title.get('content')

            if not metadata['description']:
                twitter_desc = soup.find('meta', attrs={'name': 'twitter:description'})
                if twitter_desc:
                    metadata['description'] = twitter_desc.get('content')

            if not metadata['image']:
                twitter_image = soup.find('meta', attrs={'name': 'twitter:image'})
                if twitter_image:
                    metadata['image'] = twitter_image.get('content')

            # Fallback to basic HTML tags
            if not metadata['title']:
                title_tag = soup.find('title')
                if title_tag:
                    metadata['title'] = title_tag.string

            if not metadata['description']:
                desc_tag = soup.find('meta', attrs={'name': 'description'})
                if desc_tag:
                    metadata['description'] = desc_tag.get('content')

            # Detect platform from URL
            domain = urlparse(url).netloc.lower()
            platform = None
            if 'tiktok.com' in domain:
                platform = 'TikTok'
            elif 'facebook.com' in domain or 'fb.com' in domain:
                platform = 'Facebook'
            elif 'twitter.com' in domain or 'x.com' in domain:
                platform = 'Twitter'
            elif 'instagram.com' in domain:
                platform = 'Instagram'
            elif 'linkedin.com' in domain:
                platform = 'LinkedIn'
            elif 'youtube.com' in domain or 'youtu.be' in domain:
                platform = 'YouTube'

            metadata['platform'] = platform

            return Response(metadata, status=status.HTTP_200_OK)

        except requests.exceptions.RequestException as e:
            return Response(
                {'error': f'Failed to fetch URL: {str(e)}'},
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            return Response(
                {'error': f'Error processing URL: {str(e)}'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


@api_view(['GET', 'PUT'])
def social_channels(request):
    """
    Get or update the 4 social media channel URLs
    """
    channels = SocialMediaChannels.get_channels()

    if request.method == 'GET':
        serializer = SocialMediaChannelsSerializer(channels)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SocialMediaChannelsSerializer(channels, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT'])
def contact_information(request):
    """
    Get or update contact information displayed across the frontend
    """
    contact_info = ContactInformation.get_contact_info()

    if request.method == 'GET':
        serializer = ContactInformationSerializer(contact_info)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ContactInformationSerializer(contact_info, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
