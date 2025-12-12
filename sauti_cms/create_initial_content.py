import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cms.settings')
django.setup()

from content.models import SiteContent

INITIAL_CONTENT = [
    # Home Page - Hero Section
    {'key': 'hero_image', 'label': 'Hero Image', 'value': '/assets/sauti-homepage.avif', 'page': 'home', 'type': 'photo', 'description': 'Main hero image on homepage'},
    {'key': 'hero_title', 'label': 'Hero Title', 'value': 'Every child deserves a safe voice.', 'page': 'home', 'type': 'heading', 'description': 'Main heading on homepage'},
    {'key': 'hero_subtitle', 'label': 'Hero Subtitle', 'value': 'Sauti 116 is free, confidential and available 24/7 across all telecoms. Report abuse, seek guidance, or get urgent help in your language.', 'page': 'home', 'type': 'text', 'description': 'Subtitle text under hero heading'},
    {'key': 'hero_cta_call', 'label': 'Hero Call Button', 'value': 'Call 116 Now', 'page': 'home', 'type': 'button', 'description': 'Call-to-action button text'},
    {'key': 'hero_cta_report', 'label': 'Hero Report Button', 'value': 'Report a Case', 'page': 'home', 'type': 'button', 'description': 'Report button text'},
    
    # Home Page - Quick Access Section
    {'key': 'quick_access_title', 'label': 'Quick Access Section Title', 'value': 'Get Help & Information', 'page': 'home', 'type': 'heading', 'description': 'Section heading for quick access cards'},
    {'key': 'quick_access_description', 'label': 'Quick Access Description', 'value': 'Access our comprehensive support services and resources designed to protect and empower children across Uganda.', 'page': 'home', 'type': 'text', 'description': 'Description text for quick access section'},
    {'key': 'card_report_title', 'label': 'Report Card Title', 'value': 'Report a Case', 'page': 'home', 'type': 'heading', 'description': 'Title for Report a Case card'},
    {'key': 'card_report_text', 'label': 'Report Card Text', 'value': 'Confidential, fast, and supportive reporting system.', 'page': 'home', 'type': 'text', 'description': 'Text for Report a Case card'},
    {'key': 'card_resources_title', 'label': 'Resources Card Title', 'value': 'Resources', 'page': 'home', 'type': 'heading', 'description': 'Title for Resources card'},
    {'key': 'card_resources_text', 'label': 'Resources Card Text', 'value': 'Guides, policies, and educational toolkits.', 'page': 'home', 'type': 'text', 'description': 'Text for Resources card'},
    {'key': 'card_faqs_title', 'label': 'FAQs Card Title', 'value': 'FAQs', 'page': 'home', 'type': 'heading', 'description': 'Title for FAQs card'},
    {'key': 'card_faqs_text', 'label': 'FAQs Card Text', 'value': 'Answers to common questions and concerns.', 'page': 'home', 'type': 'text', 'description': 'Text for FAQs card'},
    {'key': 'card_partners_title', 'label': 'Partners Card Title', 'value': 'Partners', 'page': 'home', 'type': 'heading', 'description': 'Title for Partners card'},
    {'key': 'card_partners_text', 'label': 'Partners Card Text', 'value': 'MGLSD, UNICEF, UCRNN, ITU collaboration.', 'page': 'home', 'type': 'text', 'description': 'Text for Partners card'},
    
    # Home Page - Journey Timeline Section
    {'key': 'journey_title', 'label': 'Journey Section Title', 'value': 'Our Journey', 'page': 'home', 'type': 'heading', 'description': 'Section heading for timeline'},
    {'key': 'journey_description', 'label': 'Journey Description', 'value': 'Key milestones in our history of child advocacy, including international recommendations and national designation of 116.', 'page': 'home', 'type': 'text', 'description': 'Description for journey section'},
    
    # Home Page - Publications Section
    {'key': 'publications_title', 'label': 'Publications Section Title', 'value': 'Recent Publications', 'page': 'home', 'type': 'heading', 'description': 'Section heading for publications'},
    {'key': 'publications_description', 'label': 'Publications Description', 'value': 'Latest articles, videos and resources to help children, families, and communities stay safe and informed.', 'page': 'home', 'type': 'text', 'description': 'Description for publications section'},
    {'key': 'publications_link', 'label': 'Publications Link', 'value': 'View all posts', 'page': 'home', 'type': 'button', 'description': 'Link text to view all posts'},
    
    # Home Page - Trust Partners Section
    {'key': 'trust_partners_title', 'label': 'Trust Partners Title', 'value': 'Trusted by Leading Organizations', 'page': 'home', 'type': 'heading', 'description': 'Title for trust partners section'},
    {'key': 'trust_partners_description', 'label': 'Trust Partners Description', 'value': 'Working in partnership with government and international agencies', 'page': 'home', 'type': 'text', 'description': 'Description for trust partners'},
    
    # Home Page - Final CTA Section
    {'key': 'final_cta_title', 'label': 'Final CTA Title', 'value': 'Need Help Right Now?', 'page': 'home', 'type': 'heading', 'description': 'Final CTA section title'},
    {'key': 'final_cta_text', 'label': 'Final CTA Text', 'value': 'Accessible 24/7 across all telecom networks. Support in multiple local languages. All services are free and confidential.', 'page': 'home', 'type': 'text', 'description': 'Final CTA section text'},
    {'key': 'final_cta_call', 'label': 'Final CTA Call Button', 'value': 'Call 116 Now', 'page': 'home', 'type': 'button', 'description': 'Final CTA call button'},
    {'key': 'final_cta_report', 'label': 'Final CTA Report Button', 'value': 'Report a Case', 'page': 'home', 'type': 'button', 'description': 'Final CTA report button'},
    {'key': 'final_cta_contact', 'label': 'Final CTA Contact Button', 'value': 'Contact Us', 'page': 'home', 'type': 'button', 'description': 'Final CTA contact button'},
    
    # About Page
    {'key': 'about_image', 'label': 'About Page Image', 'value': '/assets/sauti-aboutpage.webp', 'page': 'about', 'type': 'photo', 'description': 'Main image on about page'},
    {'key': 'about_title', 'label': 'About Page Title', 'value': 'About Sauti', 'page': 'about', 'type': 'heading', 'description': 'Main heading on about page'},
    
    # Operations Page
    {'key': 'operations_image', 'label': 'Operations Image', 'value': '/assets/our operations and case flow.jpg', 'page': 'operations', 'type': 'photo', 'description': 'Operations flowchart image'},
    
    # Header
    {'key': 'logo', 'label': 'Site Logo', 'value': '/assets/sauti-logo.jpeg', 'page': 'header', 'type': 'photo', 'description': 'Main site logo'},
]

def create_initial_content():
    created_count = 0
    updated_count = 0
    
    for item in INITIAL_CONTENT:
        obj, created = SiteContent.objects.update_or_create(
            key=item['key'],
            defaults={
                'label': item['label'],
                'value': item['value'],
                'page': item['page'],
                'type': item['type'],
                'description': item['description'],
            }
        )
        if created:
            created_count += 1
        else:
            updated_count += 1
            
    print(f"Content setup complete: {created_count} created, {updated_count} updated.")

if __name__ == '__main__':
    create_initial_content()
