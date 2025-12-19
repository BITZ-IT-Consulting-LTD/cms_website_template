#!/usr/bin/env python
"""
Create sample blog posts for testing the admin dashboard.
Aligned with Sauti 116 multi-mandate (VAC, GBV, Migrant Workers, Sexual Exploitation).
"""
import os
import django
from datetime import datetime, timedelta

# Setup Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cms.settings")
django.setup()

from django.contrib.auth import get_user_model
from posts.models import Post, Category, Tag

User = get_user_model()


def populate_posts():
    """Create sample blog posts for testing"""

    # -------------------------
    # Admin User
    # -------------------------
    admin_user, created = User.objects.get_or_create(
        username="admin",
        defaults={
            "email": "admin@sauti.ug",
            "first_name": "Admin",
            "last_name": "User",
            "role": "ADMIN",
            "is_staff": True,
            "is_superuser": True,
        },
    )

    if created:
        admin_user.set_password("admin12345")
        admin_user.save()
        print("✅ Created admin user")
    else:
        print("✅ Admin user already exists")

    # -------------------------
    # Categories
    # -------------------------
    categories_data = [
        {
            "name": "Child Protection",
            "slug": "child-protection",
            "description": "Resources on violence against children, prevention, response, and child protection systems.",
        },
        {
            "name": "Gender-Based Violence",
            "slug": "gender-based-violence",
            "description": "Information and support resources for survivors of gender-based violence.",
        },
        {
            "name": "Mental Health & Psychosocial Support",
            "slug": "mental-health-psychosocial",
            "description": "Psychosocial wellbeing resources for children, adults, and survivors.",
        },
        {
            "name": "Migrant Worker Support",
            "slug": "migrant-worker-support",
            "description": "Guidance and protection information for migrant workers experiencing distress or exploitation.",
        },
        {
            "name": "Safety & Prevention",
            "slug": "safety-prevention",
            "description": "Practical safety guidance and prevention tips for vulnerable populations.",
        },
        {
            "name": "Impact & Success Stories",
            "slug": "impact-success-stories",
            "description": "Stories highlighting the impact of Sauti 116 support services.",
        },
    ]

    categories = {}
    for data in categories_data:
        category, _ = Category.objects.update_or_create(
            slug=data["slug"], 
            defaults={
                "name": data["name"],
                "description": data["description"]
            }
        )
        categories[data["slug"]] = category

    # -------------------------
    # Tags
    # -------------------------
    tags_data = [
        {"name": "Child Rights", "slug": "child-rights"},
        {"name": "GBV", "slug": "gbv"},
        {"name": "Sexual Exploitation", "slug": "sexual-exploitation"},
        {"name": "Migrant Workers", "slug": "migrant-workers"},
        {"name": "Mental Health", "slug": "mental-health"},
        {"name": "Psychosocial Support", "slug": "psychosocial-support"},
        {"name": "Safety", "slug": "safety"},
        {"name": "Community", "slug": "community"},
        {"name": "Support Services", "slug": "support-services"},
    ]

    tags = {}
    for data in tags_data:
        tag, _ = Tag.objects.update_or_create(
            slug=data["slug"], 
            defaults={"name": data["name"]}
        )
        tags[data["slug"]] = tag

    # -------------------------
    # Posts
    # -------------------------
    posts_data = [
        {
            "title": "Understanding Protection Rights in Uganda",
            "slug": "understanding-protection-rights-uganda",
            "content": """Everyone has the right to live free from violence, abuse, and exploitation.

In Uganda, national laws and international conventions protect:
- Children from violence, abuse, and neglect
- Survivors of gender-based violence
- Migrant workers from exploitation and abuse
- Individuals at risk of sexual exploitation

Sauti 116 provides a free, confidential helpline where anyone can report concerns, seek guidance, or access referrals to protection services.

If you or someone you know is experiencing violence or exploitation, call 116. Trained counselors are available 24/7 to listen, support, and guide you to help.""",
            "excerpt": "An overview of protection rights and how Sauti 116 supports children, GBV survivors, migrant workers, and others at risk.",
            "category": categories["child-protection"],
            "tags": [
                tags["child-rights"],
                tags["support-services"],
            ],
            "status": "PUBLISHED",
            "language": "en",
            "is_featured": True,
            "views_count": 3100,
        },
        {
            "title": "Responding to Gender-Based Violence: How Help Is Available",
            "slug": "responding-gender-based-violence-help-available",
            "content": """Gender-based violence affects individuals across all ages and communities.

Survivors may experience:
- Physical or sexual violence
- Emotional or psychological abuse
- Economic or social control

Sauti 116 offers confidential counseling, safety guidance, and referrals to health, legal, and psychosocial services for survivors of GBV.

Seeking help is a sign of strength. If you are experiencing GBV or know someone who is, call 116 for free, confidential support.""",
            "excerpt": "Information on gender-based violence and how survivors can access confidential support through Sauti 116.",
            "category": categories["gender-based-violence"],
            "tags": [
                tags["gbv"],
                tags["psychosocial-support"],
            ],
            "status": "PUBLISHED",
            "language": "en",
            "is_featured": True,
            "views_count": 2450,
        },
        {
            "title": "Mental Health and Psychosocial Support: You Are Not Alone",
            "slug": "mental-health-psychosocial-support-not-alone",
            "content": """Experiencing violence, abuse, or exploitation can have a serious impact on mental health.

Common signs of distress include:
- Persistent fear or anxiety
- Withdrawal or isolation
- Sleep difficulties
- Emotional numbness

Sauti 116 provides psychosocial support and connects callers to appropriate services. Support is available for children, adults, GBV survivors, and migrant workers.

Help is available. Call 116 to speak to a trained counselor, anytime.""",
            "excerpt": "Psychosocial support services available through Sauti 116 for individuals experiencing distress.",
            "category": categories["mental-health-psychosocial"],
            "tags": [
                tags["mental-health"],
                tags["psychosocial-support"],
            ],
            "status": "PUBLISHED",
            "language": "en",
            "is_featured": False,
            "views_count": 1800,
        },
        {
            "title": "Protecting Migrant Workers from Abuse and Exploitation",
            "slug": "protecting-migrant-workers-abuse-exploitation",
            "content": """Migrant workers may face abuse, unsafe working conditions, or exploitation.

Sauti 116 provides:
- Confidential reporting
- Guidance on available support services
- Referrals to relevant authorities and partners

If you are a migrant worker in distress, or know someone who is being exploited, call 116 for help. Support is free and confidential.""",
            "excerpt": "How Sauti 116 supports migrant workers experiencing abuse or exploitation.",
            "category": categories["migrant-worker-support"],
            "tags": [
                tags["migrant-workers"],
                tags["sexual-exploitation"],
            ],
            "status": "PUBLISHED",
            "language": "en",
            "is_featured": False,
            "views_count": 1650,
        },
        {
            "title": "Impact Stories: When Calling 116 Makes a Difference",
            "slug": "impact-stories-calling-116-makes-difference",
            "content": """Every call to Sauti 116 has the potential to change a life.

Through timely counseling, referrals, and coordinated response, individuals and families are supported to move toward safety and recovery.

These stories highlight the importance of speaking up and seeking help when facing violence, abuse, or exploitation.""",
            "excerpt": "Stories highlighting the real impact of Sauti 116 support services.",
            "category": categories["impact-success-stories"],
            "tags": [
                tags["community"],
                tags["support-services"],
            ],
            "status": "DRAFT",
            "language": "en",
            "is_featured": False,
            "views_count": 0,
        },
    ]

    created_posts = 0
    for post_data in posts_data:
        post_data["published_at"] = (
            datetime.now() - timedelta(days=30)
            if post_data["status"] == "PUBLISHED"
            else None
        )

        post_tags = post_data.pop("tags")

        post, created = Post.objects.update_or_create(
            slug=post_data["slug"],
            defaults={**post_data, "author": admin_user},
        )

        post.tags.set(post_tags)
        if created:
            created_posts += 1
            print(f"✅ Created post: {post.title}")
        else:
            print(f"🔄 Updated post: {post.title}")

    print("\n🎉 Sample content setup complete")
    print(f"📊 Total posts: {Post.objects.count()}")
    print(f"📈 Published: {Post.objects.filter(status='PUBLISHED').count()}")
    print(f"📝 Drafts: {Post.objects.filter(status='DRAFT').count()}")


if __name__ == "__main__":
    populate_posts()
