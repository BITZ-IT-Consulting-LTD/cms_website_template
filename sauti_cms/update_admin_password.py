#!/usr/bin/env python
"""
Update admin user password to admin123
"""
import os
import sys
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cms.settings')
django.setup()

from django.contrib.auth import get_user_model

def update_admin_password():
    User = get_user_model()
    
    try:
        admin_user = User.objects.get(username='admin')
        admin_user.set_password('admin123')
        admin_user.save()
        print('✅ Admin password updated successfully!')
        print('Username: admin')
        print('Password: admin123')
    except User.DoesNotExist:
        print('❌ Admin user not found!')
        print('Creating new admin user...')
        User.objects.create_superuser(
            username='admin',
            email='admin@sauti.org',
            password='admin123'
        )
        print('✅ Admin user created successfully!')
        print('Username: admin')
        print('Password: admin123')

if __name__ == '__main__':
    update_admin_password()
