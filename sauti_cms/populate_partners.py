#!/usr/bin/env python
"""
Script to create sample partners for testing
Usage: python create_sample_partners.py
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cms.settings')
django.setup()

from partners.models import Partner

def populate_partners():
    """Create sample partner organizations"""
    
    partners_data = [
        {
            'name': 'Ministry of Gender, Labour and Social Development (MGLSD)',
            'description': 'The lead government ministry responsible for child protection and social services in Uganda.',
            'partner_type': 'GOVERNMENT',
            'website_url': 'https://mglsd.go.ug',
            'email': 'info@mglsd.go.ug',
            'is_active': True,
            'is_featured': True,
            'order': 1,
        },
        {
            'name': 'UNICEF Uganda',
            'description': 'United Nations agency dedicated to children, supporting critical child protection frameworks.',
            'partner_type': 'UN_AGENCY',
            'website_url': 'https://www.unicef.org/uganda',
            'is_active': True,
            'is_featured': True,
            'order': 2,
        },
        {
            'name': 'SOS Children\'s Villages Uganda',
            'description': 'Providing family-based care and community support for vulnerable children.',
            'partner_type': 'NGO',
            'website_url': 'https://www.sos-uganda.org',
            'is_active': True,
            'is_featured': True,
            'order': 3,
        },
        {
            'name': 'Plan International Uganda',
            'description': 'Advancing children\'s rights and equality for girls through community-led programs.',
            'partner_type': 'NGO',
            'website_url': 'https://plan-international.org/uganda',
            'is_active': True,
            'is_featured': True,
            'order': 4,
        },
        {
            'name': 'World Vision Uganda',
            'description': 'Humanitarian organization focused on child well-being and community development.',
            'partner_type': 'NGO',
            'website_url': 'https://www.worldvision.org/uganda',
            'is_active': True,
            'is_featured': True,
            'order': 5,
        },
        {
            'name': 'Save the Children Uganda',
            'description': 'The leading independent organization for children in need of protection.',
            'partner_type': 'NGO',
            'website_url': 'https://uganda.savethechildren.net',
            'is_active': True,
            'is_featured': True,
            'order': 6,
        },
        {
            'name': 'Uganda Police Child and Family Protection Unit (CFPU)',
            'description': 'Specialized police unit handling legal protection and enforcement in domestic cases.',
            'partner_type': 'GOVERNMENT',
            'website_url': 'https://www.upf.go.ug',
            'is_active': True,
            'is_featured': True,
            'order': 7,
        },
    ]
    
    print("Creating sample partners...")
    created_count = 0
    
    for partner_data in partners_data:
        partner, created = Partner.objects.update_or_create(
            name=partner_data['name'],
            defaults=partner_data
        )
        
        if created:
            print(f"✓ Created: {partner.name}")
            created_count += 1
        else:
            print(f"🔄 Updated: {partner.name}")
    
    print(f"\n✅ Done! Created {created_count} new partners.")
    print(f"📊 Total partners in database: {Partner.objects.count()}")

if __name__ == '__main__':
    populate_partners()

