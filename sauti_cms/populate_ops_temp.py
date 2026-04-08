#!/usr/bin/env python
"""Populate Operations page content"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sauti_cms.settings')
django.setup()

from content.models import SiteContent

ops_content = {
    # Infrastructure Section
    'operations_infra_badge': { 'key': 'operations_infra_badge', 'value': 'Our Foundation', 'label': 'Infrastructure Badge', 'page': 'operations', 'type': 'text' },
    'operations_infra_title': { 'key': 'operations_infra_title', 'value': 'A Robust Infrastructure for', 'label': 'Infrastructure Title', 'page': 'operations', 'type': 'heading' },
    'operations_infra_title_highlight': { 'key': 'operations_infra_title_highlight', 'value': 'Nationwide Impact', 'label': 'Infrastructure Title Highlight', 'page': 'operations', 'type': 'heading' },
    'operations_infra_description': { 'key': 'operations_infra_description', 'value': 'Our operations are built on sustainable pillars that ensure every caller receives expert attention, no matter where they are in Uganda.', 'label': 'Infrastructure Description', 'page': 'operations', 'type': 'text' },

    # Infrastructure Stats
    'operations_infra_stat1_value': { 'key': 'operations_infra_stat1_value', 'value': '26', 'label': 'Infrastructure Stat 1 Value', 'page': 'operations', 'type': 'text' },
    'operations_infra_stat1_label': { 'key': 'operations_infra_stat1_label', 'value': 'Languages', 'label': 'Infrastructure Stat 1 Label', 'page': 'operations', 'type': 'text' },
    'operations_infra_stat2_value': { 'key': 'operations_infra_stat2_value', 'value': '24/7', 'label': 'Infrastructure Stat 2 Value', 'page': 'operations', 'type': 'text' },
    'operations_infra_stat2_label': { 'key': 'operations_infra_stat2_label', 'value': 'Available', 'label': 'Infrastructure Stat 2 Label', 'page': 'operations', 'type': 'text' },
    'operations_infra_stat3_value': { 'key': 'operations_infra_stat3_value', 'value': '100%', 'label': 'Infrastructure Stat 3 Value', 'page': 'operations', 'type': 'text' },
    'operations_infra_stat3_label': { 'key': 'operations_infra_stat3_label', 'value': 'Coverage', 'label': 'Infrastructure Stat 3 Label', 'page': 'operations', 'type': 'text' },

    # Infrastructure Pillars
    'operations_pillar1_title': { 'key': 'operations_pillar1_title', 'value': '26 Local Languages', 'label': 'Pillar 1 Title', 'page': 'operations', 'type': 'heading' },
    'operations_pillar1_description': { 'key': 'operations_pillar1_description', 'value': 'Bridging the communication gap for every community in Uganda.', 'label': 'Pillar 1 Description', 'page': 'operations', 'type': 'text' },
    'operations_pillar2_title': { 'key': 'operations_pillar2_title', 'value': '24/7 Availability', 'label': 'Pillar 2 Title', 'page': 'operations', 'type': 'heading' },
    'operations_pillar2_description': { 'key': 'operations_pillar2_description', 'value': 'Support is always just a phone call away, day or night.', 'label': 'Pillar 2 Description', 'page': 'operations', 'type': 'text' },
    'operations_pillar3_title': { 'key': 'operations_pillar3_title', 'value': 'Sustainable Funding', 'label': 'Pillar 3 Title', 'page': 'operations', 'type': 'heading' },
    'operations_pillar3_description': { 'key': 'operations_pillar3_description', 'value': 'Partnering with MGLSD and UNICEF for long-term service stability.', 'label': 'Pillar 3 Description', 'page': 'operations', 'type': 'text' },

    # Services Section
    'services_section_title': { 'key': 'services_section_title', 'value': 'Services We Offer', 'label': 'Services Section Title', 'page': 'operations', 'type': 'heading' },
    'services_section_subtitle': { 'key': 'services_section_subtitle', 'value': 'Comprehensive support systems protecting and empowering every voice in Uganda.', 'label': 'Services Section Subtitle', 'page': 'operations', 'type': 'text' },

    # Service Items
    'service_counseling_title': { 'key': 'service_counseling_title', 'value': 'Telephone Counseling', 'label': 'Service Counseling Title', 'page': 'operations', 'type': 'heading' },
    'service_counseling_text': { 'key': 'service_counseling_text', 'value': 'Professional counseling services available 24/7 through our toll-free helpline 116.', 'label': 'Service Counseling Text', 'page': 'operations', 'type': 'text' },
    'service_walkin_title': { 'key': 'service_walkin_title', 'value': 'Walk-In Support', 'label': 'Service Walk-In Title', 'page': 'operations', 'type': 'heading' },
    'service_walkin_text': { 'key': 'service_walkin_text', 'value': 'Handle walk-in clients at our offices for face-to-face consultation and support.', 'label': 'Service Walk-In Text', 'page': 'operations', 'type': 'text' },
    'service_media_title': { 'key': 'service_media_title', 'value': 'Media Response', 'label': 'Service Media Title', 'page': 'operations', 'type': 'heading' },
    'service_media_text': { 'key': 'service_media_text', 'value': 'Respond to cases of violence against children and gender-based violence reported through media and U-report.', 'label': 'Service Media Text', 'page': 'operations', 'type': 'text' },
    'service_guidance_title': { 'key': 'service_guidance_title', 'value': 'Information & Guidance', 'label': 'Service Guidance Title', 'page': 'operations', 'type': 'heading' },
    'service_guidance_text': { 'key': 'service_guidance_text', 'value': 'Provision of information and guidance on child care and protection matters.', 'label': 'Service Guidance Text', 'page': 'operations', 'type': 'text' },
    'service_referral_title': { 'key': 'service_referral_title', 'value': 'Essential Service Referrals', 'label': 'Service Referral Title', 'page': 'operations', 'type': 'heading' },
    'service_referral_text': { 'key': 'service_referral_text', 'value': 'Referral to essential services including healthcare, legal aid, and social support.', 'label': 'Service Referral Text', 'page': 'operations', 'type': 'text' },
    'service_community_title': { 'key': 'service_community_title', 'value': 'Community Sensitization', 'label': 'Service Community Title', 'page': 'operations', 'type': 'heading' },
    'service_community_text': { 'key': 'service_community_text', 'value': 'Community sensitization activities to raise awareness about child protection and GBV prevention.', 'label': 'Service Community Text', 'page': 'operations', 'type': 'text' },
}

for key, data in ops_content.items():
    obj, created = SiteContent.objects.update_or_create(
        key=key,
        defaults={
            'value': data['value'],
            'label': data['label'],
            'page': data['page'],
            'type': data['type'],
            'is_published': True
        }
    )
    status = 'Created' if created else 'Updated'
    print(f'{status}: {key}')

print('Done populating Operations page content')
