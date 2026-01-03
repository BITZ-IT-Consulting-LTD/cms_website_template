# Refactor Summary: Case Reporting Flow

## Objective
Refactor the Case Reporting Form (`ReportForm.vue`) and Backend (`sauti_cms/reports`) to align with safeguarding best practices, ensuring robust data collection and user experience.

## Completed Actions

### 1. Backend Updates
- **Models (`reports/models.py`)**:
    - Added `safe_to_contact`, `affected_persons`, `reporting_for` fields.
- **Serializers (`reports/serializers.py`)**:
    - Updated `ReportCreateSerializer` to accept nested `reporter` and `affected_persons`.
- **Views (`reports/views.py`)**:
    - Added `JSONParser` to `ReportCreateView` to enable JSON support (previously missing).
- **Migrations**:
    - Applied migrations `0005` and `0006`.

### 2. Frontend Updates
- **`src/utils/axios.js`**:
    - **CRITICAL FIX**: Changed `reports.submit` to send structured JSON instead of `FormData`. Previously, `FormData` flattened nested objects into strings, causing "Expected dictionary, got string" errors on the backend.
- **`ReportForm.vue`**:
    - Complete refactor of intake flow (Steps 1-7).
    - Fixed state management and added payload logging.
    - Improved UI/UX (Avatars, Animations).

## Verification
- **Issue Resolved**: The `400 Bad Request` where `affected_persons` was rejected as a string is solved by switching to JSON transmission.
- **Backend Ready**: Backend now accepts the simplified JSON payload.

### 3. Admin Dashboard & Admin UI Updates
- **Django Admin (`reports/admin.py`)**: Added `safe_to_contact`, `reporting_for`, and `affected_persons` (new fieldset) to the admin interface.
- **Backend Serializers (`reports/serializers.py`)**: Updated `ReportListSerializer` and `ReportDetailSerializer` to include the new fields so they are returned to the Admin API.
- **Admin Frontend (`ReportDetailView.vue`)**: Updated to display:
    - `Safe to Contact` status.
    - `Reporting For` status.
    - `Affected Persons` list (iterating through JSON data).
- **Admin Frontend (`ReportsView.vue`)**: Updated list view to show `reporting_for` summary.

### 4. Case Management & OpenCHS Integration
- **Models**: Added `ESCALATED` and `FORWARDED` statuses, plus fields for `escalated_at` and `forwarded_to_openchs_at`.
- **Logic**: Implemented auto-timestamping when status changes via API or Admin.
- **UI**: Added "Escalate" and "Forward to OpenCHS" buttons in the Report Detail view.

## Instructions for User
- The form is fully functional. 
- **Admin Panel**: You will now see all captured data (Safety, Multiple Persons, etc.) in both the Django Admin and Sauti Admin dashboard.
- **Case Management**: You can now Escalate cases or Forward them to OpenCHS directly from the dashboard.

### 5. Report Editing
- **Hybrid Data Loading**: Updated `ReportEditView` to support both legacy and new data structures.
    - If a report uses the new `affected_persons` list, the first person's details are automatically loaded into the Age/Gender input boxes.
- **Data Synchronization**: Saving the report updates both the legacy fields and the JSON data structure, ensuring data consistency.

### 6. Global Content Management
- **Dynamic Content Loading**: Refactored `ContentManager.vue` to dynamically load and list all site content, grouped by Page (Home, About, Resources, etc.), ensuring no content is hidden.
- **Enhanced Editing**: The interface now allows editing of not just the value, but also the Label, Description, Type, and Page assignment.
- **Visual Improvements**: Added photo previews, content type badges, and a cleaner grid layout for better usability.
- **Robust Saving**: Fixed issues with saving content by ensuring the correct API payload structure and key usage.
