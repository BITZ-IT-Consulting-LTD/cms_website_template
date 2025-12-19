import os
import django
from datetime import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sauti_cms.settings')
django.setup()

from content.models import CoreValue, TimelineEvent, ProtectionApproach, TeamMember

def populate_about_page_content():
    print("Populating About Page content...")

    # Clear existing data to prevent duplicates on re-run
    CoreValue.objects.all().delete()
    TimelineEvent.objects.all().delete()
    ProtectionApproach.objects.all().delete()
    TeamMember.objects.all().delete()
    print("Cleared existing About Page content.")

    # Core Values
    core_values_data = [
        {
            "title": "Integrity",
            "description": "Upholding the highest ethical standards in all our actions.",
            "icon": "ShieldCheck",
            "color_from": "blue-500",
            "color_to": "blue-600",
            "border_color": "blue-500",
        },
        {
            "title": "Compassion",
            "description": "Responding to every call with empathy and understanding.",
            "icon": "Heart",
            "color_from": "red-500",
            "color_to": "red-600",
            "border_color": "red-500",
        },
        {
            "title": "Empowerment",
            "description": "Enabling individuals to make informed decisions and take control.",
            "icon": "Bolt",
            "color_from": "yellow-500",
            "color_to": "yellow-600",
            "border_color": "yellow-500",
        },
        {
            "title": "Confidentiality",
            "description": "Ensuring privacy and trust in every interaction.",
            "icon": "LockClosed",
            "color_from": "gray-500",
            "color_to": "gray-600",
            "border_color": "gray-500",
        },
        {
            "title": "Collaboration",
            "description": "Working with partners for a stronger, unified response.",
            "icon": "UserGroup",
            "color_from": "green-500",
            "color_to": "green-600",
            "border_color": "green-500",
        },
    ]
    for data in core_values_data:
        CoreValue.objects.create(**data)
    print(f"Populated {len(core_values_data)} Core Values.")

    # Timeline Events
    timeline_events_data = [
        {
            "title": "Sauti Helpline Established",
            "description": "Uganda's national toll-free helpline 116 officially launched.",
            "date": datetime(2015, 1, 1),
            "icon": "Phone",
        },
        {
            "title": "Nationwide Expansion",
            "description": "Services expanded to cover all telecom networks across Uganda.",
            "date": datetime(2017, 6, 15),
            "icon": "GlobeAlt",
        },
        {
            "title": "Partnership with UNICEF",
            "description": "Formal collaboration with UNICEF Uganda to strengthen child protection services.",
            "date": datetime(2018, 11, 1),
            "icon": "HandRaised",
        },
        {
            "title": "GBV Support Integration",
            "description": "Integrated specialized support for Gender-Based Violence survivors.",
            "date": datetime(2020, 3, 1),
            "icon": "Users",
        },
        {
            "title": "Migrant Worker Protection",
            "description": "Launched dedicated services for Ugandan migrant workers in distress abroad.",
            "date": datetime(2022, 9, 1),
            "icon": "Briefcase",
        },
    ]
    for data in timeline_events_data:
        TimelineEvent.objects.create(**data)
    print(f"Populated {len(timeline_events_data)} Timeline Events.")

    # Protection Approaches
    protection_approaches_data = [
        {
            "title": "24/7 Helpline Access",
            "description": "Ensuring immediate support is always available, day or night.",
            "icon": "Clock",
        },
        {
            "title": "Confidentiality & Anonymity",
            "description": "Protecting caller identities and sensitive information.",
            "icon": "LockClosed",
        },
        {
            "title": "Trained Counselors",
            "description": "Expert counselors providing trauma-informed and empathetic support.",
            "icon": "AcademicCap",
        },
        {
            "title": "Nationwide Referral Network",
            "description": "Connecting callers to local services across all regions.",
            "icon": "MapPin",
        },
        {
            "title": "Case Management",
            "description": "Structured follow-up to ensure effective resolution and support.",
            "icon": "ClipboardDocumentList",
        },
    ]
    for data in protection_approaches_data:
        ProtectionApproach.objects.create(**data)
    print(f"Populated {len(protection_approaches_data)} Protection Approaches.")

    # Team Members
    team_members_data = [
        {
            "name": "Dr. Aisha Nalubega",
            "role": "Executive Director",
            "image": "/assets/team/aisha_nalubega.webp",
            "bio": "Dr. Nalubega leads Sauti with over 20 years of experience in child protection and social policy.",
        },
        {
            "name": "Mr. David Okello",
            "role": "Head of Operations",
            "image": "/assets/team/david_okello.webp",
            "bio": "David oversees the daily functioning of the helpline, ensuring seamless service delivery.",
        },
        {
            "name": "Ms. Grace Akello",
            "role": "Lead Counselor",
            "image": "/assets/team/grace_akello.webp",
            "bio": "Grace is a seasoned counselor specializing in trauma and gender-based violence support.",
        },
        {
            "name": "Mr. Samuel Mugisha",
            "role": "Partnership Coordinator",
            "image": "/assets/team/samuel_mugisha.webp",
            "bio": "Samuel builds and maintains relationships with Sauti's network of national and international partners.",
        },
    ]
    for data in team_members_data:
        TeamMember.objects.create(**data)
    print(f"Populated {len(team_members_data)} Team Members.")

    print("About Page content population complete.")

if __name__ == "__main__":
    populate_about_page_content()
