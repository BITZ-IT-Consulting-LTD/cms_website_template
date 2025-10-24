#!/usr/bin/env python
"""
Create sample blog posts for testing the admin dashboard.
"""
import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cms.settings')
django.setup()

from django.contrib.auth import get_user_model
from posts.models import Post, Category, Tag
from datetime import datetime, timedelta

User = get_user_model()

def create_sample_posts():
    """Create sample blog posts for testing"""
    
    # Get or create admin user
    admin_user, created = User.objects.get_or_create(
        username='admin',
        defaults={
            'email': 'admin@sauti.ug',
            'first_name': 'Admin',
            'last_name': 'User',
            'role': 'ADMIN',
            'is_staff': True,
            'is_superuser': True
        }
    )
    
    if created:
        admin_user.set_password('admin12345')
        admin_user.save()
        print("✅ Created admin user")
    else:
        print("✅ Admin user already exists")
    
    # Create categories
    categories_data = [
        {'name': 'Child Protection', 'slug': 'child-protection', 'description': 'Resources about child protection'},
        {'name': 'Mental Health', 'slug': 'mental-health', 'description': 'Mental health resources for children'},
        {'name': 'Education', 'slug': 'education', 'description': 'Educational resources and tips'},
        {'name': 'Safety Tips', 'slug': 'safety-tips', 'description': 'Safety guidelines for children'},
        {'name': 'Success Stories', 'slug': 'success-stories', 'description': 'Inspiring stories from our helpline'}
    ]
    
    categories = {}
    for cat_data in categories_data:
        category, created = Category.objects.get_or_create(
            slug=cat_data['slug'],
            defaults=cat_data
        )
        categories[cat_data['slug']] = category
        if created:
            print(f"✅ Created category: {cat_data['name']}")
    
    # Create tags
    tags_data = [
        {'name': 'Rights', 'slug': 'rights'},
        {'name': 'Safety', 'slug': 'safety'},
        {'name': 'Education', 'slug': 'education'},
        {'name': 'Mental Health', 'slug': 'mental-health'},
        {'name': 'Community', 'slug': 'community'},
        {'name': 'Support', 'slug': 'support'}
    ]
    
    tags = {}
    for tag_data in tags_data:
        tag, created = Tag.objects.get_or_create(
            slug=tag_data['slug'],
            defaults=tag_data
        )
        tags[tag_data['slug']] = tag
        if created:
            print(f"✅ Created tag: {tag_data['name']}")
    
    # Create sample posts
    posts_data = [
        {
            'title': 'Understanding Child Rights in Uganda',
            'slug': 'understanding-child-rights-uganda',
            'content': '''Every child has fundamental rights that must be protected. In Uganda, children are protected under the Constitution and various international conventions.

Key rights include:
- Right to education
- Right to healthcare
- Right to protection from abuse
- Right to participate in decisions affecting them

The Sauti Child Helpline is committed to ensuring these rights are respected and protected. If you know a child whose rights are being violated, call 116 immediately.

Our trained counselors are available 24/7 to provide support and guidance. Remember, every child deserves to grow up in a safe and nurturing environment.''',
            'excerpt': 'A comprehensive guide to child rights and protection laws in Uganda, explaining how Sauti supports these fundamental principles.',
            'category': categories['child-protection'],
            'tags': [tags['rights'], tags['safety']],
            'status': 'PUBLISHED',
            'language': 'en',
            'is_featured': True,
            'views_count': 2847
        },
        {
            'title': 'The Impact of Community Support on Child Welfare',
            'slug': 'impact-community-support-child-welfare',
            'content': '''Community support plays a crucial role in ensuring child welfare and protection. When communities come together, they create a safety net that helps identify and address issues affecting children.

Benefits of community support:
- Early identification of problems
- Shared responsibility for child protection
- Local knowledge and resources
- Cultural sensitivity in interventions

The Sauti Child Helpline works closely with communities across Uganda to build awareness and provide support. We believe that protecting children is everyone's responsibility.

If you're concerned about a child in your community, don't hesitate to reach out. Our helpline is confidential and available around the clock.''',
            'excerpt': 'How community involvement and support systems contribute to better outcomes for children in need of protection.',
            'category': categories['success-stories'],
            'tags': [tags['community'], tags['support']],
            'status': 'PUBLISHED',
            'language': 'en',
            'is_featured': True,
            'views_count': 1923
        },
        {
            'title': 'Mental Health Resources for Young People',
            'slug': 'mental-health-resources-young-people',
            'content': '''Mental health is just as important as physical health, especially for young people who may be dealing with stress, anxiety, or trauma.

Signs to watch for:
- Changes in behavior or mood
- Withdrawal from friends and activities
- Difficulty concentrating
- Changes in sleep or eating patterns

The Sauti Child Helpline provides mental health support and can connect young people with appropriate resources. Our counselors are trained to handle sensitive situations with care and confidentiality.

Remember, it's okay to ask for help. Mental health challenges are common and treatable. You're not alone.''',
            'excerpt': 'Important mental health resources and support available for young people through the Sauti helpline.',
            'category': categories['mental-health'],
            'tags': [tags['mental-health'], tags['support']],
            'status': 'PUBLISHED',
            'language': 'en',
            'is_featured': False,
            'views_count': 1456
        },
        {
            'title': 'Safety Tips for Children at Home and School',
            'slug': 'safety-tips-children-home-school',
            'content': '''Safety is paramount for children in all environments. Here are some essential safety tips for parents, teachers, and caregivers:

At Home:
- Keep dangerous items out of reach
- Install safety gates and locks
- Teach children about stranger danger
- Create a safe space for children to talk

At School:
- Ensure proper supervision
- Implement anti-bullying policies
- Teach children about appropriate touch
- Create reporting mechanisms

The Sauti Child Helpline (116) is available 24/7 for any safety concerns. Early intervention can prevent serious problems and protect children from harm.

If you suspect a child is in danger, don't wait - call immediately. Every child deserves to feel safe and protected.''',
            'excerpt': 'Essential safety guidelines to protect children in home and school environments.',
            'category': categories['safety-tips'],
            'tags': [tags['safety'], tags['education']],
            'status': 'PUBLISHED',
            'language': 'en',
            'is_featured': False,
            'views_count': 2103
        },
        {
            'title': 'Success Stories: How Sauti Changed Lives',
            'slug': 'success-stories-sauti-changed-lives',
            'content': '''Real stories from children and families who found help and hope through the Sauti helpline services.

Story 1: Sarah's Journey
Sarah, a 14-year-old from Kampala, called our helpline when she was being bullied at school. Our counselors provided emotional support and connected her with resources to address the situation. Today, Sarah is thriving and has become a peer counselor herself.

Story 2: The Mwangi Family
The Mwangi family was struggling with their 8-year-old son's behavioral issues. Through our helpline, they received guidance on positive parenting techniques and were connected with local support services. The family is now stronger and more connected.

These stories remind us that every call to 116 can make a difference. If you or someone you know needs help, don't hesitate to reach out. We're here to listen, support, and guide you through difficult times.''',
            'excerpt': 'Inspiring real stories from children and families who found help through the Sauti helpline.',
            'category': categories['success-stories'],
            'tags': [tags['support'], tags['community']],
            'status': 'DRAFT',
            'language': 'en',
            'is_featured': False,
            'views_count': 0
        }
    ]
    
    created_posts = 0
    for post_data in posts_data:
        # Set publication dates
        if post_data['status'] == 'PUBLISHED':
            post_data['published_at'] = datetime.now() - timedelta(days=30)
        else:
            post_data['published_at'] = None
        
        # Remove tags from post_data for creation
        post_tags = post_data.pop('tags')
        
        # Create the post
        post, created = Post.objects.get_or_create(
            slug=post_data['slug'],
            defaults={
                **post_data,
                'author': admin_user
            }
        )
        
        if created:
            # Add tags to the post
            post.tags.set(post_tags)
            created_posts += 1
            print(f"✅ Created post: {post_data['title']}")
        else:
            print(f"ℹ️ Post already exists: {post_data['title']}")
    
    print(f"\n🎉 Successfully created {created_posts} new blog posts!")
    print(f"📊 Total posts in database: {Post.objects.count()}")
    print(f"📈 Published posts: {Post.objects.filter(status='PUBLISHED').count()}")
    print(f"📝 Draft posts: {Post.objects.filter(status='DRAFT').count()}")

if __name__ == '__main__':
    create_sample_posts()
