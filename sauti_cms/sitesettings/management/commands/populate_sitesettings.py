from django.core.management.base import BaseCommand
from django.db import transaction
from sitesettings.models import SiteSetting


class Command(BaseCommand):
    help = "Populates initial site settings data for Sauti 116."

    def add_arguments(self, parser):
        parser.add_argument(
            "--dry-run",
            action="store_true",
            help="Run the command without writing changes to the database.",
        )

    def handle(self, *args, **options):
        dry_run = options.get("dry_run", False)

        self.stdout.write(self.style.NOTICE("Starting site settings population..."))

        settings_to_create = [

            # =====================================================
            # HOME PAGE
            # =====================================================
            {
                "page": "home",
                "key": "hero_title",
                "value": "Every voice matters. Every life deserves protection.",
                "description": "Main title displayed in the homepage hero section.",
            },
            {
                "page": "home",
                "key": "hero_subtitle",
                "value": (
                    "Sauti 116 is Uganda’s national toll-free helpline providing free, "
                    "confidential, 24/7 support for children affected by violence, "
                    "survivors of gender-based violence, migrant workers in distress, "
                    "and individuals affected by sexual exploitation."
                ),
                "description": "Subtitle text in the homepage hero section.",
            },
            {
                "page": "home",
                "key": "hero_button_text",
                "value": "Call 116 Now",
                "description": "Primary call-to-action button text on the homepage.",
            },
            {
                "page": "home",
                "key": "about_section_title",
                "value": "Who We Support",
                "description": "Title for the homepage introductory section.",
            },
            {
                "page": "home",
                "key": "about_section_content",
                "value": (
                    "Sauti 116 provides immediate support, counseling, and referrals "
                    "for individuals facing violence, abuse, exploitation, or distress. "
                    "Our services are available nationwide across all telecom networks "
                    "and delivered in multiple local languages."
                ),
                "description": "Introductory text describing Sauti’s mandate on the homepage.",
            },

            # =====================================================
            # ABOUT PAGE
            # =====================================================
            {
                "page": "about",
                "key": "page_title",
                "value": "About Sauti 116",
                "description": "Main title for the About page.",
            },
            {
                "page": "about",
                "key": "mission_statement",
                "value": (
                    "To provide free, confidential, and survivor-centered helpline "
                    "services that protect children, support survivors of gender-based "
                    "violence, assist migrant workers in distress, and prevent sexual "
                    "exploitation through coordinated national response systems."
                ),
                "description": "Official mission statement.",
            },
            {
                "page": "about",
                "key": "vision_statement",
                "value": (
                    "A Uganda where all individuals live free from violence, abuse, "
                    "and exploitation, and where timely support is accessible to all."
                ),
                "description": "Official vision statement.",
            },
            {
                "page": "about",
                "key": "team_section_title",
                "value": "Our Team",
                "description": "Title for the team section on the About page.",
            },

            # =====================================================
            # CONTACT PAGE
            # =====================================================
            {
                "page": "contact",
                "key": "page_title",
                "value": "Contact Sauti 116",
                "description": "Main title for the Contact page.",
            },
            {
                "page": "contact",
                "key": "address",
                "value": "Ministry of Gender, Labour and Social Development, Kampala, Uganda",
                "description": "Physical office address.",
            },
            {
                "page": "contact",
                "key": "phone_number",
                "value": "116",
                "description": "National toll-free helpline number.",
            },
            {
                "page": "contact",
                "key": "email_address",
                "value": "sauti116@mglsd.go.ug",
                "description": "Official contact email address.",
            },
            {
                "page": "contact",
                "key": "map_embed_url",
                "value": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d...",
                "description": "Google Maps embed URL for office location.",
            },
        ]

        created_count = 0
        updated_count = 0

        if dry_run:
            self.stdout.write(self.style.WARNING("Running in DRY-RUN mode. No changes will be saved."))

        with transaction.atomic():
            for data in settings_to_create:
                if dry_run:
                    self.stdout.write(
                        self.style.HTTP_INFO(
                            f"[DRY-RUN] Would create/update: {data['page']} → {data['key']}"
                        )
                    )
                    continue

                setting, created = SiteSetting.objects.update_or_create(
                    page=data["page"],
                    key=data["key"],
                    defaults={
                        "value": data["value"],
                        "description": data["description"],
                    },
                )

                if created:
                    created_count += 1
                    self.stdout.write(self.style.SUCCESS(f"Created: {setting.page}.{setting.key}"))
                else:
                    updated_count += 1
                    self.stdout.write(self.style.NOTICE(f"Updated: {setting.page}.{setting.key}"))

        self.stdout.write(self.style.SUCCESS(
            f"Site settings complete — {created_count} created, {updated_count} updated."
        ))
