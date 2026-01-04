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
            "title": "Unwavering Integrity",
            "description": "Upholding uncompromising ethical standards in National Protection.",
            "icon": "ShieldCheck",
            "color_from": "blue-500",
            "color_to": "blue-600",
            "border_color": "blue-500",
        },
        {
            "title": "Active Compassion",
            "description": "Responding to every crisis with immediate, decisive support.",
            "icon": "Heart",
            "color_from": "red-500",
            "color_to": "red-600",
            "border_color": "red-500",
        },
        {
            "title": "True Empowerment",
            "description": "Enabling citizens to reclaim their safety and rights.",
            "icon": "Bolt",
            "color_from": "yellow-500",
            "color_to": "yellow-600",
            "border_color": "yellow-500",
        },
        {
            "title": "Total Confidentiality",
            "description": "Absolute privacy and security in every National report.",
            "icon": "LockClosed",
            "color_from": "gray-500",
            "color_to": "gray-600",
            "border_color": "gray-500",
        },
        {
            "title": "National Collaboration",
            "description": "Coordinating with Security Agencies for a unified response.",
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
            "title": "National Mandated Created",
            "description": "Uganda's national toll-free helpline 116 formally established by the Ministry.",
            "date": datetime(2015, 1, 1),
            "icon": "Phone",
        },
        {
            "title": "Total National Coverage",
            "description": "Unrestricted access across all telecom networks nationwide.",
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
            "title": "Rapid 24/7 Response",
            "description": "Immediate protection is always active, day or night.",
            "icon": "Clock",
        },
        {
            "title": "Uncompromising Privacy",
            "description": "Total security for caller identities and case data.",
            "icon": "LockClosed",
        },
        {
            "title": "Expert Response Team",
            "description": "Specialized counselors providing rapid and authoritative support.",
            "icon": "AcademicCap",
        },
        {
            "title": "National Intervention Network",
            "description": "Direct coordination with security and local services across all regions.",
            "icon": "MapPin",
        },
        {
            "title": "Active Case Management",
            "description": "Decisive follow-up to ensure full resolution and protection.",
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
