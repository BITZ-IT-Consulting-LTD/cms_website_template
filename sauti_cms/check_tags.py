#!/usr/bin/env python
"""
Script to check existing tags and create sample tags if needed
"""
import os
import sys
import django

# Add the project directory to Python path
sys.path.append('/Users/newtonbrian/Documents/Bitz/cms_website_template/sauti_cms')

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cms.settings')
django.setup()

from posts.models import Tag, Category

def check_tags():
    print("=== Checking Tags ===")
    tags = Tag.objects.all()
    print(f"Total tags: {tags.count()}")
    for tag in tags:
        print(f"- {tag.id}: {tag.name} ({tag.slug})")
    
    print("\n=== Checking Categories ===")
    categories = Category.objects.all()
    print(f"Total categories: {categories.count()}")
    for cat in categories:
        print(f"- {cat.id}: {cat.name} ({cat.slug})")
    
    # Create sample tags if none exist
    if tags.count() == 0:
        print("\n=== Creating Sample Tags ===")
        sample_tags = [
            'helpline', 'children', 'safety', 'emergency', 'support',
            'abuse', 'protection', 'rights', 'education', 'health'
        ]
        
        for tag_name in sample_tags:
            tag, created = Tag.objects.get_or_create(
                name=tag_name,
                defaults={'slug': tag_name.lower().replace(' ', '-')}
            )
            if created:
                print(f"Created tag: {tag.name}")
            else:
                print(f"Tag already exists: {tag.name}")

if __name__ == '__main__':
    check_tags()
