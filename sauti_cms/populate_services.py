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
            'title': 'NATIONAL HELPLINE 116',
            'description': 'Direct, 24/7 National response mechanism accessible nationwide across all networks. Report any form of violence immediately.',
            'icon': 'phone',
            'is_visible': True,
        },
        {
            'order': 2,
            'title': 'CRISIS INTERVENTION',
            'description': 'Rapid assessment and decisive protection for children and survivors in urgent need of security.',
            'icon': 'shield',
            'is_visible': True,
        },
        {
            'order': 3,
            'title': 'EXPERT COUNSELING',
            'description': 'Authoritative mental health support provided by specialized response experts for full trauma recovery.',
            'icon': 'guidance',
            'is_visible': True,
        },
        {
            'order': 4,
            'title': 'LEGAL ACTION & PROTECTION',
            'description': 'Direct coordination with security agencies and law enforcement to ensure justice and absolute protection.',
            'icon': 'document',
            'is_visible': True,
        },
        {
            'order': 5,
            'title': 'NATIONAL OUTREACH',
            'description': 'Authoritative education and prevention campaigns mandated to eliminate abuse and empower communities.',
            'icon': 'community',
            'is_visible': True,
        },
        {
            'order': 6,
            'title': 'RAPID MULTI-CHANNEL ACCESS',
            'description': 'Immediate access via WhatsApp, U-Report, SafePal, and National protection centers nationwide.',
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
