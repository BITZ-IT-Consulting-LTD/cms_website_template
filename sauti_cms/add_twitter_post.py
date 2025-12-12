#!/usr/bin/env python
"""
Script to add a Twitter/X post to the social media database
"""
import os
import django
import sys

# Setup Django
sys.path.insert(0, os.path.dirname(__file__))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cms.settings')
django.setup()

from social_media.models import SocialPost
from social_media.serializers import SocialPostSerializer
import requests
from bs4 import BeautifulSoup
from datetime import datetime

def fetch_twitter_metadata(url):
    """Fetch metadata from Twitter/X URL"""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')

        metadata = {
            'title': None,
            'description': None,
            'image': None,
        }

        # Try OpenGraph tags
        og_title = soup.find('meta', property='og:title')
        og_description = soup.find('meta', property='og:description')
        og_image = soup.find('meta', property='og:image')

        if og_title:
            metadata['title'] = og_title.get('content')
        if og_description:
            metadata['description'] = og_description.get('content')
        if og_image:
            metadata['image'] = og_image.get('content')

        # Fallback to Twitter Card tags
        if not metadata['image']:
            twitter_image = soup.find('meta', attrs={'name': 'twitter:image'})
            if twitter_image:
                metadata['image'] = twitter_image.get('content')

        return metadata
    except Exception as e:
        print(f"Error fetching metadata: {e}")
        return None

def add_twitter_post(url, handle='@sauti116'):
    """Add a Twitter post to the database"""
    # Check if post already exists
    existing = SocialPost.objects.filter(post_url=url).first()
    if existing:
        print(f"Post already exists: {existing.id}")
        return existing

    # Fetch metadata
    print(f"Fetching metadata from: {url}")
    metadata = fetch_twitter_metadata(url)

    # Create post
    post_data = {
        'platform': 'Twitter',
        'handle': handle,
        'content': metadata.get('description', '') if metadata else '',
        'post_url': url,
        'thumbnail_url': metadata.get('image', '') if metadata else None,
        'posted_at': datetime.now().isoformat(),
        'is_active': True,
        'order': 0,
        'likes_count': '0',
        'comments_count': '0',
        'shares_count': '0',
    }

    print(f"Creating post with data: {post_data}")

    serializer = SocialPostSerializer(data=post_data)
    if serializer.is_valid():
        post = serializer.save()
        print(f"✓ Created Twitter post: {post.id}")
        print(f"  Content: {post.content}")
        print(f"  Image: {post.image}")
        return post
    else:
        print(f"✗ Error: {serializer.errors}")
        return None

if __name__ == '__main__':
    # Add the specific Twitter post
    twitter_url = 'https://x.com/sauti116/status/1997995788517945838/photo/1'
    post = add_twitter_post(twitter_url)

    # Show all Twitter posts
    print("\nAll Twitter posts:")
    twitter_posts = SocialPost.objects.filter(platform='Twitter', is_active=True).order_by('-posted_at')
    for p in twitter_posts:
        print(f"  {p.id}: {p.handle} - {p.post_url[:50]}...")
