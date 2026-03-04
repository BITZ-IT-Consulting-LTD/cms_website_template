# Services Application

Manages the directory of helpline services offered by Sauti 116.

## Overview

This app defines and manages the various services available through the helpline platform, including counseling, support services, and resources.

## Models

### Service
- `name` - Service name
- `description` - Service description
- `category` - Service category (Counseling, Support, Resources, etc.)
- `is_active` - Availability status

## API Endpoints

- `GET /api/services/` - List all services
- `GET /api/services/{id}/` - Get service details
- `POST /api/services/` - Create service (Admin only)
- `PUT /api/services/{id}/` - Update service (Admin only)

## Admin Interface

Access at `/admin/services/service/` to manage services.

## Files

- `models.py` - Service model
- `serializers.py` - API serializers
- `views.py` - API viewsets
- `admin.py` - Admin interface
- `urls.py` - URL routing

## Related Documentation

- [Main CMS README](../README.md)
- [API Documentation](../API_DOCUMENTATION.md)
