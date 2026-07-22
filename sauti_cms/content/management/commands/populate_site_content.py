from django.core.management.base import BaseCommand
from content.models import SiteContent
from timeline.models import TimelineEvent
from services.models import Service
from content.models import Contact

class Command(BaseCommand):
    help = 'Populates the SiteContent model and TimelineEvent model with default content.'

    def handle(self, *args, **options):
        # Data for Timeline Events
        timeline_events_data = [
            {'year': '2013', 'title': 'Lobbying & Designation Effort', 'description': 'MGLSD, with UCRNN and UNICEF, lobbied for 116 to be designated as Uganda’s child helpline number.', 'order': 1},
            {'year': 'Aug 2013', 'title': 'Official Toll-Free Number', 'description': 'UCC officially designated 116 as an emergency and toll-free number.', 'order': 2},
            {'year': 'Nov 2013', 'title': 'First Call Received', 'description': 'UCHL received the first call on code 116 on 4th November 2013.', 'order': 3},
            {'year': 'Dec 2014', 'title': 'Government Takes Over', 'description': 'MGLSD took over the management of UCHL from UCRNN.', 'order': 4},
            {'year': '2016', 'title': 'Legal & Regulatory Framework', 'description': 'UCHL instituted by law (Children’s Act cap 59 2016, as amended) section 42 C.', 'order': 5},
            {'year': '2021', 'title': 'GBV Response Integrated', 'description': 'Gender-based violence response integrated into Sauti’s work nationwide.', 'order': 6},
        ]

        for i, event_data in enumerate(timeline_events_data):
            event_obj, created = TimelineEvent.objects.get_or_create(
                year=event_data['year'],
                title=event_data['title'],
                defaults={
                    'description': event_data['description'],
                    'order': event_data['order'],
                    'is_visible': True, # Default to visible
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Created TimelineEvent: {event_data['year']} - {event_data['title']}"))
            else:
                self.stdout.write(self.style.WARNING(f"TimelineEvent already exists: {event_data['year']} - {event_data['title']}"))

        # Data for Services
        services_data = [
            {'title': 'Telephone Counseling', 'description': 'Immediate, confidential support via 116.', 'icon': 'phone', 'order': 1},
            {'title': 'Walk-in Support', 'description': 'On-site help and rapid referrals.', 'icon': 'walk', 'order': 2},
            {'title': 'Media & U-Report', 'description': 'Engagement via broadcast and U-Report 8500.', 'icon': 'media', 'order': 3},
            {'title': 'Guidance & Referral', 'description': 'Connections to specialized services.', 'icon': 'guidance', 'order': 4},
            {'title': 'Community Sensitization', 'description': 'Awareness and advocacy in communities nationwide.', 'icon': 'community', 'order': 5},
        ]

        for i, service_data in enumerate(services_data):
            try:
                service_obj, created = Service.objects.get_or_create(
                    title=service_data['title'],
                    defaults={
                        'description': service_data['description'],
                        'icon': service_data['icon'],
                        'order': service_data['order'],
                        'is_visible': True, # Default to visible
                    }
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f"Created Service: {service_data['title']}"))
                else:
                    self.stdout.write(self.style.WARNING(f"Service already exists: {service_data['title']}"))
            except Exception as e:
                self.stdout.write(self.style.WARNING(f"Could not create service '{service_data['title']}': {str(e)}"))

        # Data for Contacts
        contacts_data = [
            {'name': 'Emergency Hotline', 'value': '116', 'type': 'phone', 'icon': 'phone', 'order': 1},
            {'name': 'WhatsApp', 'value': '+256 743 889 999', 'type': 'phone', 'icon': 'whatsapp', 'order': 2},
            {'name': 'Email', 'value': 'info@sauti.mglsd.go.ug', 'type': 'email', 'icon': 'envelope', 'order': 3},
            {'name': 'Office Location', 'value': 'Ministry of Gender, Labour & Social Development, Kampala, Uganda', 'type': 'location', 'icon': 'location-marker', 'order': 4},
            {'name': 'Facebook', 'value': 'https://www.facebook.com/sauti116uganda', 'type': 'social', 'icon': 'facebook', 'order': 5},
            {'name': 'Twitter', 'value': 'https://twitter.com/sauti116', 'type': 'social', 'icon': 'twitter', 'order': 6},
        ]

        for i, contact_data in enumerate(contacts_data):
            contact_obj, created = Contact.objects.get_or_create(
                name=contact_data['name'],
                defaults={
                    'value': contact_data['value'],
                    'type': contact_data['type'],
                    'icon': contact_data['icon'],
                    'order': contact_data['order'],
                    'is_visible': True, # Default to visible
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Created Contact: {contact_data['name']}"))
            else:
                self.stdout.write(self.style.WARNING(f"Contact already exists: {contact_data['name']}"))

        default_content = {
            # Home Page - Hero Section
            'home_hero_headline': { 'key': 'home_hero_headline', 'value': 'TAKE NO CHANCES!', 'label': 'Home Hero Headline', 'page': 'home', 'type': 'heading', 'description': 'Main headline in hero section' },
            'home_hero_subheadline': { 'key': 'home_hero_subheadline', 'value': 'Report a case now', 'label': 'Home Hero Subheadline', 'page': 'home', 'type': 'heading', 'description': 'Secondary headline in hero section' },
            'home_hero_cta_text': { 'key': 'home_hero_cta_text', 'value': 'Call {hotline} Toll Free', 'label': 'Home Hero CTA Text', 'page': 'home', 'type': 'text', 'description': 'Text above buttons - {hotline} will be replaced with hotline number' },
            'home_hero_call_button': { 'key': 'home_hero_call_button', 'value': 'Call Now', 'label': 'Home Hero Call Button', 'page': 'home', 'type': 'button', 'description': 'Primary call button text' },
            'home_hero_report_button': { 'key': 'home_hero_report_button', 'value': 'Report a case here', 'label': 'Home Hero Report Button', 'page': 'home', 'type': 'button', 'description': 'Secondary report button text' },
            'home_logo_sauti_alt': { 'key': 'home_logo_sauti_alt', 'value': 'Sauti 116 - Speak Up Against Violence', 'label': 'Home Sauti Logo Alt Text', 'page': 'home', 'type': 'text', 'description': 'Alt text for Sauti logo' },
            'home_logo_uganda_alt': { 'key': 'home_logo_uganda_alt', 'value': 'Republic of Uganda', 'label': 'Home Uganda Logo Alt Text', 'page': 'home', 'type': 'text', 'description': 'Alt text for Uganda coat of arms' },
            'home_hero_image_alt': { 'key': 'home_hero_image_alt', 'value': 'Ugandan mother protecting her children', 'label': 'Home Hero Image Alt Text', 'page': 'home', 'type': 'text', 'description': 'Alt text for hero section image' },
            
            # Home Page - News/Updates Section
            'home_news_badge_text': { 'key': 'home_news_badge_text', 'value': 'Our Impact', 'label': 'Home News Badge Text', 'page': 'home', 'type': 'text', 'description': 'Badge text above news section title' },
            
            # Home Page - Partners Section (managed via settings but can have overrides)
            
            # Home Page - Social Media Links
            'home_social_twitter_url': { 'key': 'home_social_twitter_url', 'value': 'https://x.com/sauti116?s=21', 'label': 'Home Twitter/X URL', 'page': 'home', 'type': 'text', 'description': 'Twitter/X profile URL' },
            'home_social_twitter_label': { 'key': 'home_social_twitter_label', 'value': 'X (formerly Twitter)', 'label': 'Home Twitter/X Label', 'page': 'home', 'type': 'text', 'description': 'ARIA label for Twitter/X link' },
            'home_social_instagram_url': { 'key': 'home_social_instagram_url', 'value': 'https://www.instagram.com/sauti116helpline?igsh=MTdyNjgwOG42ZjB2dA%3D%3D&utm_source=qr', 'label': 'Home Instagram URL', 'page': 'home', 'type': 'text', 'description': 'Instagram profile URL' },
            'home_social_instagram_label': { 'key': 'home_social_instagram_label', 'value': 'Instagram', 'label': 'Home Instagram Label', 'page': 'home', 'type': 'text', 'description': 'ARIA label for Instagram link' },
            'home_social_facebook_url': { 'key': 'home_social_facebook_url', 'value': 'https://www.facebook.com/share/14W6eurox1o/', 'label': 'Home Facebook URL', 'page': 'home', 'type': 'text', 'description': 'Facebook page URL' },
            'home_social_facebook_label': { 'key': 'home_social_facebook_label', 'value': 'Facebook', 'label': 'Home Facebook Label', 'page': 'home', 'type': 'text', 'description': 'ARIA label for Facebook link' },
            'home_social_tiktok_url': { 'key': 'home_social_tiktok_url', 'value': 'https://www.tiktok.com/@sauti116helplineuganda?_r=1&_t=ZS-952NtlMMSIs', 'label': 'Home TikTok URL', 'page': 'home', 'type': 'text', 'description': 'TikTok profile URL' },
            'home_social_tiktok_label': { 'key': 'home_social_tiktok_label', 'value': 'TikTok', 'label': 'Home TikTok Label', 'page': 'home', 'type': 'text', 'description': 'ARIA label for TikTok link' },
            'home_social_youtube_url': { 'key': 'home_social_youtube_url', 'value': 'https://www.youtube.com/@Sauti116HelplineUganda', 'label': 'Home YouTube URL', 'page': 'home', 'type': 'text', 'description': 'YouTube channel URL' },
            'home_social_youtube_label': { 'key': 'home_social_youtube_label', 'value': 'YouTube', 'label': 'Home YouTube Label', 'page': 'home', 'type': 'text', 'description': 'ARIA label for YouTube link' },

            # Home Page - Mock News Content (for empty state)
            'home_news_mock_featured_category': { 'key': 'home_news_mock_featured_category', 'value': 'Community', 'label': 'Home Mock Featured Category', 'page': 'home', 'type': 'text', 'description': 'Category for mock featured news' },
            'home_news_mock_featured_title': { 'key': 'home_news_mock_featured_title', 'value': 'Sauti 116 Expands Reach to Rural Areas', 'label': 'Home Mock Featured Title', 'page': 'home', 'type': 'heading', 'description': 'Title for mock featured news' },
            'home_news_mock_featured_text': { 'key': 'home_news_mock_featured_text', 'value': 'We are dedicated to ensuring every voice is heard. Our latest initiative focuses on reaching remote villages to provide immediate support.', 'label': 'Home Mock Featured Text', 'page': 'home', 'type': 'text', 'description': 'Description for mock featured news' },
            'home_news_mock_featured_date': { 'key': 'home_news_mock_featured_date', 'value': 'Jan 12, 2026', 'label': 'Home Mock Featured Date', 'page': 'home', 'type': 'text', 'description': 'Date for mock featured news' },
            'home_news_mock_side1_category': { 'key': 'home_news_mock_side1_category', 'value': 'Education', 'label': 'Home Mock Side 1 Category', 'page': 'home', 'type': 'text', 'description': 'Category for first side news item' },
            'home_news_mock_side1_title': { 'key': 'home_news_mock_side1_title', 'value': 'School Outreach Programs Launching Soon', 'label': 'Home Mock Side 1 Title', 'page': 'home', 'type': 'heading', 'description': 'Title for first side news item' },
            'home_news_mock_side1_date': { 'key': 'home_news_mock_side1_date', 'value': 'Jan 10, 2026', 'label': 'Home Mock Side 1 Date', 'page': 'home', 'type': 'text', 'description': 'Date for first side news item' },
            'home_news_mock_side2_category': { 'key': 'home_news_mock_side2_category', 'value': 'Health', 'label': 'Home Mock Side 2 Category', 'page': 'home', 'type': 'text', 'description': 'Category for second side news item' },
            'home_news_mock_side2_title': { 'key': 'home_news_mock_side2_title', 'value': 'Partnership with Ministry of Health', 'label': 'Home Mock Side 2 Title', 'page': 'home', 'type': 'heading', 'description': 'Title for second side news item' },
            'home_news_mock_side2_date': { 'key': 'home_news_mock_side2_date', 'value': 'Jan 08, 2026', 'label': 'Home Mock Side 2 Date', 'page': 'home', 'type': 'text', 'description': 'Date for second side news item' },
            'home_news_mock_side3_category': { 'key': 'home_news_mock_side3_category', 'value': 'Training', 'label': 'Home Mock Side 3 Category', 'page': 'home', 'type': 'text', 'description': 'Category for third side news item' },
            'home_news_mock_side3_title': { 'key': 'home_news_mock_side3_title', 'value': 'Counselor Training Certification Complete', 'label': 'Home Mock Side 3 Title', 'page': 'home', 'type': 'heading', 'description': 'Title for third side news item' },
            'home_news_mock_side3_date': { 'key': 'home_news_mock_side3_date', 'value': 'Jan 05, 2026', 'label': 'Home Mock Side 3 Date', 'page': 'home', 'type': 'text', 'description': 'Date for third side news item' },
            
            # Legacy content keys (kept for backwards compatibility)
            'hero_title': { 'key': 'hero_title', 'value': 'Every One Deserves to Be Heard.', 'label': 'Hero Title', 'page': 'home', 'type': 'heading' },
            'hero_subtitle': { 'key': 'hero_subtitle', 'value': 'Sauti 116 is free, confidential and available 24/7 across all telecoms. Report abuse, seek guidance, or get urgent help in your language.', 'label': 'Hero Subtitle', 'page': 'home', 'type': 'text' },
            'hero_cta_call': { 'key': 'hero_cta_call', 'value': 'Call 116 Now', 'label': 'Hero CTA Call', 'page': 'home', 'type': 'button' },
            'hero_cta_report': { 'key': 'hero_cta_report', 'value': 'Report a Case', 'label': 'Hero CTA Report', 'page': 'home', 'type': 'button' },
            'quick_access_title': { 'key': 'quick_access_title', 'value': 'Get Help & Information', 'label': 'Quick Access Title', 'page': 'home', 'type': 'heading' },
            'quick_access_description': { 'key': 'quick_access_description', 'value': 'Access our comprehensive support services and resources designed to protect and empower children across Uganda.', 'label': 'Quick Access Description', 'page': 'home', 'type': 'text' },
            'card_report_title': { 'key': 'card_report_title', 'value': 'Report a Case', 'label': 'Card Report Title', 'page': 'home', 'type': 'heading' },
            'card_report_text': { 'key': 'card_report_text', 'value': 'Report abuse confidentially. Our trained counselors are available 24/7 to listen and support you.', 'label': 'Card Report Text', 'page': 'home', 'type': 'text' },
            'card_resources_title': { 'key': 'card_resources_title', 'value': 'Resources', 'label': 'Card Resources Title', 'page': 'home', 'type': 'heading' },
            'card_resources_text': { 'key': 'card_resources_text', 'value': 'Access vital information, safety guides, and educational materials to protect children.', 'label': 'Card Resources Text', 'page': 'home', 'type': 'text' },
            'card_faqs_title': { 'key': 'card_faqs_title', 'value': 'FAQs', 'label': 'Card FAQs Title', 'page': 'home', 'type': 'heading' },
            'card_faqs_text': { 'key': 'card_faqs_text', 'value': 'Find quick answers to common questions about our services, reporting process, and safety.', 'label': 'Card FAQs Text', 'page': 'home', 'type': 'text' },
            'card_partners_title': { 'key': 'card_partners_title', 'value': 'Partners', 'label': 'Card Partners Title', 'page': 'home', 'type': 'heading' },
            'card_partners_text': { 'key': 'card_partners_text', 'value': 'Collaborating with government and international organizations to ensure child safety.', 'label': 'Card Partners Text', 'page': 'home', 'type': 'text' },
            'publications_title': { 'key': 'publications_title', 'value': 'Recent Publications', 'label': 'Publications Title', 'page': 'home', 'type': 'heading' },
            'publications_description': { 'key': 'publications_description', 'value': 'Latest articles, videos and resources to help children, families, and communities stay safe and informed.', 'label': 'Publications Description', 'page': 'home', 'type': 'text' },
            'publications_link': { 'key': 'publications_link', 'value': 'View all posts', 'label': 'Publications Link', 'page': 'home', 'type': 'button' },
            'trust_partners_title': { 'key': 'trust_partners_title', 'value': 'Trusted by Leading Organizations', 'label': 'Trust Partners Title', 'page': 'home', 'type': 'heading' },
            'trust_partners_description': { 'key': 'trust_partners_description', 'value': 'Working in partnership with government and international agencies', 'label': 'Trust Partners Description', 'page': 'home', 'type': 'text' },
            'final_cta_title': { 'key': 'final_cta_title', 'value': 'Need Help Right Now?', 'label': 'Final CTA Title', 'page': 'home', 'type': 'heading' },
            'final_cta_text': { 'key': 'final_cta_text', 'value': 'Accessible 24/7 across all telecom networks. Support in multiple local languages. All services are free and confidential.', 'label': 'Final CTA Text', 'page': 'home', 'type': 'text' },
            'final_cta_call': { 'key': 'final_cta_call', 'value': 'Call 116 Now', 'label': 'Final CTA Call', 'page': 'home', 'type': 'button' },
            'final_cta_report': { 'key': 'final_cta_report', 'value': 'Report a Case', 'label': 'Final CTA Report', 'page': 'home', 'type': 'button' },
            'final_cta_contact': { 'key': 'final_cta_contact', 'value': 'Contact Us', 'label': 'Final CTA Contact', 'page': 'home', 'type': 'button' },

            # About Page Content
            'about_hero_title': { 'key': 'about_hero_title', 'value': 'About Sauti 116 helpline', 'label': 'About Hero Title', 'page': 'about', 'type': 'heading' },
            'about_hero_subtitle': { 'key': 'about_hero_subtitle', 'value': 'Free, confidential and accessible 24/7 across all telecoms. We protect and empower children, GBV survivors and migrant workers with rapid, compassionate support.', 'label': 'About Hero Subtitle', 'page': 'about', 'type': 'text' },
            'about_stat_1_title': { 'key': 'about_stat_1_title', 'value': '116', 'label': 'About Stat 1 Title', 'page': 'about', 'type': 'text' },
            'about_stat_1_text': { 'key': 'about_stat_1_text', 'value': 'Toll-free Hotline', 'label': 'About Stat 1 Text', 'page': 'about', 'type': 'text' },
            'about_stat_2_title': { 'key': 'about_stat_2_title', 'value': '24/7', 'label': 'About Stat 2 Title', 'page': 'about', 'type': 'text' },
            'about_stat_2_text': { 'key': 'about_stat_2_text', 'value': 'Always Available', 'label': 'About Stat 2 Text', 'page': 'about', 'type': 'text' },
            'about_stat_3_title': { 'key': 'about_stat_3_title', 'value': '26+', 'label': 'About Stat 3 Title', 'page': 'about', 'type': 'text' },
            'about_stat_3_text': { 'key': 'about_stat_3_text', 'value': 'Local Languages', 'label': 'About Stat 3 Text', 'page': 'about', 'type': 'text' },
            'about_stat_4_title': { 'key': 'about_stat_4_title', 'value': '100%', 'label': 'About Stat 4 Title', 'page': 'about', 'type': 'text' },
            'about_stat_4_text': { 'key': 'about_stat_4_text', 'value': 'National Coverage', 'label': 'About Stat 4 Text', 'page': 'about', 'type': 'text' },
            'about_mission_title': { 'key': 'about_mission_title', 'value': 'Our Mission', 'label': 'About Mission Title', 'page': 'about', 'type': 'heading' },
            'about_mission_text': { 'key': 'about_mission_text', 'value': 'To protect and empower vulnerable populations through accessible, confidential, and professional support services available 24/7.', 'label': 'About Mission Text', 'page': 'about', 'type': 'text' },
            'about_values_title': { 'key': 'about_values_title', 'value': 'Core Values', 'label': 'About Values Title', 'page': 'about', 'type': 'heading' },
            'about_background_title': { 'key': 'about_background_title', 'value': 'Background', 'label': 'About Background Title', 'page': 'about', 'type': 'heading' },
            'about_background_item_1': { 'key': 'about_background_item_1', 'value': 'In early 2013, MGLSD in partnership with UCRNN and UNICEF lobbied for 116 to be designated as a child helpline number.', 'label': 'About Background Item 1', 'page': 'about', 'type': 'text' },
            'about_background_item_2': { 'key': 'about_background_item_2', 'value': 'August 2013, 116 was officially designated as an emergency and toll-free number by UCC.', 'label': 'About Background Item 2', 'page': 'about', 'type': 'text' },
            'about_background_item_3': { 'key': 'about_background_item_3', 'value': 'On 4th November 2013, the first call was received by UCHL on the code 116.', 'label': 'About Background Item 3', 'page': 'about', 'type': 'text' },
            'about_background_item_4': { 'key': 'about_background_item_4', 'value': 'In December 2014, government (MGLSD) took over the management of UCHL from UCRNN.', 'label': 'About Background Item 4', 'page': 'about', 'type': 'text' },
            'about_background_item_5': { 'key': 'about_background_item_5', 'value': 'UCHL was instituted by law (Children’s Act cap 59 2016, as amended) section 42 C.', 'label': 'About Background Item 5', 'page': 'about', 'type': 'text' },
            'about_background_item_6': { 'key': 'about_background_item_6', 'value': 'In 2021, GBV response was integrated into Sauti’s work.', 'label': 'About Background Item 6', 'page': 'about', 'type': 'text' },
            'about_background_note': { 'key': 'about_background_note', 'value': 'Note: In October 2007, ITU asked all countries around the world to allocate 116 to Child Helplines.', 'label': 'About Background Note', 'page': 'about', 'type': 'text' },
            'about_operations_title': { 'key': 'about_operations_title', 'value': 'Operations', 'label': 'About Operations Title', 'page': 'about', 'type': 'heading' },
            'about_operations_item_1': { 'key': 'about_operations_item_1', 'value': 'Sauti is a Swahili word that means “voice”.', 'label': 'About Operations Item 1', 'page': 'about', 'type': 'text' },
            'about_operations_item_2': { 'key': 'about_operations_item_2', 'value': 'Operates on short code 116 (toll-free), accessible from any telecom network.', 'label': 'About Operations Item 2', 'page': 'about', 'type': 'text' },
            'about_operations_item_3': { 'key': 'about_operations_item_3', 'value': 'Operational 24/7 and accessible from every part of the country.', 'label': 'About Operations Item 3', 'page': 'about', 'type': 'text' },
            'about_operations_item_4': { 'key': 'about_operations_item_4', 'value': 'The counselors speak a total of 26 local languages.', 'label': 'About Operations Item 4', 'page': 'about', 'type': 'text' },
            'about_resolution_title': { 'key': 'about_resolution_title', 'value': 'Path to Resolution', 'label': 'About Resolution Title', 'page': 'about', 'type': 'heading' },
            'about_partners_title': { 'key': 'about_partners_title', 'value': 'Partners & Affiliations', 'label': 'About Partners Title', 'page': 'about', 'type': 'heading' },
            'about_partner_1': { 'key': 'about_partner_1', 'value': 'MGLSD', 'label': 'About Partner 1', 'page': 'about', 'type': 'text' },
            'about_partner_2': { 'key': 'about_partner_2', 'value': 'UNICEF', 'label': 'About Partner 2', 'page': 'about', 'type': 'text' },
            'about_partner_3': { 'key': 'about_partner_3', 'value': 'UCRNN', 'label': 'About Partner 3', 'page': 'about', 'type': 'text' },
            'about_partner_4': { 'key': 'about_partner_4', 'value': 'ITU 116', 'label': 'About Partner 4', 'page': 'about', 'type': 'text' },
            'about_partners_text': { 'key': 'about_partners_text', 'value': 'Legally designated 116 child helpline; compliant with national and international standards.', 'label': 'About Partners Text', 'page': 'about', 'type': 'text' },
            'about_cta_title': { 'key': 'about_cta_title', 'value': 'Need help or ready to partner?', 'label': 'About CTA Title', 'page': 'about', 'type': 'heading' },
            'about_cta_text': { 'key': 'about_cta_text', 'value': 'Reach out any time. Your call or message could change a life.', 'label': 'About CTA Text', 'page': 'about', 'type': 'text' },

            # About Page - Additional Content
            # Hero Section Right Column
            'about_hero_right_column': { 'key': 'about_hero_right_column', 'value': 'Every Voice Matters', 'label': 'About Hero Right Column', 'page': 'about', 'type': 'heading' },

            # Statistics Cards (Reach Across the Nation)
            'about_stats_title': { 'key': 'about_stats_title', 'value': 'Reach Across the Nation', 'label': 'About Statistics Title', 'page': 'about', 'type': 'heading' },
            'about_stats_stat_1_label': { 'key': 'about_stats_stat_1_label', 'value': 'Since', 'label': 'About Statistics Stat 1 Label', 'page': 'about', 'type': 'text' },
            'about_stats_stat_1_value': { 'key': 'about_stats_stat_1_value', 'value': 'Nov 2013', 'label': 'About Statistics Stat 1 Value', 'page': 'about', 'type': 'text' },
            'about_stats_stat_2_label': { 'key': 'about_stats_stat_2_label', 'value': 'Children Reached', 'label': 'About Statistics Stat 2 Label', 'page': 'about', 'type': 'text' },
            'about_stats_stat_2_value': { 'key': 'about_stats_stat_2_value', 'value': '2.7M+', 'label': 'About Statistics Stat 2 Value', 'page': 'about', 'type': 'text' },
            'about_stats_stat_3_label': { 'key': 'about_stats_stat_3_label', 'value': 'Cases Documented', 'label': 'About Statistics Stat 3 Label', 'page': 'about', 'type': 'text' },
            'about_stats_stat_3_value': { 'key': 'about_stats_stat_3_value', 'value': '40,000', 'label': 'About Statistics Stat 3 Value', 'page': 'about', 'type': 'text' },
            'about_stats_stat_4_label': { 'key': 'about_stats_stat_4_label', 'value': 'Compliance Rating', 'label': 'About Statistics Stat 4 Label', 'page': 'about', 'type': 'text' },
            'about_stats_stat_4_value': { 'key': 'about_stats_stat_4_value', 'value': '120/143', 'label': 'About Statistics Stat 4 Value', 'page': 'about', 'type': 'text' },
            'about_stats_stat_5_label': { 'key': 'about_stats_stat_5_label', 'value': 'Monthly Calls', 'label': 'About Statistics Stat 5 Label', 'page': 'about', 'type': 'text' },
            'about_stats_stat_5_value': { 'key': 'about_stats_stat_5_value', 'value': '1500-2000', 'label': 'About Statistics Stat 5 Value', 'page': 'about', 'type': 'text' },
            'about_stats_stat_6_label': { 'key': 'about_stats_stat_6_label', 'value': 'Partner Organizations', 'label': 'About Statistics Stat 6 Label', 'page': 'about', 'type': 'text' },
            'about_stats_stat_6_value': { 'key': 'about_stats_stat_6_value', 'value': '50+', 'label': 'About Statistics Stat 6 Value', 'page': 'about', 'type': 'text' },

            # Resolution Section
            'about_resolution_subtitle': { 'key': 'about_resolution_subtitle', 'value': 'How we ensure every case leads to safety', 'label': 'About Resolution Subtitle', 'page': 'about', 'type': 'text' },
            'about_resolution_central_goal': { 'key': 'about_resolution_central_goal', 'value': 'Safe Child', 'label': 'About Resolution Central Goal', 'page': 'about', 'type': 'heading' },
            'about_resolution_central_text': { 'key': 'about_resolution_central_text', 'value': 'Our Goal', 'label': 'About Resolution Central Text', 'page': 'about', 'type': 'text' },
            'about_resolution_mobile_goal_text': { 'key': 'about_resolution_mobile_goal_text', 'value': 'The ultimate goal of our journey.', 'label': 'About Resolution Mobile Goal Text', 'page': 'about', 'type': 'text' },

            # Core Values Stats
            'about_values_stat_1_value': { 'key': 'about_values_stat_1_value', 'value': '10+', 'label': 'About Values Stat 1 Value', 'page': 'about', 'type': 'text' },
            'about_values_stat_1_label': { 'key': 'about_values_stat_1_label', 'value': 'Years of Service', 'label': 'About Values Stat 1 Label', 'page': 'about', 'type': 'text' },
            'about_values_stat_2_value': { 'key': 'about_values_stat_2_value', 'value': '1M+', 'label': 'About Values Stat 2 Value', 'page': 'about', 'type': 'text' },
            'about_values_stat_2_label': { 'key': 'about_values_stat_2_label', 'value': 'Lives Touched', 'label': 'About Values Stat 2 Label', 'page': 'about', 'type': 'text' },

            # Operations Page - Hero Section
            'operations_page_title': { 'key': 'operations_page_title', 'value': 'How We', 'label': 'Operations Page Title', 'page': 'operations', 'type': 'heading', 'description': 'Hero section main title' },
            'operations_page_title_highlight': { 'key': 'operations_page_title_highlight', 'value': 'Operate', 'label': 'Operations Page Title Highlight', 'page': 'operations', 'type': 'heading', 'description': 'Hero section highlighted word' },
            'operations_page_subtitle': { 'key': 'operations_page_subtitle', 'value': 'Sauti is a Swahili word that means voice. Discover how we serve every citizen across Uganda 24/7.', 'label': 'Operations Page Subtitle', 'page': 'operations', 'type': 'text', 'description': 'Hero section subtitle text' },

            # Operations Page - Journey of a Voice Section
            'operations_journey_title': { 'key': 'operations_journey_title', 'value': 'The Journey of a', 'label': 'Operations Journey Title', 'page': 'operations', 'type': 'heading', 'description': 'Journey section title' },
            'operations_journey_title_highlight': { 'key': 'operations_journey_title_highlight', 'value': 'Voice', 'label': 'Operations Journey Title Highlight', 'page': 'operations', 'type': 'heading', 'description': 'Journey section highlighted word' },
            'operations_journey_subtitle': { 'key': 'operations_journey_subtitle', 'value': 'Every call goes through a carefully designed process to ensure the best possible outcome', 'label': 'Operations Journey Subtitle', 'page': 'operations', 'type': 'text', 'description': 'Journey section subtitle' },

            # Journey Step 1 - Access
            'operations_journey_step1_label': { 'key': 'operations_journey_step1_label', 'value': 'Step 1', 'label': 'Journey Step 1 Label', 'page': 'operations', 'type': 'text', 'description': 'Step 1 label' },
            'operations_journey_step1_title': { 'key': 'operations_journey_step1_title', 'value': 'Access', 'label': 'Journey Step 1 Title', 'page': 'operations', 'type': 'heading', 'description': 'Step 1 title' },
            'operations_journey_step1_description': { 'key': 'operations_journey_step1_description', 'value': 'Toll-free 116 available 24/7 from any network across Uganda.', 'label': 'Journey Step 1 Description', 'page': 'operations', 'type': 'text', 'description': 'Step 1 description' },

            # Journey Step 2 - Response
            'operations_journey_step2_label': { 'key': 'operations_journey_step2_label', 'value': 'Step 2', 'label': 'Journey Step 2 Label', 'page': 'operations', 'type': 'text', 'description': 'Step 2 label' },
            'operations_journey_step2_title': { 'key': 'operations_journey_step2_title', 'value': 'Response', 'label': 'Journey Step 2 Title', 'page': 'operations', 'type': 'heading', 'description': 'Step 2 title' },
            'operations_journey_step2_description': { 'key': 'operations_journey_step2_description', 'value': 'Professional counselors responding in 26 local languages.', 'label': 'Journey Step 2 Description', 'page': 'operations', 'type': 'text', 'description': 'Step 2 description' },

            # Journey Step 3 - Management
            'operations_journey_step3_label': { 'key': 'operations_journey_step3_label', 'value': 'Step 3', 'label': 'Journey Step 3 Label', 'page': 'operations', 'type': 'text', 'description': 'Step 3 label' },
            'operations_journey_step3_title': { 'key': 'operations_journey_step3_title', 'value': 'Management', 'label': 'Journey Step 3 Title', 'page': 'operations', 'type': 'heading', 'description': 'Step 3 title' },
            'operations_journey_step3_description': { 'key': 'operations_journey_step3_description', 'value': 'Case follow-up and specialized support coordination.', 'label': 'Journey Step 3 Description', 'page': 'operations', 'type': 'text', 'description': 'Step 3 description' },

            # Journey Step 4 - Protection
            'operations_journey_step4_label': { 'key': 'operations_journey_step4_label', 'value': 'Step 4', 'label': 'Journey Step 4 Label', 'page': 'operations', 'type': 'text', 'description': 'Step 4 label' },
            'operations_journey_step4_title': { 'key': 'operations_journey_step4_title', 'value': 'Protection', 'label': 'Journey Step 4 Title', 'page': 'operations', 'type': 'heading', 'description': 'Step 4 title' },
            'operations_journey_step4_description': { 'key': 'operations_journey_step4_description', 'value': 'Resolution and community reintegration support.', 'label': 'Journey Step 4 Description', 'page': 'operations', 'type': 'text', 'description': 'Step 4 description' },

            # Operations Page - Infrastructure Section
            'operations_infra_badge': { 'key': 'operations_infra_badge', 'value': 'Our Foundation', 'label': 'Infrastructure Badge', 'page': 'operations', 'type': 'text', 'description': 'Infrastructure section badge text' },
            'operations_infra_title': { 'key': 'operations_infra_title', 'value': 'A Robust Infrastructure for', 'label': 'Infrastructure Title', 'page': 'operations', 'type': 'heading', 'description': 'Infrastructure section title' },
            'operations_infra_title_highlight': { 'key': 'operations_infra_title_highlight', 'value': 'Nationwide Impact', 'label': 'Infrastructure Title Highlight', 'page': 'operations', 'type': 'heading', 'description': 'Infrastructure section highlighted text' },
            'operations_infra_description': { 'key': 'operations_infra_description', 'value': 'Our operations are built on sustainable pillars that ensure every caller receives expert attention, no matter where they are in Uganda.', 'label': 'Infrastructure Description', 'page': 'operations', 'type': 'text', 'description': 'Infrastructure section description' },

            # Infrastructure Stats
            'operations_infra_stat1_value': { 'key': 'operations_infra_stat1_value', 'value': '26', 'label': 'Infrastructure Stat 1 Value', 'page': 'operations', 'type': 'text', 'description': 'First stat value (Languages)' },
            'operations_infra_stat1_label': { 'key': 'operations_infra_stat1_label', 'value': 'Languages', 'label': 'Infrastructure Stat 1 Label', 'page': 'operations', 'type': 'text', 'description': 'First stat label' },
            'operations_infra_stat2_value': { 'key': 'operations_infra_stat2_value', 'value': '24/7', 'label': 'Infrastructure Stat 2 Value', 'page': 'operations', 'type': 'text', 'description': 'Second stat value (Availability)' },
            'operations_infra_stat2_label': { 'key': 'operations_infra_stat2_label', 'value': 'Available', 'label': 'Infrastructure Stat 2 Label', 'page': 'operations', 'type': 'text', 'description': 'Second stat label' },
            'operations_infra_stat3_value': { 'key': 'operations_infra_stat3_value', 'value': '100%', 'label': 'Infrastructure Stat 3 Value', 'page': 'operations', 'type': 'text', 'description': 'Third stat value (Coverage)' },
            'operations_infra_stat3_label': { 'key': 'operations_infra_stat3_label', 'value': 'Coverage', 'label': 'Infrastructure Stat 3 Label', 'page': 'operations', 'type': 'text', 'description': 'Third stat label' },

            # Infrastructure Pillars
            'operations_pillar1_title': { 'key': 'operations_pillar1_title', 'value': '26 Local Languages', 'label': 'Pillar 1 Title', 'page': 'operations', 'type': 'heading', 'description': 'First pillar title' },
            'operations_pillar1_description': { 'key': 'operations_pillar1_description', 'value': 'Bridging the communication gap for every community in Uganda.', 'label': 'Pillar 1 Description', 'page': 'operations', 'type': 'text', 'description': 'First pillar description' },
            'operations_pillar2_title': { 'key': 'operations_pillar2_title', 'value': '24/7 Availability', 'label': 'Pillar 2 Title', 'page': 'operations', 'type': 'heading', 'description': 'Second pillar title' },
            'operations_pillar2_description': { 'key': 'operations_pillar2_description', 'value': 'Support is always just a phone call away, day or night.', 'label': 'Pillar 2 Description', 'page': 'operations', 'type': 'text', 'description': 'Second pillar description' },
            'operations_pillar3_title': { 'key': 'operations_pillar3_title', 'value': 'Sustainable Funding', 'label': 'Pillar 3 Title', 'page': 'operations', 'type': 'heading', 'description': 'Third pillar title' },
            'operations_pillar3_description': { 'key': 'operations_pillar3_description', 'value': 'Partnering with MGLSD and UNICEF for long-term service stability.', 'label': 'Pillar 3 Description', 'page': 'operations', 'type': 'text', 'description': 'Third pillar description' },

            # Operations Page - Key Facts Section
            'operations_key_facts_title': { 'key': 'operations_key_facts_title', 'value': 'Operations at a', 'label': 'Key Facts Title', 'page': 'operations', 'type': 'heading', 'description': 'Key facts section title' },
            'operations_key_facts_title_highlight': { 'key': 'operations_key_facts_title_highlight', 'value': 'Glance', 'label': 'Key Facts Title Highlight', 'page': 'operations', 'type': 'heading', 'description': 'Key facts section highlighted word' },
            'operations_page_description': { 'key': 'operations_page_description', 'value': 'Our comprehensive case management system ensures every report is handled with care and urgency.', 'label': 'Operations Page Description', 'page': 'operations', 'type': 'text', 'description': 'Key facts section description' },
            'operations_availability_title': { 'key': 'operations_availability_title', 'value': '24/7 Nationwide Coverage', 'label': 'Operations Availability Title', 'page': 'operations', 'type': 'heading', 'description': 'Key fact: availability' },
            'operations_availability_text': { 'key': 'operations_availability_text', 'value': 'Operational 24/7 and accessible from every part of the country.', 'label': 'Operations Availability Text', 'page': 'operations', 'type': 'text', 'description': 'Key fact: availability' },
            'operations_funding_title': { 'key': 'operations_funding_title', 'value': 'Funding & Support', 'label': 'Operations Funding Title', 'page': 'operations', 'type': 'heading', 'description': 'Key fact: funding' },
            'operations_funding_text': { 'key': 'operations_funding_text', 'value': 'Government of Uganda covers utility bills and 14% of salaries, while donors (UNICEF) support case management funds and project staff salaries.', 'label': 'Operations Funding Text', 'page': 'operations', 'type': 'text', 'description': 'Key fact: funding' },
            'operations_languages_title': { 'key': 'operations_languages_title', 'value': 'Multilingual Counselors', 'label': 'Operations Languages Title', 'page': 'operations', 'type': 'heading', 'description': 'Key fact: languages' },
            'operations_languages_text': { 'key': 'operations_languages_text', 'value': 'Our counselors speak a total of 26 local languages to serve every community.', 'label': 'Operations Languages Text', 'page': 'operations', 'type': 'text', 'description': 'Key fact: languages' },
            'operations_shortcode_title': { 'key': 'operations_shortcode_title', 'value': 'Toll-Free Access', 'label': 'Operations Shortcode Title', 'page': 'operations', 'type': 'heading', 'description': 'Key fact: shortcode' },
            'operations_shortcode_text': { 'key': 'operations_shortcode_text', 'value': 'Operates on the short code 116 (toll free) accessible from any telecom network.', 'label': 'Operations Shortcode Text', 'page': 'operations', 'type': 'text', 'description': 'Key fact: shortcode' },
            'operations_structure_title': { 'key': 'operations_structure_title', 'value': 'Two-Division Structure', 'label': 'Operations Structure Title', 'page': 'operations', 'type': 'heading', 'description': 'Key fact: structure' },
            'operations_structure_text': { 'key': 'operations_structure_text', 'value': 'Divided into 2 sections: call center for immediate response and case work for follow-up support.', 'label': 'Operations Structure Text', 'page': 'operations', 'type': 'text', 'description': 'Key fact: structure' },

            # Operations Page - Services Section
            'services_section_title': { 'key': 'services_section_title', 'value': 'Services We', 'label': 'Services Section Title', 'page': 'operations', 'type': 'heading', 'description': 'Services carousel title' },
            'services_section_title_highlight': { 'key': 'services_section_title_highlight', 'value': 'Offer', 'label': 'Services Section Title Highlight', 'page': 'operations', 'type': 'heading', 'description': 'Services carousel title highlighted word' },
            'services_section_subtitle': { 'key': 'services_section_subtitle', 'value': 'Comprehensive support systems protecting and empowering every voice in Uganda.', 'label': 'Services Section Subtitle', 'page': 'operations', 'type': 'text', 'description': 'Services carousel subtitle' },

            # Service Items (titles and descriptions)
            'service_counseling_title': { 'key': 'service_counseling_title', 'value': 'Telephone Counseling', 'label': 'Service Counseling Title', 'page': 'operations', 'type': 'heading', 'description': 'Telephone counseling service title' },
            'service_counseling_text': { 'key': 'service_counseling_text', 'value': 'Professional counseling services available 24/7 through our toll-free helpline 116.', 'label': 'Service Counseling Text', 'page': 'operations', 'type': 'text', 'description': 'Telephone counseling service description' },
            'service_walkin_title': { 'key': 'service_walkin_title', 'value': 'Walk-In Support', 'label': 'Service Walk-In Title', 'page': 'operations', 'type': 'heading', 'description': 'Walk-in support service title' },
            'service_walkin_text': { 'key': 'service_walkin_text', 'value': 'Handle walk-in clients at our offices for face-to-face consultation and support.', 'label': 'Service Walk-In Text', 'page': 'operations', 'type': 'text', 'description': 'Walk-in support service description' },
            'service_media_title': { 'key': 'service_media_title', 'value': 'Media Response', 'label': 'Service Media Title', 'page': 'operations', 'type': 'heading', 'description': 'Media response service title' },
            'service_media_text': { 'key': 'service_media_text', 'value': 'Respond to cases of violence against children and gender-based violence reported through media and U-report.', 'label': 'Service Media Text', 'page': 'operations', 'type': 'text', 'description': 'Media response service description' },
            'service_guidance_title': { 'key': 'service_guidance_title', 'value': 'Information & Guidance', 'label': 'Service Guidance Title', 'page': 'operations', 'type': 'heading', 'description': 'Guidance service title' },
            'service_guidance_text': { 'key': 'service_guidance_text', 'value': 'Provision of information and guidance on child care and protection matters.', 'label': 'Service Guidance Text', 'page': 'operations', 'type': 'text', 'description': 'Guidance service description' },
            'service_referral_title': { 'key': 'service_referral_title', 'value': 'Essential Service Referrals', 'label': 'Service Referral Title', 'page': 'operations', 'type': 'heading', 'description': 'Referral service title' },
            'service_referral_text': { 'key': 'service_referral_text', 'value': 'Referral to essential services including healthcare, legal aid, and social support.', 'label': 'Service Referral Text', 'page': 'operations', 'type': 'text', 'description': 'Referral service description' },
            'service_community_title': { 'key': 'service_community_title', 'value': 'Community Sensitization', 'label': 'Service Community Title', 'page': 'operations', 'type': 'heading', 'description': 'Community service title' },
            'service_community_text': { 'key': 'service_community_text', 'value': 'Community sensitization activities to raise awareness about child protection and GBV prevention.', 'label': 'Service Community Text', 'page': 'operations', 'type': 'text', 'description': 'Community service description' },
            'service_chatbot_title': { 'key': 'service_chatbot_title', 'value': 'MHPSS Chatbot', 'label': 'Service Chatbot Title', 'page': 'operations', 'type': 'heading', 'description': 'Chatbot service title' },
            'service_chatbot_text': { 'key': 'service_chatbot_text', 'value': 'Mental Health and Psychosocial Support chatbot for immediate automated assistance.', 'label': 'Service Chatbot Text', 'page': 'operations', 'type': 'text', 'description': 'Chatbot service description' },

            # Resources Page Content
            'resources_title': { 'key': 'resources_title', 'value': 'Resources & Statistics', 'label': 'Resources Title', 'page': 'resources', 'type': 'heading' },
            'resources_subtitle': { 'key': 'resources_subtitle', 'value': 'Real-time insights from case reports and downloadable resources to support communities', 'label': 'Resources Subtitle', 'page': 'resources', 'type': 'text' },
            'resources_stats_title': { 'key': 'resources_stats_title', 'value': 'Case Report Statistics', 'label': 'Resources Stats Title', 'page': 'resources', 'type': 'heading' },
            'resources_stats_updated': { 'key': 'resources_stats_updated', 'value': 'Updated in real-time', 'label': 'Resources Stats Updated', 'page': 'resources', 'type': 'text' },
            'resources_stats_loading': { 'key': 'resources_stats_loading', 'value': 'Loading statistics...', 'label': 'Resources Stats Loading', 'page': 'resources', 'type': 'text' },
            'resources_stats_error': { 'key': 'resources_stats_error', 'value': 'Failed to load statistics. Please try again later.', 'label': 'Resources Stats Error', 'page': 'resources', 'type': 'text' },
            'resources_total_reports': { 'key': 'resources_total_reports', 'value': 'Total Reports', 'label': 'Resources Total Reports', 'page': 'resources', 'type': 'text' },
            'resources_child_protection': { 'key': 'resources_child_protection', 'value': 'Child Protection', 'label': 'Resources Child Protection', 'page': 'resources', 'type': 'text' },
            'resources_gbv_cases': { 'key': 'resources_gbv_cases', 'value': 'GBV Cases', 'label': 'Resources GBV Cases', 'page': 'resources', 'type': 'text' },
            'resources_migrant_worker': { 'key': 'resources_migrant_worker', 'value': 'Migrant Worker', 'label': 'Resources Migrant Worker', 'page': 'resources', 'type': 'text' },
            'resources_cases_by_category': { 'key': 'resources_cases_by_category', 'value': 'Cases by Category', 'label': 'Resources Cases by Category', 'page': 'resources', 'type': 'heading' },
            'resources_interactive': { 'key': 'resources_interactive', 'value': 'Interactive', 'label': 'Resources Interactive', 'page': 'resources', 'type': 'text' },
            'resources_reports_over_time': { 'key': 'resources_reports_over_time', 'value': 'Reports Over Time', 'label': 'Resources Reports Over Time', 'page': 'resources', 'type': 'heading' },
            'resources_last_6_months': { 'key': 'resources_last_6_months', 'value': 'Last 6 Months', 'label': 'Resources Last 6 Months', 'page': 'resources', 'type': 'text' },
            'resources_status_distribution': { 'key': 'resources_status_distribution', 'value': 'Report Status Distribution', 'label': 'Resources Status Distribution', 'page': 'resources', 'type': 'heading' },
            'resources_pending': { 'key': 'resources_pending', 'value': 'Pending', 'label': 'Resources Pending', 'page': 'resources', 'type': 'text' },
            'resources_in_progress': { 'key': 'resources_in_progress', 'value': 'In Progress', 'label': 'Resources In Progress', 'page': 'resources', 'type': 'text' },
            'resources_resolved': { 'key': 'resources_resolved', 'value': 'Resolved', 'label': 'Resources Resolved', 'page': 'resources', 'type': 'text' },
            'resources_closed': { 'key': 'resources_closed', 'value': 'Closed', 'label': 'Resources Closed', 'page': 'resources', 'type': 'text' },
            'resources_downloads_title': { 'key': 'resources_downloads_title', 'value': 'Downloadable Resources', 'label': 'Resources Downloads Title', 'page': 'resources', 'type': 'heading' },
            'resources_downloads_subtitle': { 'key': 'resources_downloads_subtitle', 'value': 'Guides, policies, and toolkits available in multiple languages', 'label': 'Resources Downloads Subtitle', 'page': 'resources', 'type': 'text' },
            'resources_available': { 'key': 'resources_available', 'value': 'resources available', 'label': 'Resources Available', 'page': 'resources', 'type': 'text' },
            'resources_search_placeholder': { 'key': 'resources_search_placeholder', 'value': 'Search resources by title or description...', 'label': 'Resources Search Placeholder', 'page': 'resources', 'type': 'text' },
            'resources_all_categories': { 'key': 'resources_all_categories', 'value': 'All Categories', 'label': 'Resources All Categories', 'page': 'resources', 'type': 'text' },
            'resources_all_languages': { 'key': 'resources_all_languages', 'value': 'All Languages', 'label': 'Resources All Languages', 'page': 'resources', 'type': 'text' },
            'resources_loading': { 'key': 'resources_loading', 'value': 'Loading resources...', 'label': 'Resources Loading', 'page': 'resources', 'type': 'text' },
            'resources_no_results': { 'key': 'resources_no_results', 'value': 'No resources found', 'label': 'Resources No Results', 'page': 'resources', 'type': 'text' },
            'resources_no_results_subtitle': { 'key': 'resources_no_results_subtitle', 'value': 'Try adjusting your search or filters', 'label': 'Resources No Results Subtitle', 'page': 'resources', 'type': 'text' },
            'resources_previous': { 'key': 'resources_previous', 'value': 'Previous', 'label': 'Resources Previous', 'page': 'resources', 'type': 'button' },
            'resources_next': { 'key': 'resources_next', 'value': 'Next', 'label': 'Resources Next', 'page': 'resources', 'type': 'button' },
            'resources_coming_soon': { 'key': 'resources_coming_soon', 'value': 'Coming Soon', 'label': 'Resources Coming Soon', 'page': 'resources', 'type': 'text' },

            # Reports & Insights Page Content
            'reports_insights_title': { 'key': 'reports_insights_title', 'value': 'Reports & Insights', 'label': 'Reports & Insights Title', 'page': 'reports_insights', 'type': 'heading' },
            'reports_insights_subtitle': { 'key': 'reports_insights_subtitle', 'value': 'Explore the data collected by Sauti Uganda 116 helpline to understand the trends and patterns in child abuse and neglect across the country.', 'label': 'Reports & Insights Subtitle', 'page': 'reports_insights', 'type': 'text' },
            'reports_insights_search_label': { 'key': 'reports_insights_search_label', 'value': 'Search', 'label': 'Reports & Insights Search Label', 'page': 'reports_insights', 'type': 'text' },
            'reports_insights_search_placeholder': { 'key': 'reports_insights_search_placeholder', 'value': 'Search reports by keyword', 'label': 'Reports & Insights Search Placeholder', 'page': 'reports_insights', 'type': 'text' },
            'reports_insights_region_label': { 'key': 'reports_insights_region_label', 'value': 'Region', 'label': 'Reports & Insights Region Label', 'page': 'reports_insights', 'type': 'text' },
            'reports_insights_all_regions': { 'key': 'reports_insights_all_regions', 'value': 'All Regions', 'label': 'Reports & Insights All Regions', 'page': 'reports_insights', 'type': 'text' },
            'reports_insights_apply_filters': { 'key': 'reports_insights_apply_filters', 'value': 'Apply Filters', 'label': 'Reports & Insights Apply Filters', 'page': 'reports_insights', 'type': 'button' },
            'reports_insights_date_range_placeholder': { 'key': 'reports_insights_date_range_placeholder', 'value': 'Date Range Picker (placeholder)', 'label': 'Reports & Insights Date Range Placeholder', 'page': 'reports_insights', 'type': 'text' },
            'reports_insights_cases_per_category': { 'key': 'reports_insights_cases_per_category', 'value': 'Cases Per Category', 'label': 'Reports & Insights Cases Per Category', 'page': 'reports_insights', 'type': 'heading' },
            'reports_insights_key_insights': { 'key': 'reports_insights_key_insights', 'value': 'Key Insights:', 'label': 'Reports & Insights Key Insights', 'page': 'reports_insights', 'type': 'text' },
            'reports_insights_child_neglect_stat': { 'key': 'reports_insights_child_neglect_stat', 'value': 'Child Neglect: 48.1% (2,746 cases)', 'label': 'Reports & Insights Child Neglect Stat', 'page': 'reports_insights', 'type': 'text' },
            'reports_insights_physical_violence_stat': { 'key': 'reports_insights_physical_violence_stat', 'value': 'Physical Violence: 17.0% (817 cases)', 'label': 'Reports & Insights Physical Violence Stat', 'page': 'reports_insights', 'type': 'text' },
            'reports_insights_sexual_violence_stat': { 'key': 'reports_insights_sexual_violence_stat', 'value': 'Sexual Violence: 14.7% (595 cases)', 'label': 'Reports & Insights Sexual Violence Stat', 'page': 'reports_insights', 'type': 'text' },
            'reports_insights_economic_violence_stat': { 'key': 'reports_insights_economic_violence_stat', 'value': 'Economic Violence: 5.0% (423 cases)', 'label': 'Reports & Insights Economic Violence Stat', 'page': 'reports_insights', 'type': 'text' },
            'reports_insights_summary_title': { 'key': 'reports_insights_summary_title', 'value': 'Summary', 'label': 'Reports & Insights Summary Title', 'page': 'reports_insights', 'type': 'heading' },
            'reports_insights_summary_paragraph_1': { 'key': 'reports_insights_summary_paragraph_1', 'value': 'Child Neglect remains the highest reported category, accounting for 48.1% of all cases (2,746 cases). This reflects the critical need for child protection services and support systems.', 'label': 'Reports & Insights Summary Paragraph 1', 'page': 'reports_insights', 'type': 'text' },
            'reports_insights_summary_paragraph_2': { 'key': 'reports_insights_summary_paragraph_2', 'value': 'Physical Violence follows at 17.0% (817 cases), while Sexual Violence represents 14.7% (595 cases), highlighting the urgent need for comprehensive protection services.', 'label': 'Reports & Insights Summary Paragraph 2', 'page': 'reports_insights', 'type': 'text' },
            'reports_insights_summary_paragraph_3': { 'key': 'reports_insights_summary_paragraph_3', 'value': 'These trends indicate the importance of continued awareness campaigns and accessible reporting mechanisms across all regions of Uganda.', 'label': 'Reports & Insights Summary Paragraph 3', 'page': 'reports_insights', 'type': 'text' },
            'reports_insights_cases_per_region': { 'key': 'reports_insights_cases_per_region', 'value': 'Cases Per Region', 'label': 'Reports & Insights Cases Per Region', 'page': 'reports_insights', 'type': 'heading' },
            'reports_insights_date_range': { 'key': 'reports_insights_date_range', 'value': '01/01/2025 12:00 AM - 31/12/2025 12:00 AM', 'label': 'Reports & Insights Date Range', 'page': 'reports_insights', 'type': 'text' },
            'reports_insights_regions_label': { 'key': 'reports_insights_regions_label', 'value': 'Regions:', 'label': 'Reports & Insights Regions Label', 'page': 'reports_insights', 'type': 'text' },
            'reports_insights_region_central': { 'key': 'reports_insights_region_central', 'value': 'Central', 'label': 'Reports & Insights Region Central', 'page': 'reports_insights', 'type': 'text' },
            'reports_insights_region_eastern': { 'key': 'reports_insights_region_eastern', 'value': 'Eastern', 'label': 'Reports & Insights Region Eastern', 'page': 'reports_insights', 'type': 'text' },
            'reports_insights_region_northern': { 'key': 'reports_insights_region_northern', 'value': 'Northern', 'label': 'Reports & Insights Region Northern', 'page': 'reports_insights', 'type': 'text' },
            'reports_insights_region_western': { 'key': 'reports_insights_region_western', 'value': 'Western', 'label': 'Reports & Insights Region Western', 'page': 'reports_insights', 'type': 'text' },
            'reports_insights_region_international': { 'key': 'reports_insights_region_international', 'value': 'International', 'label': 'Reports & Insights Region International', 'page': 'reports_insights', 'type': 'text' },
            'reports_insights_region_unknown': { 'key': 'reports_insights_region_unknown', 'value': 'Unknown', 'label': 'Reports & Insights Region Unknown', 'page': 'reports_insights', 'type': 'text' },
            'reports_insights_regional_trends': { 'key': 'reports_insights_regional_trends', 'value': 'Regional Trends', 'label': 'Reports & Insights Regional Trends', 'page': 'reports_insights', 'type': 'heading' },
            'reports_insights_regional_trends_paragraph_1': { 'key': 'reports_insights_regional_trends_paragraph_1', 'value': 'Central region consistently reports the highest number of cases throughout the year, with peaks in May (470 cases) and April (330 cases).', 'label': 'Reports & Insights Regional Trends Paragraph 1', 'page': 'reports_insights', 'type': 'text' },
            'reports_insights_regional_trends_paragraph_2': { 'key': 'reports_insights_regional_trends_paragraph_2', 'value': 'Eastern region shows steady reporting with 1,320 total cases, while Northern region has 650 cases, with notable spikes in May (290 cases) and October (170 cases).', 'label': 'Reports & Insights Regional Trends Paragraph 2', 'page': 'reports_insights', 'type': 'text' },
            'reports_insights_regional_trends_paragraph_3': { 'key': 'reports_insights_regional_trends_paragraph_3', 'value': 'This data helps guide resource allocation and targeted intervention programs across different regions.', 'label': 'Reports & Insights Regional Trends Paragraph 3', 'page': 'reports_insights', 'type': 'text' },
            'reports_insights_case_categories_per_age_group': { 'key': 'reports_insights_case_categories_per_age_group', 'value': 'Case Categories per Age Group', 'label': 'Reports & Insights Case Categories Per Age Group', 'page': 'reports_insights', 'type': 'heading' },
            'reports_insights_age_groups_label': { 'key': 'reports_insights_age_groups_label', 'value': 'Age Groups:', 'label': 'Reports & Insights Age Groups Label', 'page': 'reports_insights', 'type': 'text' },
            'reports_insights_age_group_04': { 'key': 'reports_insights_age_group_04', 'value': '0-04', 'label': 'Reports & Insights Age Group 0-4', 'page': 'reports_insights', 'type': 'text' },
            'reports_insights_age_group_0509': { 'key': 'reports_insights_age_group_0509', 'value': '05-09', 'label': 'Reports & Insights Age Group 05-09', 'page': 'reports_insights', 'type': 'text' },
            'reports_insights_age_group_1013': { 'key': 'reports_insights_age_group_1013', 'value': '10-13', 'label': 'Reports & Insights Age Group 10-13', 'page': 'reports_insights', 'type': 'text' },
            'reports_insights_age_group_1417': { 'key': 'reports_insights_age_group_1417', 'value': '14-17', 'label': 'Reports & Insights Age Group 14-17', 'page': 'reports_insights', 'type': 'text' },
            'reports_insights_age_group_1824': { 'key': 'reports_insights_age_group_1824', 'value': '18-24', 'label': 'Reports & Insights Age Group 18-24', 'page': 'reports_insights', 'type': 'text' },
            'reports_insights_age_group_2530': { 'key': 'reports_insights_age_group_2530', 'value': '25-30', 'label': 'Reports & Insights Age Group 25-30', 'page': 'reports_insights', 'type': 'text' },
            'reports_insights_age_group_3145': { 'key': 'reports_insights_age_group_3145', 'value': '31-45', 'label': 'Reports & Insights Age Group 31-45', 'page': 'reports_insights', 'type': 'text' },
            'reports_insights_age_group_above_60': { 'key': 'reports_insights_age_group_above_60', 'value': 'Above 60', 'label': 'Reports & Insights Age Group Above 60', 'page': 'reports_insights', 'type': 'text' },
            'reports_insights_age_group_unknown': { 'key': 'reports_insights_age_group_unknown', 'value': 'Unknown', 'label': 'Reports & Insights Age Group Unknown', 'page': 'reports_insights', 'type': 'text' },
            'reports_insights_case_categories_per_gender': { 'key': 'reports_insights_case_categories_per_gender', 'value': 'Case Categories per Gender', 'label': 'Reports & Insights Case Categories Per Gender', 'page': 'reports_insights', 'type': 'heading' },
            'reports_insights_gender_breakdown_label': { 'key': 'reports_insights_gender_breakdown_label', 'value': 'Gender Breakdown:', 'label': 'Reports & Insights Gender Breakdown Label', 'page': 'reports_insights', 'type': 'text' },
            'reports_insights_gender_female': { 'key': 'reports_insights_gender_female', 'value': 'Female', 'label': 'Reports & Insights Gender Female', 'page': 'reports_insights', 'type': 'text' },
            'reports_insights_gender_male': { 'key': 'reports_insights_gender_male', 'value': 'Male', 'label': 'Reports & Insights Gender Male', 'page': 'reports_insights', 'type': 'text' },
            'reports_insights_gender_unknown': { 'key': 'reports_insights_gender_unknown', 'value': 'Unknown', 'label': 'Reports & Insights Gender Unknown', 'page': 'reports_insights', 'type': 'text' },
            'reports_insights_privacy_policy': { 'key': 'reports_insights_privacy_policy', 'value': 'Privacy Policy', 'label': 'Reports & Insights Privacy Policy', 'page': 'reports_insights', 'type': 'button' },
            'reports_insights_terms_of_service': { 'key': 'reports_insights_terms_of_service', 'value': 'Terms of Service', 'label': 'Reports & Insights Terms of Service', 'page': 'reports_insights', 'type': 'button' },
            'reports_insights_contact_us': { 'key': 'reports_insights_contact_us', 'value': 'Contact Us', 'label': 'Reports & Insights Contact Us', 'page': 'reports_insights', 'type': 'button' },
            'reports_insights_footer_text': { 'key': 'reports_insights_footer_text', 'value': '© 2024 Sauti Uganda 116 helpline. All rights reserved.', 'label': 'Reports & Insights Footer Text', 'page': 'reports_insights', 'type': 'text' },

            # Videos Page Content
            'videos_page_title': { 'key': 'videos_page_title', 'value': 'Video Gallery', 'label': 'Videos Page Title', 'page': 'videos', 'type': 'heading', 'description': 'Hero section main title' },
            'videos_page_title_highlight': { 'key': 'videos_page_title_highlight', 'value': 'Audio-Visuals', 'label': 'Videos Page Title Highlight', 'page': 'videos', 'type': 'heading', 'description': 'Hero section highlighted word' },
            'videos_page_description': { 'key': 'videos_page_description', 'value': 'Explore our archive of official media content, awareness videos, and community stories.', 'label': 'Videos Page Description', 'page': 'videos', 'type': 'text', 'description': 'Hero section subtitle text' },
            'videos_search_heading': { 'key': 'videos_search_heading', 'value': 'Search Official Media', 'label': 'Videos Search Heading', 'page': 'videos', 'type': 'heading', 'description': 'Heading above the search bar' },
            'videos_search_placeholder': { 'key': 'videos_search_placeholder', 'value': 'Search videos...', 'label': 'Videos Search Placeholder', 'page': 'videos', 'type': 'text' },
            'videos_search_button': { 'key': 'videos_search_button', 'value': 'Search', 'label': 'Videos Search Button', 'page': 'videos', 'type': 'button' },
            'videos_section_title': { 'key': 'videos_section_title', 'value': 'Videos', 'label': 'Videos Section Title', 'page': 'videos', 'type': 'heading', 'description': 'Heading above the video grid' },
            'videos_audio_section_title': { 'key': 'videos_audio_section_title', 'value': 'Audio', 'label': 'Videos Audio Section Title', 'page': 'videos', 'type': 'heading', 'description': 'Heading above the audio list' },

            # FAQs Page Content
            'faqs_support_title': { 'key': 'faqs_support_title', 'value': '24/7 Support', 'label': 'FAQs Support Title', 'page': 'faqs', 'type': 'heading' },
            'faqs_support_subtitle': { 'key': 'faqs_support_subtitle', 'value': 'Always here to help', 'label': 'FAQs Support Subtitle', 'page': 'faqs', 'type': 'text' },
            'faqs_quick_response_title': { 'key': 'faqs_quick_response_title', 'value': 'Quick Response', 'label': 'FAQs Quick Response Title', 'page': 'faqs', 'type': 'heading' },
            'faqs_quick_response_subtitle': { 'key': 'faqs_quick_response_subtitle', 'value': 'Get help immediately', 'label': 'FAQs Quick Response Subtitle', 'page': 'faqs', 'type': 'text' },
            'faqs_quick_response_text': { 'key': 'faqs_quick_response_text', 'value': 'Our trained counselors are available 24/7 to provide immediate support and guidance.', 'label': 'FAQs Quick Response Text', 'page': 'faqs', 'type': 'text' },
            'faqs_immediate_help_title': { 'key': 'faqs_immediate_help_title', 'value': 'Need Immediate Help?', 'label': 'FAQs Immediate Help Title', 'page': 'faqs', 'type': 'heading' },
            'faqs_immediate_help_subtitle': { 'key': 'faqs_immediate_help_subtitle', 'value': 'Call our toll-free helpline', 'label': 'FAQs Immediate Help Subtitle', 'page': 'faqs', 'type': 'text' },
            'faqs_call_button': { 'key': 'faqs_call_button', 'value': 'Call 116', 'label': 'FAQs Call Button', 'page': 'faqs', 'type': 'button' },
            'faqs_page_title': { 'key': 'faqs_page_title', 'value': 'Frequently Asked', 'label': 'FAQs Page Title', 'page': 'faqs', 'type': 'heading' },
            'faqs_page_title_highlight': { 'key': 'faqs_page_title_highlight', 'value': 'Questions', 'label': 'FAQs Page Title Highlight', 'page': 'faqs', 'type': 'heading' },
            'faqs_page_subtitle': { 'key': 'faqs_page_subtitle', 'value': 'Questions & Answers', 'label': 'FAQs Page Subtitle', 'page': 'faqs', 'type': 'heading' },
            'faqs_search_placeholder': { 'key': 'faqs_search_placeholder', 'value': 'Search questions', 'label': 'FAQs Search Placeholder', 'page': 'faqs', 'type': 'text' },
            'faqs_all_categories_button': { 'key': 'faqs_all_categories_button', 'value': 'All Categories', 'label': 'FAQs All Categories Button', 'page': 'faqs', 'type': 'button' },
            'faqs_no_results': { 'key': 'faqs_no_results', 'value': 'No FAQs found', 'label': 'FAQs No Results', 'page': 'faqs', 'type': 'text' },
            'faqs_no_results_subtitle': { 'key': 'faqs_no_results_subtitle', 'value': 'Try adjusting your search or category filter', 'label': 'FAQs No Results Subtitle', 'page': 'faqs', 'type': 'text' },
            'faqs_privacy_policy': { 'key': 'faqs_privacy_policy', 'value': 'Privacy Policy', 'label': 'FAQs Privacy Policy', 'page': 'faqs', 'type': 'button' },
            'faqs_terms_of_service': { 'key': 'faqs_terms_of_service', 'value': 'Terms of Service', 'label': 'FAQs Terms of Service', 'page': 'faqs', 'type': 'button' },
            'faqs_contact_us': { 'key': 'faqs_contact_us', 'value': 'Contact Us', 'label': 'FAQs Contact Us', 'page': 'faqs', 'type': 'button' },
            'faqs_footer_text': { 'key': 'faqs_footer_text', 'value': '© 2024 Sauti Uganda. All rights reserved. A sanctuary for every child.', 'label': 'FAQs Footer Text', 'page': 'faqs', 'type': 'text' },

            # Header Navigation and CTAs
            'header_brand_name': { 'key': 'header_brand_name', 'value': 'Sauti 116 Helpline', 'label': 'Header Brand Name', 'page': 'header', 'type': 'text', 'description': 'Brand name displayed in the header' },
            'header_nav_home': { 'key': 'header_nav_home', 'value': 'Home', 'label': 'Header Nav Home', 'page': 'header', 'type': 'button', 'description': 'Home navigation link text' },
            'header_nav_about': { 'key': 'header_nav_about', 'value': 'Who We Are', 'label': 'Header Nav About', 'page': 'header', 'type': 'button', 'description': 'About navigation link text' },
            'header_nav_operations': { 'key': 'header_nav_operations', 'value': 'Our Operations', 'label': 'Header Nav Operations', 'page': 'header', 'type': 'button', 'description': 'Operations navigation link text' },
            'header_nav_resources': { 'key': 'header_nav_resources', 'value': 'Resources', 'label': 'Header Nav Resources', 'page': 'header', 'type': 'button', 'description': 'Resources navigation link text' },
            'header_nav_blog': { 'key': 'header_nav_blog', 'value': 'Blog', 'label': 'Header Nav Blog', 'page': 'header', 'type': 'button', 'description': 'Blog navigation link text' },
            'header_nav_news': { 'key': 'header_nav_news', 'value': 'News', 'label': 'Header Nav News', 'page': 'header', 'type': 'button', 'description': 'News navigation link text' },
            'header_nav_videos': { 'key': 'header_nav_videos', 'value': 'Videos', 'label': 'Header Nav Videos', 'page': 'header', 'type': 'button', 'description': 'Videos navigation link text' },
            'header_nav_partners': { 'key': 'header_nav_partners', 'value': 'Partners', 'label': 'Header Nav Partners', 'page': 'header', 'type': 'button', 'description': 'Partners navigation link text' },
            'header_nav_contact': { 'key': 'header_nav_contact', 'value': 'Contact', 'label': 'Header Nav Contact', 'page': 'header', 'type': 'button', 'description': 'Contact navigation link text' },
            'header_call_button': { 'key': 'header_call_button', 'value': 'Call 116', 'label': 'Header Call Button', 'page': 'header', 'type': 'button', 'description': 'Call CTA button text' },
            'header_report_button': { 'key': 'header_report_button', 'value': 'Report a case', 'label': 'Header Report Button', 'page': 'header', 'type': 'button', 'description': 'Report CTA button text' },

            # Footer Navigation and Social Links
            'footer_brand_name': { 'key': 'footer_brand_name', 'value': 'Sauti 116', 'label': 'Footer Brand Name', 'page': 'footer', 'type': 'text', 'description': 'Brand name displayed in the footer' },
            'footer_nav_home': { 'key': 'footer_nav_home', 'value': 'Home', 'label': 'Footer Nav Home', 'page': 'footer', 'type': 'button', 'description': 'Home footer link text' },
            'footer_nav_about': { 'key': 'footer_nav_about', 'value': 'About Us', 'label': 'Footer Nav About', 'page': 'footer', 'type': 'button', 'description': 'About footer link text' },
            'footer_nav_operations': { 'key': 'footer_nav_operations', 'value': 'Operations', 'label': 'Footer Nav Operations', 'page': 'footer', 'type': 'button', 'description': 'Operations footer link text' },
            'footer_nav_resources': { 'key': 'footer_nav_resources', 'value': 'Resources', 'label': 'Footer Nav Resources', 'page': 'footer', 'type': 'button', 'description': 'Resources footer link text' },
            'footer_nav_blog': { 'key': 'footer_nav_blog', 'value': 'Blog', 'label': 'Footer Nav Blog', 'page': 'footer', 'type': 'button', 'description': 'Blog footer link text' },
            'footer_nav_news': { 'key': 'footer_nav_news', 'value': 'News', 'label': 'Footer Nav News', 'page': 'footer', 'type': 'button', 'description': 'News footer link text' },
            'footer_nav_partners': { 'key': 'footer_nav_partners', 'value': 'Partners', 'label': 'Footer Nav Partners', 'page': 'footer', 'type': 'button', 'description': 'Partners footer link text' },
            'footer_nav_contact': { 'key': 'footer_nav_contact', 'value': 'Contact', 'label': 'Footer Nav Contact', 'page': 'footer', 'type': 'button', 'description': 'Contact footer link text' },
            'footer_social_x_url': { 'key': 'footer_social_x_url', 'value': 'https://x.com/sauti116?s=21', 'label': 'Footer X URL', 'page': 'footer', 'type': 'text', 'description': 'X/Twitter social media URL' },
            'footer_social_x_label': { 'key': 'footer_social_x_label', 'value': 'X', 'label': 'Footer X Label', 'page': 'footer', 'type': 'text', 'description': 'X/Twitter display name' },
            'footer_social_facebook_url': { 'key': 'footer_social_facebook_url', 'value': 'https://www.facebook.com/share/14W6eurox1o/', 'label': 'Footer Facebook URL', 'page': 'footer', 'type': 'text', 'description': 'Facebook social media URL' },
            'footer_social_facebook_label': { 'key': 'footer_social_facebook_label', 'value': 'Facebook', 'label': 'Footer Facebook Label', 'page': 'footer', 'type': 'text', 'description': 'Facebook display name' },
            'footer_social_instagram_url': { 'key': 'footer_social_instagram_url', 'value': 'https://www.instagram.com/sauti116helpline?igsh=MTdyNjgwOG42ZjB2dA%3D%3D&utm_source=qr', 'label': 'Footer Instagram URL', 'page': 'footer', 'type': 'text', 'description': 'Instagram social media URL' },
            'footer_social_instagram_label': { 'key': 'footer_social_instagram_label', 'value': 'Instagram', 'label': 'Footer Instagram Label', 'page': 'footer', 'type': 'text', 'description': 'Instagram display name' },
            'footer_social_youtube_url': { 'key': 'footer_social_youtube_url', 'value': 'https://www.youtube.com/@Sauti116HelplineUganda', 'label': 'Footer YouTube URL', 'page': 'footer', 'type': 'text', 'description': 'YouTube social media URL' },
            'footer_social_youtube_label': { 'key': 'footer_social_youtube_label', 'value': 'YouTube', 'label': 'Footer YouTube Label', 'page': 'footer', 'type': 'text', 'description': 'YouTube display name' },
            'footer_social_tiktok_url': { 'key': 'footer_social_tiktok_url', 'value': 'https://www.tiktok.com/@sauti116helplineuganda?_r=1&_t=ZS-952NtlMMSIs', 'label': 'Footer TikTok URL', 'page': 'footer', 'type': 'text', 'description': 'TikTok social media URL' },
            'footer_social_tiktok_label': { 'key': 'footer_social_tiktok_label', 'value': 'TikTok', 'label': 'Footer TikTok Label', 'page': 'footer', 'type': 'text', 'description': 'TikTok display name' },

            # Footer contact block (previously unseeded — the footer fell back to
            # hardcoded values, so admin edits could never reach it). The email
            # keys contain "_email_" so ContentManager surfaces them under its
            # footer "Contact Information" section.
            'footer_hotline_label': { 'key': 'footer_hotline_label', 'value': 'Toll Free', 'label': 'Footer Hotline Label', 'page': 'footer', 'type': 'text', 'description': 'Label above the footer hotline number' },
            'footer_hotline_number': { 'key': 'footer_hotline_number', 'value': 'Call 116', 'label': 'Footer Hotline Number', 'page': 'footer', 'type': 'text', 'description': 'Footer hotline number text' },
            'footer_email_label': { 'key': 'footer_email_label', 'value': 'Email Us', 'label': 'Footer Email Label', 'page': 'footer', 'type': 'text', 'description': 'Label above the footer email address' },
            'footer_email_address': { 'key': 'footer_email_address', 'value': 'info@sauti116.ug', 'label': 'Footer Email Address', 'page': 'footer', 'type': 'text', 'description': 'Contact email shown in the footer (edit here to update it site-wide)' },
            'footer_copyright': { 'key': 'footer_copyright', 'value': '© 2026 Sauti 116. Ministry of Gender, Labour and Social Development.', 'label': 'Footer Copyright', 'page': 'footer', 'type': 'text', 'description': 'Footer copyright line' },
            'footer_country_label': { 'key': 'footer_country_label', 'value': 'Uganda', 'label': 'Footer Country Label', 'page': 'footer', 'type': 'text', 'description': 'Country label in the footer bottom bar' },

            # Contact Page Form Text
            'contact_page_title': { 'key': 'contact_page_title', 'value': 'Get in', 'label': 'Contact Page Title', 'page': 'contact', 'type': 'heading', 'description': 'Contact page title prefix' },
            'contact_page_title_highlight': { 'key': 'contact_page_title_highlight', 'value': 'Touch', 'label': 'Contact Page Title Highlight', 'page': 'contact', 'type': 'heading', 'description': 'Contact page title highlight text' },
            'contact_page_description': { 'key': 'contact_page_description', 'value': 'Have a question or need to report a concern? Choose the channel that works best for you.', 'label': 'Contact Page Description', 'page': 'contact', 'type': 'text', 'description': 'Contact page subtitle' },
            'contact_channels_title': { 'key': 'contact_channels_title', 'value': 'Contact Channels', 'label': 'Contact Channels Title', 'page': 'contact', 'type': 'heading', 'description': 'Contact channels section title' },
            'contact_channels_description': { 'key': 'contact_channels_description', 'value': 'Choose the best way to reach us for your needs.', 'label': 'Contact Channels Description', 'page': 'contact', 'type': 'text', 'description': 'Contact channels section description' },
            'contact_fallback_email_title': { 'key': 'contact_fallback_email_title', 'value': 'Email Us', 'label': 'Contact Fallback Email Title', 'page': 'contact', 'type': 'heading', 'description': 'Fallback email card title' },
            'contact_fallback_email_description': { 'key': 'contact_fallback_email_description', 'value': 'For general inquiries and information.', 'label': 'Contact Fallback Email Description', 'page': 'contact', 'type': 'text', 'description': 'Fallback email card description' },
            'contact_fallback_email_address': { 'key': 'contact_fallback_email_address', 'value': 'info@sauti116.ug', 'label': 'Contact Fallback Email Address', 'page': 'contact', 'type': 'text', 'description': 'Fallback email address' },
            'contact_action_send_email': { 'key': 'contact_action_send_email', 'value': 'Send Email', 'label': 'Contact Send Email Action', 'page': 'contact', 'type': 'button', 'description': 'Send email action button text' },
            'contact_form_title': { 'key': 'contact_form_title', 'value': 'Send a Message', 'label': 'Contact Form Title', 'page': 'contact', 'type': 'heading', 'description': 'Contact form card title' },
            'contact_form_subtitle': { 'key': 'contact_form_subtitle', 'value': 'We typically respond within 24 hours.', 'label': 'Contact Form Subtitle', 'page': 'contact', 'type': 'text', 'description': 'Contact form card subtitle' },
            'contact_form_name_label': { 'key': 'contact_form_name_label', 'value': 'Your Name', 'label': 'Contact Form Name Label', 'page': 'contact', 'type': 'text', 'description': 'Name field label' },
            'contact_form_name_placeholder': { 'key': 'contact_form_name_placeholder', 'value': 'John Doe', 'label': 'Contact Form Name Placeholder', 'page': 'contact', 'type': 'text', 'description': 'Name field placeholder' },
            'contact_form_email_label': { 'key': 'contact_form_email_label', 'value': 'Email Address', 'label': 'Contact Form Email Label', 'page': 'contact', 'type': 'text', 'description': 'Email field label' },
            'contact_form_email_placeholder': { 'key': 'contact_form_email_placeholder', 'value': 'name@example.com', 'label': 'Contact Form Email Placeholder', 'page': 'contact', 'type': 'text', 'description': 'Email field placeholder' },
            'contact_form_message_label': { 'key': 'contact_form_message_label', 'value': 'How can we help?', 'label': 'Contact Form Message Label', 'page': 'contact', 'type': 'text', 'description': 'Message field label' },
            'contact_form_message_placeholder': { 'key': 'contact_form_message_placeholder', 'value': 'Type your message here...', 'label': 'Contact Form Message Placeholder', 'page': 'contact', 'type': 'text', 'description': 'Message field placeholder' },
            'contact_form_sending': { 'key': 'contact_form_sending', 'value': 'Sending...', 'label': 'Contact Form Sending', 'page': 'contact', 'type': 'text', 'description': 'Form submit button loading state' },
            'contact_form_submit': { 'key': 'contact_form_submit', 'value': 'Send Message', 'label': 'Contact Form Submit', 'page': 'contact', 'type': 'button', 'description': 'Form submit button text' },
            'contact_success_title': { 'key': 'contact_success_title', 'value': 'Message Sent!', 'label': 'Contact Success Title', 'page': 'contact', 'type': 'heading', 'description': 'Success message title' },
            'contact_success_message': { 'key': 'contact_success_message', 'value': 'Thank you for reaching out. We will get back to you shortly.', 'label': 'Contact Success Message', 'page': 'contact', 'type': 'text', 'description': 'Success message body' },
            'contact_send_another': { 'key': 'contact_send_another', 'value': 'Send another message', 'label': 'Contact Send Another', 'page': 'contact', 'type': 'button', 'description': 'Send another message link text' },
            'contact_trust_signal': { 'key': 'contact_trust_signal', 'value': 'Your communication is secure. This service is operated under the mandate of the Ministry of Gender, Labour and Social Development.', 'label': 'Contact Trust Signal', 'page': 'contact', 'type': 'text', 'description': 'Trust signal message' },

            # Partners Page Text
            'partners_page_title_prefix': { 'key': 'partners_page_title_prefix', 'value': 'Our', 'label': 'Partners Page Title Prefix', 'page': 'partners', 'type': 'heading', 'description': 'Partners page title prefix' },
            'partners_page_title_highlight': { 'key': 'partners_page_title_highlight', 'value': 'Partners', 'label': 'Partners Page Title Highlight', 'page': 'partners', 'type': 'heading', 'description': 'Partners page title highlight' },
            'partners_page_subtitle': { 'key': 'partners_page_subtitle', 'value': 'Working together with organizations committed to protecting children and vulnerable communities across Uganda.', 'label': 'Partners Page Subtitle', 'page': 'partners', 'type': 'text', 'description': 'Partners page subtitle' },
            'partners_glance_title': { 'key': 'partners_glance_title', 'value': 'Partnership at a Glance', 'label': 'Partners Glance Title', 'page': 'partners', 'type': 'heading', 'description': 'Partnership glance section title' },
            'partners_feature1_title': { 'key': 'partners_feature1_title', 'value': 'Official Network', 'label': 'Partners Feature 1 Title', 'page': 'partners', 'type': 'heading', 'description': 'First feature title' },
            'partners_feature1_description': { 'key': 'partners_feature1_description', 'value': 'Backed by the **Ministry of Gender, Labour and Social Development**.', 'label': 'Partners Feature 1 Description', 'page': 'partners', 'type': 'text', 'description': 'First feature description' },
            'partners_feature2_title': { 'key': 'partners_feature2_title', 'value': 'National Reach', 'label': 'Partners Feature 2 Title', 'page': 'partners', 'type': 'heading', 'description': 'Second feature title' },
            'partners_feature2_description': { 'key': 'partners_feature2_description', 'value': 'Connected to **over 50 NGOs** and international agencies.', 'label': 'Partners Feature 2 Description', 'page': 'partners', 'type': 'text', 'description': 'Second feature description' },
            'partners_feature3_title': { 'key': 'partners_feature3_title', 'value': 'Expert Support', 'label': 'Partners Feature 3 Title', 'page': 'partners', 'type': 'heading', 'description': 'Third feature title' },
            'partners_feature3_description': { 'key': 'partners_feature3_description', 'value': 'Collaborations with **UNICEF and local district leaders**.', 'label': 'Partners Feature 3 Description', 'page': 'partners', 'type': 'text', 'description': 'Third feature description' },
            'partners_directory_title': { 'key': 'partners_directory_title', 'value': 'Who We Work With', 'label': 'Partners Directory Title', 'page': 'partners', 'type': 'heading', 'description': 'Partner directory section title' },
            'partners_loading': { 'key': 'partners_loading', 'value': 'Loading partner organizations...', 'label': 'Partners Loading', 'page': 'partners', 'type': 'text', 'description': 'Loading message' },
            'partners_visit_site': { 'key': 'partners_visit_site', 'value': 'Visit official site →', 'label': 'Partners Visit Site', 'page': 'partners', 'type': 'button', 'description': 'Visit partner site link text' },
            'partners_empty_state': { 'key': 'partners_empty_state', 'value': 'No partners listed yet.', 'label': 'Partners Empty State', 'page': 'partners', 'type': 'text', 'description': 'Empty state message' },
            'partners_cta_title': { 'key': 'partners_cta_title', 'value': 'How We Work Together', 'label': 'Partners CTA Title', 'page': 'partners', 'type': 'heading', 'description': 'CTA section title' },
            'partners_cta_text': { 'key': 'partners_cta_text', 'value': 'Interested in joining our mission to protect the children of Uganda? We are always looking for organizations that share our commitment.', 'label': 'Partners CTA Text', 'page': 'partners', 'type': 'text', 'description': 'CTA section description' },
            'partners_cta_interest_button': { 'key': 'partners_cta_interest_button', 'value': 'Express Interest', 'label': 'Partners CTA Interest Button', 'page': 'partners', 'type': 'button', 'description': 'Express interest button text' },
            'partners_cta_learn_button': { 'key': 'partners_cta_learn_button', 'value': 'Learn About Our Impact', 'label': 'Partners CTA Learn Button', 'page': 'partners', 'type': 'button', 'description': 'Learn more button text' },

            # Resources Page - Additional Keys
            'resources_live_data_badge': { 'key': 'resources_live_data_badge', 'value': 'Live Data', 'label': 'Resources Live Data Badge', 'page': 'resources', 'type': 'text', 'description': 'Live data indicator badge' },
            'resources_filter_time_period': { 'key': 'resources_filter_time_period', 'value': 'Time Period', 'label': 'Resources Filter Time Period', 'page': 'resources', 'type': 'text', 'description': 'Time period filter label' },
            'resources_filter_region': { 'key': 'resources_filter_region', 'value': 'Region', 'label': 'Resources Filter Region', 'page': 'resources', 'type': 'text', 'description': 'Region filter label' },
            'resources_filter_case_type': { 'key': 'resources_filter_case_type', 'value': 'Case Type', 'label': 'Resources Filter Case Type', 'page': 'resources', 'type': 'text', 'description': 'Case type filter label' },
            'resources_filter_all': { 'key': 'resources_filter_all', 'value': 'All', 'label': 'Resources Filter All', 'page': 'resources', 'type': 'text', 'description': 'All filter option' },
            'resources_chart_gender_title': { 'key': 'resources_chart_gender_title', 'value': 'Cases by Gender', 'label': 'Resources Chart Gender Title', 'page': 'resources', 'type': 'heading', 'description': 'Gender chart title' },
            'resources_chart_gender_subtitle': { 'key': 'resources_chart_gender_subtitle', 'value': 'Distribution of reported cases by gender', 'label': 'Resources Chart Gender Subtitle', 'page': 'resources', 'type': 'text', 'description': 'Gender chart subtitle' },
            'resources_chart_age_title': { 'key': 'resources_chart_age_title', 'value': 'Age Distribution', 'label': 'Resources Chart Age Title', 'page': 'resources', 'type': 'heading', 'description': 'Age chart title' },
            'resources_chart_age_subtitle': { 'key': 'resources_chart_age_subtitle', 'value': 'Cases by age groups', 'label': 'Resources Chart Age Subtitle', 'page': 'resources', 'type': 'text', 'description': 'Age chart subtitle' },
            'resources_chart_region_title': { 'key': 'resources_chart_region_title', 'value': 'Regional Breakdown', 'label': 'Resources Chart Region Title', 'page': 'resources', 'type': 'heading', 'description': 'Region chart title' },
            'resources_chart_region_subtitle': { 'key': 'resources_chart_region_subtitle', 'value': 'Cases reported per region', 'label': 'Resources Chart Region Subtitle', 'page': 'resources', 'type': 'text', 'description': 'Region chart subtitle' },
            'resources_download': { 'key': 'resources_download', 'value': 'Download', 'label': 'Resources Download', 'page': 'resources', 'type': 'button', 'description': 'Download button text' },
            'resources_downloading': { 'key': 'resources_downloading', 'value': 'Downloading...', 'label': 'Resources Downloading', 'page': 'resources', 'type': 'text', 'description': 'Download button loading state' },
            'resources_page_title': { 'key': 'resources_page_title', 'value': 'Resources', 'label': 'Resources Page Title', 'page': 'resources', 'type': 'heading', 'description': 'Resources hero title prefix' },
            'resources_page_title_highlight': { 'key': 'resources_page_title_highlight', 'value': 'and Statistics', 'label': 'Resources Page Title Highlight', 'page': 'resources', 'type': 'heading', 'description': 'Resources hero title highlight' },
            'resources_page_subtitle': { 'key': 'resources_page_subtitle', 'value': 'Access our library of official reports, awareness materials, and real-time helpline statistics.', 'label': 'Resources Page Subtitle', 'page': 'resources', 'type': 'text', 'description': 'Resources hero subtitle' },
            'statistics_dashboard_title': { 'key': 'statistics_dashboard_title', 'value': 'Live Statistics', 'label': 'Statistics Dashboard Title', 'page': 'resources', 'type': 'heading', 'description': 'Statistics dashboard section title' },
            'statistics_dashboard_subtitle': { 'key': 'statistics_dashboard_subtitle', 'value': 'Real-time data from the Sauti 116 Helpline', 'label': 'Statistics Dashboard Subtitle', 'page': 'resources', 'type': 'text', 'description': 'Statistics dashboard section subtitle' },
            'stats_kpi_calls': { 'key': 'stats_kpi_calls', 'value': 'Total Calls', 'label': 'Stats KPI Calls', 'page': 'resources', 'type': 'text', 'description': 'Total calls KPI label' },
            'stats_kpi_cases': { 'key': 'stats_kpi_cases', 'value': 'Total Cases', 'label': 'Stats KPI Cases', 'page': 'resources', 'type': 'text', 'description': 'Total cases KPI label' },
            'stats_kpi_gbv': { 'key': 'stats_kpi_gbv', 'value': 'Total GBV Cases', 'label': 'Stats KPI GBV', 'page': 'resources', 'type': 'text', 'description': 'Total GBV cases KPI label' },
            'stats_kpi_sea': { 'key': 'stats_kpi_sea', 'value': 'Total SEA Cases', 'label': 'Stats KPI SEA', 'page': 'resources', 'type': 'text', 'description': 'Total SEA cases KPI label' },
            'stats_kpi_migrant': { 'key': 'stats_kpi_migrant', 'value': 'Migrant Workers', 'label': 'Stats KPI Migrant', 'page': 'resources', 'type': 'text', 'description': 'Migrant workers KPI label' },
            'resources_loading_charts': { 'key': 'resources_loading_charts', 'value': 'Loading...', 'label': 'Resources Loading Charts', 'page': 'resources', 'type': 'text', 'description': 'Chart loading indicator' },
            'resources_chart_district_title': { 'key': 'resources_chart_district_title', 'value': 'Top Districts', 'label': 'Resources Chart District Title', 'page': 'resources', 'type': 'heading', 'description': 'District chart title' },
            'resources_chart_district_subtitle': { 'key': 'resources_chart_district_subtitle', 'value': 'Districts with highest case volumes', 'label': 'Resources Chart District Subtitle', 'page': 'resources', 'type': 'text', 'description': 'District chart subtitle' },
            'resources_downloads_divider': { 'key': 'resources_downloads_divider', 'value': 'Downloads', 'label': 'Resources Downloads Divider', 'page': 'resources', 'type': 'text', 'description': 'Downloads section divider label' },
            'resources_all_formats': { 'key': 'resources_all_formats', 'value': 'All Formats', 'label': 'Resources All Formats', 'page': 'resources', 'type': 'text', 'description': 'All formats filter option' },
            'resources_clear_filters': { 'key': 'resources_clear_filters', 'value': 'Clear all filters', 'label': 'Resources Clear Filters', 'page': 'resources', 'type': 'button', 'description': 'Clear filters button text' },
            'resources_read_more': { 'key': 'resources_read_more', 'value': '+ Read more', 'label': 'Resources Read More', 'page': 'resources', 'type': 'button', 'description': 'Expand description button text' },
            'resources_show_less': { 'key': 'resources_show_less', 'value': '− Show less', 'label': 'Resources Show Less', 'page': 'resources', 'type': 'button', 'description': 'Collapse description button text' },
            'resources_downloads_count': { 'key': 'resources_downloads_count', 'value': 'downloads', 'label': 'Resources Downloads Count', 'page': 'resources', 'type': 'text', 'description': 'Download count suffix label' },

            # Videos Page - Additional Keys
            'videos_filter_videos': { 'key': 'videos_filter_videos', 'value': 'VIDEOS', 'label': 'Videos Filter Videos', 'page': 'videos', 'type': 'button', 'description': 'Jump-to-Videos-section nav pill' },
            'videos_filter_audio': { 'key': 'videos_filter_audio', 'value': 'AUDIO', 'label': 'Videos Filter Audio', 'page': 'videos', 'type': 'button', 'description': 'Jump-to-Audio-section nav pill' },
            'videos_empty_title': { 'key': 'videos_empty_title', 'value': 'No videos found', 'label': 'Videos Empty Title', 'page': 'videos', 'type': 'heading', 'description': 'Empty state title (Videos section)' },
            'videos_empty_subtitle': { 'key': 'videos_empty_subtitle', 'value': 'Try adjusting your filters or check back later for new content.', 'label': 'Videos Empty Subtitle', 'page': 'videos', 'type': 'text', 'description': 'Empty state subtitle (Videos section)' },
            'videos_audio_empty_title': { 'key': 'videos_audio_empty_title', 'value': 'No audio content found', 'label': 'Videos Audio Empty Title', 'page': 'videos', 'type': 'heading', 'description': 'Empty state title (Audio section)' },
            'videos_audio_empty_subtitle': { 'key': 'videos_audio_empty_subtitle', 'value': 'Check back later for new content', 'label': 'Videos Audio Empty Subtitle', 'page': 'videos', 'type': 'text', 'description': 'Empty state subtitle (Audio section)' },

            # Blog Page Buttons
            'blog_search_button': { 'key': 'blog_search_button', 'value': 'Search', 'label': 'Blog Search Button', 'page': 'blog', 'type': 'button', 'description': 'Search button text' },
            'blog_all_filter': { 'key': 'blog_all_filter', 'value': 'ALL', 'label': 'Blog All Filter', 'page': 'blog', 'type': 'button', 'description': 'All filter chip text' },
            'blog_all_categories': { 'key': 'blog_all_categories', 'value': 'All Categories', 'label': 'Blog All Categories', 'page': 'blog', 'type': 'text', 'description': 'All categories dropdown option' },
            'blog_clear_filters': { 'key': 'blog_clear_filters', 'value': 'Clear all filters', 'label': 'Blog Clear Filters', 'page': 'blog', 'type': 'button', 'description': 'Clear filters button text' },

            # News Page Buttons
            'news_search_button': { 'key': 'news_search_button', 'value': 'Search', 'label': 'News Search Button', 'page': 'news', 'type': 'button', 'description': 'Search button text' },
            'news_all_filter': { 'key': 'news_all_filter', 'value': 'ALL', 'label': 'News All Filter', 'page': 'news', 'type': 'button', 'description': 'All filter chip text' },
            'news_all_categories': { 'key': 'news_all_categories', 'value': 'All Categories', 'label': 'News All Categories', 'page': 'news', 'type': 'text', 'description': 'All categories dropdown option' },
            'news_clear_filters': { 'key': 'news_clear_filters', 'value': 'Clear all filters', 'label': 'News Clear Filters', 'page': 'news', 'type': 'button', 'description': 'Clear filters button text' },
        }

        for key, data in default_content.items():
            content_obj, created = SiteContent.objects.get_or_create(
                key=key,
                defaults={
                    'label': data['label'],
                    'value': data['value'],
                    'type': data['type'],
                    'page': data['page'],
                    'description': data.get('description', ''),
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Created content for '{key}'"))
            else:
                self.stdout.write(self.style.WARNING(f"Content for '{key}' already exists"))
