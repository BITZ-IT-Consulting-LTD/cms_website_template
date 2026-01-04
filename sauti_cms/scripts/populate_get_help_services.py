"""
Populate Get Help Services content in GlobalSettings.

This script seeds the Quick Access / Get Help services section with
realistic content for Child Protection, GBV Support, Migrant Workers, and PSEA.

Run with: python manage.py shell < scripts/populate_get_help_services.py
"""

from sitesettings.models import GlobalSettings


def populate_get_help_services():
    """Populate Get Help services content."""
    
    # Get or create GlobalSettings instance
    settings, created = GlobalSettings.objects.get_or_create()
    
    # Section Header
    settings.quick_access_title = "How Can We Help You?"
    settings.quick_access_description = (
        "Sauti 116 provides free, confidential support for children, families, and vulnerable individuals. "
        "Our trained counselors are available 24/7 to listen, guide, and connect you with the help you need. "
        "Choose a service below to learn more."
    )
    
    # Child Protection Service
    settings.qa_child_protection_title = "Child Protection"
    settings.qa_child_protection_text = (
        "We provide immediate support and intervention for children at risk of abuse, neglect, or exploitation. "
        "Our services include emergency response, counseling, family reunification, and long-term case management. "
        "If you know a child who needs help, or if you are a child in danger, call us immediately on 116. "
        "All reports are treated with strict confidentiality and handled by trained child protection specialists."
    )
    settings.qa_child_protection_icon = "UserGroupIcon"
    
    # GBV Support Service
    settings.qa_gbv_title = "GBV Support"
    settings.qa_gbv_text = (
        "Gender-Based Violence (GBV) survivors deserve compassionate, professional support. "
        "We offer crisis counseling, medical referrals, legal assistance, and safe shelter coordination. "
        "Our services are available to all survivors regardless of gender, age, or background. "
        "We work with a network of healthcare providers, police, and legal aid organizations to ensure comprehensive care. "
        "Your safety and wellbeing are our top priorities. Call 116 for immediate, confidential support."
    )
    settings.qa_gbv_icon = "ShieldCheckIcon"
    
    # Migrant Workers Service
    settings.qa_migrants_title = "Migrant Workers"
    settings.qa_migrants_text = (
        "Migrant workers face unique challenges including exploitation, unsafe working conditions, and limited access to services. "
        "Sauti 116 provides information on labor rights, assistance with employment disputes, and connections to legal support. "
        "We help migrant workers understand their rights, report abuse, and access healthcare and social services. "
        "Our multilingual counselors can assist you in multiple languages. "
        "Whether you're facing wage theft, unsafe conditions, or need help navigating the system, we're here for you."
    )
    settings.qa_migrants_icon = "GlobeAltIcon"
    
    # PSEA Service
    settings.qa_psea_title = "PSEA"
    settings.qa_psea_text = (
        "Protection from Sexual Exploitation and Abuse (PSEA) is a fundamental right. "
        "If you have experienced or witnessed sexual exploitation or abuse by aid workers, peacekeepers, or anyone in a position of power, "
        "we provide a safe, confidential channel to report these incidents. "
        "We work with international organizations and local authorities to investigate complaints and ensure accountability. "
        "Your report will be taken seriously, handled with sensitivity, and you will be connected with appropriate support services. "
        "No one should abuse their position of trust. Speak up safely through Sauti 116."
    )
    settings.qa_psea_icon = "ScaleIcon"
    
    # Save the settings
    settings.save()
    
    action = "Created" if created else "Updated"
    print(f"✓ {action} Get Help Services content in GlobalSettings")
    print("\nService Content Summary:")
    print(f"  • Section Title: {settings.quick_access_title}")
    print(f"  • Child Protection: {settings.qa_child_protection_title}")
    print(f"  • GBV Support: {settings.qa_gbv_title}")
    print(f"  • Migrant Workers: {settings.qa_migrants_title}")
    print(f"  • PSEA: {settings.qa_psea_title}")
    print("\nAll Get Help services have been populated with production-ready content.")


if __name__ == '__main__':
    print("Populating Get Help Services content...")
    print("-" * 60)
    populate_get_help_services()
    print("-" * 60)
    print("✓ Get Help Services population complete!")

# Auto-execute when run via manage.py shell
populate_get_help_services()
