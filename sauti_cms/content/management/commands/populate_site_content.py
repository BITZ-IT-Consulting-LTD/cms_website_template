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
            'about_resolution_card_1_title': { 'key': 'about_resolution_card_1_title', 'value': 'Caller', 'label': 'About Resolution Card 1 Title', 'page': 'about', 'type': 'text' },
            'about_resolution_card_1_text': { 'key': 'about_resolution_card_1_text', 'value': 'Case reported', 'label': 'About Resolution Card 1 Text', 'page': 'about', 'type': 'text' },
            'about_resolution_card_2_title': { 'key': 'about_resolution_card_2_title', 'value': 'Call Center', 'label': 'About Resolution Card 2 Title', 'page': 'about', 'type': 'text' },
            'about_resolution_card_3_title': { 'key': 'about_resolution_card_3_title', 'value': 'Case Management Department', 'label': 'About Resolution Card 3 Title', 'page': 'about', 'type': 'text' },
            'about_resolution_card_4_title': { 'key': 'about_resolution_card_4_title', 'value': 'Probation Offices (DACs)', 'label': 'About Resolution Card 4 Title', 'page': 'about', 'type': 'text' },
            'about_resolution_card_4_text': { 'key': 'about_resolution_card_4_text', 'value': 'Supported by partners & CSOs, police, court, etc.', 'label': 'About Resolution Card 4 Text', 'page': 'about', 'type': 'text' },
            'about_resolution_card_5_title': { 'key': 'about_resolution_card_5_title', 'value': 'Local Leaders, CDOs, Para-Social Workers, VHTs, etc.', 'label': 'About Resolution Card 5 Title', 'page': 'about', 'type': 'text' },
            'about_resolution_card_5_text': { 'key': 'about_resolution_card_5_text', 'value': 'Feedback shared back through the chain.', 'label': 'About Resolution Card 5 Text', 'page': 'about', 'type': 'text' },
            'about_partners_title': { 'key': 'about_partners_title', 'value': 'Partners & Affiliations', 'label': 'About Partners Title', 'page': 'about', 'type': 'heading' },
            'about_partner_1': { 'key': 'about_partner_1', 'value': 'MGLSD', 'label': 'About Partner 1', 'page': 'about', 'type': 'text' },
            'about_partner_2': { 'key': 'about_partner_2', 'value': 'UNICEF', 'label': 'About Partner 2', 'page': 'about', 'type': 'text' },
            'about_partner_3': { 'key': 'about_partner_3', 'value': 'UCRNN', 'label': 'About Partner 3', 'page': 'about', 'type': 'text' },
            'about_partner_4': { 'key': 'about_partner_4', 'value': 'ITU 116', 'label': 'About Partner 4', 'page': 'about', 'type': 'text' },
            'about_partners_text': { 'key': 'about_partners_text', 'value': 'Legally designated 116 child helpline; compliant with national and international standards.', 'label': 'About Partners Text', 'page': 'about', 'type': 'text' },
            'about_cta_title': { 'key': 'about_cta_title', 'value': 'Need help or ready to partner?', 'label': 'About CTA Title', 'page': 'about', 'type': 'heading' },
            'about_cta_text': { 'key': 'about_cta_text', 'value': 'Reach out any time. Your call or message could change a life.', 'label': 'About CTA Text', 'page': 'about', 'type': 'text' },

            # Operations Page Content
            'operations_title': { 'key': 'operations_title', 'value': 'Our Operations and Case Flow', 'label': 'Operations Title', 'page': 'operations', 'type': 'heading' },
            'operations_subtitle': { 'key': 'operations_subtitle', 'value': 'A transparent look into how we handle every call to ensure every child\'s voice is heard and acted upon with care and urgency.', 'label': 'Operations Subtitle', 'page': 'operations', 'type': 'text' },
            'operations_path_title': { 'key': 'operations_path_title', 'value': 'The Path to Resolution', 'label': 'Operations Path Title', 'page': 'operations', 'type': 'heading' },
            'operations_path_subtitle': { 'key': 'operations_path_subtitle', 'value': 'Our streamlined process from report to resolution, ensuring every case receives the attention and action it deserves.', 'label': 'Operations Path Subtitle', 'page': 'operations', 'type': 'text' },
            'operations_step_1_title': { 'key': 'operations_step_1_title', 'value': 'Initial Contact', 'label': 'Operations Step 1 Title', 'page': 'operations', 'type': 'text' },
            'operations_step_1_text': { 'key': 'operations_step_1_text', 'value': 'A child or concerned individual calls the toll-free 116 helpline or reaches out via WhatsApp.', 'label': 'Operations Step 1 Text', 'page': 'operations', 'type': 'text' },
            'operations_step_1_tag': { 'key': 'operations_step_1_tag', 'value': 'Immediate Response', 'label': 'Operations Step 1 Tag', 'page': 'operations', 'type': 'text' },
            'operations_step_2_title': { 'key': 'operations_step_2_title', 'value': 'Counselor Support', 'label': 'Operations Step 2 Title', 'page': 'operations', 'type': 'text' },
            'operations_step_2_text': { 'key': 'operations_step_2_text', 'value': 'Trained counselors provide immediate emotional support and gather essential information with empathy.', 'label': 'Operations Step 2 Text', 'page': 'operations', 'type': 'text' },
            'operations_step_2_tag': { 'key': 'operations_step_2_tag', 'value': 'Professional Care', 'label': 'Operations Step 2 Tag', 'page': 'operations', 'type': 'text' },
            'operations_step_3_title': { 'key': 'operations_step_3_title', 'value': 'Case Assessment', 'label': 'Operations Step 3 Title', 'page': 'operations', 'type': 'text' },
            'operations_step_3_text': { 'key': 'operations_step_3_text', 'value': 'The case is documented, assessed for urgency level, and classified according to protection needs.', 'label': 'Operations Step 3 Text', 'page': 'operations', 'type': 'text' },
            'operations_step_3_tag': { 'key': 'operations_step_3_tag', 'value': 'Detailed Documentation', 'label': 'Operations Step 3 Tag', 'page': 'operations', 'type': 'text' },
            'operations_step_4_title': { 'key': 'operations_step_4_title', 'value': 'Referral & Follow-up', 'label': 'Operations Step 4 Title', 'page': 'operations', 'type': 'text' },
            'operations_step_4_text': { 'key': 'operations_step_4_text', 'value': 'Referrals are made to relevant authorities and continuous follow-up ensures case resolution.', 'label': 'Operations Step 4 Text', 'page': 'operations', 'type': 'text' },
            'operations_step_4_tag': { 'key': 'operations_step_4_tag', 'value': 'Action & Closure', 'label': 'Operations Step 4 Tag', 'page': 'operations', 'type': 'text' },
            'operations_metrics_1_title': { 'key': 'operations_metrics_1_title', 'value': '24/7', 'label': 'Operations Metrics 1 Title', 'page': 'operations', 'type': 'text' },
            'operations_metrics_1_text': { 'key': 'operations_metrics_1_text', 'value': 'Always Available', 'label': 'Operations Metrics 1 Text', 'page': 'operations', 'type': 'text' },
            'operations_metrics_2_title': { 'key': 'operations_metrics_2_title', 'value': '100%', 'label': 'Operations Metrics 2 Title', 'page': 'operations', 'type': 'text' },
            'operations_metrics_2_text': { 'key': 'operations_metrics_2_text', 'value': 'Confidential', 'label': 'Operations Metrics 2 Text', 'page': 'operations', 'type': 'text' },
            'operations_metrics_3_title': { 'key': 'operations_metrics_3_title', 'value': 'Free', 'label': 'Operations Metrics 3 Title', 'page': 'operations', 'type': 'text' },
            'operations_metrics_3_text': { 'key': 'operations_metrics_3_text', 'value': 'Toll-Free Service', 'label': 'Operations Metrics 3 Text', 'page': 'operations', 'type': 'text' },
            'operations_highlights_title': { 'key': 'operations_highlights_title', 'value': 'Operational Highlights', 'label': 'Operations Highlights Title', 'page': 'operations', 'type': 'heading' },
            'operations_highlight_1_title': { 'key': 'operations_highlight_1_title', 'value': '116 Toll-Free Helpline', 'label': 'Operations Highlight 1 Title', 'page': 'operations', 'type': 'text' },
            'operations_highlight_1_text': { 'key': 'operations_highlight_1_text', 'value': 'Accessible nationwide across all telecom networks.', 'label': 'Operations Highlight 1 Text', 'page': 'operations', 'type': 'text' },
            'operations_highlight_2_title': { 'key': 'operations_highlight_2_title', 'value': '24/7 Availability', 'label': 'Operations Highlight 2 Title', 'page': 'operations', 'type': 'text' },
            'operations_highlight_2_text': { 'key': 'operations_highlight_2_text', 'value': 'Help any time of day, all year round.', 'label': 'Operations Highlight 2 Text', 'page': 'operations', 'type': 'text' },
            'operations_highlight_3_title': { 'key': 'operations_highlight_3_title', 'value': 'Language Support', 'label': 'Operations Highlight 3 Title', 'page': 'operations', 'type': 'text' },
            'operations_highlight_3_text': { 'key': 'operations_highlight_3_text', 'value': 'English, Luganda, Swahili, and additional local languages.', 'label': 'Operations Highlight 3 Text', 'page': 'operations', 'type': 'text' },
            'operations_highlight_4_title': { 'key': 'operations_highlight_4_title', 'value': 'Strict Confidentiality', 'label': 'Operations Highlight 4 Title', 'page': 'operations', 'type': 'text' },
            'operations_highlight_4_text': { 'key': 'operations_highlight_4_text', 'value': 'Handled with the utmost privacy.', 'label': 'Operations Highlight 4 Text', 'page': 'operations', 'type': 'text' },
            'operations_highlight_5_title': { 'key': 'operations_highlight_5_title', 'value': 'Trained Professionals', 'label': 'Operations Highlight 5 Title', 'page': 'operations', 'type': 'text' },
            'operations_highlight_5_text': { 'key': 'operations_highlight_5_text', 'value': 'Counselors undergo rigorous training.', 'label': 'Operations Highlight 5 Text', 'page': 'operations', 'type': 'text' },
            'operations_highlight_6_title': { 'key': 'operations_highlight_6_title', 'value': 'Multiple Channels', 'label': 'Operations Highlight 6 Title', 'page': 'operations', 'type': 'text' },
            'operations_highlight_6_text': { 'key': 'operations_highlight_6_text', 'value': 'WhatsApp, U-Report, SafePal App, email, and walk-ins.', 'label': 'Operations Highlight 6 Text', 'page': 'operations', 'type': 'text' },

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
            'videos_title': { 'key': 'videos_title', 'value': 'Videos', 'label': 'Videos Title', 'page': 'videos', 'type': 'heading' },
            'videos_resources_link': { 'key': 'videos_resources_link', 'value': 'Resources →', 'label': 'Videos Resources Link', 'page': 'videos', 'type': 'button' },
            'videos_search_placeholder': { 'key': 'videos_search_placeholder', 'value': 'Search videos...', 'label': 'Videos Search Placeholder', 'page': 'videos', 'type': 'text' },
            'videos_search_button': { 'key': 'videos_search_button', 'value': 'Search', 'label': 'Videos Search Button', 'page': 'videos', 'type': 'button' },
            'videos_chip_all': { 'key': 'videos_chip_all', 'value': 'All', 'label': 'Videos Chip All', 'page': 'videos', 'type': 'button' },
            'videos_chip_education': { 'key': 'videos_chip_education', 'value': 'Education', 'label': 'Videos Chip Education', 'page': 'videos', 'type': 'button' },
            'videos_chip_safety': { 'key': 'videos_chip_safety', 'value': 'Safety', 'label': 'Videos Chip Safety', 'page': 'videos', 'type': 'button' },
            'videos_chip_support': { 'key': 'videos_chip_support', 'value': 'Support', 'label': 'Videos Chip Support', 'page': 'videos', 'type': 'button' },
            'videos_chip_recency': { 'key': 'videos_chip_recency', 'value': 'Recency', 'label': 'Videos Chip Recency', 'page': 'videos', 'type': 'button' },
            'videos_chip_popular': { 'key': 'videos_chip_popular', 'value': 'Popular', 'label': 'Videos Chip Popular', 'page': 'videos', 'type': 'button' },

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
            'faqs_page_subtitle': { 'key': 'faqs_page_subtitle', 'value': 'Questions & Answers', 'label': 'FAQs Page Subtitle', 'page': 'faqs', 'type': 'heading' },
            'faqs_search_placeholder': { 'key': 'faqs_search_placeholder', 'value': 'Search questions', 'label': 'FAQs Search Placeholder', 'page': 'faqs', 'type': 'text' },
            'faqs_all_categories_button': { 'key': 'faqs_all_categories_button', 'value': 'All Categories', 'label': 'FAQs All Categories Button', 'page': 'faqs', 'type': 'button' },
            'faqs_no_results': { 'key': 'faqs_no_results', 'value': 'No FAQs found', 'label': 'FAQs No Results', 'page': 'faqs', 'type': 'text' },
            'faqs_no_results_subtitle': { 'key': 'faqs_no_results_subtitle', 'value': 'Try adjusting your search or category filter', 'label': 'FAQs No Results Subtitle', 'page': 'faqs', 'type': 'text' },
            'faqs_privacy_policy': { 'key': 'faqs_privacy_policy', 'value': 'Privacy Policy', 'label': 'FAQs Privacy Policy', 'page': 'faqs', 'type': 'button' },
            'faqs_terms_of_service': { 'key': 'faqs_terms_of_service', 'value': 'Terms of Service', 'label': 'FAQs Terms of Service', 'page': 'faqs', 'type': 'button' },
            'faqs_contact_us': { 'key': 'faqs_contact_us', 'value': 'Contact Us', 'label': 'FAQs Contact Us', 'page': 'faqs', 'type': 'button' },
            'faqs_footer_text': { 'key': 'faqs_footer_text', 'value': '© 2024 Sauti Uganda. All rights reserved. A sanctuary for every child.', 'label': 'FAQs Footer Text', 'page': 'faqs', 'type': 'text' },
        }

        for key, data in default_content.items():
            content_obj, created = SiteContent.objects.get_or_create(
                key=key,
                defaults={
                    'label': data['label'],
                    'value': data['value'],
                    'type': data['type'],
                    'page': data['page'],
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Created content for '{key}'"))
            else:
                self.stdout.write(self.style.WARNING(f"Content for '{key}' already exists"))
