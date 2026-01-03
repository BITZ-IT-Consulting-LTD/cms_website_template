import os
import django
import sys
from pathlib import Path

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cms.settings')
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
    # ABOUT PAGE - HERO SECTION
    # =========================
    {
        "key": "about_hero_title",
        "label": "About Page Hero Title",
        "value": "About Sauti: Your Voice, Our Mission",
        "page": "about",
        "type": "heading",
        "description": "Main heading for the About Page hero section"
    },
    {
        "key": "about_hero_description",
        "label": "About Page Hero Description",
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
        "description": "Main descriptive text for the About Page hero section"
    },
    {
        "key": "about_hero_image",
        "label": "About Page Hero Image",
        "value": "/assets/sauti-aboutpage.webp",
        "page": "about",
        "type": "photo",
        "description": "Main image for the About Page hero section"
    },
    {
        "key": "about_hero_cta_call",
        "label": "About Page Hero Call Button",
        "value": "Call 116",
        "page": "about",
        "type": "button",
        "description": "Call-to-action button text in hero section"
    },
    {
        "key": "about_hero_cta_report",
        "label": "About Page Hero Report Button",
        "value": "Report a Case",
        "page": "about",
        "type": "button",
        "description": "Report button text in hero section"
    },
    {
        "key": "about_hero_badge1_text",
        "label": "About Page Hero Badge 1 Text",
        "value": "24/7",
        "page": "about",
        "type": "text",
        "description": "Text for the first badge in hero section"
    },
    {
        "key": "about_hero_badge1_class",
        "label": "About Page Hero Badge 1 Class",
        "value": "badge-blue",
        "page": "about",
        "type": "text",
        "description": "CSS class for the first badge in hero section"
    },
    {
        "key": "about_hero_badge2_text",
        "label": "About Page Hero Badge 2 Text",
        "value": "All Telecoms",
        "page": "about",
        "type": "text",
        "description": "Text for the second badge in hero section"
    },
    {
        "key": "about_hero_badge2_class",
        "label": "About Page Hero Badge 2 Class",
        "value": "badge-orange",
        "page": "about",
        "type": "text",
        "description": "CSS class for the second badge in hero section"
    },
    {
        "key": "about_hero_badge3_text",
        "label": "About Page Hero Badge 3 Text",
        "value": "EN • LG • SW",
        "page": "about",
        "type": "text",
        "description": "Text for the third badge in hero section"
    },
    {
        "key": "about_hero_badge3_class",
        "label": "About Page Hero Badge 3 Class",
        "value": "badge-teal",
        "page": "about",
        "type": "text",
        "description": "CSS class for the third badge in hero section"
    },

    # =========================
    # ABOUT PAGE - IDENTITY SECTION (Who We Are / Stats)
    # =========================
    {
        "key": "about_identity_stat1_title",
        "label": "About Page Identity Stat 1 Title",
        "value": "116",
        "page": "about",
        "type": "heading",
        "description": "Title for the first identity stat card"
    },
    {
        "key": "about_identity_stat1_text",
        "label": "About Page Identity Stat 1 Text",
        "value": "National Helpline",
        "page": "about",
        "type": "text",
        "description": "Text for the first identity stat card"
    },
    {
        "key": "about_identity_stat1_icon",
        "label": "About Page Identity Stat 1 Icon",
        "value": "Phone",
        "page": "about",
        "type": "icon",
        "description": "Icon for the first identity stat card (Heroicon name)"
    },
    {
        "key": "about_identity_stat1_color_from",
        "label": "About Page Identity Stat 1 Color From",
        "value": "blue-500",
        "page": "about",
        "type": "text",
        "description": "Tailwind gradient start color for stat card 1"
    },
    {
        "key": "about_identity_stat1_color_to",
        "label": "About Page Identity Stat 1 Color To",
        "value": "blue-600",
        "page": "about",
        "type": "text",
        "description": "Tailwind gradient end color for stat card 1"
    },

    {
        "key": "about_identity_stat2_title",
        "label": "About Page Identity Stat 2 Title",
        "value": "24/7",
        "page": "about",
        "type": "heading",
        "description": "Title for the second identity stat card"
    },
    {
        "key": "about_identity_stat2_text",
        "label": "About Page Identity Stat 2 Text",
        "value": "Always Available",
        "page": "about",
        "type": "text",
        "description": "Text for the second identity stat card"
    },
    {
        "key": "about_identity_stat2_icon",
        "label": "About Page Identity Stat 2 Icon",
        "value": "Clock",
        "page": "about",
        "type": "icon",
        "description": "Icon for the second identity stat card (Heroicon name)"
    },
    {
        "key": "about_identity_stat2_color_from",
        "label": "About Page Identity Stat 2 Color From",
        "value": "teal-500",
        "page": "about",
        "type": "text",
        "description": "Tailwind gradient start color for stat card 2"
    },
    {
        "key": "about_identity_stat2_color_to",
        "label": "About Page Identity Stat 2 Color To",
        "value": "teal-600",
        "page": "about",
        "type": "text",
        "description": "Tailwind gradient end color for stat card 2"
    },

    {
        "key": "about_identity_stat3_title",
        "label": "About Page Identity Stat 3 Title",
        "value": "10+",
        "page": "about",
        "type": "heading",
        "description": "Title for the third identity stat card"
    },
    {
        "key": "about_identity_stat3_text",
        "label": "About Page Identity Stat 3 Text",
        "value": "Languages",
        "page": "about",
        "type": "text",
        "description": "Text for the third identity stat card"
    },
    {
        "key": "about_identity_stat3_icon",
        "label": "About Page Identity Stat 3 Icon",
        "value": "GlobeAlt",
        "page": "about",
        "type": "icon",
        "description": "Icon for the third identity stat card (Heroicon name)"
    },
    {
        "key": "about_identity_stat3_color_from",
        "label": "About Page Identity Stat 3 Color From",
        "value": "orange-500",
        "page": "about",
        "type": "text",
        "description": "Tailwind gradient start color for stat card 3"
    },
    {
        "key": "about_identity_stat3_color_to",
        "label": "About Page Identity Stat 3 Color To",
        "value": "orange-600",
        "page": "about",
        "type": "text",
        "description": "Tailwind gradient end color for stat card 3"
    },

    {
        "key": "about_identity_stat4_title",
        "label": "About Page Identity Stat 4 Title",
        "value": "Free",
        "page": "about",
        "type": "heading",
        "description": "Title for the fourth identity stat card"
    },
    {
        "key": "about_identity_stat4_text",
        "label": "About Page Identity Stat 4 Text",
        "value": "Confidential Support",
        "page": "about",
        "type": "text",
        "description": "Text for the fourth identity stat card"
    },
    {
        "key": "about_identity_stat4_icon",
        "label": "About Page Identity Stat 4 Icon",
        "value": "LockClosed",
        "page": "about",
        "type": "icon",
        "description": "Icon for the fourth identity stat card (Heroicon name)"
    },
    {
        "key": "about_identity_stat4_color_from",
        "label": "About Page Identity Stat 4 Color From",
        "value": "purple-500",
        "page": "about",
        "type": "text",
        "description": "Tailwind gradient start color for stat card 4"
    },
    {
        "key": "about_identity_stat4_color_to",
        "label": "About Page Identity Stat 4 Color To",
        "value": "purple-600",
        "page": "about",
        "type": "text",
        "description": "Tailwind gradient end color for stat card 4"
    },

    # =========================
    # ABOUT PAGE - SERVICES SECTION (What We Do)
    # =========================
    {
        "key": "about_services_title",
        "label": "About Page Services Title",
        "value": "Our Comprehensive Support Services",
        "page": "about",
        "type": "heading",
        "description": "Title for the services section"
    },
    {
        "key": "about_services_description",
        "label": "About Page Services Description",
        "value": (
            "Sauti provides a range of critical services designed to protect and empower "
            "vulnerable individuals across Uganda. Our approach is holistic, ensuring "
            "that every caller receives the support they need."
        ),
        "page": "about",
        "type": "text",
        "description": "Description for the services section"
    },
    {
        "key": "about_services_item1_title",
        "label": "About Page Service 1 Title",
        "value": "Confidential Counseling",
        "page": "about",
        "type": "heading",
        "description": "Title for the first service item"
    },
    {
        "key": "about_services_item1_text",
        "label": "About Page Service 1 Text",
        "value": "Immediate, private support from trained counselors.",
        "page": "about",
        "type": "text",
        "description": "Text for the first service item"
    },
    {
        "key": "about_services_item1_icon",
        "label": "About Page Service 1 Icon",
        "value": "ChatAlt2",
        "page": "about",
        "type": "icon",
        "description": "Icon for the first service item (Heroicon name)"
    },
    {
        "key": "about_services_item1_color",
        "label": "About Page Service 1 Color",
        "value": "blue",
        "page": "about",
        "type": "text",
        "description": "Tailwind color for the first service item"
    },

    {
        "key": "about_services_item2_title",
        "label": "About Page Service 2 Title",
        "value": "Crisis Intervention",
        "page": "about",
        "type": "heading",
        "description": "Title for the second service item"
    },
    {
        "key": "about_services_item2_text",
        "label": "About Page Service 2 Text",
        "value": "Rapid response to urgent situations and emergencies.",
        "page": "about",
        "type": "text",
        "description": "Text for the second service item"
    },
    {
        "key": "about_services_item2_icon",
        "label": "About Page Service 2 Icon",
        "value": "ExclamationCircle",
        "page": "about",
        "type": "icon",
        "description": "Icon for the second service item (Heroicon name)"
    },
    {
        "key": "about_services_item2_color",
        "label": "About Page Service 2 Color",
        "value": "teal",
        "page": "about",
        "type": "text",
        "description": "Tailwind color for the second service item"
    },

    {
        "key": "about_services_item3_title",
        "label": "About Page Service 3 Title",
        "value": "Referral Services",
        "page": "about",
        "type": "heading",
        "description": "Title for the third service item"
    },
    {
        "key": "about_services_item3_text",
        "label": "About Page Service 3 Text",
        "value": "Connecting callers to health, legal, and social support.",
        "page": "about",
        "type": "text",
        "description": "Text for the third service item"
    },
    {
        "key": "about_services_item3_icon",
        "label": "About Page Service 3 Icon",
        "value": "Link",
        "page": "about",
        "type": "icon",
        "description": "Icon for the third service item (Heroicon name)"
    },
    {
        "key": "about_services_item3_color",
        "label": "About Page Service 3 Color",
        "value": "orange",
        "page": "about",
        "type": "text",
        "description": "Tailwind color for the third service item"
    },

    {
        "key": "about_services_item4_title",
        "label": "About Page Service 4 Title",
        "value": "Information & Guidance",
        "page": "about",
        "type": "heading",
        "description": "Title for the fourth service item"
    },
    {
        "key": "about_services_item4_text",
        "label": "About Page Service 4 Text",
        "value": "Providing vital knowledge on rights and protection.",
        "page": "about",
        "type": "text",
        "description": "Text for the fourth service item"
    },
    {
        "key": "about_services_item4_icon",
        "label": "About Page Service 4 Icon",
        "value": "InformationCircle",
        "page": "about",
        "type": "icon",
        "description": "Icon for the fourth service item (Heroicon name)"
    },
    {
        "key": "about_services_item4_color",
        "label": "About Page Service 4 Color",
        "value": "purple",
        "page": "about",
        "type": "text",
        "description": "Tailwind color for the fourth service item"
    },

    {
        "key": "about_services_item5_title",
        "label": "About Page Service 5 Title",
        "value": "Follow-up & Case Management",
        "page": "about",
        "type": "heading",
        "description": "Title for the fifth service item"
    },
    {
        "key": "about_services_item5_text",
        "label": "About Page Service 5 Text",
        "value": "Ensuring sustained support and resolution for complex cases.",
        "page": "about",
        "type": "text",
        "description": "Text for the fifth service item"
    },
    {
        "key": "about_services_item5_icon",
        "label": "About Page Service 5 Icon",
        "value": "ClipboardList",
        "page": "about",
        "type": "icon",
        "description": "Icon for the fifth service item (Heroicon name)"
    },
    {
        "key": "about_services_item5_color",
        "label": "About Page Service 5 Color",
        "value": "green",
        "page": "about",
        "type": "text",
        "description": "Tailwind color for the fifth service item"
    },

    # Core Values Title (used in services section)
    {
        "key": "about_values_title",
        "label": "About Page Core Values Title",
        "value": "Our Core Values",
        "page": "about",
        "type": "heading",
        "description": "Title for the core values section"
    },







    # =========================
    # ABOUT PAGE - TRUST SIGNALS SECTION (Partners / Legitimacy)
    # =========================
    {
        "key": "about_trust_signals_title",
        "label": "About Page Trust Signals Title",
        "value": "Our Valued Partners",
        "page": "about",
        "type": "heading",
        "description": "Title for the trust signals section"
    },
    {
        "key": "about_trust_signals_description",
        "label": "About Page Trust Signals Description",
        "value": "Collaborating with leading organizations to amplify our impact.",
        "page": "about",
        "type": "text",
        "description": "Description for the trust signals section"
    },
    {
        "key": "about_trust_signals_partner1",
        "label": "About Page Trust Signals Partner 1",
        "value": "Ministry of Gender, Labour and Social Development",
        "page": "about",
        "type": "text",
        "description": "Name of the first partner"
    },
    {
        "key": "about_trust_signals_partner2",
        "label": "About Page Trust Signals Partner 2",
        "value": "UNICEF Uganda",
        "page": "about",
        "type": "text",
        "description": "Name of the second partner"
    },
    {
        "key": "about_trust_signals_partner3",
        "label": "About Page Trust Signals Partner 3",
        "value": "Uganda Police Force",
        "page": "about",
        "type": "text",
        "description": "Name of the third partner"
    },
    {
        "key": "about_trust_signals_partner4",
        "label": "About Page Trust Signals Partner 4",
        "value": "ChildFund International",
        "page": "about",
        "type": "text",
        "description": "Name of the fourth partner"
    },

    # =========================
    # ABOUT PAGE - CALL TO ACTION SECTION
    # =========================
    {
        "key": "about_call_to_action_title",
        "label": "About Page CTA Title",
        "value": "Make a Difference Today",
        "page": "about",
        "type": "heading",
        "description": "Title for the call to action section"
    },
    {
        "key": "about_call_to_action_text",
        "label": "About Page CTA Text",
        "value": "Your support helps us protect vulnerable children and individuals. Get involved or reach out for help.",
        "page": "about",
        "type": "text",
        "description": "Text for the call to action section"
    },
    {
        "key": "about_call_to_action_cta_call",
        "label": "About Page CTA Call Button",
        "value": "Call 116",
        "page": "about",
        "type": "button",
        "description": "Call button text for CTA section"
    },
    {
        "key": "about_call_to_action_cta_report",
        "label": "About Page CTA Report Button",
        "value": "Report a Case",
        "page": "about",
        "type": "button",
        "description": "Report button text for CTA section"
    },
    {
        "key": "about_call_to_action_cta_contact",
        "label": "About Page CTA Contact Button",
        "value": "Contact Us",
        "page": "about",
        "type": "button",
        "description": "Contact button text for CTA section"
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

    # =========================
    # CONTACT PAGE INFO
    # =========================
    {
        "key": "contact_phone_main",
        "label": "Main Support Phone",
        "value": "116",
        "page": "contact",
        "type": "text",
        "description": "Primary hotline number"
    },
    {
        "key": "contact_email_info",
        "label": "General Info Email",
        "value": "info@sauti.mglsd.go.ug",
        "page": "contact",
        "type": "text",
        "description": "General inquiries email"
    },
    {
        "key": "contact_email_sautichl",
        "label": "Sauti CHL Email",
        "value": "sautichl@mglsd.go.ug",
        "page": "contact",
        "type": "text",
        "description": "Helpline specific email"
    },
    {
        "key": "contact_website",
        "label": "Website URL",
        "value": "https://sauti.mglsd.go.ug",
        "page": "contact",
        "type": "text",
        "description": "Official website link"
    },
    {
        "key": "office_address",
        "label": "Office Address",
        "value": "Ministry of Gender, Labour and Social Development, P.O. Box 7136, Kampala, Uganda",
        "page": "contact",
        "type": "text",
        "description": "Physical office address"
    },

    # =========================
    # FOOTER / SOCIAL MEDIA
    # =========================
    {
        "key": "social_facebook",
        "label": "Facebook URL",
        "value": "https://www.facebook.com/Sauti116Helpline",
        "page": "footer",
        "type": "text",
        "description": "Facebook page link"
    },
    {
        "key": "social_twitter",
        "label": "Twitter/X URL",
        "value": "https://x.com/sauti116",
        "page": "footer",
        "type": "text",
        "description": "Twitter profile link"
    },
    {
        "key": "social_whatsapp",
        "label": "WhatsApp URL",
        "value": "https://wa.me/256743889999",
        "page": "footer",
        "type": "text",
        "description": "WhatsApp contact link"
    },
    {
        "key": "social_instagram",
        "label": "Instagram URL",
        "value": "https://instagram.com",
        "page": "footer",
        "type": "text",
        "description": "Instagram profile link"
    },
    {
        "key": "social_linkedin",
        "label": "LinkedIn URL",
        "value": "https://linkedin.com",
        "page": "footer",
        "type": "text",
        "description": "LinkedIn profile link"
    },
    {
        "key": "social_youtube",
        "label": "YouTube URL",
        "value": "https://youtube.com",
        "page": "footer",
        "type": "text",
        "description": "YouTube channel link"
    },
    {
        "key": "social_tiktok",
        "label": "TikTok URL",
        "value": "https://tiktok.com",
        "page": "footer",
        "type": "text",
        "description": "TikTok profile link"
    },
    {
        "key": "social_ureport",
        "label": "U-Report URL",
        "value": "https://ureport.in",
        "page": "footer",
        "type": "text",
        "description": "U-Report link"
    },
    {
        "key": "social_safepal",
        "label": "SafePal URL",
        "value": "https://www.unicef.org/uganda/safepal-app",
        "page": "footer",
        "type": "text",
        "description": "SafePal link"
    },
    {
        "key": "footer_text",
        "label": "Footer Copyright Text",
        "value": "© 2025 Sauti 116. All rights reserved.",
        "page": "footer",
        "type": "text",
        "description": "Copyright notice"
    },
    {
        "key": "ministry_attribution_text",
        "label": "Ministry Attribution",
        "value": "A project of the Ministry of Gender, Labour and Social Development, supported by UNICEF & partners.",
        "page": "footer",
        "type": "text",
        "description": "Ministry attribution text"
    },
    {
        "key": "disclaimer_text",
        "label": "Disclaimer Text",
        "value": "Information shared on this platform is for guidance and assistance. In case of emergency, always call 116 immediately.",
        "page": "footer",
        "type": "text",
        "description": "Legal disclaimer"
    },
    {
        "key": "privacy_policy_url",
        "label": "Privacy Policy URL",
        "value": "/privacy",
        "page": "footer",
        "type": "text",
        "description": "Link to privacy policy"
    },
    {
        "key": "terms_of_service_url",
        "label": "Terms of Service URL",
        "value": "/terms",
        "page": "footer",
        "type": "text",
        "description": "Link to terms of service"
    },
    {
        "key": "accessibility_url",
        "label": "Accessibility URL",
        "value": "/accessibility",
        "page": "footer",
        "type": "text",
        "description": "Link to accessibility statement"
    },

    # =========================
    # GLOBAL SETTINGS
    # =========================
    {
        "key": "site_name",
        "label": "Site Name",
        "value": "Sauti 116",
        "page": "global",
        "type": "text",
        "description": "Global application name"
    },
    {
        "key": "site_description",
        "label": "Site Description",
        "value": "Sauti is Uganda’s national toll-free helpline operated under the Ministry of Gender, Labour and Social Development.",
        "page": "global",
        "type": "text",
        "description": "Meta description for SEO"
    },
    {
        "key": "mission_statement",
        "label": "Mission Statement",
        "value": "To provide a confidential, toll-free, and 24/7 helpline service for reporting abuse and seeking help.",
        "page": "global",
        "type": "text",
        "description": "Organization mission"
    },
    {
        "key": "vision_statement",
        "label": "Vision Statement",
        "value": "A society where every child and vulnerable person is safe, heard, and protected.",
        "page": "global",
        "type": "text",
        "description": "Organization vision"
    },
    {
        "key": "hotline_text",
        "label": "Hotline Text",
        "value": "Toll-free National Helpline",
        "page": "global",
        "type": "text",
        "description": "Text displayed next to hotline"
    },
    {
        "key": "operating_hours_text",
        "label": "Operating Hours",
        "value": "24/7",
        "page": "global",
        "type": "text",
        "description": "Operating hours definition"
    },
    {
        "key": "primary_cta_text",
        "label": "Primary CTA Text",
        "value": "Get Help Now",
        "page": "global",
        "type": "text",
        "description": "Text for primary call to action buttons"
    }
]

def populate_initial_content():
    created_count = 0
    updated_count = 0

    # Keys to be removed (old keys that are replaced by new structured keys)
    keys_to_remove = [
        "about_title", "about_description", "about_image",
        "aboutStat1Title", "aboutStat1Text",
        "aboutStat2Title", "aboutStat2Text",
        "aboutStat3Title", "aboutStat3Text",
        "aboutStat4Title", "aboutStat4Text",
        "aboutMissionTitle", "aboutMissionText",
        "aboutService1Title", "aboutService1Text",
        "aboutService2Title", "aboutService2Text",
        "aboutService3Title", "aboutService3Text",
        "aboutService4Title", "aboutService4Text",
        "aboutService5Title", "aboutService5Text",
        "aboutPartnersTitle", "aboutPartner1", "aboutPartner2", "aboutPartner3",
        "aboutPartner4", "aboutPartnersText",
        "aboutCtaTitle", "aboutCtaText", "aboutCtaCall", "aboutCtaReport", "aboutCtaContact",
    ]

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

    # Remove old keys that are no longer used
    deleted_count = SiteContent.objects.filter(key__in=keys_to_remove).delete()
    if deleted_count[0] > 0:
        print(f"Removed {deleted_count[0]} old SiteContent entries.")

    print(f"Content setup complete: {created_count} created, {updated_count} updated.")

def populate_global_settings():
    settings, created = GlobalSettings.objects.get_or_create()
    settings.site_name = "Sauti 116"
    settings.site_description = "Sauti is Uganda’s national toll-free helpline operated under the Ministry of Gender, Labour and Social Development."
    settings.hotline_number = "116"
    settings.primary_cta_text = "Get Help Now"
    settings.hotline_text = "Toll-free National Helpline"
    settings.support_email_text = "info@sauti.mglsd.go.ug"
    settings.operating_hours_text = "24/7"
    
    settings.footer_text = "© 2025 Sauti 116. All rights reserved."
    settings.ministry_attribution_text = "A project of the Ministry of Gender, Labour and Social Development, supported by UNICEF & partners."
    settings.disclaimer_text = "Information shared on this platform is for guidance and assistance. In case of emergency, always call 116 immediately."
    settings.privacy_policy_url = "https://sauti.mglsd.go.ug/privacy"

    # 1. Hero
    settings.hero_title = "Every voice matters. Every life deserves protection."
    settings.hero_subtitle = "Sauti 116 provides confidential, 24/7 support for children, survivors of gender-based violence, and migrant workers."
    settings.hero_value_prop = "Free and accessible across all telecom networks in multiple local languages."

    # 2. Intro
    settings.intro_title = "Who We Are"
    settings.intro_description = "Sauti 116 is Uganda’s National Child Helpline, a confidential service that provides support, guidance, and crisis intervention for children and individuals facing violence, exploitation, or abuse."

    # 3. Quick Access
    settings.quick_access_title = "How Can We Help?"
    settings.quick_access_description = "Our trained counselors offer immediate assistance and referrals for various protection needs."
    
    settings.qa_child_protection_title = "Child Protection"
    settings.qa_child_protection_text = "Report abuse, exploitation, or neglect. We provide immediate safety guidance and referrals."
    settings.qa_child_protection_icon = "UserGroupIcon"
    
    settings.qa_gbv_title = "GBV Support"
    settings.qa_gbv_text = "Safe space for survivors of gender-based violence to seek support and legal guidance."
    settings.qa_gbv_icon = "ShieldCheckIcon"
    
    settings.qa_migrants_title = "Migrant Workers"
    settings.qa_migrants_text = "Support for migrant workers in distress or facing exploitation, both home and abroad."
    settings.qa_migrants_icon = "GlobeAltIcon"
    
    settings.qa_psea_title = "PSEA"
    settings.qa_psea_text = "Protection from Sexual Exploitation and Abuse. Report misconduct and seek justice."
    settings.qa_psea_icon = "ScaleIcon"

    # 4. News
    settings.news_title = "Latest Stories & Updates"
    settings.news_description = "Stay informed with the latest news from Sauti and our work across communities."
    settings.news_link_text = "View All Articles"

    # 5. Partners
    settings.partners_title = "Our Trusted Partners"
    settings.partners_description = "Working together with national and international organizations to protect every voice."

    # Social & Links
    settings.social_facebook = "https://www.facebook.com/Sauti116Helpline"
    settings.social_twitter = "https://x.com/sauti116"
    settings.social_whatsapp = "https://wa.me/256743889999"
    settings.social_ureport = "https://ureport.in"
    settings.social_safepal = "https://www.unicef.org/uganda/safepal-app"
    
    settings.contact_email_info = "info@sauti.mglsd.go.ug"
    settings.contact_email_sautichl = "sautichl@mglsd.go.ug"
    settings.contact_website = "https://sauti.mglsd.go.ug"
    settings.contact_phone_main = "116"
    
    settings.save()
    print("Unified Homepage Settings successfully populated.")


if __name__ == "__main__":
    populate_initial_content()
    populate_global_settings()
