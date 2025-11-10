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

def create_sample_partners():
    """Create sample partner organizations"""
    
    partners_data = [
        {
            'name': 'Ministry of Gender, Labour and Social Development (MGLSD)',
            'description': 'Government ministry overseeing child protection and social services in Uganda.',
            'partner_type': 'GOVERNMENT',
            'website_url': 'https://mglsd.go.ug',
            'email': 'info@mglsd.go.ug',
            'phone': '+256-414-347854',
            'is_active': True,
            'is_featured': True,
            'order': 1,
        },
        {
            'name': 'UNICEF Uganda',
            'description': 'United Nations agency for children, supporting child protection programs in Uganda.',
            'partner_type': 'UN_AGENCY',
            'website_url': 'https://www.unicef.org/uganda',
            'email': 'kampala@unicef.org',
            'phone': '+256-417-171000',
            'is_active': True,
            'is_featured': True,
            'order': 2,
        },
        {
            'name': 'SOS Children\'s Villages Uganda',
            'description': 'International NGO providing family-based care for vulnerable children.',
            'partner_type': 'NGO',
            'website_url': 'https://www.sos-uganda.org',
            'email': 'info@sos-uganda.org',
            'phone': '+256-312-200400',
            'is_active': True,
            'is_featured': True,
            'order': 3,
        },
        {
            'name': 'Uganda 116 helpline',
            'description': 'National toll-free helpline for children in need of protection and support.',
            'partner_type': 'NGO',
            'website_url': 'https://childhelpline.or.ug',
            'email': 'info@childhelpline.or.ug',
            'phone': '116',
            'is_active': True,
            'is_featured': True,
            'order': 4,
        },
        {
            'name': 'Plan International Uganda',
            'description': 'Development and humanitarian organization advancing children\'s rights.',
            'partner_type': 'NGO',
            'website_url': 'https://plan-international.org/uganda',
            'email': 'uganda.co@plan-international.org',
            'phone': '+256-414-340883',
            'is_active': True,
            'is_featured': False,
            'order': 5,
        },
        {
            'name': 'World Vision Uganda',
            'description': 'International Christian humanitarian organization focused on child well-being.',
            'partner_type': 'NGO',
            'website_url': 'https://www.worldvision.org/uganda',
            'email': 'uganda_info@wvi.org',
            'phone': '+256-414-231600',
            'is_active': True,
            'is_featured': False,
            'order': 6,
        },
        {
            'name': 'Save the Children Uganda',
            'description': 'Leading organization for children\'s rights and welfare.',
            'partner_type': 'NGO',
            'website_url': 'https://uganda.savethechildren.net',
            'email': 'uganda.info@savethechildren.org',
            'phone': '+256-417-712300',
            'is_active': True,
            'is_featured': False,
            'order': 7,
        },
        {
            'name': 'Uganda Police Child and Family Protection Unit',
            'description': 'Specialized police unit handling cases of child abuse and family violence.',
            'partner_type': 'GOVERNMENT',
            'website_url': 'https://www.upf.go.ug',
            'email': 'cfpu@upf.go.ug',
            'phone': '+256-414-343225',
            'is_active': True,
            'is_featured': False,
            'order': 8,
        },
    ]
    
    print("Creating sample partners...")
    created_count = 0
    
    for partner_data in partners_data:
        partner, created = Partner.objects.get_or_create(
            name=partner_data['name'],
            defaults=partner_data
        )
        
        if created:
            print(f"✓ Created: {partner.name}")
            created_count += 1
        else:
            print(f"- Already exists: {partner.name}")
    
    print(f"\n✅ Done! Created {created_count} new partners.")
    print(f"📊 Total partners in database: {Partner.objects.count()}")

if __name__ == '__main__':
    create_sample_partners()

