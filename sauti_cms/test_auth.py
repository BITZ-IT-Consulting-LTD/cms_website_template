#!/usr/bin/env python
"""
Script to test authentication and permissions
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
from rest_framework_simplejwt.tokens import RefreshToken

def test_auth():
    User = get_user_model()
    
    try:
        admin_user = User.objects.get(username='admin')
        print(f'✅ Admin user found: {admin_user.username}')
        print(f'Role: {admin_user.role}')
        print(f'Is Staff: {admin_user.is_staff}')
        print(f'Is Superuser: {admin_user.is_superuser}')
        print(f'Is Editor: {admin_user.is_editor}')
        print(f'Is Admin: {admin_user.is_admin}')
        print(f'Can Publish: {admin_user.can_publish()}')
        print(f'Can Delete: {admin_user.can_delete()}')
        
        # Test JWT token generation
        refresh = RefreshToken.for_user(admin_user)
        access_token = str(refresh.access_token)
        refresh_token = str(refresh)
        
        print(f'\n✅ JWT Tokens generated:')
        print(f'Access Token: {access_token[:50]}...')
        print(f'Refresh Token: {refresh_token[:50]}...')
        
        # Test token validation
        from rest_framework_simplejwt.tokens import AccessToken
        try:
            token = AccessToken(access_token)
            print(f'\n✅ Token validation successful')
            print(f'User ID from token: {token["user_id"]}')
            print(f'Token type: {token["token_type"]}')
        except Exception as e:
            print(f'\n❌ Token validation failed: {e}')
            
    except User.DoesNotExist:
        print('❌ Admin user not found!')

if __name__ == '__main__':
    test_auth()
