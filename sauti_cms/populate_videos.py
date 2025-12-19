#!/usr/bin/env python
"""
Create sample video data for the Sauti CMS
"""
import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cms.settings')
django.setup()

from videos.models import Video, VideoCategory
from users.models import User

def populate_videos():
    """Create sample video categories and videos"""
    
    # Create video categories
    categories_data = [
        {
            'name': 'Child Rights Education',
            'description': 'Educational videos about child rights and protection'
        },
        {
            'name': 'Success Stories',
            'description': 'Inspiring stories from children and families we have helped'
        },
        {
            'name': 'Awareness Campaigns',
            'description': 'Public awareness videos about child protection'
        },
        {
            'name': 'Training Materials',
            'description': 'Training videos for staff and partners'
        }
    ]
    
    categories = []
    for cat_data in categories_data:
        category, created = VideoCategory.objects.update_or_create(
            name=cat_data['name'],
            defaults={'description': cat_data['description']}
        )
        categories.append(category)
        print(f"{'Created' if created else 'Updated'} category: {category.name}")
    
    # Get admin user
    try:
        admin_user = User.objects.get(username='admin')
    except User.DoesNotExist:
        print("Admin user not found. Please create an admin user first.")
        return
    
    # Create sample videos
    videos_data = [
        {
            'title': 'Understanding Child Rights in Uganda',
            'description': 'A comprehensive video explaining child rights as outlined in the Ugandan Constitution and international conventions.',
            'youtube_url': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ',
            'category': categories[0],
            'video_type': 'YOUTUBE',
            'status': 'PUBLISHED',
            'is_featured': True,
            'views_count': 1250
        },
        {
            'title': 'How to Report Child Abuse Safely',
            'description': 'Step-by-step guide on how to report child abuse while protecting the child and yourself.',
            'youtube_url': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ',
            'category': categories[0],
            'video_type': 'YOUTUBE',
            'status': 'PUBLISHED',
            'is_featured': True,
            'views_count': 980
        },
        {
            'title': 'Sarah\'s Story: From Victim to Survivor',
            'description': 'An inspiring story of a young girl who found help through Sauti and is now thriving.',
            'youtube_url': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ',
            'category': categories[1],
            'video_type': 'YOUTUBE',
            'status': 'PUBLISHED',
            'is_featured': False,
            'views_count': 750
        },
        {
            'title': 'Community Awareness: Protecting Our Children',
            'description': 'A community awareness video about the importance of protecting children from harm.',
            'youtube_url': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ',
            'category': categories[2],
            'video_type': 'YOUTUBE',
            'status': 'PUBLISHED',
            'is_featured': True,
            'views_count': 2100
        },
        {
            'title': 'Staff Training: Active Listening Skills',
            'description': 'Training video for Sauti staff on how to actively listen to children in distress.',
            'youtube_url': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ',
            'category': categories[3],
            'video_type': 'YOUTUBE',
            'status': 'DRAFT',
            'is_featured': False,
            'views_count': 0
        }
    ]
    
    for video_data in videos_data:
        video, created = Video.objects.update_or_create(
            title=video_data['title'],
            defaults={
                'description': video_data['description'],
                'youtube_url': video_data['youtube_url'],
                'category': video_data['category'],
                'video_type': video_data['video_type'],
                'status': video_data['status'],
                'is_featured': video_data['is_featured'],
                'views_count': video_data['views_count'],
                'author': admin_user
            }
        )
        print(f"{'Created' if created else 'Updated'} video: {video.title}")
    
    print(f"\n✅ Created {len(categories)} video categories and {len(videos_data)} videos")

if __name__ == '__main__':
    populate_videos()
