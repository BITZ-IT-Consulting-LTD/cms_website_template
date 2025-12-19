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
from populate_admin import populate_admin
from populate_infographics import populate_infographics
from populate_initial_content import populate_initial_content, populate_global_settings
from populate_partners import populate_partners
from populate_posts import populate_posts
from populate_videos import populate_videos
from populate_social_posts import populate as populate_social_posts
from add_twitter_post import add_twitter_post
from populate_timeline import populate_timeline
from populate_contacts import populate_contacts
from populate_about_page_content import populate_about_page_content
from populate_faqs import populate_faqs
from populate_services import populate_services


def populate_all():
    """
    Run all content population scripts in a logical order.
    """
    print("--- Starting to populate all content ---")

    print("\n[1/14] Creating admin user...")
    populate_admin()

    print("\n[2/14] Creating initial site content...")
    populate_initial_content()

    print("\n[3/14] Populating global settings...")
    populate_global_settings()

    print("\n[4/14] Populating About Page content (Core Values, Timeline, Protection Approach, Team)...")
    populate_about_page_content()

    print("\n[5/14] Creating sample blog posts, categories, and tags...")
    populate_posts()

    print("\n[6/14] Creating sample videos and video categories...")
    populate_videos()

    print("\n[7/14] Creating sample partners...")
    populate_partners()

    print("\n[8/14] Creating infographics category...")
    populate_infographics()

    print("\n[9/14] Populating social media posts...")
    populate_social_posts()

    print("\n[10/14] Adding a specific Twitter post...")
    twitter_url = 'https://x.com/sauti116/status/1997995788517945838/photo/1'
    add_twitter_post(twitter_url)

    print("\n[11/14] Populating timeline...")
    populate_timeline()

    print("\n[12/14] Populating contacts...")
    populate_contacts()

    print("\n[13/14] Populating FAQs...")
    populate_faqs()

    print("\n[14/14] Populating services...")
    populate_services()

    print("\n--- All content population complete! ---")

if __name__ == '__main__':
    populate_all()
