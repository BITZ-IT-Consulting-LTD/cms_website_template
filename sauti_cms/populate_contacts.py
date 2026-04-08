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
        {'name': 'Call', 'value': '116', 'type': 'phone', 'icon': 'phone', 'order': 1, 'description': 'Free, confidential hotline available 24/7'},
        {'name': 'WhatsApp', 'value': '0743889999', 'type': 'phone', 'icon': 'whatsapp', 'order': 2, 'description': 'Chat with us on WhatsApp'},
        {'name': 'Email', 'value': 'sautichl@mglsd.go.ug', 'type': 'email', 'icon': 'envelope', 'order': 3, 'description': 'Send us an email for inquiries'},
        {'name': 'Online Reporting', 'value': 'https://sauti.mglsd.go.ug', 'type': 'social', 'icon': 'globe', 'order': 4, 'description': 'Report cases online through our portal'},
        {'name': 'SMS', 'value': 'Hello to 116', 'type': 'other', 'icon': 'message-square', 'order': 5, 'description': 'Send SMS to 116 and follow chatbot prompts'},
        {'name': 'Facebook', 'value': 'https://www.facebook.com/Sauti116Helpline', 'type': 'social', 'icon': 'facebook', 'order': 6, 'description': 'Follow us on Facebook'},
        {'name': 'Twitter', 'value': 'https://x.com/sauti116', 'type': 'social', 'icon': 'twitter', 'order': 7, 'description': 'Follow us on X (Twitter)'},
        {'name': 'TikTok', 'value': 'https://www.tiktok.com/@sauti116helplineuganda', 'type': 'social', 'icon': 'video', 'order': 8, 'description': 'Follow us on TikTok'},
        {'name': 'Office Location', 'value': 'Ministry of Gender, Labour & Social Development, Kampala, Uganda', 'type': 'location', 'icon': 'location-marker', 'order': 9, 'description': 'Visit our head office'},
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
                'description': contact_data.get('description', ''),
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
