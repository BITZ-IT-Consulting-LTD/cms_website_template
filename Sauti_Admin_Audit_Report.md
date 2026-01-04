# Sauti Admin Application Audit Report

## Executive Summary (Admin Perspective)
The Sauti Admin application provides a comprehensive interface for managing the Sauti system's content and operations. It is built on a modern Vue.js stack with Pinia for state management and Axios for API interactions, connecting to a Django REST Framework backend. The application's routing structure is generally well-defined, and many content areas are clearly exposed for administrative control.

However, the audit reveals several areas where consistency, discoverability, and critical functionality visibility could be significantly improved for a non-technical government program manager. Key concerns include potential route redundancies, navigation inconsistencies that hinder intuitive content management, gaps in operational dashboard reporting, and a critical lack of visibility into the backend's existing audit trail capabilities. Addressing these issues will enhance the system's governance maturity, improve maintainability, and empower non-technical administrators to manage the platform effectively without developer intervention.

## Findings

### Routes
- **List of duplicated or redundant routes:**
    - `/posts` and `/blogs`: Both point to `PostsView` and `BlogsView` respectively, which likely manage similar content (blog posts). While `PostsView` is for general posts, `BlogsView` might be a specific filtered view or a redundant entry.
    - `/reports` and `/reports/urgent`, `/reports/archive`: These all point to `ReportsView`. While the latter two use query parameters or internal logic to filter, the base `/reports` route could serve as the primary entry, with filters applied within the view.
    - `/content` and several specific content routes like `/team`, `/core-values`, `/protection-approach`, `/timeline`, `/services`, `/contacts`: The `/content` route points to `ContentManagerView`, which might be a generic content management area, while other routes point to specific content types. This could lead to overlap or confusion if `ContentManagerView` also manages these specific types.
- **Recommendation on consolidation or deprecation:**
    - **Consolidate Blog/Posts:** Evaluate if `PostsView` and `BlogsView` are truly distinct. If they manage the same underlying content, consolidate them into a single view (e.g., `PostsView`) and use filters or tabs within that view to differentiate between "all posts" and "blogs." Deprecate the redundant route.
    - **Rationalize Reports Routes:** Consolidate `/repoxrts/urgent` and `/reports/archive` into the main `/reports` route, using query parameters or internal view state to manage filtering (e.g., `/reports?status=urgent`). This reduces route clutter and centralizes report management.
    - **Clarify Generic Content Route:** Define the clear purpose of `/content` (`ContentManagerView`). If it's a dashboard for all content types, ensure it provides clear links or navigation to specific content management areas (e.g., Team, Core Values). If it's redundant with other specific content routes, consider deprecating it.
- **Clear rationale (governance, maintainability, UX):**
    - **Governance:** Clear, distinct routes prevent confusion about where to manage specific content, reducing the risk of administrators using incorrect or outdated interfaces.
    - **Maintainability:** Fewer, well-defined routes simplify future development, testing, and debugging. It reduces the surface area for potential bugs arising from overlapping logic.
    - **UX:** A consistent and logical routing structure makes the application more intuitive for administrators, reducing the learning curve and improving efficiency.

### Navigation
- **Navigation inconsistencies:**
    - **Scattered Content Management:** Content types like "Team," "Core Values," "Protection Approach," "Timeline," "Services," and "Contact Info" are listed as top-level items in the router, but conceptually they are all "content" or "site settings." This scattering makes it difficult for a non-technical administrator to find all editable content in one logical place.
    - **"Blogs" vs. "Posts":** The presence of both `/posts` and `/blogs` routes (and potentially corresponding navigation items) for what appears to be similar content can be confusing.
    - **"Uploads":** The "Uploads" section (`UploadsView`) is a generic name. It's unclear from the name alone what kind of "uploads" it manages (e.g., media library, documents, specific content assets).
- **Missing or misclassified admin sections:**
    - **Centralized Content Hub:** There isn't a single, clearly defined "Content Management" or "Site Content" section that groups all editable content types (Homepage, About Page, Legal, etc.).
    - **Settings Grouping:** While "Settings" (`SettingsView`) exists, it's unclear if it encompasses all site-wide configurations or if some are managed elsewhere.
- **Recommended high-level navigation grouping (no UI mockups):**
    - **Dashboard:** (Existing) Overview of system activity.
    - **Content Management:**
        - Posts/Blogs (Consolidated)
        - Videos
        - Resources
        - FAQs
        - Homepage Content (e.g., Hero, Intro, Quick Access, News)
        - About Page Content (e.g., Core Values, Team, Protection Approach, Timeline)
        - Legal & Footer (e.g., Privacy, Terms, Accessibility)
        - Partners
        - Contact Information
        - Social Media (Links & Posts)
        - Media Library (Consolidated "Uploads")
    - **Case Management:**
        - Reports (Consolidated, with internal filters for Urgent/Archive)
    - **User Management:**
        - Admin Users
    - **System Settings:**
        - Global Site Settings (e.g., SEO, general configuration)

### Dashboards & Reporting
- **Existing dashboards:**
    - `DashboardView` (likely a general overview).
    - `ReportsView` (lists active reports, with routes for urgent/archive).
    - `api.dashboard.stats` and `api.dashboard.analytics` endpoints suggest backend capabilities for various metrics.
- **Whether dashboards answer operational questions:**
    - The presence of `ReportsView` with filtering capabilities (urgent/archive routes) suggests it can answer "How many cases by status?".
    - `api.dashboard.stats` and `api.dashboard.analytics` imply the *potential* to answer questions like "How many cases today?" or "By category?". However, it's not clear if these are fully surfaced in the `DashboardView` or `ReportsView`.
    - Metrics like "By age/gender" are not explicitly available in the backend `Report` model, so they cannot be surfaced.
- **Gaps in reporting visibility:**
    - **Operational Metrics:** It's unclear if the `DashboardView` provides immediate, at-a-glance operational metrics (e.g., new cases today, cases by category, average resolution time).
    - **Management/Donor Reporting:** There's no explicit dashboard or report component tailored for management summaries or donor reporting, which often require aggregated data, trends, and potentially export functionalities.
    - **Missing Demographic Data:** Due to the absence of explicit age and gender fields in the `Report` model, reporting by these demographics is not possible.
- **Recommendations for dashboard rationalisation:**
    - **Operational Dashboard Enhancement:** Enhance `DashboardView` to prominently display key operational metrics for case management (e.g., new reports today, reports by category, reports by status, reports assigned to current user).
    - **Dedicated Reporting Section:** Create a dedicated "Reporting" section under "Case Management" that offers more detailed, filterable, and exportable reports for management and donor purposes. This could include:
        - Case trends over time.
        - Case distribution by category, status, and location.
        - (Once implemented) Case distribution by reported person's age and gender.
        - User activity reports (if audit trail is enhanced).
    - **Clear Separation:**
        - **Operational dashboards:** Focus on real-time or near real-time data for day-to-day decision-making (e.g., `DashboardView`).
        - **Management summaries:** Provide aggregated, historical data, and trends for strategic oversight (e.g., a new "Reports & Analytics" section).
        - **Editorial/content dashboards:** (Currently not present) Could show content performance metrics (e.g., most viewed posts, engagement on social media posts).

### Audit Trail Visibility (Critical)
- **Whether audit trail is sufficiently exposed to admins:**
    - **Visibility of who created/updated records:** The backend `sauti_cms` uses `created_by` and `last_updated_by` fields, which are populated via `OwnershipViewSetMixin` for API-driven changes. It is highly probable that these fields are displayed in the `sauti-admin`'s detail/edit views (e.g., `ReportDetailView`, `PostEditView`). However, this is limited to the last modifier.
    - **Ability to view historical changes:** The backend currently lacks a robust, field-level historical audit trail. Therefore, `sauti-admin` cannot expose this capability.
    - **Admin awareness of audit data:** Admins are likely aware of "created by" and "last updated by" fields, but not of a comprehensive, immutable audit log.
    - **Separation between editable data and immutable audit logs:** The backend's current audit fields (`created_at`, `updated_at`, `created_by`, `last_updated_by`) are part of the main models, meaning they are not inherently immutable or separate from editable data.
- **Gaps between backend audit capability and admin visibility:**
    - The most significant gap is the backend's limited audit capability itself. `sauti-admin` can only expose what the backend provides.
    - Admins cannot view a history of *all* changes made to a record, *what specific fields* were changed, or *who* made those changes beyond the last update.
    - There is no visibility into deletion events.
- **Recommendations to improve audit transparency (not implementation):**
    - **Display Comprehensive Audit Information:** Once the backend audit trail is enhanced (e.g., with `django-auditlog`), `sauti-admin` should display a dedicated "Audit History" or "Change Log" section within the detail view of each record (e.g., for reports, posts, settings). This section should clearly show:
        - Who made the change.
        - When the change was made.
        - What specific fields were changed (old value vs. new value).
        - The type of action (create, update, delete).
    - **Read-Only Audit Views:** Ensure that audit logs displayed in `sauti-admin` are strictly read-only and cannot be altered by administrators.
    - **Educate Administrators:** Provide clear guidance and training to administrators on how to access and interpret the audit information, emphasizing its importance for accountability and data integrity.

### Non-Technical Admin Coverage (Critical)
- **List of non-technical admin gaps:**
    - **Scattered Content Management:** As noted in "Navigation," various content types (Team, Core Values, Protection Approach, Timeline, Services, Contact Info) are managed through separate routes/components, making it difficult for a non-technical user to find all editable content in one place.
    - **"Uploads" Clarity:** The generic "Uploads" section lacks clarity on what it manages, potentially leading to confusion for non-technical users looking for a media library.
    - **Legal/Footer Text:** While `GlobalSettings` likely contains footer text, explicit routes/components for managing legal texts (Privacy, Terms, Accessibility) are not clearly visible in the router, suggesting they might be hardcoded or managed indirectly.
    - **Get Help Service Content:** The content for `/get-help/:service` (e.g., child-protection, GBV) is critical but its management interface is not explicitly clear. It might be part of `SiteContent` or `GlobalSettings`, but its discoverability is low.
- **Recommendations to centralise or clarify responsibility:**
    - **Create a Centralized "Content Management" Hub:** Introduce a primary navigation item for "Content Management" that serves as a gateway to all editable content types. This hub should provide clear links or sub-navigation to:
        - Homepage Content (Hero, Intro, News, Quick Access)
        - About Page Content (Core Values, Team, Protection Approach, Timeline)
        - Blog Posts
        - Videos
        - Resources
        - FAQs
        - Partners
        - Contact Information
        - Social Media Links & Posts
        - Legal & Footer Text (Privacy Policy, Terms of Service, Accessibility Statement, Footer details)
        - Media Library (renamed from "Uploads" for clarity)
        - Get Help Service Content (e.g., descriptions for child-protection, GBV services).
    - **Rename "Uploads" to "Media Library":** This provides a clearer understanding of its purpose for non-technical users.
    - **Explicit Routes for Legal/Footer Text:** Ensure there are clear, dedicated routes and components for managing legal and footer texts, even if they are stored in `GlobalSettings` or `SiteContent`.
    - **Clarify Get Help Service Content Management:** Clearly define where the content for the `/get-help/:service` pages is managed and make it easily discoverable within the "Content Management" hub.
- **Governance risks if left unchanged:**
    - **Increased Reliance on Developers:** Non-technical administrators will frequently require developer assistance to locate and update content or settings, leading to inefficiencies and bottlenecks.
    - **Inconsistent Content:** Without a clear, centralized content management structure, there's a higher risk of content being scattered, duplicated, or inconsistently updated across the platform.
    - **Compliance Risks:** Critical legal texts or service descriptions might be overlooked or difficult to update, leading to compliance issues.
    - **Poor User Experience:** Inconsistent or outdated content due to difficult administration directly impacts the end-user experience on the public frontend.

## Overall Cleanup & Governance Recommendations

### High
1.  **Implement Robust Audit Trail:** Integrate a third-party Django auditing package (e.g., `django-auditlog`) across all critical models in `sauti_cms`. This is crucial for accountability, data integrity, and compliance, especially for sensitive case reporting data.
2.  **Address Case Reporting Data Gaps:** Implement explicit `reported_person_age`, `reported_person_gender`, and `is_self_report` fields in the `Report` model. Update backend serializers and frontend forms in both `sauti-frontend` and `sauti-admin` to capture this vital demographic and contextual information.
3.  **Fix Social Media `fetch_metadata` Bug:** Add `import requests` and `from bs4 import BeautifulSoup` to `sauti_cms/social_media/views.py`. This is a critical bug that will prevent social media metadata fetching from working.

### Medium
1.  **Centralize Content Management Navigation:** Restructure `sauti-admin`'s navigation to introduce a primary "Content Management" hub that groups all editable content types, improving discoverability and ease of use for non-technical administrators.
2.  **Rationalize Reports & Blog Routes:** Consolidate redundant routes (e.g., `/reports/urgent`, `/reports/archive` into `/reports`; `/posts` and `/blogs` if they manage the same content) to simplify routing and navigation.
3.  **Enhance Operational Dashboard:** Improve `DashboardView` to display key operational metrics for case management (e.g., new reports today, reports by category/status).
4.  **Consolidate Social Media Profile Links:** Refactor backend to use a single source of truth for social media profile links (e.g., `GlobalSettings`) and update `sauti-admin` to reflect this unified management.
5.  **Cache Busting for Partner Logos:** Implement a custom storage backend for `Partner.logo` to ensure unique filenames on update, or configure CDN cache purging.
6.  **Update "Twitter" to "X" Branding:** Review and update all UI elements in `sauti-admin` and `sauti-frontend` that display "Twitter" to "X" or "Twitter/X" for consistent branding.

### Low
1.  **Rename "Uploads" to "Media Library":** Improve clarity for non-technical users.
2.  **Explicit Routes for Legal/Footer Text:** Ensure clear, dedicated routes and components for managing legal and footer texts.
3.  **Clarify Get Help Service Content Management:** Clearly define and make discoverable the interface for managing content on `/get-help/:service` pages.

## Out-of-Scope / Do-Not-Change Items
- **UI Redesigns:** No recommendations for visual UI changes or specific component layouts.
- **Backend API Structure:** Recommendations focus on how `sauti-admin` interacts with and exposes backend capabilities, not on fundamental changes to the Django API endpoints themselves (unless directly required by a critical gap).
- **Core Frameworks:** No changes to Vue.js, Pinia, Vue Router, Axios, or Django REST Framework usage.
- **Performance Optimizations:** While performance is always a consideration, specific code-level performance optimizations are out of scope for this audit.
