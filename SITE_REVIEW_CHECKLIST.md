### SAUTI WEBSITE – CONFIRMED GAP ANALYSIS CHECKLIST

#### 1. HOME

*   **Hero content partially hardcoded instead of CMS-driven:**
    *   **Confirmed Weak Area:** The decorative badges ("24/7 Available", "Multiple Languages", "Free & Confidential") in the hero section are currently hardcoded in `HomePage.vue`.
*   **Hotline (116) not persistent across scroll or mobile:**
    *   **Not a Gap:** The `AppHeader.vue` component used throughout the site is sticky (`sticky top-0 z-50`) and contains the hotline number, making it persistent across scroll.
*   **“Get Help Now” CTA not globally consistent:**
    *   **Confirmed Weak Area:** CTA buttons are implemented inconsistently using generic `<a>` or `<router-link>` tags with styling. A dedicated, reusable CTA component is not in place.
*   **Quick-access buttons not mapped to real service pages:**
    *   **Confirmed Weak Area:** The quick-access buttons link to `/report?category=...` rather than dedicated service detail pages (e.g., `/get-help/child-protection`). Dedicated pages for each service area do not currently exist.
*   **News/blog section not auto-hiding when empty:**
    *   **Not a Gap:** The News section on `HomePage.vue` correctly uses `v-if="latestVideos.length > 0"` to hide when there are no items.
*   **Partner logos duplicated or hardcoded:**
    *   **Confirmed Weak Area (Component Duplication):** While partner data is sourced from the CMS, the visual rendering logic for the partner grid is duplicated between `HomePage.vue` and `AboutPage.vue`.
*   **Footer content inconsistent across pages:**
    *   **Confirmed Weak Area:** The main navigation links (`navLinks`) and legal links (`legalLinks`) in `AppFooter.vue` are hardcoded within the component's script.

#### 2. ABOUT SAUTI

*   **History text hardcoded:**
    *   **Not a Gap (Fixed):** The "History" section (now "Our Journey") is dynamically populated from the `timeline-events` API endpoint and rendered via the `AppTimeline` component.
*   **Mission & Vision duplicated across pages:**
    *   **Not a Gap (Fixed):** Mission and Vision are now stored in `GlobalSettings` (accessible via "About Page Settings" in admin) and fetched from a single source.
*   **Core values not structured:**
    *   **Not a Gap (Fixed):** Core values are fetched from the `/content/core-values/` API endpoint, providing a structured list.
*   **Impact stats static or missing entirely:**
    *   **Confirmed Weak Area (Improvement Needed):** Impact statistics are currently sourced from generic `about_statX_title`/`text` fields within the monolithic `GlobalSettings` model, rather than a dedicated, structured model for impact data.
*   **Partner descriptions inconsistent with homepage:**
    *   **Not a Gap (Fixed):** The "Partners" section on the About Page now uses the same rendering logic and data sourcing as the Home Page.

#### 3. GET HELP

*   **Subsections exist but content depth is inconsistent:**
    *   **Confirmed Gap:** Dedicated, content-rich pages (e.g., `/get-help/child-protection`) for each quick-access service area do not exist. The current implementation only supports linking to the `ReportPage` with a category pre-selected.
*   **Steps for getting help unclear or text-heavy:**
    *   **Confirmed Gap (Implied):** Since no dedicated "Get Help" detail pages exist, the detailed steps for getting help are not present in a structured, user-friendly format.
*   **Reporting links not standardized:**
    *   **Confirmed Gap (Implied):** Without dedicated service pages, the consistency of reporting links across different service contexts cannot be enforced.
*   **WhatsApp / hotline links inconsistent:**
    *   **Confirmed Gap (Implied):** Similar to reporting links, consistency is difficult to maintain without a central component or structured approach for links on "Get Help" pages.
*   **Downloadable resources missing per subsection:**
    *   **Confirmed Gap (Implied):** Dedicated "Get Help" pages would typically feature relevant resources, which are currently missing due to the absence of these pages.

#### 4. REPORT CASE

*   **Anonymous logic unclear to users:**
    *   **Confirmed Weak Area:** The chat-bot style `ReportForm.vue` allows skipping contact details, and the `handleSubmit` process explicitly sends `is_anonymous: false` while populating contact name with 'Anonymous' if skipped. The `is_anonymous` flag should be accurately set when a user chooses to be anonymous.
*   **Confirmation message vague or absent:**
    *   **Not a Gap:** The `ReportForm.vue` clearly provides a success message with a reference number and explains next steps after submission.
*   **No expectation-setting after submission:**
    *   **Not a Gap:** The `ReportPage.vue` clearly sets expectations _before_ submission with a "How it works" stepper (Fill details, Submit securely, We follow up). The `ReportForm.vue` also provides clear post-submission messages.
*   **File upload validation unclear:**
    *   **Confirmed Gap:** The `ReportForm.vue` component currently has no functionality for file uploads.
*   **No category-based routing:**
    *   **Not a Gap:** While not dedicated routes, the `ReportPage` already handles category pre-selection via query parameters (`/report?category=...`), effectively routing inputs based on category.

#### 5. NEWS & BLOGS

*   **No clear separation between News and Blogs:**
    *   **Confirmed Gap:** The `Post` model in `sauti_cms/posts/models.py` lacks a specific field (e.g., `type: 'News'` or `'Blog'`) to distinguish between news articles and blog posts.
*   **Categories not enforced:**
    *   **Not a Gap:** Categories are enforced via the `Category` foreign key in the `Post` model.
*   **Author/date metadata inconsistent:**
    *   **Not a Gap:** `author` and `published_at` fields exist and are used.
*   **Images optional but not validated:**
    *   **Not a Gap:** The `featured_image` field in `Post` model is optional, as expected. Frontend validation for client-side uploads is typical but not explicitly requested as a gap.

#### 6. RESOURCES

*   **Downloads scattered or mixed with blogs:**
    *   **Not a Gap:** Resources are managed by a dedicated `Resource` model and displayed on `ResourcesPage.vue`, separate from blog posts.
*   **No language tagging:**
    *   **Not a Gap:** The `Resource` model includes a `language` field with English, Luganda, and Swahili choices, and `ResourcesPage.vue` uses this for filtering.
*   **FAQs hardcoded:**
    *   **Not a Gap:** FAQs are managed by `FAQ` and `FAQCategory` models and pulled from the API on `FaqsPage.vue`.
*   **No search or filters:**
    *   **Not a Gap:** The `ResourcesPage.vue` has search, category, and language filters.

#### 7. CONTACT US

*   **Contact channels scattered:**
    *   **Not a Gap:** Contact channels are fetched from the `/content/contacts/` API endpoint and displayed centrally on `ContactPage.vue`.
*   **WhatsApp link inconsistent:**
    *   **Not a Gap:** WhatsApp links are sourced from the API and displayed consistently.
*   **Feedback form unclear purpose:**
    *   **Confirmed Gap:** The `ContactPage.vue` component currently does not include a feedback form.
*   **Physical address not standardized:**
    *   **Not a Gap:** The physical address (e.g., `ministry_attribution_text`) is sourced from `GlobalSettings`, ensuring a single authoritative entry.

#### CROSS-CUTTING GAPS (CRITICAL)

1.  **Content Governance**
    *   **Missing draft/publish states for content:**
        *   **Confirmed Weak Area:** While the `Post` model supports draft/publish states, other content models like `Resource` and `FAQ` primarily rely on a simple `is_active` boolean or are published upon creation, lacking a full draft/publish workflow.
    *   **No clear ownership of updates:**
        *   **Confirmed Weak Area:** The ownership of updates is not explicitly tracked or displayed across all content types.
2.  **Consistency & Reuse**
    *   **Components duplicated with small differences:**
        *   **Confirmed Weak Area:**
            *   **CTA Button:** No dedicated reusable component exists; buttons are styled using Tailwind classes on `<a>` or `<router-link>` tags.
            *   **Partner Grid:** The rendering logic for the partner grid was duplicated between `HomePage.vue` and `AboutPage.vue` (though I recently aligned them, it's still duplicate logic rather than a single component).
            *   **Help Steps:** No such component exists due to the absence of dedicated "Get Help" service pages.
            *   **Section Header:** No standardized section header component is used; headers are styled directly in each page/section.
3.  **Accessibility**
    *   **Confirmed Area for Review:** This requires a manual audit against WCAG AA standards, which cannot be automated by the tool. This remains a critical area for human verification.