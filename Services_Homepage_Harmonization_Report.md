# Services Page Harmonization with Home Page Report

## Context
We currently have two pages:
- Home page (entry point, narrative-driven)
- Services page (detailed explanation of services, identified as `/get-help/:service` using `GetHelpDetail.vue`)

The ultimate goal is to completely remove the standalone Services page and make the Home page the single authoritative location for all services content, while preserving clarity, usability, and maintainability.

## PRIMARY OBJECTIVE (NON-NEGOTIABLE)
Eliminate the Services page entirely. All service-related content must be fully integrated into the Home page in a way that:
- Feels intentional, not crowded
- Preserves information hierarchy
- Maintains design consistency
- Avoids content loss
- Remains CMS-driven

After completion:
- `/services` (or `/get-help/:service`) must no longer be needed as a page
- Users must understand what we do without navigating away from Home

---

## 1. FULL CONTENT AUDIT

### A. Complete Inventory of Sections/Components on Home Page (`sauti-frontend/src/views/HomePage.vue`)
1.  **Hero Section:** (CMS: `GlobalSettings`)
    *   Title, Value Proposition, Hotline CTA, Report CTA, Dynamic Badges.
2.  **Intro Section:** (CMS: `GlobalSettings`)
    *   "Who We Are" title, description.
3.  **Quick Access Buttons (Service Overview):** (CMS: `GlobalSettings`)
    *   "How Can We Help?" title, description.
    *   4 cards (Child Protection, GBV, Migrants, PSEA), each with title, short text, icon, linking to `/get-help/:service`.
4.  **Latest News / Blogs Section:** (CMS: `GlobalSettings` for titles/descriptions, `Posts` app for blog data)
    *   Title, Description, "View All News" CTA.
    *   Displays 3 latest published posts (thumbnail, category, title).
5.  **Partner Logos Section:** (CMS: `GlobalSettings` for titles/descriptions, `Partners` app for partner data)
    *   Title, Description.
    *   Displays partner logos via `PartnerGrid`.

### B. Complete Inventory of Sections/Components on Services Page (`sauti-frontend/src/views/GetHelpDetail.vue`)
(Content for 'child-protection', 'gbv', 'migrants', 'psea' is loaded dynamically)
1.  **Hero Section:** (Frontend `staticServices` fallback, API `/sitesettings/...` for `title`/`intro_text` derived from `GlobalSettings`)
    *   Service Icon (static fallback or default).
    *   Service Title (`Child Protection`, `GBV Support`, etc.).
    *   Service Short Description (`Protecting children from ...`).
2.  **Main Content (Left Column):**
    *   **"What does this include?" Section:**
        *   Introductory Text (`introText`). (Frontend `staticServices` fallback, API `/sitesettings/...` for `intro_text` derived from `GlobalSettings`)
        *   Scope Items (list of bullet points). (Frontend `staticServices` fallback, API `/sitesettings/...` returns `[]`)
    *   **"How we can help" Section:**
        *   Help Steps (list of detailed steps). (Frontend `staticServices` fallback, API `/sitesettings/...` returns `[]`)
3.  **Actions (Right Column):** (CMS: `GlobalSettings` for help contacts)
    *   "Get Help Now" Call to Action.
    *   Help Contacts.

### C. Overlapping Concepts, Redundant Content, Content Missing from Home

*   **Overlapping Concepts:**
    *   Overall Service Categories (Child Protection, GBV, Migrants, PSEA) - central to both pages.
    *   High-level service descriptions/titles.
*   **Redundant Content:**
    *   **Titles & Short Descriptions of Services:** `GlobalSettings.qa_..._title/text` (HomePage) vs. `HelpService.title/intro_text` (Backend Model) vs. `staticServices.title/description/introText` (ServicesPage Frontend).
    *   **Service Icons:** Hardcoded in HomePage vs. in `staticServices` in ServicesPage.
*   **Content Missing from Home but present in Services (Detailed Service Content):** This is the main content to be integrated. It currently lives in `sauti_cms/services.HelpService` and `sauti_cms/services.HelpStep` models but is pulled by `GetHelpDetail.vue` from its local `staticServices` fallback due to the `sitesettings` API returning empty `scope_items` and `steps`.
    *   Detailed `introText` for each service.
    *   `scopeItems` (list of what's covered).
    *   `helpSteps` (how we can help, step-by-step).
    *   Service-specific icons (though `staticServices` are currently providing them).
    *   Service-specific contact information/CTAs (via `HelpContacts` component).

---

## 2. CONTENT RESTRUCTURING DECISIONS

For every `GetHelpDetail.vue` section:

1.  **Hero Section (Service Icon, Title, Short Description):**
    *   **Decision:** Merge with Home's "Quick Access Buttons" (Service Overview) and enhance those cards.
    *   **Justification:** Integrates high-level service description directly into the main navigation flow on the Home page, providing immediate context and avoiding redundancy.

2.  **"What does this include?" Section (Introductory Text, Scope Items):**
    *   **Decision:** Move to Home (full content, integrated into expanded service sections).
    *   **Justification:** Essential for understanding service offerings and needs to be present on the Home page, providing the "what" of each service.

3.  **"How we can help" Section (Help Steps):**
    *   **Decision:** Move to Home (full content, integrated into expanded service sections).
    *   **Justification:** Provides the "how" of each service, crucial for user action, and needs to be easily accessible directly on the Home page.

4.  **Actions (Right Column - "Get Help Now" CTA, Help Contacts):**
    *   **Decision:** Move to Home (condensed version/merge with existing CTAs and contextual placement).
    *   **Justification:** Primary CTA is already in the Home page Hero. Service-specific contact details should be presented contextually within each expanded service section on the Home page.

---

## 3. HOME PAGE RE-ARCHITECTURE

**Proposed Section Order (Top to Bottom):**

1.  **Hero Section:** (Existing)
    *   Large title, value prop, primary CTAs (Call Hotline, Report a Case).
    *   Dynamic badges.
2.  **Intro Section:** (Existing)
    *   "Who We Are" short description.
3.  **"How We Can Help" - Services Overview (Enhanced):** (Existing "Quick Access Buttons" + merged service intro)
    *   Title: "How We Can Help?"
    *   Description: "Access immediate support across these key protection areas."
    *   A grid of 4 cards, one for each core service (Child Protection, GBV, Migrants, PSEA).
    *   Each card will clearly show: `service.title`, `service.summary` (condensed intro text), and `service.icon`.
    *   **Clicking/Tapping a card will unveil / progressively disclose the *detailed* content for that specific service directly on the Home page.**
4.  **(Hidden by default) Detailed Service Sections:** (New, revealed on interaction with "Services Overview" cards)
    *   These will be individual, expandable sections, one for each `HelpService` (Child Protection, GBV, Migrants, PSEA).
    *   When a user interacts with a service card in the "How We Can Help" section, the corresponding detailed section below will expand (scroll to view, or accordion/modal).
    *   Each expanded section will contain:
        *   **Service Hero:** (Title, Description from `HelpService`)
        *   **"What does this include?"**: `HelpService.intro_text` and `HelpService.scope_items`.
        *   **"How we can help"**: `HelpStep`s from `HelpService`.
        *   **Service-specific CTAs/Contacts:** A small, contextual block with relevant contact methods/CTAs.
5.  **Latest News / Blogs Section:** (Existing)
6.  **Partner Logos Section:** (Existing)

---

## 4. DESIGN CONSISTENCY REQUIREMENTS

The integration must feel native to the Home page.

*   **Use Existing Home page components:**
    *   **Typography:** Maintain existing font sizes, weights, and line heights.
    *   **Colors:** Adhere to the existing color palette.
    *   **Spacing:** Follow `section-padding` for vertical rhythm and existing `gap` values for horizontal spacing.
    *   **Cards/Grids:** The "Quick Access Buttons" section already uses a grid of cards (`avm-card`). The expanded service sections should aim to echo this visual style or use similar container elements.
*   **Avoid introducing a “Services-page-looking” block:** Do not bring over styles or layouts that are unique to the `GetHelpDetail.vue`. The goal is full integration, not embedding.
*   **Follow the Home page visual rhythm:** Sections should flow logically with appropriate headings and visual breaks, building on the existing `HomePage.vue` structure.
*   **If new components are required:**
    *   They must be Home-native (i.e., designed to fit the existing visual language of `HomePage.vue`).
    *   Reusable (e.g., a generic `ExpandableSection` component).
    *   Minimal (avoid excessive styling or complex interactions).

---

## 5. SERVICES CONTENT PRESENTATION MODEL

A progressive disclosure pattern on Home is crucial.

*   **Overview layer (quick understanding):**
    *   The "How We Can Help" section (enhanced Quick Access cards) serves as the overview layer. Each card provides the service title, a condensed summary, and an icon.
*   **Expanded service sections (still on Home):**
    *   Upon user interaction (e.g., clicking on a service card), a corresponding detailed service section will progressively disclose directly on the Home page.
*   **Proposed Progressive Disclosure Mechanism:**
    *   An **accordion-style expand/collapse section** is the most suitable. When a user clicks a "How We Can Help" card, the corresponding accordion for that service expands. This keeps the initial page load fast and uncluttered, allows users to explore details on demand, and maintains a single-page experience. A smooth scroll to the expanded section would enhance UX.

---

## 6. CMS / DATA MODEL (SINGLE SOURCE OF TRUTH)

The core issue identified was the discrepancy between the `HelpService`/`HelpStep` models (containing detailed content) and the `GlobalSettings` fields (containing summary content used by the frontend). The `staticServices` in `GetHelpDetail.vue` is a stop-gap.

*   **Primary Source of Truth:** The `sauti_cms/services.HelpService` and `sauti_cms/services.HelpStep` models will become the single, authoritative source of truth for all service-related content, including summaries, icons, and detailed explanations.
*   **Modify `HelpService` Model (`sauti_cms/services/models.py`):**
    ```python
    from django.db import models
    # Assuming User model is imported or referenced properly

    class HelpService(models.Model):
        SERVICE_KEYS = [
            ('child-protection', 'Child Protection'),
            ('gbv', 'Gender Based Violence'),
            ('migrants', 'Migrant Workers'),
            ('psea', 'PSEA'),
        ]

        key = models.CharField(max_length=50, choices=SERVICE_KEYS, unique=True, help_text="Unique key for the service URL and internal reference")
        title = models.CharField(max_length=255, help_text="Main title of the service (e.g., Child Protection)")
        summary = models.TextField(blank=True, null=True, help_text="A short summary for quick overview on the homepage.") # NEW FIELD
        intro_text = models.TextField(help_text="Detailed introductory paragraph for the service section.")
        scope_items = models.JSONField(default=list, blank=True, help_text="List of items covered by this service (JSON array of strings)")
        icon_name = models.CharField(max_length=50, blank=True, null=True, help_text="Name of the HeroIcons icon for display (e.g., 'UserGroupIcon')") # NEW FIELD - assumes frontend uses HeroIcons
        homepage_display_order = models.IntegerField(default=0, help_text="Order in which this service appears on the homepage quick access section.") # NEW FIELD

        created_by = models.ForeignKey(
            'users.User',
            on_delete=models.SET_NULL,
            null=True,
            blank=True,
            related_name='%(class)s_created'
        )
        last_updated_by = models.ForeignKey(
            'users.User',
            on_delete=models.SET_NULL,
            null=True,
            blank=True,
            related_name='%(class)s_updated'
        )
        is_active = models.BooleanField(default=True, help_text="Whether this service is active and should be displayed.")
        
        class Meta:
            ordering = ['homepage_display_order', 'order'] # Prioritize homepage order
            verbose_name = "Help Service"
            verbose_name_plural = "Help Services"

        def __str__(self):
            return self.title

    class HelpStep(models.Model):
        # ... no changes to this model ...
        service = models.ForeignKey(HelpService, related_name='steps', on_delete=models.CASCADE)
        title = models.CharField(max_length=255)
        description = models.TextField()
        step_order = models.IntegerField(default=0)

        class Meta:
            ordering = ['step_order']
            verbose_name = "Help Step"
            verbose_name_plural = "Help Steps"

        def __str__(self):
            return f"{self.service.title} - Step {self.step_order}"

    # Deprecate the `Service` model if it's no longer used for any purpose beyond what HelpService will now cover.
    # Otherwise, clearly define its distinct purpose (e.g., general organizational services).
    
    ```
*   **Remove Redundant `GlobalSettings` Fields:**
    *   In `sauti_cms/sitesettings/models.py`, remove the `qa_child_protection_title`, `qa_child_protection_text`, `qa_gbv_title`, `qa_gbv_text`, `qa_migrants_title`, `qa_migrants_text`, `qa_psea_title`, `qa_psea_text` and their corresponding icon fields (`qa_..._icon`). These will now be sourced from `HelpService`.
*   **Update Serializers (`sauti_cms/services/serializers.py`):**
    *   Modify `HelpServiceSerializer` to include the new `summary`, `icon_name`, and `homepage_display_order` fields.
    *   Remove `ServiceSerializer` if `Service` model is deprecated.
*   **Update Views (`sauti_cms/services/views.py`):**
    *   The `HelpServiceViewSet` should remain `ReadOnlyModelViewSet`. It will now serve as the primary API for all detailed service content.
    *   Remove `ServiceViewSet` if `Service` model is deprecated.
    *   **Crucially:** Remove `GetHelpServicesView` and `GetHelpServiceDetailView` from `sauti_cms/sitesettings/views.py` and corresponding URL patterns. The frontend will directly call `HelpServiceViewSet`.

---

## 7. ROUTING & DECOMMISSIONING

*   **Decommissioning `/get-help/:service`:**
    *   **Remove Route:** Delete the `/get-help/:service` route entry from `sauti-frontend/src/router/index.js`.
    *   **Remove Component:** Delete `sauti-frontend/src/views/GetHelpDetail.vue`.
*   **Handling Existing Links:**
    *   **301 Redirect to Home Anchor:** For each `service` slug (e.g., `child-protection`, `gbv`, `migrants`, `psea`), implement a 301 Permanent Redirect (server-side, e.g., in Nginx, Apache, or a Django middleware) from `/get-help/:service` to `/home#<service-anchor>`.
    *   Example: `/get-help/child-protection` redirects to `/home#child-protection`.
    *   The Home page will need to implement anchor links for each detailed service section.
*   **Mitigating SEO Impact:**
    *   **301 Redirects:** Permanent 301 redirects are essential for transferring SEO value from the old `/get-help/:service` URLs to the new Home page sections.
    *   **Canonical Tags:** Ensure the Home page has a self-referencing canonical tag.
    *   **Sitemap Update:** Update the sitemap (`sitemap.xml`) to remove the `/get-help/:service` URLs and ensure only the canonical URLs are listed.
    *   **Internal Linking:** Update all internal links within the website that point to `/get-help/:service` to instead point to `/home#<service-anchor>`.

---

## Before → After Home page structure

**Before Home Page Structure:**
1.  Hero Section (CMS: `GlobalSettings`)
2.  Intro Section (CMS: `GlobalSettings`)
3.  Quick Access Buttons (Service Overview - 4 cards, linking to `/get-help/:service`) (CMS: `GlobalSettings`)
4.  Latest News / Blogs Section (CMS: `GlobalSettings`, `Posts` app)
5.  Partner Logos Section (CMS: `GlobalSettings`, `Partners` app)

**After Home Page Structure:**
1.  **Hero Section:** (Existing content)
2.  **Intro Section:** (Existing content)
3.  **"How We Can Help" - Services Overview (Enhanced and Interactive):**
    *   Grid of 4 interactive cards, one for each core service.
    *   Each card: Service `title`, `summary`, `icon` (all from `HelpService` model).
    *   Clicking/tapping a card progressively discloses the detailed content for that specific service directly below it on the Home page.
4.  **Detailed Service Sections (Hidden by default, progressively disclosed):**
    *   One expandable section for each `HelpService` (e.g., "Child Protection," "GBV," etc.).
    *   Each section contains:
        *   Service Title, `intro_text`, `scope_items` (from `HelpService`).
        *   "How we can help" steps (from `HelpStep`).
        *   Contextual Call to Action / Help Contacts (derived from `HelpContacts` or `GlobalSettings`).
5.  **Latest News / Blogs Section:** (Existing content)
6.  **Partner Logos Section:** (Existing content)

### Mapping table: Services page section → Home page section

| Services Page Section (`GetHelpDetail.vue`)                       | Home Page Section (Post-Migration)                           | Justification                                                                |
| :---------------------------------------------------------------- | :----------------------------------------------------------- | :--------------------------------------------------------------------------- |
| Hero Section (Service Icon, Title, Short Description)             | "How We Can Help" - Services Overview (Enhanced Cards)       | High-level overview integrated into primary navigation for services.         |
| "What does this include?" (Introductory Text, Scope Items)        | Detailed Service Section (Expanded Content)                  | Essential detailed information moved to progressive disclosure on Home.      |
| "How we can help" (Help Steps)                                    | Detailed Service Section (Expanded Content)                  | Critical "how-to" information moved to progressive disclosure on Home.       |
| Actions (Right Column - "Get Help Now" CTA, Service-specific Contacts) | Detailed Service Section (Contextual CTAs/Contacts) & existing Hero CTA | Integrated service-specific actions within relevant expanded sections; primary CTA remains in Hero. |

### Detailed Home page section descriptions

1.  **Hero Section:** Remains unchanged in its purpose. Strong visual impact, primary helpline number, and general "Report a Case" CTA.
2.  **Intro Section:** Remains unchanged. High-level "Who We Are" statement.
3.  **"How We Can Help" - Services Overview (Enhanced and Interactive):**
    *   **Purpose:** To provide a clear, scannable overview of the core services offered, acting as the primary entry point for detailed service exploration on the Home page.
    *   **Content:** A grid of distinct cards, each representing a `HelpService` (e.g., Child Protection). Each card will concisely present the `HelpService.title`, `HelpService.summary`, and `HelpService.icon_name`.
    *   **Interaction:** Clicking any card will dynamically expand (or scroll to) the corresponding "Detailed Service Section" on the same Home page, showcasing its full content.
4.  **Detailed Service Sections (Hidden by default, progressively disclosed):**
    *   **Purpose:** To present the comprehensive details of each service offering, accessible on demand directly from the Home page, avoiding navigation to a separate page.
    *   **Content:** Each section will be dedicated to a single `HelpService` (e.g., "Child Protection"). It will include:
        *   A clear heading (`HelpService.title`).
        *   The detailed introductory paragraph (`HelpService.intro_text`).
        *   A bulleted list of "What we cover" (`HelpService.scope_items`).
        *   A step-by-step guide explaining "How we can help" (`HelpStep`s, including `title` and `description` for each step).
        *   A contextual call-to-action or contact information block (e.g., "Need immediate help? Call 116 or chat with us").
    *   **Structure:** Each service's detailed content will be contained within an expandable element (e.g., accordion, expand/collapse component) to prevent overwhelming the initial page view.
5.  **Latest News / Blogs Section:** Remains unchanged. Displays recent news/blog posts.
6.  **Partner Logos Section:** Remains unchanged. Displays partner organizations.

### Frontend implementation notes

*   **API Calls:**
    *   `HomePage.vue` will call `/api/services/help-services/` to fetch *all* `HelpService` objects. This single API call will provide all the necessary data for both the "How We Can Help" overview cards and the detailed expanded service sections.
    *   Remove the `api.get(/sitesettings/get-help-services/${serviceSlug.value}/)` call from `GetHelpDetail.vue` (and by extension from `HomePage.vue` if it was still relying on `qa_...` from `GlobalSettings` for service summaries).
*   **State Management:**
    *   Create a dedicated Pinia store (e.g., `store/helpServices.js`) to fetch and manage the list of `HelpService` objects.
    *   `HomePage.vue` will use this store.
*   **Component Structure in `HomePage.vue`:**
    *   In the "How We Can Help" section, iterate over the `helpServices` fetched from the new store to render the interactive overview cards. Each card will bind its data (`title`, `summary`, `icon_name`, `key`) directly from the `HelpService` object.
    *   Below this overview section, dynamically render the "Detailed Service Sections". These can be implemented as a `v-for` loop over `helpServices`, each wrapped in an `ExpandableSection` component.
    *   The `ExpandableSection` component (to be created) will manage its own `expanded` state, display the `HelpService.title` as its header, and conditionally render the `HelpService.intro_text`, `HelpService.scope_items`, and nested `HelpStep`s from the `HelpService` object when expanded.
    *   Implement smooth scrolling to the expanded section when a corresponding overview card is clicked.
*   **Icon Handling:** Convert the `icon_name` string from `HelpService` into the actual HeroIcons component in `HomePage.vue`. (Example: If `icon_name` is 'UserGroupIcon', render `<UserGroupIcon />`).
*   **Decommission `staticServices`:** Remove the `staticServices` object from `GetHelpDetail.vue` once the API is correctly integrated and tested.

### Services page decommissioning plan

1.  **Backend Data Model Refinement:**
    *   Modify `sauti_cms/services/models.py`: Add `summary`, `icon_name`, `homepage_display_order` to `HelpService`.
    *   Run Django migrations.
    *   Update `sauti_cms/services/serializers.py`: Include new fields in `HelpServiceSerializer`.
    *   Remove `Service` model and its related serializer/viewset if deemed redundant.
    *   **Migrate Data:** Populate the new `summary`, `icon_name`, `homepage_display_order` fields in existing `HelpService` instances via Django Admin or a data migration script. Use the data currently in `GlobalSettings.qa_...` and `staticServices` as source.
    *   **Remove Redundant GlobalSettings:** Delete obsolete `qa_...` fields from `sauti_cms/sitesettings/models.py` and run migrations.
    *   Remove `GetHelpServicesView` and `GetHelpServiceDetailView` from `sauti_cms/sitesettings/views.py` and corresponding URL patterns.

2.  **Frontend Implementation (`sauti-frontend`):**
    *   Create `store/helpServices.js` Pinia store to fetch `HelpService` data.
    *   Modify `HomePage.vue`:
        *   Integrate the new Pinia store to fetch `HelpService` data.
        *   Refactor "Quick Access Buttons" to display enhanced interactive cards using `HelpService` data.
        *   Implement the "Detailed Service Sections" using a progressive disclosure pattern (e.g., accordion component), dynamically rendering content from `HelpService` and `HelpStep` data.
    *   **Delete `sauti-frontend/src/views/GetHelpDetail.vue`.**
    *   Remove the `'/get-help/:service'` route from `sauti-frontend/src/router/index.js`.
    *   Remove any related imports or utility functions that become unused.

3.  **Routing & SEO:**
    *   **Server-Side Redirects:** Configure 301 Permanent Redirects on the web server (Nginx/Apache) from `/get-help/:service` to `/home#<service-anchor>` for each service key.
        *   Example Nginx: `rewrite ^/get-help/(.*)$ /#$1 permanent;` (adjust regex to match specific service keys for better control)
    *   **Internal Link Updates:** Update all internal links across the Sauti website (frontend, admin, CMS content) that refer to `/get-help/:service` URLs to point to the Home page with relevant anchors (e.g., `/home#child-protection`).
    *   **Sitemap:** Update `sitemap.xml` to remove old `/get-help/...` URLs and ensure the Home page is correctly indexed.
