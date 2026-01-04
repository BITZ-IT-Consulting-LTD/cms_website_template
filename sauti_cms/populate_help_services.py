import os
import django
import sys
from pathlib import Path

# Add the project directory to Python path
BASE_DIR = Path(__file__).resolve().parent
sys.path.append(str(BASE_DIR))

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cms.settings')
django.setup()

from services.models import HelpService, HelpStep

def populate_help_services():
    """
    Populates the HelpService model with default content.
    """
    print("Populating HelpService model...")
    
    services_data = [
        {
            'key': 'child-protection',
            'title': 'Child Protection',
            'intro_text': "We provide immediate support and intervention for children at risk of abuse, neglect, or exploitation. Our services include emergency response, counseling, family reunification, and long-term case management. If you know a child who needs help, or if you are a child in danger, call us immediately on 116.",
            'scope_items': [
                "Emergency response for physical abuse",
                "Support for neglected children",
                "Intervention in child labor cases",
                "Protection from child marriage",
                "Family reunification services"
            ],
            'summary': "Immediate support and intervention for children at risk of abuse, neglect, or exploitation.",
            'icon_name': 'UserGroupIcon',
            'order': 1,
            'steps': [
                {'title': 'Call 116', 'description': 'Dial 116 immediately to report a case.', 'step_order': 1},
                {'title': 'Assessment', 'description': 'A counselor will assess the situation and safety risks.', 'step_order': 2},
                {'title': 'Intervention', 'description': 'We coordinate with local authorities for immediate protection.', 'step_order': 3},
                {'title': 'Follow-up', 'description': 'Ongoing support and case management until resolution.', 'step_order': 4},
            ]
        },
        {
            'key': 'gbv',
            'title': 'Gender-Based Violence',
            'intro_text': "Gender-Based Violence (GBV) survivors deserve compassionate, professional support. We offer crisis counseling, medical referrals, legal assistance, and safe shelter coordination. Our services are available to all survivors regardless of gender, age, or background.",
            'scope_items': [
                "Crisis counseling for survivors",
                "Medical referrals and support",
                "Legal assistance and advice",
                "Safe shelter coordination",
                "Psychosocial support"
            ],
            'summary': "Crisis counseling, medical referrals, and legal assistance for GBV survivors.",
            'icon_name': 'ShieldCheckIcon',
            'order': 2,
            'steps': [
                {'title': 'Contact Us', 'description': 'Call 116 for confidential support.', 'step_order': 1},
                {'title': 'Counseling', 'description': 'Speak with a trained counselor for emotional support.', 'step_order': 2},
                {'title': 'Referrals', 'description': 'We connect you with medical and legal experts.', 'step_order': 3},
                {'title': 'Safety Planning', 'description': 'Develop a plan for your ongoing safety.', 'step_order': 4},
            ]
        },
        {
            'key': 'migrants',
            'title': 'Migrant Workers',
            'intro_text': "Migrant workers face unique challenges. Sauti 116 provides information on labor rights, assistance with employment disputes, and connections to legal support. We help migrant workers understand their rights, report abuse, and access healthcare and social services.",
            'scope_items': [
                "Labor rights information",
                "Employment dispute assistance",
                "Legal support connection",
                "Healthcare access guidance",
                "Report abuse tracking"
            ],
            'summary': "Information on labor rights, employment disputes, and legal support for migrant workers.",
            'icon_name': 'GlobeAltIcon',
            'order': 3,
            'steps': [
                {'title': 'Reach Out', 'description': 'Call or message for advice on your rights.', 'step_order': 1},
                {'title': 'Verification', 'description': 'We verify your employment and legal status queries.', 'step_order': 2},
                {'title': 'Guidance', 'description': 'Get connected to legal and labor support.', 'step_order': 3},
                {'title': 'Resolution', 'description': 'Support through dispute resolution processes.', 'step_order': 4},
            ]
        },
        {
            'key': 'psea',
            'title': 'PSEA',
            'intro_text': "Protection from Sexual Exploitation and Abuse (PSEA) is a fundamental right. If you have experienced or witnessed sexual exploitation or abuse by aid workers or anyone in a position of power, we provide a safe, confidential channel to report these incidents.",
            'scope_items': [
                "Confidential reporting channel",
                "Independent investigation support",
                "Victim assistance services",
                "Accountability tracking",
                "Awareness and prevention"
            ],
            'summary': "Safe, confidential channel to report sexual exploitation and abuse by aid workers.",
            'icon_name': 'ScaleIcon',
            'order': 4,
            'steps': [
                {'title': 'Report Safely', 'description': 'Use our confidential channels to report abuse.', 'step_order': 1},
                {'title': 'Documentation', 'description': 'Your report is securely documented.', 'step_order': 2},
                {'title': 'Investigation', 'description': 'Independent bodies investigate the claim.', 'step_order': 3},
                {'title': 'Action', 'description': 'Ensuring accountability and support for victims.', 'step_order': 4},
            ]
        },
    ]

    created_count = 0
    updated_count = 0

    for service_data in services_data:
        steps_data = service_data.pop('steps')
        service_obj, created = HelpService.objects.update_or_create(
            key=service_data['key'],
            defaults=service_data
        )
        
        if created:
            created_count += 1
            print(f"Created HelpService: {service_data['title']}")
        else:
            updated_count += 1
            print(f"Updated HelpService: {service_data['title']}")

        # Populate steps
        for step_data in steps_data:
            HelpStep.objects.update_or_create(
                service=service_obj,
                step_order=step_data['step_order'],
                defaults=step_data
            )

    print(f"HelpService population complete. {created_count} created, {updated_count} updated.")

if __name__ == '__main__':
    populate_help_services()
