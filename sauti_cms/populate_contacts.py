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

from content.models import Contact

def populate_contacts():
    """
    Populates the Contact model with default content.
    """
    print("Populating contact items...")
    
    contacts_data = [
        {'name': 'Emergency Hotline', 'value': '116', 'type': 'phone', 'icon': 'phone', 'order': 1},
        {'name': 'WhatsApp', 'value': '+256 743 889 999', 'type': 'phone', 'icon': 'whatsapp', 'order': 2},
        {'name': 'Email', 'value': 'info@sauti.mglsd.go.ug', 'type': 'email', 'icon': 'envelope', 'order': 3},
        {'name': 'Office Location', 'value': 'Ministry of Gender, Labour & Social Development, Kampala, Uganda', 'type': 'location', 'icon': 'location-marker', 'order': 4},
        {'name': 'Facebook', 'value': 'https://www.facebook.com/sauti116uganda', 'type': 'social', 'icon': 'facebook', 'order': 5},
        {'name': 'Twitter', 'value': 'https://twitter.com/sauti116', 'type': 'social', 'icon': 'twitter', 'order': 6},
    ]

    created_count = 0
    updated_count = 0

    for contact_data in contacts_data:
        contact_obj, created = Contact.objects.update_or_create(
            name=contact_data['name'],
            defaults={
                'value': contact_data['value'],
                'type': contact_data['type'],
                'icon': contact_data['icon'],
                'order': contact_data['order'],
                'is_visible': True,
            }
        )
        if created:
            created_count += 1
            print(f"Created Contact: {contact_data['name']}")
        else:
            updated_count += 1
            print(f"Updated Contact: {contact_data['name']}")

    print(f"Contact population complete: {created_count} created, {updated_count} updated.")

if __name__ == '__main__':
    populate_contacts()
