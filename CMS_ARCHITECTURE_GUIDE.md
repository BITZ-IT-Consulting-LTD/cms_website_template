# Sauti 116 CMS Architecture & Content Governance

This document defines the content model and workflow strategies for the Sauti 116 Helpline CMS (Django Administration). It ensures that non-technical editors can maintain the site’s professional, survivor-centered tone without developer intervention.

---

## 1. CMS Content Model (Prompt P)

To support a dynamic, editable website, the CMS is structured into semantic modules. Each field includes "Help Text" to guide editors.

### **Module A: Site Identity & Branding**
*Location: `sitesettings.OrganizationProfile`*

| Field Name | Type | Purpose | Editor Guidance |
| :--- | :--- | :--- | :--- |
| `name` | String | Organization Name | Use "Sauti 116 Helpline" |
| `logo` | Image | Primary Logo | PNG/SVG, White background or Transparent |
| `brand_colors` | JSON | Primary/Secondary/Emergency | Hex codes only. Do not change without Brand Approval. |
| `hotline_number` | String | The call number | Default: 116. Appears in all Urgent CTAs. |

### **Module B: Homepage Content**
*Location: `sitesettings.GlobalSettings`*

| Field Name | Type | Purpose | Editor Guidance |
| :--- | :--- | :--- | :--- |
| `hero_title` | Text | Main Heading | Simple, empathetic language (e.g., "Your Voice Matters") |
| `hero_subtitle` | Long Text | Value Proposition | Explain confidentiality and 24/7 availability. |
| `primary_cta_text`| String | Button Text | Action-oriented (e.g., "Report Online"). |
| `intro_title` | String | Secondary Section | Direct and supportive (e.g., "Our Promise"). |

### **Module C: Partnerships & Credibility**
*Location: `partners.Partner`*

| Field Name | Type | Purpose | Editor Guidance |
| :--- | :--- | :--- | :--- |
| `name` | String | Partner Organization | Full legal name. |
| `logo` | Image | Brand Mark | Use high-quality logos with no background. |
| `website_url` | URL | Partner Site | Link to their official homepage. |
| `is_active` | Boolean | Visibility | Toggle to remove from site without deleting data. |

### **Module D: Legal & Policies**
*Location: `content.Policy`*

| Field Name | Type | Purpose | Editor Guidance |
| :--- | :--- | :--- | :--- |
| `title` | String | Page Heading | e.g., "Privacy Policy", "Safety Protocol" |
| `slug` | Slug | URL Path | Use lowercase, hyphenated (e.g., `privacy-policy`) |
| `content` | Rich Text | Policy Body | Use H3 headings for sections. Avoid bureaucratic jargon. |

---

## 2. Notification & Workflow Setup (Prompt Q)

Safe and accurate content is critical. The following workflows prevent unauthorized or accidental changes to sensitive information.

### **Workflow A: Content Review Cycle**
1.  **Draft State**: New articles (Stories & Updates) or Policy changes start as `DRAFT`.
2.  **Peers Review**: A notification is triggered to the "Senior Editor" group via the CMS Dashboard.
3.  **Approval**: Content is moved to `PUBLISHED` status. Only admins with `can_publish` permissions can finalize this.

### **Workflow B: Permission Tiers**
-   **Junior Editor**: Can create/edit Stories, FAQs, and Helpful Guides. Cannot edit Branding or Hotline numbers.
-   **Protection Admin**: Can manage "Help Services" and view anonymized "Incident Reports."
-   **Superuser**: Full access to color tokens and site-wide settings.

### **Workflow C: Data Validation Rules**
-   **Hotline Field**: Must be exactly 3 digits (116). CMS will reject any other input.
-   **Image Size**: Logos must be under 500KB to ensure fast mobile page speeds.
-   **Hex Codes**: Color fields must start with `#` and be 6 characters long.

### **Workflow D: Notification Triggers**
| Event | Recipient | Channel | Rationale |
| :--- | :--- | :--- | :--- |
| **New Report Filed** | Protection Team | Secure Dashboard + SMS | Immediate response for crisis intervention. |
| **Setting Changed** | Site Owner | Email | Security audit for changes to hotline/logo/colors. |
| **New Post Added** | All Editors | Slack/Internal | Ensures team alignment on new public messaging. |

---

## 3. Editor Guidance (Tone of Voice)
-   **Avoid**: "Intake", "Offence", "Bureau of", "Official Procedure".
-   **Use**: "Support", "What happened", "Helping you", "Safe space".
-   **Survivor-Centered**: Always explain *why* we need information (e.g., "To help us get you the right support").
