# GIZ Integration Module

This folder is reserved for German Development Cooperation (GIZ) specific features and integrations for the Sauti 116 helpline platform.

## Overview

**GIZ** stands for **Gesellschaft für Internationale Zusammenarbeit** (German International Cooperation Agency). This module contains GIZ-specific functionality, integrations, and customizations that enhance the Sauti 116 platform for GIZ partnership requirements.

## Current Status

This folder is currently empty and serves as a placeholder for future GIZ-specific modules and features.

## Planned Features

Future GIZ integration may include:
- GIZ branding and styling customization
- GIZ-specific reporting and analytics
- GIZ partnership management features
- German language support
- GIZ impact measurement modules
- Integration with GIZ monitoring systems

## Related GIZ Features

Currently, GIZ-specific functionality is implemented in:

### Frontend (`sauti-frontend/`)
- `src/components/giz/` - GIZ-specific Vue components
  - `FloatingChatBot.vue` - Voice-enabled chatbot interface
  - `DynamicChatWindow.vue` - Chat window component
  - `VoiceCapture.vue` - Voice capture functionality
- `src/assets/giz-css/` - GIZ-specific CSS styling

### Admin Dashboard (`sauti-admin/`)
- May contain GIZ-specific admin panels

### Backend (`sauti_cms/`)
- GIZ-specific API endpoints (to be documented)
- GIZ partnership models

## How to Use This Folder

When adding new GIZ-specific features:

1. **Create Django App** (if needed):
   ```bash
   python manage.py startapp giz_custom sauti_cms/giz
   ```

2. **Create Vue Components** (if needed):
   ```
   sauti-frontend/src/components/giz/
   sauti-admin/src/components/giz/
   ```

3. **Update Documentation**:
   - Add subdirectory README.md files
   - Update parent README.md files
   - Document new API endpoints

4. **Add Configuration**:
   - Extend `sauti_cms/cms/settings.py` if needed
   - Add environment variables to `.env.example`

## Documentation Structure

Once features are added, organize documentation as:
```
Giz/
├── README.md (this file)
├── FEATURES.md (GIZ-specific features)
├── INTEGRATION_GUIDE.md (Integration instructions)
└── [subdirectories with their own README.md]
```

## Related Files and Directories

- **Frontend GIZ Components**: `sauti-frontend/src/components/giz/`
- **Frontend GIZ Styling**: `sauti-frontend/src/assets/giz-css/`
- **Backend API**: `sauti_cms/`
- **Admin Dashboard**: `sauti-admin/`

## Contact and Contributions

For GIZ-related questions or to add new features to this module:
1. Review existing GIZ implementations in frontend/admin/backend
2. Create a feature branch: `git checkout -b giz/feature-name`
3. Add comprehensive documentation
4. Test thoroughly with GIZ requirements
5. Submit pull request with detailed documentation

## GIZ Partnership Context

The Sauti 116 platform is developed in partnership with GIZ to provide:
- Comprehensive helpline and counseling services
- Mental health support
- Gender-based violence resources
- Survivor empowerment services
- Data-driven impact measurement

All GIZ integrations should align with:
- GIZ branding guidelines
- Partnership objectives
- Data protection requirements
- Impact measurement frameworks

## Resources

- [GIZ Official Website](https://www.giz.de/en)
- [Sauti 116 Platform Documentation](../docs/)
- [Frontend Documentation](../sauti-frontend/README.md)
- [Backend Documentation](../sauti_cms/README.md)
- [Admin Dashboard Documentation](../sauti-admin/README.md)
