#!/usr/bin/env python
"""
Combined script to populate all initial data for the Sauti CMS.
This script calls the functions from the individual population scripts.
"""
import os
import django
import sys
from pathlib import Path

# Add the project directory to Python path
BASE_DIR = Path(__file__).resolve().parent
sys.path.append(str(BASE_DIR))

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cms.settings')
django.setup()

# Import functions from the individual scripts
from create_admin import create_admin
from create_infographics_category import create_category as create_infographics_category
from create_initial_content import create_initial_content
from create_sample_partners import create_sample_partners
from create_sample_posts import create_sample_posts
from create_sample_videos import create_sample_videos
from populate_social_posts import populate as populate_social_posts
from add_twitter_post import add_twitter_post

def populate_all():
    """
    Run all content population scripts in a logical order.
    """
    print("--- Starting to populate all content ---")

    print("\n[1/8] Creating admin user...")
    create_admin()

    print("\n[2/8] Creating initial site content...")
    create_initial_content()

    print("\n[3/8] Creating sample blog posts, categories, and tags...")
    create_sample_posts()

    print("\n[4/8] Creating sample videos and video categories...")
    create_sample_videos()

    print("\n[5/8] Creating sample partners...")
    create_sample_partners()

    print("\n[6/8] Creating infographics category...")
    create_infographics_category()

    print("\n[7/8] Populating social media posts...")
    populate_social_posts()

    print("\n[8/8] Adding a specific Twitter post...")
    twitter_url = 'https://x.com/sauti116/status/1997995788517945838/photo/1'
    add_twitter_post(twitter_url)

    print("\n--- All content population complete! ---")

if __name__ == '__main__':
    populate_all()
