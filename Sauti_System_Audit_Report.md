# Sauti System Audit Report

## Executive Summary
The Sauti system demonstrates a solid foundation with well-structured Django backend APIs and Vue.js frontend and admin applications. Many core functionalities, such as blog post management, incident category enforcement, and dynamic configuration, are fully implemented. The system leverages modern frameworks (Django REST Framework, Vue 3, Pinia, Axios) and follows good practices for API design and frontend state management.

However, several critical gaps and areas for improvement have been identified, particularly concerning the completeness of the Case Reporting Flow data capture, the robustness of the system-wide audit trail, and minor inconsistencies/bugs in social media handling and cache management.

**Key Risks:**
- **Incomplete Case Reporting Data:** Lack of explicit age and gender fields for reported individuals could lead to data quality issues and hinder comprehensive analysis of reported cases.
- **Weak Audit Trail:** The current audit mechanism is basic, lacking field-level change tracking, historical logs, and tamper-resistance, which is a significant risk for a system handling sensitive case data and configuration.
- **Potential Data Inconsistency:** Overlapping social media link management between `GlobalSettings` and `ContactInformation` could lead to inconsistent data if not carefully managed.

**High-Priority Gaps:**
- Missing explicit age and gender fields in the `Report` model.
- Lack of clear distinction between reporter and victim details in the Case Reporting Flow.
- Absence of a robust, field-level, tamper-resistant audit trail.
- Critical bug in `sauti_cms/social_media/views.py` (missing imports).

## Scope & Methodology
This audit reviewed the codebase of the Sauti system, specifically:
- **Sauti CMS / Backend (Django):** Located in `sauti_cms/`, including models, views, serializers, and URL patterns for all relevant applications.
- **Sauti Admin (Vue.js):** Located in `sauti-admin/`, focusing on main entry points, routing, Pinia stores, and API client (`axios`) interactions.
- **Sauti Frontend (Vue.js):** Located in `sauti-frontend/`, focusing on main entry points, routing, Pinia stores, and API client (`axios`) interactions.

The review assessed the implementation against eight key functional, UX, and configuration areas. Evidence was gathered by inspecting file contents, directory structures, and API client configurations.

**Assumptions and Limitations:**
- **Runtime Behavior:** This audit is based solely on code review. Actual runtime behavior, performance, and visual UX/UI aspects (e.g., "enhanced design," "renders correctly") could not be fully verified without deploying and interacting with the live application.
- **External Systems:** Integrations with external systems (e.g., email services for notifications) were assumed to be functional based on code presence.
- **Django Admin UI:** The specific configuration and user experience of the Django Admin interface were not directly inspected, though its role in content management was inferred.
- **Completeness of Codebase:** Assumed the provided codebase is complete and representative of the deployed system.

## Detailed Findings

### Case Reporting Flow
- **Status:** Partially Implemented
- **Findings:**
    - The `sauti_cms/reports` app provides a robust backend for case reporting, including a `Report` model with fields for `description`, `attachment`, `status`, `category` (enforced via `TextChoices`), `is_anonymous`, `contact_name`, `contact_phone`, `contact_email`, and `location`.
    - Public report submission (`POST /api/reports/`) is handled by `ReportCreateView`, which captures IP/user agent and sends email notifications.
    - Admin views (`ReportListView`, `ReportDetailView`, `ReportEditView`) in `sauti-admin` allow for comprehensive management of reports, including adding follow-ups.
    - The `sauti-frontend` provides a `ReportPage.vue` for public submission and `GetHelpDetail.vue` for category selection.
    - Incident categories (`CHILD_PROTECTION`, `GBV`, `MIGRANT`, `PSEA`) are properly defined and enforced.
- **Gaps:**
    - **Data Capture Order (UX):** The exact order of fields in the `sauti-frontend`'s `ReportPage.vue` form (narrative after category, phone after narrative, then name → age → gender → location) needs to be visually verified.
    - **Missing Victim Details:** The `Report` model lacks explicit fields for the *reported person's* `age` and `gender`. This information would currently be embedded in the `description`, hindering structured analysis.
    - **Ambiguous Self-Reporting:** While `is_anonymous` is present, there are no explicit fields to clearly distinguish between a self-report and a report made for another person, nor an explicit age question for self-reporting.
- **Recommendations:**
    - **Backend (Django):**
        - Add `reported_person_age` (e.g., `models.IntegerField(null=True, blank=True)`) and `reported_person_gender` (e.g., `models.CharField(max_length=10, choices=GENDER_CHOICES, null=True, blank=True)`) fields to the `Report` model.
        - Consider adding a `is_self_report` boolean field to the `Report` model to explicitly track if the reporter is also the victim.
        - Update `ReportCreateSerializer`, `ReportDetailSerializer`, and `ReportUpdateSerializer` to include these new fields and any necessary validation.
    - **Frontend (Vue.js):**
        - Review and reorder form fields in `sauti-frontend/src/views/ReportPage.vue` to match the specified UX flow: incident category → narrative → phone number → name → age → gender → location.
        - Implement conditional logic in `ReportPage.vue` to ask "Are you reporting for yourself or someone else?" and adjust subsequent form fields (e.g., show separate victim details if reporting for another, ask explicit age question for self-reporting).
        - Update `api.reports.submit` to send the new `age`, `gender`, and `is_self_report` fields.
    - **Admin (Vue.js):**
        - Update `sauti-admin/src/views/ReportDetailView.vue` and `ReportEditView.vue` to display and edit the newly added `age`, `gender`, and `is_self_report` fields.

### Channels & Configuration
- **Status:** Fully Implemented
- **Findings:**
    - The `sauti_cms/sitesettings` app uses a `GlobalSettings` singleton model to manage all site-wide dynamic configurations, including social media links.
    - These settings are editable via `sauti-admin` through the `api.siteSettings.update` endpoint and the `SettingsView` component.
    - Configuration changes persist in the database and are dynamically fetched by the `sauti-frontend` (via `useSettingsStore`), reflecting without redeployment.
    - Social media links are managed in both `GlobalSettings` and `social_media.ContactInformation`, both accessible via admin.
- **Gaps:**
    - **Overlap in Social Media Links:** The presence of social media profile links in both `GlobalSettings` and `social_media.ContactInformation` creates a potential for data inconsistency and confusion in the admin interface.
- **Recommendations:**
    - **Backend (Django):** Consolidate social media profile links into a single source of truth, preferably within `GlobalSettings`, and remove redundant fields from `social_media.ContactInformation` if their purpose is identical. If `ContactInformation` serves a distinct purpose (e.g., contact page-specific links), clarify this distinction in documentation and code.
    - **Admin (Vue.js):** Present a unified and clear interface in `sauti-admin` for managing all social media profile links, ideally sourcing from the consolidated backend model.

### Homepage
- **Status:** Fully Implemented
- **Findings:**
    - The `sauti-frontend`'s `HomePage.vue` consumes content dynamically from `sauti_cms` APIs (`api.content`, `api.siteSettings`, `api.partners`, `api.socialMedia`).
    - `SiteContent` model (with `page='home'`) allows for flexible key-value content, including image URLs.
    - `Partner` logos are managed via `ImageField` in the `Partner` model and uploaded through `sauti-admin` using `createFormData`.
    - `GlobalSettings` also contains configurable sections for the homepage (hero, intro, etc.).
- **Gaps:**
    - **Image Upload for `SiteContent`:** While `SiteContent` can reference image URLs, the explicit mechanism for uploading these images (if not direct via API) is not detailed within the `content` app's API. It's likely handled through Django Admin or a separate media management system.
    - **Design Verification:** "Enhanced design" is a UX/UI aspect that cannot be verified from code alone.
- **Recommendations:**
    - **Backend (Django):** Ensure a clear and user-friendly media management system (e.g., a dedicated media library in Django Admin or an API endpoint for general media uploads) for images referenced by URL in `SiteContent`.
    - **Admin (Vue.js):** The `ContentManagerView` in `sauti-admin` should provide an intuitive workflow for uploading new images or selecting existing ones from a media library when configuring `SiteContent` items that are images.
    - **UX/UI Review:** Conduct a visual UX/UI review of the `sauti-frontend` homepage to assess layout, hierarchy, and usability.

### About Page
- **Status:** Partially Implemented
- **Findings:**
    - The `sauti-frontend`'s `AboutPage.vue` consumes content from `sauti_cms` APIs (`api.content` for `SiteContent`, `api.coreValues`, `api.teamMembers`, `api.protectionApproaches`).
    - `sauti-admin` provides dedicated components (`CoreValuesAdmin`, `TeamAdmin`, `ProtectionApproachAdmin`) for managing these sections.
    - Vision and Mission sections can be managed as `SiteContent` items or within `GlobalSettings`.
- **Gaps:**
    - **Rendering Verification:** "Renders correctly" is a visual/UX aspect that cannot be confirmed from code.
    - **Timeline Event Editability:** The `TimelineEventViewSet` in `sauti_cms` is `ReadOnlyModelViewSet`, meaning `TimelineEvent` objects are likely only editable via the Django Admin, not through the `sauti-admin` API.
- **Recommendations:**
    - **Frontend:** Visually inspect `sauti-frontend/src/views/AboutPage.vue` to ensure all content renders correctly and as expected.
    - **Backend (Django):** If `TimelineEvent`s are intended to be editable via `sauti-admin`, change `TimelineEventViewSet` from `ReadOnlyModelViewSet` to `ModelViewSet` and implement corresponding CRUD functionality.
    - **Admin (Vue.js):** If `TimelineEventViewSet` is made editable, implement the necessary CRUD forms and logic in `sauti-admin/src/views/TimelineAdmin.vue`.

### Blog Module
- **Status:** Fully Implemented
- **Findings:**
    - The `sauti_cms/posts` app provides a comprehensive `Post` model with `status` (DRAFT/PUBLISHED), `published_at`, and `featured_image`.
    - `Post` model's `save` method and `PostCreateUpdateSerializer`'s `validate_status` correctly handle status transitions and enforce publishing permissions.
    - Backend `get_queryset` methods ensure only `PUBLISHED` posts are returned to unauthenticated users and non-editors, effectively hiding drafts from the frontend.
    - `sauti-admin` provides `PostsView`, `PostEditView`, and `DraftsView` for full management, including `featured_image` uploads via `createFormData`.
    - `sauti-frontend` displays published blogs via `BlogPage.vue` and `BlogDetailPage.vue`.
- **Gaps:** None identified.
- **Recommendations:** None.

### Contacts & Partners
- **Status:** Partially Implemented
- **Findings:**
    - **Contacts:** General contact information (email, phone) is managed within `GlobalSettings` (`sauti_cms/sitesettings`) and is editable via `sauti-admin`. The `sauti_cms/contact` app is solely for feedback message submission.
    - **Partners:** The `sauti_cms/partners` app manages partner information, including `logo` uploads via `ImageField` and `sauti-admin`'s `createFormData`.
- **Gaps:**
    - **Cache Invalidation for Partner Logos:** No explicit cache invalidation mechanism was found for partner logos. If a logo is updated with the same filename, old cached versions might persist.
- **Recommendations:**
    - **Backend (Django):** Implement a custom storage backend that appends a hash or timestamp to the filename of uploaded logos to ensure unique URLs on update (cache busting).
    - **Deployment/Infrastructure:** Ensure proper HTTP caching headers are set for media files and consider CDN cache purging for critical assets like logos.

### Social Media Naming
- **Status:** Partially Implemented
- **Findings:**
    - **Backend (CMS):** The `sauti_cms/social_media` app's `ContactInformation` model's `twitter_url` field's help text explicitly mentions "Twitter/X". The `SocialPostViewSet.fetch_metadata` action correctly handles both `twitter.com` and `x.com` domains, mapping them internally to 'Twitter'.
    - **Admin/Frontend:** `sauti-admin`'s `api.socialMedia.fetchMetadata` is available. Frontend and admin UIs would display social media links/posts.
- **Gaps:**
    - **Internal Naming Inconsistency:** The `SocialPost.PLATFORM_CHOICES` still uses "Twitter" internally, which is not a full "rename across CMS".
    - **Critical Bug:** `sauti_cms/social_media/views.py` is missing `import requests` and `from bs4 import BeautifulSoup`, which will cause the `fetch_metadata` endpoint to fail.
    - **UI Display:** The actual display text in `sauti-admin` and `sauti-frontend` UIs for "Twitter" vs. "X" needs to be verified for consistency.
- **Recommendations:**
    - **Backend (Django):**
        - **FIX BUG:** Add `import requests` and `from bs4 import BeautifulSoup` to the top of `sauti_cms/social_media/views.py`.
        - Consider updating `SocialPost.PLATFORM_CHOICES` from 'Twitter' to 'X' (or 'Twitter/X') for full internal consistency, potentially requiring a data migration.
    - **Frontend/Admin (Vue.js):**
        - Review all UI elements (labels, icons, tooltips, hardcoded text) in `sauti-admin` and `sauti-frontend` that refer to "Twitter" and update them to "X" or "Twitter/X" for consistent branding.

## Audit Trail Assessment
- **Current State:**
    The system implements a basic, custom audit trail primarily through the widespread use of `created_at`, `updated_at`, `created_by`, and `last_updated_by` fields across many Django models.
    - `created_at` (auto_now_add=True) and `updated_at` (auto_now=True) automatically track creation and last update timestamps.
    - `created_by` and `last_updated_by` (ForeignKey to User) track the user who created or last modified a record.
    - The `OwnershipViewSetMixin` in DRF ViewSets (e.g., in `sauti_cms/content/views.py`) automatically populates `created_by` and `last_updated_by` with `request.user` during API-driven `create` and `update` operations.
    - A commented-out `RequestLogMiddleware` in `settings.py` suggests an earlier consideration for request-level logging, but the corresponding file is missing.
- **Risks:**
    - **Lack of Granularity ("What"):** The current system does not record *what specific fields* were changed during an update, making it difficult to reconstruct the exact nature of a modification.
    - **No Historical Log ("All Changes"):** Only the *last* updater is recorded. There is no history of all intermediate changes or users who modified a record over time.
    - **Tamper-Resistance:** The audit fields are part of the main model, making them susceptible to direct modification if a user has write access to the model, compromising the integrity of the audit trail.
    - **Incomplete Coverage:** While many models have these fields, coverage is not guaranteed for all models, and changes made outside of the `OwnershipViewSetMixin` (e.g., direct ORM operations) might bypass this tracking.
    - **No Deletion Logging:** Deletion actions are not explicitly logged with "who" and "when" information.
    - **No Request-Level Audit:** The absence of a functional request logging middleware means there's no comprehensive record of all user interactions with the system, including read operations or failed attempts.
- **Recommended Architecture:**
    To achieve a robust, tamper-resistant, and comprehensive audit trail suitable for a system handling sensitive data (like case reports) and critical configurations, a dedicated auditing solution is required.
    - **Integrate a Third-Party Auditing Package:** Implement a well-maintained Django auditing package such as `django-auditlog` or `django-simple-history`. These packages typically provide:
        - **Field-level change tracking:** Records old and new values for each modified field.
        - **Historical versions:** Stores a complete history of all changes to a model instance.
        - **User and timestamp tracking:** Automatically records who made the change and when.
        - **Deletion logging:** Records when objects are deleted.
        - **Read-only audit logs:** Often store audit data in separate, immutable tables, enhancing tamper-resistance.
    - **Comprehensive Application:** Ensure the chosen auditing solution is applied to all critical models across `sauti_cms` apps (e.g., `Report`, `GlobalSettings`, `Post`, `Partner`, `User`, etc.).
    - **Request Logging (Optional but Recommended):** Re-evaluate and implement a custom request logging middleware to capture all incoming requests, including user, timestamp, endpoint, and request body (with sensitive data redacted). This provides a broader "where" and "when" for all system interactions.
    - **Audit Log Access:** Provide a read-only interface (e.g., in `sauti-admin`) for authorized users to view audit logs.

## Priority Recommendations

### Immediate (Critical)
1.  **Fix Social Media `fetch_metadata` Bug:** Add `import requests` and `from bs4 import BeautifulSoup` to `sauti_cms/social_media/views.py`. This is a critical bug that will cause the social media metadata fetching to fail.
2.  **Implement Explicit Age/Gender Fields for Case Reporting:** Add `reported_person_age` and `reported_person_gender` fields to the `Report` model in `sauti_cms/reports/models.py`, update serializers, and modify frontend forms in `sauti-frontend/src/views/ReportPage.vue` and admin views in `sauti-admin`. This addresses a fundamental data capture gap.
3.  **Clarify Self-Reporting vs. Reporting for Another:** Implement `is_self_report` in the `Report` model and corresponding frontend logic in `sauti-frontend/src/views/ReportPage.vue` to explicitly differentiate between reporter and victim details.

### Short-term
1.  **Implement Robust Audit Trail:** Integrate a third-party Django auditing package (e.g., `django-auditlog`) across all critical models in `sauti_cms` to provide field-level change tracking, historical logs, and deletion logging.
2.  **Consolidate Social Media Profile Links:** Refactor the backend to use a single source of truth for social media profile links (e.g., `GlobalSettings`) and update `sauti-admin` to reflect this unified management.
3.  **Cache Busting for Partner Logos:** Implement a custom storage backend for `Partner.logo` to ensure unique filenames on update, or configure CDN cache purging.
4.  **Update "Twitter" to "X" Branding:** Review and update all UI elements in `sauti-admin` and `sauti-frontend` that display "Twitter" to "X" or "Twitter/X" for consistent branding.

### Medium-term
1.  **Media Management System for `SiteContent`:** Develop a dedicated media library or API endpoint for managing images referenced by URL in `SiteContent`, and integrate this into `sauti-admin`'s `ContentManagerView`.
2.  **Enable `TimelineEvent` Editing in Admin:** If required, change `TimelineEventViewSet` to `ModelViewSet` and implement CRUD functionality in `sauti-admin`.
3.  **Comprehensive Request Logging:** Implement a custom request logging middleware to capture all user interactions for a more complete audit trail.

## Conclusion
The Sauti system is generally well-architected and functional in many areas. The identified gaps, particularly in case reporting data completeness and audit trail robustness, represent significant areas for improvement that should be prioritized. Addressing these will enhance data quality, system accountability, and overall reliability.

**Readiness Assessment:**
The system is **Partially Ready** for full operational deployment, primarily due to the critical data capture gaps in case reporting and the insufficient audit trail. While core functionalities are present, these issues pose risks to data integrity, compliance, and accountability.

**Next Steps:**
1.  Prioritize and implement the "Immediate (Critical)" recommendations.
2.  Develop a detailed plan for integrating a robust audit trail solution.
3.  Conduct a thorough UX/UI review of both `sauti-frontend` and `sauti-admin` to verify visual aspects and user flows.
4.  Address "Short-term" and "Medium-term" recommendations as part of ongoing development cycles.
