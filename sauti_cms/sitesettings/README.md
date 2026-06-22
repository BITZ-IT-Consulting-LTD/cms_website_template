# Site Settings Application

Global configuration and settings for the Sauti 116 platform.

## Overview

Manages site-wide configuration using key-value pairs stored in the database, allowing admins to configure settings without code changes.

## Models

### SiteSetting
- `key` - Setting key (e.g., "site_title", "support_phone")
- `value` - Setting value
- `description` - Setting description
- `is_active` - Whether setting is in use

## Common Settings

- `site_title` - Website title
- `site_description` - Meta description
- `support_phone` - Support phone number
- `support_email` - Support email
- `social_facebook_url` - Facebook link
- `social_twitter_url` - Twitter link
- `social_tiktok_url` - TikTok link
- `logo_url` - Logo image URL
- `maintenance_mode` - Enable/disable maintenance mode

## API Endpoints

- `GET /api/sitesettings/` - Get all settings
- `PUT /api/sitesettings/` - Update settings (Admin only)

## Admin Interface

Access at `/admin/sitesettings/sitesetting/` to manage site settings.

## Management Commands

- `populate_sitesettings.py` - Initialize default settings

## Files

- `models.py` - SiteSetting model
- `serializers.py` - API serializers
- `views.py` - API viewsets
- `admin.py` - Admin interface
- `urls.py` - URL routing

## Related Documentation

- [Main CMS README](../README.md)
- [API Documentation](../API_DOCUMENTATION.md)
