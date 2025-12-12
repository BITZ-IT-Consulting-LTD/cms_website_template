#!/usr/bin/env python
"""
Quick script to create admin user
"""
import os
import sys
import django
from pathlib import Path

# Add the project directory to Python path (use current directory)
BASE_DIR = Path(__file__).resolve().parent
sys.path.append(str(BASE_DIR))

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cms.settings')
django.setup()

from django.contrib.auth import get_user_model

def create_admin():
    User = get_user_model()

    if not User.objects.filter(username='admin').exists():
        admin_user = User.objects.create_superuser(
            username='admin',
            email='admin@sauti.org',
            password='admin123'
        )
        # Explicitly set ADMIN role
        admin_user.role = 'ADMIN'
        admin_user.save()
        print('✅ Admin user created successfully!')
        print('Username: admin')
        print('Password: admin123')
        print('Email: admin@sauti.org')
        print('Role: ADMIN')
    else:
        # Update existing admin to have ADMIN role
        admin_user = User.objects.get(username='admin')
        if admin_user.role != 'ADMIN':
            admin_user.role = 'ADMIN'
            admin_user.is_superuser = True
            admin_user.is_staff = True
            admin_user.save()
            print('ℹ️ Admin user role updated to ADMIN!')
        else:
            print('ℹ️ Admin user already exists!')
        print('Username: admin')
        print('Password: admin123')

if __name__ == '__main__':
    create_admin()
