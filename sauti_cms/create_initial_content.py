import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cms.settings")
django.setup()

from content.models import SiteContent
from sitesettings.models import GlobalSettings

INITIAL_CONTENT = [

    # =========================
    # HOME PAGE – HERO SECTION
    # =========================
    {
        "key": "hero_image",
        "label": "Hero Image",
        "value": "/assets/sauti-homepage.avif",
        "page": "home",
        "type": "photo",
        "description": "Main hero image on homepage"
    },
    {
        "key": "hero_title",
        "label": "Hero Title",
        "value": "Every voice matters. Every life deserves protection.",
        "page": "home",
        "type": "heading",
        "description": "Main heading on homepage"
    },
    {
        "key": "hero_subtitle",
        "label": "Hero Subtitle",
        "value": (
            "Sauti 116 is Uganda’s national toll-free helpline providing confidential, "
            "24/7 support for children affected by violence, survivors of gender-based "
            "violence, migrant workers in distress, and individuals experiencing sexual "
            "exploitation. Support is available across all telecom networks and in "
            "multiple local languages."
        ),
        "page": "home",
        "type": "text",
        "description": "Subtitle text under hero heading"
    },
    {
        "key": "hero_cta_call",
        "label": "Hero Call Button",
        "value": "Call 116 Now",
        "page": "home",
        "type": "button",
        "description": "Call-to-action button text"
    },
    {
        "key": "hero_cta_report",
        "label": "Hero Report Button",
        "value": "Report a Case",
        "page": "home",
        "type": "button",
        "description": "Report button text"
    },

    # =================================
    # HOME PAGE – QUICK ACCESS SECTION
    # =================================
    {
        "key": "quick_access_title",
        "label": "Quick Access Section Title",
        "value": "Get Help, Protection & Information",
        "page": "home",
        "type": "heading",
        "description": "Section heading for quick access cards"
    },
    {
        "key": "quick_access_description",
        "label": "Quick Access Description",
        "value": (
            "Sauti provides free, confidential support services for children and adults "
            "facing violence, abuse, exploitation, or distress. Our trained counselors "
            "offer immediate assistance, guidance, and referrals to appropriate "
            "protection and response services nationwide."
        ),
        "page": "home",
        "type": "text",
        "description": "Description text for quick access section"
    },

    # Quick Access Cards
    {
        "key": "card_report_title",
        "label": "Report Card Title",
        "value": "Report a Case",
        "page": "home",
        "type": "heading",
        "description": "Title for Report a Case card"
    },
    {
        "key": "card_report_text",
        "label": "Report Card Text",
        "value": (
            "Safely and confidentially report cases of violence against children, "
            "gender-based violence, sexual exploitation, or abuse involving migrant workers."
        ),
        "page": "home",
        "type": "text",
        "description": "Text for Report a Case card"
    },
    {
        "key": "card_services_title",
        "label": "Support Services Card Title",
        "value": "Support Services",
        "page": "home",
        "type": "heading",
        "description": "Title for Support Services card"
    },
    {
        "key": "card_services_text",
        "label": "Support Services Card Text",
        "value": (
            "Access counseling, crisis response, information, and referrals to health, "
            "legal, psychosocial, and protection services across Uganda."
        ),
        "page": "home",
        "type": "text",
        "description": "Text for Support Services card"
    },
    {
        "key": "card_faqs_title",
        "label": "FAQs Card Title",
        "value": "FAQs",
        "page": "home",
        "type": "heading",
        "description": "Title for FAQs card"
    },
    {
        "key": "card_faqs_text",
        "label": "FAQs Card Text",
        "value": (
            "Learn how the helpline works, who can call, what services are available, "
            "and how confidentiality is protected."
        ),
        "page": "home",
        "type": "text",
        "description": "Text for FAQs card"
    },
    {
        "key": "card_partners_title",
        "label": "Partners Card Title",
        "value": "Partners",
        "page": "home",
        "type": "heading",
        "description": "Title for Partners card"
    },
    {
        "key": "card_partners_text",
        "label": "Partners Card Text",
        "value": (
            "Delivered in collaboration with Government of Uganda institutions, UNICEF, "
            "civil society organizations, and international partners."
        ),
        "page": "home",
        "type": "text",
        "description": "Text for Partners card"
    },

    # =================================
    # HOME PAGE – PUBLICATIONS SECTION
    # =================================
    {
        "key": "publications_title",
        "label": "Publications Section Title",
        "value": "Resources & Publications",
        "page": "home",
        "type": "heading",
        "description": "Section heading for publications"
    },
    {
        "key": "publications_description",
        "label": "Publications Description",
        "value": (
            "Explore guidance materials, public awareness resources, research, and updates "
            "on child protection, gender-based violence prevention, migrant worker safety, "
            "and protection from sexual exploitation."
        ),
        "page": "home",
        "type": "text",
        "description": "Description for publications section"
    },
    {
        "key": "publications_link",
        "label": "Publications Link",
        "value": "View all resources",
        "page": "home",
        "type": "button",
        "description": "Link text to view all resources"
    },

    # =================================
    # HOME PAGE – TRUST PARTNERS
    # =================================
    {
        "key": "trust_partners_title",
        "label": "Trust Partners Title",
        "value": "Trusted National & International Partners",
        "page": "home",
        "type": "heading",
        "description": "Title for trust partners section"
    },
    {
        "key": "trust_partners_description",
        "label": "Trust Partners Description",
        "value": (
            "Sauti works closely with government ministries, development partners, UN "
            "agencies, and civil society organizations to ensure coordinated, "
            "survivor-centered responses."
        ),
        "page": "home",
        "type": "text",
        "description": "Description for trust partners"
    },

    # =================================
    # HOME PAGE – FINAL CTA
    # =================================
    {
        "key": "final_cta_title",
        "label": "Final CTA Title",
        "value": "Need Help Right Now?",
        "page": "home",
        "type": "heading",
        "description": "Final CTA section title"
    },
    {
        "key": "final_cta_text",
        "label": "Final CTA Text",
        "value": (
            "Call 116 for immediate, free, and confidential support. Services are available "
            "24/7 across all telecom networks and in multiple local languages for children, "
            "survivors of gender-based violence, migrant workers, and individuals affected "
            "by sexual exploitation."
        ),
        "page": "home",
        "type": "text",
        "description": "Final CTA section text"
    },
    {
        "key": "final_cta_call",
        "label": "Final CTA Call Button",
        "value": "Call 116 Now",
        "page": "home",
        "type": "button",
        "description": "Final CTA call button"
    },
    {
        "key": "final_cta_report",
        "label": "Final CTA Report Button",
        "value": "Report a Case",
        "page": "home",
        "type": "button",
        "description": "Final CTA report button"
    },
    {
        "key": "final_cta_contact",
        "label": "Final CTA Contact Button",
        "value": "Contact Us",
        "page": "home",
        "type": "button",
        "description": "Final CTA contact button"
    },

    # =========================
    # ABOUT PAGE
    # =========================
    {
        "key": "about_image",
        "label": "About Page Image",
        "value": "/assets/sauti-aboutpage.webp",
        "page": "about",
        "type": "photo",
        "description": "Main image on about page"
    },
    {
        "key": "about_title",
        "label": "About Page Title",
        "value": "About Sauti",
        "page": "about",
        "type": "heading",
        "description": "Main heading on about page"
    },
    {
        "key": "about_description",
        "label": "About Page Description",
        "value": (
            "Sauti is Uganda’s national toll-free helpline operated under the Ministry of "
            "Gender, Labour and Social Development. It provides confidential, "
            "survivor-centered support services for children affected by violence, "
            "survivors of gender-based violence, migrant workers in distress, and "
            "individuals at risk of or affected by sexual exploitation. "
            "Through trained counselors, case management systems, and referral networks, "
            "Sauti connects callers to protection, health, psychosocial, legal, and social "
            "support services across the country."
        ),
        "page": "about",
        "type": "text",
        "description": "Main descriptive text on about page"
    },

    # =========================
    # OPERATIONS PAGE
    # =========================
    {
        "key": "operations_image",
        "label": "Operations Image",
        "value": "/assets/our operations and case flow.jpg",
        "page": "operations",
        "type": "photo",
        "description": "Operations flowchart image"
    },

    # =========================
    # GLOBAL / HEADER
    # =========================
    {
        "key": "logo",
        "label": "Site Logo",
        "value": "/assets/sauti-logo.jpeg",
        "page": "header",
        "type": "photo",
        "description": "Main site logo"
    },
]

def create_initial_content():
    created_count = 0
    updated_count = 0

    for item in INITIAL_CONTENT:
        obj, created = SiteContent.objects.update_or_create(
            key=item["key"],
            defaults={
                "label": item["label"],
                "value": item["value"],
                "page": item["page"],
                "type": item["type"],
                "description": item["description"],
            }
        )
        if created:
            created_count += 1
        else:
            updated_count += 1

    print(f"Content setup complete: {created_count} created, {updated_count} updated.")

def create_global_settings():
    settings, created = GlobalSettings.objects.get_or_create()
    settings.site_name = "Sauti"
    settings.site_description = "Sauti is Uganda’s national toll-free helpline operated under the Ministry of Gender, Labour and Social Development."
    settings.hotline_text = "Call 116 Now"
    settings.support_email_text = "support@sauti.org"
    settings.operating_hours_text = "24/7"
    settings.footer_text = "© 2025 Sauti. All rights reserved."
    settings.ministry_attribution_text = "A project of the Ministry of Gender, Labour and Social Development."
    settings.disclaimer_text = "The information on this website is for general information purposes only."
    settings.default_meta_title_suffix = " | Sauti"
    settings.default_meta_description = "Sauti provides free, confidential support services for children and adults facing violence, abuse, exploitation, or distress."
    settings.environment_label = "Development"
    settings.hero_title = "Every One Deserves to Be Heard."
    settings.hero_subtitle = "Sauti 116 is free, confidential and available 24/7 across all telecoms. Report abuse, seek guidance, or get urgent help in your language."
    settings.hero_cta_call = "Call 116 Now"
    settings.hero_cta_report = "Report a Case"
    settings.quick_access_title = "Get Help & Information"
    settings.quick_access_description = "Access our comprehensive support services and resources designed to protect and empower children across Uganda."
    settings.card_report_title = "Report a Case"
    settings.card_report_text = "Report abuse confidentially. Our trained counselors are available 24/7 to listen and support you."
    settings.card_resources_title = "Resources"
    settings.card_resources_text = "Access vital information, safety guides, and educational materials to protect children."
    settings.card_faqs_title = "FAQs"
    settings.card_faqs_text = "Find quick answers to common questions about our services, reporting process, and safety."
    settings.card_partners_title = "Partners"
    settings.card_partners_text = "Collaborating with government and international organizations to ensure child safety."
    settings.journey_title = "Our Journey"
    settings.journey_description = "Key milestones in our history of child advocacy, including international recommendations and national designation of 116."
    settings.publications_title = "Recent Publications"
    settings.publications_description = "Latest articles, videos and resources to help children, families, and communities stay safe and informed."
    settings.publications_link = "View all posts"
    settings.trust_partners_title = "Trusted by Leading Organizations"
    settings.trust_partners_description = "Working in partnership with government and international agencies"
    settings.final_cta_title = "Need Help Right Now?"
    settings.final_cta_text = "Accessible 24/7 across all telecom networks. Support in multiple local languages. All services are free and confidential."
    settings.final_cta_call = "Call 116 Now"
    settings.final_cta_report = "Report a Case"
    settings.final_cta_contact = "Contact Us"
    settings.social_facebook = "https://www.facebook.com/Sauti116Helpline"
    settings.social_twitter = "https://x.com/sauti116"
    settings.social_whatsapp = "https://wa.me/256743889999"
    settings.social_ureport = "https://ureport.in"
    settings.social_safepal = "https://www.unicef.org/uganda/safepal-app"
    settings.contact_email_info = "info@sauti.mglsd.go.ug"
    settings.contact_email_sautichl = "sautichl@mglsd.go.ug"
    settings.contact_website = "https://sauti.mglsd.go.ug"
    settings.contact_phone_main = "116"
    settings.resources_title = "Resources"
    settings.resources_subtitle = "Download educational materials, guides, and resources to help protect children and support communities."
    settings.resources_stats_title = "Statistics Dashboard"
    settings.resources_stats_updated = "Updated in real-time"
    settings.resources_stats_loading = "Loading statistics..."
    settings.resources_stats_error = "Failed to load statistics"
    settings.resources_total_reports = "Total Reports"
    settings.resources_child_protection = "Child Protection"
    settings.resources_gbv_cases = "GBV Cases"
    settings.resources_migrant_worker = "Migrant Worker"
    settings.resources_cases_by_category = "Cases by Category"
    settings.resources_interactive = "Interactive"
    settings.resources_reports_over_time = "Reports Over Time"
    settings.resources_last_6_months = "Last 6 months"
    settings.resources_status_distribution = "Status Distribution"
    settings.resources_pending = "Pending"
    settings.resources_in_progress = "In Progress"
    settings.resources_resolved = "Resolved"
    settings.resources_closed = "Closed"
    settings.resources_downloads_title = "Downloadable Resources"
    settings.resources_downloads_subtitle = "Access guides, toolkits, and educational materials"
    settings.resources_available = "resources available"
    settings.resources_search_placeholder = "Search resources..."
    settings.resources_all_categories = "All Categories"
    settings.resources_all_languages = "All Languages"
    settings.resources_loading = "Loading resources..."
    settings.resources_coming_soon = "Coming Soon"
    settings.resources_no_results = "No resources found"
    settings.resources_no_results_subtitle = "Try adjusting your filters or check back later"
    settings.resources_previous = "Previous"
    settings.resources_next = "Next"
    settings.save()
    print("Global settings created/updated.")


if __name__ == "__main__":
    create_initial_content()
    create_global_settings()
