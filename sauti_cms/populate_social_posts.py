import os
import django
import requests
from bs4 import BeautifulSoup
from django.core.files.base import ContentFile

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cms.settings')
django.setup()

from social_media.models import SocialPost

def fetch_og_data(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            
            og_image = soup.find('meta', property='og:image')
            og_description = soup.find('meta', property='og:description')
            
            image_url = og_image['content'] if og_image else None
            description = og_description['content'] if og_description else None
            
            return image_url, description
    except Exception as e:
        print(f"Error fetching {url}: {e}")
    return None, None

def populate():
    print("Populating social media posts...")
    # Clear existing data to prevent duplicates on re-run
    SocialPost.objects.all().delete()
    print("Cleared existing Social Posts.")

    posts = [
        {
            'platform': 'Facebook',
            'handle': 'Sauti 116 Helpline',
            'url': 'https://www.facebook.com/sauti116',
            'default_image': 'https://images.unsplash.com/photo-1576602976047-174e57a47881?q=80&w=800&auto=format&fit=crop'
        },
        {
            'platform': 'Twitter',
            'handle': '@sauti116',
            'url': 'https://x.com/sauti116?s=21',
            'default_image': 'https://images.unsplash.com/photo-1488521787991-ed7bbaae773c?q=80&w=800&auto=format&fit=crop'
        },
        {
            'platform': 'TikTok',
            'handle': '@sauti116helplineuganda',
            'url': 'https://www.tiktok.com/@sauti116helplineuganda?_t=ZM-91y3NHbqzDY',
            'default_image': 'https://images.unsplash.com/photo-1516627145497-ae6968895b74?q=80&w=800&auto=format&fit=crop'
        }
    ]

    for i, post_data in enumerate(posts):
        print(f"Processing {post_data['platform']}...")
        
        # Try to fetch real data
        image_url, description = fetch_og_data(post_data['url'])
        
        post, created = SocialPost.objects.update_or_create(
            platform=post_data['platform'],
            defaults={
                'handle': post_data['handle'],
                'post_url': post_data['url'],
                'content': description or f"Follow us on {post_data['platform']}",
                'order': i,
                'is_active': True,
                'posted_at': django.utils.timezone.now()
            }
        )
        
        # If we got an image URL, try to save it (only if created or if you want to refresh)
        if image_url:
            try:
                img_resp = requests.get(image_url, timeout=10)
                if img_resp.status_code == 200:
                    file_name = f"{post_data['platform'].lower()}_og.jpg"
                    post.image.save(file_name, ContentFile(img_resp.content), save=True)
                    print(f"  - Fetched OG image for {post_data['platform']}")
            except Exception as e:
                print(f"  - Failed to download OG image: {e}")
        
        print(f"{'Created' if created else 'Updated'} post for {post_data['platform']}")

if __name__ == '__main__':
    populate()
