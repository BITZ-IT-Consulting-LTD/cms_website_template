# Timeline Application

Manages timeline events and historical records for the Sauti 116 platform.

## Overview

This app tracks important milestones, events, and historical information for the helpline, useful for displaying the organization's journey and achievements.

## Models

### Timeline Entry
- `title` - Event title
- `description` - Event details
- `date` - Event date
- `category` - Event category (Milestone, Award, Update, etc.)
- `image` - Event image/icon
- `is_published` - Publication status

## API Endpoints

- `GET /api/timeline/` - List all timeline events
- `GET /api/timeline/{id}/` - Get event details
- `POST /api/timeline/` - Create event (Admin only)
- `PUT /api/timeline/{id}/` - Update event (Admin only)

## Admin Interface

Access at `/admin/timeline/timelineentry/` to manage timeline events.

## Files

- `models.py` - Timeline models
- `serializers.py` - API serializers
- `views.py` - API viewsets
- `admin.py` - Admin interface
- `urls.py` - URL routing

## Related Documentation

- [Main CMS README](../README.md)
- [API Documentation](../API_DOCUMENTATION.md)
