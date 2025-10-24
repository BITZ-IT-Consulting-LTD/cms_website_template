#!/usr/bin/env python
"""
Quick script to create admin user
"""
import os
import sys
import django

# Add the project directory to Python path
sys.path.append('/Users/newtonbrian/Documents/Bitz/cms_website_template/sauti_cms')

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cms.settings')
django.setup()

from django.contrib.auth import get_user_model

def create_admin():
    User = get_user_model()
    
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser(
            username='admin',
            email='admin@sauti.org',
            password='admin12345'
        )
        print('✅ Admin user created successfully!')
        print('Username: admin')
        print('Password: admin12345')
        print('Email: admin@sauti.org')
    else:
        print('ℹ️ Admin user already exists!')
        print('Username: admin')
        print('Password: admin12345')

if __name__ == '__main__':
    create_admin()
