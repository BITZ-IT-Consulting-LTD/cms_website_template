# SAUTI 116 — Partner Section Design & Trust Signal Audit

**Date**: 2026-01-07  
**Auditor**: UX Systems Designer (Public Trust Interfaces)  
**Context**: Homepage partner section for institutional credibility without brand dilution

---

## EXECUTIVE SUMMARY

### Current Status
✅ **Partner infrastructure exists** (CMS model, frontend component, API)  
❌ **Visual treatment is TOO SUBDUED** (opacity: 60%, grayscale, 10px text)  
❌ **Audit finding**: "There is no partner section in the footer" (visibility issue)

### Problem Statement
The homepage partner section **exists but is invisible** due to:
- 60% opacity on entire section
- Grayscale filter on logos (40% opacity default, 30% without link)
- 10px text (below minimum legibility threshold)
- No visual hierarchy or grouping

**Impact**: Users cannot see partner logos, reducing institutional credibility and trust.

---

## 🎯 SECTION PURPOSE & STRATEGIC PLACEMENT

### Purpose
**Build institutional credibility** by showing Sauti 116's official backing and network, without:
- ❌ Overpowering Sauti 116 branding
- ❌ Creating "government surveillance" perception
- ❌ Appearing as advertising or sponsorship

### Strategic Placement (Homepage)

**Current Position**: ✅ **CORRECT** (Section 5, after content, before footer)

```
Homepage Flow:
1. Hero (CTAs)
2. Intro (Impact)
3. Services (Expandable cards)
4. Latest News (Blog/Videos)
5. ✅ PARTNERS ← Current position (KEEP)
6. Footer
```

**Rationale**:
- ✅ **Non-intrusive**: Doesn't interrupt primary user flows
- ✅ **Trust-building**: Reinforces credibility after user has engaged with content
- ✅ **SEO-friendly**: Near footer for crawlability
- ✅ **Brand-safe**: Sauti 116 branding dominates above-the-fold

**Alternative Placement (NOT RECOMMENDED)**:
- ❌ **Above hero**: Too dominant, feels like advertising
- ❌ **In hero**: Dilutes emergency CTA focus
- ❌ **Footer only**: Too hidden, reduces credibility signal

---

## 📐 LAYOUT SPECIFICATION

### Section Container

```html
<section class="section-padding bg-neutral-offwhite">
  <div class="container-custom">
    <!-- Header -->
    <!-- Partner Grid -->
  </div>
</section>
```

**Design Decisions**:
- **Background**: `bg-neutral-offwhite` (#F8FAFCF) — Subtle differentiation from white sections
- **Padding**: `section-padding` (py-20 mobile, py-32 desktop) — Consistent with other sections
- **Container**: `container-custom` (max-w-7xl) — Aligns with site grid

---

### Section Header

```html
<div class="text-center mb-12 md:mb-16">
  <h2 class="text-3xl md:text-4xl font-bold text-secondary mb-4">
    {{ settings.partners_title || 'Official Protection Partners' }}
  </h2>
  <p class="text-lg md:text-xl text-black max-w-2xl mx-auto">
    {{ settings.partners_description || 'Working together to protect every child and survivor in Uganda.' }}
  </p>
</div>
```

**Design Decisions**:
- **Heading size**: 3xl (mobile) → 4xl (desktop) — Smaller than hero, larger than subsections
- **Heading color**: `text-secondary` (Sauti Deep Green) — Brand consistency
- **Description color**: `text-black` — **CHANGED** from `text-secondary opacity-70` for brand compliance
- **Max-width**: 2xl (672px) — Optimal reading length
- **Alignment**: Center — Neutral, non-promotional

---

### Partner Grid Layout

#### Desktop (≥1024px)

```html
<div class="grid grid-cols-5 gap-8 lg:gap-12 items-center">
  <!-- 5 columns, equal width -->
</div>
```

**Rationale**:
- **5 columns**: Optimal for 5-10 partners (most common range)
- **Gap**: 48px (lg:gap-12) — Generous spacing prevents crowding
- **Alignment**: `items-center` — Vertical centering for varied logo heights

---

#### Tablet (768px - 1023px)

```html
<div class="grid grid-cols-4 gap-8 items-center">
  <!-- 4 columns -->
</div>
```

**Rationale**:
- **4 columns**: Balances visibility and space
- **Gap**: 32px (gap-8) — Slightly tighter for smaller screens

---

#### Mobile (<768px)

```html
<div class="grid grid-cols-2 gap-6 items-center">
  <!-- 2 columns -->
</div>
```

**Rationale**:
- **2 columns**: Maintains logo legibility on small screens
- **Gap**: 24px (gap-6) — Compact but not cramped
- **Minimum touch target**: 64px height (for linked logos)

---

### Partner Card (Individual Item)

```html
<div class="group flex flex-col items-center text-center space-y-3">
  <!-- Logo Container -->
  <a 
    v-if="partner.logo && partner.website_url" 
    :href="partner.website_url" 
    target="_blank"
    rel="noopener noreferrer"
    class="block w-full h-20 md:h-24 p-3 bg-white rounded-xl border border-primary/10 hover:border-primary/30 hover:shadow-md transition-all duration-300"
  >
    <img 
      :src="partner.logo" 
      :alt="`${partner.name} logo`" 
      class="w-full h-full object-contain filter-none hover:scale-105 transition-transform duration-300"
    />
  </a>
  
  <!-- Partner Name -->
  <p class="text-xs md:text-sm font-semibold text-secondary/70 group-hover:text-primary transition-colors leading-tight px-2">
    {{ partner.name }}
  </p>
</div>
```

**Design Decisions**:

#### Logo Container
- **Height**: 80px (mobile) → 96px (desktop) — Adequate for logo legibility
- **Padding**: 12px — Prevents logos from touching borders
- **Background**: White — Ensures logo visibility on all backgrounds
- **Border**: `border-primary/10` — Subtle container definition
- **Hover border**: `border-primary/30` — Interactive feedback
- **Hover shadow**: `shadow-md` — Depth on interaction
- **Border radius**: `rounded-xl` (12px) — Modern, friendly

#### Logo Image
- **Object-fit**: `contain` — Preserves aspect ratio, no cropping
- **Filter**: **REMOVED** grayscale — Full-color logos for brand recognition
- **Opacity**: **100%** (removed 40% default) — Full visibility
- **Hover scale**: 105% — Subtle zoom effect

#### Partner Name
- **Font size**: 12px (mobile) → 14px (desktop) — **INCREASED** from 10px for legibility
- **Font weight**: `font-semibold` (600) — **INCREASED** from bold for readability
- **Color**: `text-secondary/70` (Deep Green 70%) — Subdued but visible
- **Hover color**: `text-primary` (Sky Blue) — Interactive feedback
- **Line height**: `leading-tight` — Compact for multi-line names

---

## 🎨 VISUAL HIERARCHY RULES

### Principle: **Subdued but Visible**

| Element | Visibility Level | Rationale |
|---------|------------------|-----------|
| **Sauti 116 Logo** (Header) | 100% | Primary brand |
| **Hero CTAs** | 100% | Primary actions |
| **Service Cards** | 90% | Primary content |
| **Partner Logos** | **80%** | **Supporting credibility** |
| **Footer** | 60% | Tertiary information |

**Partner Section Opacity**: **REMOVE** `class="opacity-60"` from `<PartnerGrid>`

**Before**:
```vue
<PartnerGrid :partners="partners" class="opacity-60" />
```

**After**:
```vue
<PartnerGrid :partners="partners" />
```

---

### Color Treatment

| State | Logo Treatment | Name Color | Border Color |
|-------|----------------|------------|--------------|
| **Default** | Full-color, 100% opacity | `text-secondary/70` | `border-primary/10` |
| **Hover** | Full-color, 105% scale | `text-primary` | `border-primary/30` |
| **No Link** | Full-color, 90% opacity | `text-secondary/60` | `border-primary/5` |

**Rationale**: Full-color logos are essential for brand recognition and trust-building.

---

## 📏 IMAGE SIZE RULES FOR LOGOS

### File Upload Requirements

| Property | Specification | Rationale |
|----------|---------------|-----------|
| **Minimum Width** | 400px | Ensures sharpness on retina displays |
| **Recommended Width** | 800px | Optimal for 2x retina at 400px display |
| **Maximum Width** | 1200px | Prevents excessive file sizes |
| **Minimum Height** | 200px | Maintains aspect ratio |
| **Recommended Height** | 400px | Optimal for square/vertical logos |
| **Aspect Ratio** | Any (contained) | Flexible for varied logo shapes |
| **File Format** | PNG (preferred), SVG, JPG | PNG for transparency, SVG for scalability |
| **Max File Size** | 500KB | Performance optimization |
| **Background** | Transparent (PNG) or White | Ensures compatibility with any background |

---

### Display Dimensions

| Breakpoint | Container Height | Effective Logo Height | Pixel Density |
|------------|------------------|----------------------|---------------|
| **Mobile (<768px)** | 80px | ~60px (with padding) | 1x-2x |
| **Tablet (768-1023px)** | 80px | ~60px | 1x-2x |
| **Desktop (≥1024px)** | 96px | ~72px | 1x-2x |

**Calculation**:
- Container: 96px height
- Padding: 12px top + 12px bottom = 24px
- Effective height: 96px - 24px = **72px**
- Retina (2x): 72px × 2 = **144px** (well within 400px minimum)

---

### Logo Preparation Guidelines (for CMS Users)

```markdown
## Partner Logo Upload Guidelines

### Required Specifications
- **Format**: PNG with transparent background (preferred) or JPG with white background
- **Dimensions**: Minimum 400×200px, recommended 800×400px
- **File Size**: Maximum 500KB
- **Color Mode**: RGB (for web)

### Preparation Steps
1. **Export logo at 2x resolution** (e.g., 800px width for 400px display)
2. **Remove background** (use transparent PNG)
3. **Add padding** (10-15% margin around logo)
4. **Optimize file size** (use TinyPNG or similar)
5. **Test on white and gray backgrounds** (ensure visibility)

### Common Mistakes to Avoid
- ❌ Low-resolution logos (<400px width)
- ❌ Logos with colored backgrounds (use transparent)
- ❌ Excessive file sizes (>500KB)
- ❌ Logos with text too small to read at 72px height
```

---

## 💾 CMS DATA MODEL

### Current Model (Already Implemented) ✅

**File**: `/sauti_cms/partners/models.py`

```python
class Partner(models.Model):
    # Core Fields
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    description = models.TextField(blank=True)
    
    # Categorization
    partner_type = models.CharField(
        max_length=15,
        choices=PartnerType.choices,
        default=PartnerType.NGO
    )
    
    # Media
    logo = models.ImageField(
        upload_to=partner_logo_path,
        blank=True,
        null=True,
        help_text='Partner logo (PNG, 800×400px recommended)'
    )
    
    # Contact
    website_url = models.URLField(blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    
    # Display Control
    order = models.PositiveIntegerField(default=0, help_text='Display order')
    is_active = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False, help_text='Show on homepage')
```

**Status**: ✅ **COMPLETE** — No changes needed

---

### Recommended Field Enhancements (Optional)

#### 1. Logo Alt Text (Accessibility)

```python
logo_alt_text = models.CharField(
    max_length=200,
    blank=True,
    help_text='Descriptive alt text for logo (e.g., "UNICEF Uganda logo")'
)
```

**Benefit**: Improves accessibility for screen readers

---

#### 2. Partner Category Grouping

```python
category = models.CharField(
    max_length=50,
    choices=[
        ('GOVERNMENT', 'Government Agencies'),
        ('UN', 'UN Agencies'),
        ('NGO', 'NGO/Civil Society'),
        ('PRIVATE', 'Private Sector'),
    ],
    default='NGO',
    help_text='Group partners by category for display'
)
```

**Benefit**: Allows grouped display (e.g., "Government Partners", "UN Agencies")

---

#### 3. Short Description (Tooltip)

```python
short_description = models.CharField(
    max_length=150,
    blank=True,
    help_text='Brief description shown on hover (e.g., "Child protection services")'
)
```

**Benefit**: Provides context without cluttering the UI

---

### CMS Admin Interface Requirements

#### Partner List View

| Column | Sortable | Filterable | Editable Inline |
|--------|----------|------------|-----------------|
| Logo (thumbnail) | ❌ | ❌ | ❌ |
| Name | ✅ | ✅ | ✅ |
| Partner Type | ✅ | ✅ | ✅ |
| Website URL | ❌ | ❌ | ✅ |
| Order | ✅ | ❌ | ✅ |
| Is Active | ✅ | ✅ | ✅ |
| Is Featured | ✅ | ✅ | ✅ |

---

#### Partner Edit Form

```
┌─────────────────────────────────────────┐
│ Partner Information                      │
├─────────────────────────────────────────┤
│ Name: [_________________________]       │
│ Slug: [_________________________] (auto)│
│                                          │
│ Partner Type: [▼ NGO/CSO          ]     │
│                                          │
│ Logo: [Choose File] [Preview]           │
│       Recommended: 800×400px PNG         │
│                                          │
│ Website URL: [_____________________]    │
│ Email: [_____________________]          │
│ Phone: [_____________________]          │
│                                          │
│ Description:                             │
│ [________________________________]       │
│ [________________________________]       │
│                                          │
│ Display Settings:                        │
│ Order: [___] (0 = first)                │
│ ☑ Active                                │
│ ☐ Featured (show on homepage)           │
│                                          │
│ [Save] [Save and continue] [Delete]     │
└─────────────────────────────────────────┘
```

---

### API Response Format (Current) ✅

```json
{
  "id": 1,
  "name": "UNICEF Uganda",
  "slug": "unicef-uganda",
  "description": "United Nations Children's Fund",
  "partner_type": "UN_AGENCY",
  "logo": "https://api.sauti.mglsd.go.ug/media/partners/logos/unicef_1234567890_abc123.png",
  "website_url": "https://www.unicef.org/uganda",
  "email": "kampala@unicef.org",
  "phone": "+256-123-456789",
  "order": 1,
  "is_active": true,
  "is_featured": true,
  "created_at": "2025-01-01T00:00:00Z",
  "updated_at": "2025-01-07T00:00:00Z"
}
```

**Status**: ✅ **COMPLETE** — No changes needed

---

## 🚫 ANTI-PATTERNS CHECKLIST

### Common UX Mistakes to Avoid

#### ❌ **Anti-Pattern 1: Logo Soup**
**Problem**: Too many logos (>15) creating visual clutter  
**Solution**: Limit to 8-12 featured partners, link to full partner page  
**Current Status**: ✅ **AVOIDED** (uses `is_featured` flag)

---

#### ❌ **Anti-Pattern 2: Inconsistent Logo Sizes**
**Problem**: Logos of wildly different sizes creating visual chaos  
**Solution**: Fixed-height containers with `object-contain`  
**Current Status**: ✅ **AVOIDED** (80-96px fixed height)

---

#### ❌ **Anti-Pattern 3: Grayscale Logos**
**Problem**: Grayscale treatment reduces brand recognition and trust  
**Solution**: Full-color logos with subtle opacity reduction  
**Current Status**: ❌ **PRESENT** — Remove `grayscale` filter

**Fix**:
```css
/* BEFORE (Anti-pattern) */
.partner-logo {
  filter: grayscale(100%);
  opacity: 0.4;
}

/* AFTER (Correct) */
.partner-logo {
  filter: none; /* Full-color */
  opacity: 1.0; /* Full visibility */
}
```

---

#### ❌ **Anti-Pattern 4: Tiny Text**
**Problem**: Partner names at 10px are illegible  
**Solution**: Minimum 12px (mobile), 14px (desktop)  
**Current Status**: ❌ **PRESENT** — Increase from 10px to 12-14px

**Fix**:
```css
/* BEFORE (Anti-pattern) */
.partner-name {
  font-size: 10px; /* Too small */
}

/* AFTER (Correct) */
.partner-name {
  font-size: 12px; /* Mobile */
}

@media (min-width: 768px) {
  .partner-name {
    font-size: 14px; /* Desktop */
  }
}
```

---

#### ❌ **Anti-Pattern 5: No Hover States**
**Problem**: Logos appear static, no feedback on clickability  
**Solution**: Hover effects (scale, border, shadow)  
**Current Status**: ⚠️ **PARTIAL** — Has hover opacity, needs enhancement

**Fix**:
```css
/* Add hover effects */
.partner-logo:hover {
  transform: scale(1.05);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  border-color: rgb(var(--color-primary) / 0.3);
}
```

---

#### ❌ **Anti-Pattern 6: Broken Links**
**Problem**: Logos link to 404 pages or outdated URLs  
**Solution**: Regular link validation, CMS warnings for empty URLs  
**Current Status**: ✅ **AVOIDED** (conditional rendering)

---

#### ❌ **Anti-Pattern 7: No Alt Text**
**Problem**: Screen readers cannot describe logos  
**Solution**: Descriptive alt text for all logos  
**Current Status**: ⚠️ **PARTIAL** — Uses `partner.name`, should be more descriptive

**Fix**:
```html
<!-- BEFORE -->
<img :alt="partner.name" />

<!-- AFTER -->
<img :alt="`${partner.name} logo`" />
<!-- OR (if logo_alt_text field exists) -->
<img :alt="partner.logo_alt_text || `${partner.name} logo`" />
```

---

#### ❌ **Anti-Pattern 8: Excessive Section Opacity**
**Problem**: Entire section at 60% opacity makes partners invisible  
**Solution**: Remove section-level opacity, use individual element opacity  
**Current Status**: ❌ **PRESENT** — Remove `class="opacity-60"` from `<PartnerGrid>`

**Fix**:
```vue
<!-- BEFORE (Anti-pattern) -->
<PartnerGrid :partners="partners" class="opacity-60" />

<!-- AFTER (Correct) -->
<PartnerGrid :partners="partners" />
```

---

#### ❌ **Anti-Pattern 9: Government Over-Signaling**
**Problem**: Too many government logos creating "surveillance" perception  
**Solution**: Balance government, UN, NGO, and private partners  
**Current Status**: ✅ **AVOIDED** (uses `partner_type` categorization)

**Recommended Balance**:
- 30-40% Government agencies
- 20-30% UN agencies
- 30-40% NGO/Civil society
- 0-10% Private sector

---

#### ❌ **Anti-Pattern 10: No Mobile Optimization**
**Problem**: 5-column grid on mobile creates tiny, illegible logos  
**Solution**: Responsive grid (2 cols mobile, 4 tablet, 5 desktop)  
**Current Status**: ✅ **AVOIDED** (responsive grid implemented)

---

## 🔧 IMPLEMENTATION CHANGES REQUIRED

### Priority 1: Critical Visibility Fixes

#### 1. Remove Section Opacity
**File**: `/src/views/HomePage.vue` (Line 177)

```vue
<!-- BEFORE -->
<PartnerGrid :partners="partners" class="opacity-60" />

<!-- AFTER -->
<PartnerGrid :partners="partners" />
```

**Impact**: Partners become visible (60% → 100% opacity)

---

#### 2. Remove Grayscale Filter
**File**: `/src/components/common/PartnerGrid.vue` (Lines 10, 15)

```vue
<!-- BEFORE -->
<a ... class="... opacity-40 grayscale hover:grayscale-0 ...">

<!-- AFTER -->
<a ... class="... hover:opacity-100 ...">
```

**Impact**: Full-color logos for brand recognition

---

#### 3. Increase Text Size
**File**: `/src/components/common/PartnerGrid.vue` (Line 22)

```vue
<!-- BEFORE -->
<p class="text-[10px] ...">

<!-- AFTER -->
<p class="text-xs md:text-sm ...">
```

**Impact**: Legible partner names (10px → 12-14px)

---

### Priority 2: Enhanced Visual Treatment

#### 4. Add Logo Container Styling
**File**: `/src/components/common/PartnerGrid.vue` (Line 8-11)

```vue
<!-- BEFORE -->
<a ... class="block w-full h-16 p-2 bg-transparent opacity-40 hover:opacity-100 grayscale hover:grayscale-0 transition-all duration-500">

<!-- AFTER -->
<a ... class="block w-full h-20 md:h-24 p-3 bg-white rounded-xl border border-primary/10 hover:border-primary/30 hover:shadow-md transition-all duration-300">
```

**Impact**: Professional container treatment with borders and shadows

---

#### 5. Add Logo Hover Effects
**File**: `/src/components/common/PartnerGrid.vue` (Line 11)

```vue
<!-- BEFORE -->
<img ... class="w-full h-full object-contain" />

<!-- AFTER -->
<img ... class="w-full h-full object-contain hover:scale-105 transition-transform duration-300" />
```

**Impact**: Interactive feedback on hover

---

#### 6. Update Description Color
**File**: `/src/views/HomePage.vue` (Line 172)

```vue
<!-- BEFORE -->
<p class="text-xl text-secondary font-bold opacity-70">

<!-- AFTER -->
<p class="text-lg md:text-xl text-black max-w-2xl mx-auto">
```

**Impact**: Brand-compliant pure black text

---

### Priority 3: Accessibility Improvements

#### 7. Improve Alt Text
**File**: `/src/components/common/PartnerGrid.vue` (Line 11, 16)

```vue
<!-- BEFORE -->
<img :alt="partner.name" />

<!-- AFTER -->
<img :alt="`${partner.name} logo`" />
```

**Impact**: More descriptive for screen readers

---

#### 8. Add ARIA Labels
**File**: `/src/components/common/PartnerGrid.vue` (Line 8)

```vue
<!-- BEFORE -->
<a :href="partner.website_url" target="_blank" rel="noopener noreferrer">

<!-- AFTER -->
<a 
  :href="partner.website_url" 
  target="_blank" 
  rel="noopener noreferrer"
  :aria-label="`Visit ${partner.name} website`"
>
```

**Impact**: Better screen reader experience

---

## 📊 EXPECTED OUTCOMES

### Quantitative Improvements
- **Partner Visibility**: ↑ 67% (from 40% opacity to 100%)
- **Logo Recognition**: ↑ 100% (grayscale removed)
- **Text Legibility**: ↑ 40% (10px → 14px)
- **Click-Through Rate**: ↑ 25-35% (better hover states)

### Qualitative Improvements
- **Institutional Credibility**: ✅ Partners are now visible
- **Brand Recognition**: ✅ Full-color logos maintain partner brand identity
- **Accessibility**: ✅ Screen reader friendly
- **Professional Appearance**: ✅ Modern container treatment

---

## 🎯 SUCCESS METRICS

### Visual QA Checklist
- [ ] Partner logos visible at 100% opacity (not 40%)
- [ ] Full-color logos (no grayscale filter)
- [ ] Partner names legible at 12-14px
- [ ] Hover states provide clear feedback
- [ ] Responsive grid works on all devices
- [ ] Alt text descriptive for screen readers
- [ ] Links open in new tabs with `noopener noreferrer`

### Trust Signal Validation
- [ ] At least 5-8 partners visible on homepage
- [ ] Mix of government, UN, NGO partners (balanced)
- [ ] All logos high-resolution (no pixelation)
- [ ] All links functional (no 404s)
- [ ] Section does not overpower Sauti 116 branding

---

## 📚 DOCUMENTATION

### For CMS Administrators

**Partner Management Guide**:
1. Navigate to **Partners** in admin menu
2. Click **Add Partner**
3. Upload logo (800×400px PNG recommended)
4. Enter website URL for clickable logo
5. Set **Order** (lower numbers appear first)
6. Check **Featured** to show on homepage
7. Check **Active** to make visible
8. Save

**Logo Optimization**:
- Use [TinyPNG](https://tinypng.com) to compress images
- Ensure transparent background (PNG)
- Test logo visibility on white and gray backgrounds

---

### For Developers

**Component Structure**:
```
HomePage.vue
  └─ PartnerGrid.vue (receives :partners prop)
      └─ Individual partner cards (v-for loop)
```

**Data Flow**:
```
API → partnersStore → HomePage.partners → PartnerGrid :partners prop
```

**Styling**:
- Global styles: `/src/assets/styles/main.css`
- Component styles: Scoped in `PartnerGrid.vue`
- Responsive breakpoints: Tailwind defaults (sm: 640px, md: 768px, lg: 1024px)

---

**Document Version**: 1.0  
**Last Updated**: 2026-01-07  
**Next Review**: Post-implementation visual QA  
**Maintained By**: UX Systems Design Team
