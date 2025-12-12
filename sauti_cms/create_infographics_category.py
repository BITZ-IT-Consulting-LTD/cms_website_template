import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cms.settings')
django.setup()

from resources.models import ResourceCategory

def create_category():
    category, created = ResourceCategory.objects.get_or_create(
        name='Infographics',
        defaults={
            'description': 'Visual representations of data and information',
            'icon': 'PhotoIcon'
        }
    )
    
    if created:
        print(f"Created category: {category.name}")
    else:
        print(f"Category already exists: {category.name}")

if __name__ == '__main__':
    create_category()
