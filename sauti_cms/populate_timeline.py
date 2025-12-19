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

from timeline.models import TimelineEvent

def populate_timeline():
    """
    Populates the TimelineEvent model with default content.
    """
    print("Populating timeline events...")
    
    timeline_events_data = [
        {'year': '2013', 'title': 'Lobbying & Designation Effort', 'description': 'MGLSD, with UCRNN and UNICEF, lobbied for 116 to be designated as Uganda’s child helpline number.', 'order': 1},
        {'year': 'Aug 2013', 'title': 'Official Toll-Free Number', 'description': 'UCC officially designated 116 as an emergency and toll-free number.', 'order': 2},
        {'year': 'Nov 2013', 'title': 'First Call Received', 'description': 'UCHL received the first call on code 116 on 4th November 2013.', 'order': 3},
        {'year': 'Dec 2014', 'title': 'Government Takes Over', 'description': 'MGLSD took over the management of UCHL from UCRNN.', 'order': 4},
        {'year': '2016', 'title': 'Legal & Regulatory Framework', 'description': 'UCHL instituted by law (Children’s Act cap 59 2016, as amended) section 42 C.', 'order': 5},
        {'year': '2021', 'title': 'GBV Response Integrated', 'description': 'Gender-based violence response integrated into Sauti’s work nationwide.', 'order': 6},
    ]

    created_count = 0
    updated_count = 0

    for event_data in timeline_events_data:
        event_obj, created = TimelineEvent.objects.update_or_create(
            order=event_data['order'],
            defaults={
                'year': event_data['year'],
                'title': event_data['title'],
                'description': event_data['description'],
                'is_visible': True,
            }
        )
        if created:
            created_count += 1
            print(f"Created: {event_data['year']} - {event_data['title']}")
        else:
            updated_count += 1
            print(f"Updated: {event_data['year']} - {event_data['title']}")

    print(f"Timeline population complete: {created_count} created, {updated_count} updated.")

if __name__ == '__main__':
    populate_timeline()
