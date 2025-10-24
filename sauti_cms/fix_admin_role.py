#!/usr/bin/env python
"""
Script to fix admin user role
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

def fix_admin_role():
    User = get_user_model()
    
    try:
        admin_user = User.objects.get(username='admin')
        admin_user.role = 'ADMIN'
        admin_user.is_staff = True
        admin_user.is_superuser = True
        admin_user.save()
        
        print('✅ Admin user role updated successfully!')
        print(f'Username: {admin_user.username}')
        print(f'Role: {admin_user.role}')
        print(f'Is Staff: {admin_user.is_staff}')
        print(f'Is Superuser: {admin_user.is_superuser}')
        print(f'Can Publish: {admin_user.can_publish()}')
        print(f'Can Delete: {admin_user.can_delete()}')
        
    except User.DoesNotExist:
        print('❌ Admin user not found!')
        print('Please run create_admin.py first')

if __name__ == '__main__':
    fix_admin_role()
