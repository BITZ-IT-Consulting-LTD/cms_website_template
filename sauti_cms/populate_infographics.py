import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cms.settings')
django.setup()

from resources.models import ResourceCategory

def populate_infographics():
    category, created = ResourceCategory.objects.update_or_create(
        name='Infographics',
        defaults={
            'description': 'Visual representations of data and information',
            'icon': 'PhotoIcon'
        }
    )
    
    if created:
        print(f"Created category: {category.name}")
    else:
        print(f"Updated category: {category.name}")

if __name__ == '__main__':
    populate_infographics()
