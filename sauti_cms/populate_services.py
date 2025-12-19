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

from services.models import Service

def populate_services():
    """
    Populates the Service model with default content.
    """
    print("Populating services...")
    
    services_data = [
        {
            'order': 1,
            'title': '116 Toll-Free Helpline',
            'description': 'Our primary 24/7 toll-free helpline accessible nationwide across all telecom networks for immediate child protection reports.',
            'icon': 'phone',
            'is_visible': True,
        },
        {
            'order': 2,
            'title': 'Crisis Intervention & Triage',
            'description': 'Rapid assessment and immediate emotional support for children and GBV survivors in urgent need of protection.',
            'icon': 'shield',
            'is_visible': True,
        },
        {
            'order': 3,
            'title': 'Mental Health & Counseling',
            'description': 'Professional counseling services provided by trained experts to help victims process trauma and find a path to healing.',
            'icon': 'guidance',
            'is_visible': True,
        },
        {
            'order': 4,
            'title': 'Legal Aid Referrals',
            'description': 'Connecting survivors with legal professionals and law enforcement to ensure justice and legal protection.',
            'icon': 'document',
            'is_visible': True,
        },
        {
            'order': 5,
            'title': 'Community Outreach & Awareness',
            'description': 'Educational programs and awareness campaigns tailored for communities to prevent abuse and empower children.',
            'icon': 'community',
            'is_visible': True,
        },
        {
            'order': 6,
            'title': 'Multi-Channel Support',
            'description': 'Reach us via WhatsApp, U-Report, SafePal App, email, or physical walk-ins at our child protection centers.',
            'icon': 'media',
            'is_visible': True,
        },
    ]

    created_count = 0
    updated_count = 0

    for service_data in services_data:
        service_obj, created = Service.objects.update_or_create(
            order=service_data['order'],
            defaults={
                'title': service_data['title'],
                'description': service_data['description'],
                'icon': service_data['icon'],
                'is_visible': service_data['is_visible'],
            }
        )
        if created:
            created_count += 1
            print(f"Created service: {service_data['title']}")
        else:
            updated_count += 1
            print(f"Updated service: {service_data['title']}")

    print(f"Service population complete. {created_count} created, {updated_count} updated.")

if __name__ == '__main__':
    populate_services()
