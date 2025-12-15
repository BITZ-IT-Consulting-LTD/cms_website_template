from django.core.management.base import BaseCommand
from sitesettings.models import SiteSetting

class Command(BaseCommand):
    help = 'Populates initial site settings data.'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Populating initial site settings...'))

        settings_to_create = [
            # Home Page Settings
            {'page': 'home', 'key': 'hero_title', 'value': 'Welcome to Sauti 116 Helpline', 'description': 'Main title on the homepage hero section.'},
            {'page': 'home', 'key': 'hero_subtitle', 'value': 'Empowering children, GBV survivors, and migrant workers', 'description': 'Subtitle on the homepage hero section.'},
            {'page': 'home', 'key': 'hero_button_text', 'value': 'Learn More', 'description': 'Text for the main call-to-action button on the homepage.'},
            {'page': 'home', 'key': 'about_section_title', 'value': 'Our Mission', 'description': 'Title for the "About" section on the homepage.'},
            {'page': 'home', 'key': 'about_section_content', 'value': 'Sauti 116 Helpline is dedicated to providing support and resources...', 'description': 'Content for the "About" section on the homepage.'},

            # About Page Settings
            {'page': 'about', 'key': 'page_title', 'value': 'About Us', 'description': 'Main title for the About Us page.'},
            {'page': 'about', 'key': 'mission_statement', 'value': 'Our mission is to create a safe and supportive environment...', 'description': 'The organization\'s mission statement.'},
            {'page': 'about', 'key': 'vision_statement', 'value': 'A future where every individual is empowered and protected.', 'description': 'The organization\'s vision statement.'},
            {'page': 'about', 'key': 'team_section_title', 'value': 'Meet Our Team', 'description': 'Title for the team section on the About Us page.'},

            # Contact Page Settings
            {'page': 'contact', 'key': 'page_title', 'value': 'Contact Us', 'description': 'Main title for the Contact Us page.'},
            {'page': 'contact', 'key': 'address', 'value': '123 Sauti Street, Kampala, Uganda', 'description': 'Physical address of the organization.'},
            {'page': 'contact', 'key': 'phone_number', 'value': '+256 116', 'description': 'Primary contact phone number.'},
            {'page': 'contact', 'key': 'email_address', 'value': 'info@sauti116.org', 'description': 'Primary contact email address.'},
            {'page': 'contact', 'key': 'map_embed_url', 'value': 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d...', 'description': 'Google Maps embed URL for the contact page.'},
        ]

        for setting_data in settings_to_create:
            setting, created = SiteSetting.objects.update_or_create(
                page=setting_data['page'],
                key=setting_data['key'],
                defaults={
                    'value': setting_data['value'],
                    'description': setting_data['description']
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Created SiteSetting: {setting}"))
            else:
                self.stdout.write(self.style.MIGRATE_HEADING(f"Updated SiteSetting: {setting}"))

        self.stdout.write(self.style.SUCCESS('Site settings population complete.'))
