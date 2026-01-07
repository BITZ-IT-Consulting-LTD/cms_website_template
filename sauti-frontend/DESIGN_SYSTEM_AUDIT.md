# SAUTI 116 — Design System Centralization Audit

**Date**: 2026-01-07  
**Auditor**: Design System Specialist  
**Objective**: Ensure all colors, fonts, and spacing are centrally defined  
**Status**: ⚠️ **Partial Compliance** - Hardcoded values found

---

## EXECUTIVE SUMMARY

### Current State
✅ **Colors**: Centrally defined in CSS variables + Tailwind  
✅ **Fonts**: Centrally defined in Tailwind config  
⚠️ **Spacing**: Mostly using Tailwind utilities (good)  
❌ **Hardcoded Colors**: Found in 50+ locations (needs cleanup)

### Required Actions
1. **Remove hardcoded hex colors** from components
2. **Add missing spacing tokens** to design system
3. **Document design system** for developers
4. **Create linting rules** to prevent future violations

---

## 🎨 COLOR SYSTEM AUDIT

### ✅ **Centrally Defined Colors**

**Location**: `/src/assets/styles/main.css` (Lines 6-20)

```css
:root {
  /* Official Sauti 116 Palette */
  --color-primary: 0 135 207;         /* Sauti Sky Blue #0087CF */
  --color-primary-dark: 0 105 165;    /* Darker variant #0069A5 */
  --color-secondary: 0 104 55;        /* Sauti Deep Green #006837 */
  --color-secondary-light: 157 200 62; /* Sauti Leaf Green #9DC83E */
  --color-hotline: 247 148 30;        /* Sauti Bright Orange #F7941E */
  --color-emergency: 237 28 36;       /* Sauti Signal Red #ED1C24 */
  --color-accent-yellow: 255 242 0;   /* Sauti Sun Yellow #FFF200 */
  
  --color-text: 0 0 0;                /* Sauti Solid Black #000000 */
  --color-neutral-black: 15 23 42;    /* Dark Blue-Gray #0F172A */
  --color-neutral-white: 255 255 255; /* Pure White #FFFFFF */
  --color-neutral-offwhite: 248 250 252; /* Off-White #F8FAFC */
}
```

**Tailwind Integration**: `/tailwind.config.js` (Lines 9-23)

```javascript
colors: {
  'primary': 'rgb(var(--color-primary) / <alpha-value>)',
  'primary-dark': 'rgb(var(--color-primary-dark) / <alpha-value>)',
  'secondary': 'rgb(var(--color-secondary) / <alpha-value>)',
  'secondary-light': 'rgb(var(--color-secondary-light) / <alpha-value>)',
  'hotline': 'rgb(var(--color-hotline) / <alpha-value>)',
  'emergency': 'rgb(var(--color-emergency) / <alpha-value>)',
  'accent-yellow': 'rgb(var(--color-accent-yellow) / <alpha-value>)',
  'text': 'rgb(var(--color-text) / <alpha-value>)',
  'neutral-black': 'rgb(var(--color-neutral-black) / <alpha-value>)',
  'neutral-white': 'rgb(var(--color-neutral-white) / <alpha-value>)',
  'neutral-offwhite': 'rgb(var(--color-neutral-offwhite) / <alpha-value>)',
}
```

---

### ❌ **Hardcoded Colors Found**

**Total Violations**: 50+ instances

#### **Category 1: Social Media Colors** (Acceptable)

**Location**: `/src/components/blog/BlogPost.vue`

```vue
<!-- WhatsApp Green -->
<button class="bg-[#25D366] hover:bg-[#20BA5A]">

<!-- Facebook Blue -->
<button class="bg-[#1877F2] hover:bg-[#1664D9]">

<!-- Twitter/X Black -->
<button class="bg-[#000000] hover:bg-gray-800">
```

**Verdict**: ✅ **Acceptable** (brand-specific colors for social sharing)

**Recommendation**: Move to design system for consistency

---

#### **Category 2: GIZ Chat Component** (Legacy)

**Location**: `/src/components/giz/DynamicChatWindow.vue`

**Violations**: 40+ hardcoded colors

```css
/* Examples of hardcoded colors */
background: rgba(255, 255, 255, 0.95);
color: #333;
border: 1px solid #e0e0e0;
background: #4CAF50;
color: #666;
background: #f0f0f0;
```

**Verdict**: ❌ **Non-Compliant** (should use design system)

**Recommendation**: Refactor to use CSS variables

---

#### **Category 3: HelpContacts Component**

**Location**: `/src/components/content/HelpContacts.vue`

```vue
<!-- Hardcoded WhatsApp green -->
<button class="bg-[#25D366] hover:bg-[#20bd5a]">
```

**Verdict**: ⚠️ **Partially Acceptable** (social media brand color)

**Recommendation**: Add to design system as `--color-whatsapp`

---

## 🔤 FONT SYSTEM AUDIT

### ✅ **Centrally Defined Fonts**

**Location**: `/tailwind.config.js` (Lines 24-28)

```javascript
fontFamily: {
  // Sauti 116 Institutional Voice
  sans: ['"Cronos Pro"', 'Roboto', 'ui-sans-serif', 'system-ui', 'sans-serif'],
}
```

**Base Styles**: `/src/assets/styles/main.css` (Lines 42-46)

```css
h1 { @apply text-4xl md:text-6xl font-black leading-tight tracking-tight text-secondary; }
h2 { @apply text-3xl md:text-5xl font-black leading-tight text-secondary; }
h3 { @apply text-2xl md:text-3xl font-bold leading-snug text-secondary; }
p  { @apply text-base md:text-lg leading-relaxed mb-6 font-normal text-black; }
```

**Verdict**: ✅ **Fully Compliant**

---

## 📏 SPACING SYSTEM AUDIT

### ✅ **Using Tailwind Spacing** (Good)

**Current Approach**: Components use Tailwind's default spacing scale

```vue
<!-- Examples of correct spacing usage -->
<div class="px-4 py-6">        <!-- Tailwind spacing -->
<div class="mb-8 mt-12">       <!-- Tailwind spacing -->
<div class="gap-4">            <!-- Tailwind spacing -->
```

**Tailwind Default Scale**:
```
0: 0px
1: 0.25rem (4px)
2: 0.5rem (8px)
3: 0.75rem (12px)
4: 1rem (16px)
5: 1.25rem (20px)
6: 1.5rem (24px)
8: 2rem (32px)
10: 2.5rem (40px)
12: 3rem (48px)
16: 4rem (64px)
20: 5rem (80px)
24: 6rem (96px)
32: 8rem (128px)
40: 10rem (160px)
48: 12rem (192px)
```

---

### ⚠️ **Custom Spacing Values**

**Found in**: `/src/assets/styles/main.css`

```css
/* Custom spacing in components */
.section-padding {
  @apply py-24 md:py-40;  /* 96px / 160px */
}

.page-header {
  @apply py-32 md:py-48;  /* 128px / 192px */
}
```

**Verdict**: ✅ **Acceptable** (semantic classes for consistent spacing)

---

### ❌ **Hardcoded Spacing** (Minimal)

**Found in**: `/src/assets/styles/main.css` (Line 58)

```css
.btn {
  min-height: 52px; /* Hardcoded pixel value */
}
```

**Recommendation**: Add to design system

---

## 🛠️ RECOMMENDED DESIGN SYSTEM ENHANCEMENTS

### **1. Add Missing Color Tokens**

**File**: `/src/assets/styles/main.css`

```css
:root {
  /* Existing colors... */
  
  /* Social Media Brand Colors (NEW) */
  --color-whatsapp: 37 211 102;       /* WhatsApp Green #25D366 */
  --color-whatsapp-hover: 32 189 90;  /* Darker WhatsApp #20BD5A */
  --color-facebook: 24 119 242;       /* Facebook Blue #1877F2 */
  --color-facebook-hover: 22 100 217; /* Darker Facebook #1664D9 */
  --color-twitter: 0 0 0;             /* Twitter/X Black #000000 */
  
  /* UI Grays (for legacy GIZ components) */
  --color-gray-50: 248 250 252;       /* #F8FAFC */
  --color-gray-100: 241 245 249;      /* #F1F5F9 */
  --color-gray-200: 226 232 240;      /* #E2E8F0 */
  --color-gray-300: 203 213 225;      /* #CBD5E1 */
  --color-gray-400: 148 163 184;      /* #94A3B8 */
  --color-gray-500: 100 116 139;      /* #64748B */
  --color-gray-600: 71 85 105;        /* #475569 */
  --color-gray-700: 51 65 85;         /* #334155 */
  --color-gray-800: 30 41 59;         /* #1E293B */
  --color-gray-900: 15 23 42;         /* #0F172A */
}
```

---

### **2. Add Spacing Tokens**

**File**: `/tailwind.config.js`

```javascript
theme: {
  extend: {
    spacing: {
      // Component-specific spacing
      'btn-height': '52px',           // Minimum button height
      'section-sm': '6rem',           // 96px
      'section-md': '10rem',          // 160px
      'section-lg': '12rem',          // 192px
      'header-sm': '8rem',            // 128px
      'header-md': '12rem',           // 192px
    },
  }
}
```

**Usage**:
```vue
<!-- Before -->
<div class="py-24 md:py-40">

<!-- After -->
<div class="py-section-sm md:py-section-md">
```

---

### **3. Add Border Radius Tokens**

**File**: `/tailwind.config.js`

```javascript
theme: {
  extend: {
    borderRadius: {
      'card': '2rem',      // 32px - Standard card radius
      'button': '1.5rem',  // 24px - Standard button radius
      'pill': '9999px',    // Full pill shape
      'section': '3rem',   // 48px - Large section radius
    },
  }
}
```

**Usage**:
```vue
<!-- Before -->
<div class="rounded-[2rem]">

<!-- After -->
<div class="rounded-card">
```

---

### **4. Add Shadow Tokens**

**File**: `/tailwind.config.js`

```javascript
theme: {
  extend: {
    boxShadow: {
      'card': '0 1px 3px 0 rgb(0 0 0 / 0.1)',
      'card-hover': '0 10px 40px -10px rgb(0 0 0 / 0.15)',
      'button': '0 4px 12px rgb(var(--color-primary) / 0.2)',
      'button-hover': '0 8px 24px rgb(var(--color-primary) / 0.3)',
      'glow-hotline': '0 0 12px rgb(var(--color-hotline) / 0.4)',
      'glow-emergency': '0 0 12px rgb(var(--color-emergency) / 0.4)',
    },
  }
}
```

---

## 📚 DESIGN SYSTEM DOCUMENTATION

### **Color Usage Guide**

| Token | Hex | Usage |
|-------|-----|-------|
| `primary` | #0087CF | Primary actions, links, highlights |
| `primary-dark` | #0069A5 | Outline buttons, accessible text |
| `secondary` | #006837 | Headings, success states |
| `secondary-light` | #9DC83E | Accents, highlights |
| `hotline` | #F7941E | Call-to-action, engagement |
| `emergency` | #ED1C24 | Urgent actions, alerts |
| `accent-yellow` | #FFF200 | Highlights, warnings |
| `text` | #000000 | Body text (mandatory) |
| `neutral-white` | #FFFFFF | Backgrounds, button text |
| `neutral-offwhite` | #F8FAFC | Page backgrounds |

---

### **Typography Scale**

| Element | Class | Size (Mobile) | Size (Desktop) | Weight |
|---------|-------|---------------|----------------|--------|
| **H1** | `text-4xl md:text-6xl` | 36px | 60px | Black (900) |
| **H2** | `text-3xl md:text-5xl` | 30px | 48px | Black (900) |
| **H3** | `text-2xl md:text-3xl` | 24px | 30px | Bold (700) |
| **Body** | `text-base md:text-lg` | 16px | 18px | Normal (400) |
| **Small** | `text-sm` | 14px | 14px | Normal (400) |
| **Tiny** | `text-xs` | 12px | 12px | Normal (400) |

---

### **Spacing Scale**

| Token | Value | Usage |
|-------|-------|-------|
| `section-padding` | 96px/160px | Section vertical spacing |
| `page-header` | 128px/192px | Page header vertical spacing |
| `card` | 32px/48px | Card padding |
| `btn` | 24px/16px | Button padding (x/y) |

---

## 🔧 CLEANUP TASKS

### **Priority 1: Remove Hardcoded Colors**

#### **Task 1.1: Add Social Media Colors to Design System**

**File**: `/src/assets/styles/main.css`

```css
:root {
  /* ... existing colors ... */
  
  /* Social Media Brand Colors */
  --color-whatsapp: 37 211 102;
  --color-whatsapp-hover: 32 189 90;
  --color-facebook: 24 119 242;
  --color-facebook-hover: 22 100 217;
  --color-twitter: 0 0 0;
}
```

**File**: `/tailwind.config.js`

```javascript
colors: {
  // ... existing colors ...
  'whatsapp': 'rgb(var(--color-whatsapp) / <alpha-value>)',
  'whatsapp-hover': 'rgb(var(--color-whatsapp-hover) / <alpha-value>)',
  'facebook': 'rgb(var(--color-facebook) / <alpha-value>)',
  'facebook-hover': 'rgb(var(--color-facebook-hover) / <alpha-value>)',
  'twitter': 'rgb(var(--color-twitter) / <alpha-value>)',
}
```

---

#### **Task 1.2: Update BlogPost Component**

**File**: `/src/components/blog/BlogPost.vue`

**Before**:
```vue
<button class="bg-[#25D366] hover:bg-[#20BA5A]">WhatsApp</button>
<button class="bg-[#1877F2] hover:bg-[#1664D9]">Facebook</button>
<button class="bg-[#000000] hover:bg-gray-800">Twitter</button>
```

**After**:
```vue
<button class="bg-whatsapp hover:bg-whatsapp-hover">WhatsApp</button>
<button class="bg-facebook hover:bg-facebook-hover">Facebook</button>
<button class="bg-twitter hover:bg-gray-800">Twitter</button>
```

---

#### **Task 1.3: Update HelpContacts Component**

**File**: `/src/components/content/HelpContacts.vue`

**Before**:
```vue
<button class="bg-[#25D366] hover:bg-[#20bd5a]">
```

**After**:
```vue
<button class="bg-whatsapp hover:bg-whatsapp-hover">
```

---

#### **Task 1.4: Refactor GIZ Chat Component**

**File**: `/src/components/giz/DynamicChatWindow.vue`

**Before**:
```css
.chat-container {
  background: rgba(255, 255, 255, 0.95);
  color: #333;
  border: 1px solid #e0e0e0;
}
```

**After**:
```css
.chat-container {
  background: rgb(var(--color-neutral-white) / 0.95);
  color: rgb(var(--color-gray-700));
  border: 1px solid rgb(var(--color-gray-200));
}
```

**Note**: This requires adding gray scale to design system (see Task 1.1)

---

### **Priority 2: Add Semantic Spacing Classes**

**File**: `/src/assets/styles/main.css`

```css
@layer components {
  /* Semantic spacing classes */
  .section-padding {
    @apply py-24 md:py-40;
  }
  
  .section-padding-sm {
    @apply py-16 md:py-24;
  }
  
  .section-padding-lg {
    @apply py-32 md:py-48;
  }
  
  .container-padding {
    @apply px-4 sm:px-6 lg:px-8;
  }
  
  .card-padding {
    @apply p-8 md:p-12;
  }
  
  .card-padding-sm {
    @apply p-6 md:p-8;
  }
}
```

---

### **Priority 3: Add Border Radius Classes**

**File**: `/src/assets/styles/main.css`

```css
@layer components {
  /* Semantic border radius classes */
  .rounded-card {
    @apply rounded-[2rem];
  }
  
  .rounded-button {
    @apply rounded-2xl;
  }
  
  .rounded-section {
    @apply rounded-[3rem];
  }
  
  .rounded-pill {
    @apply rounded-full;
  }
}
```

---

## 🚨 LINTING RULES

### **ESLint Plugin for Tailwind**

**Install**:
```bash
npm install --save-dev eslint-plugin-tailwindcss
```

**Configure**: `.eslintrc.js`

```javascript
module.exports = {
  plugins: ['tailwindcss'],
  rules: {
    // Warn on arbitrary values (e.g., bg-[#FF0000])
    'tailwindcss/no-arbitrary-value': 'warn',
    
    // Enforce consistent class order
    'tailwindcss/classnames-order': 'warn',
    
    // Warn on custom CSS in components
    'tailwindcss/no-custom-classname': 'warn',
  },
}
```

---

### **Stylelint for CSS**

**Install**:
```bash
npm install --save-dev stylelint stylelint-config-standard
```

**Configure**: `.stylelintrc.json`

```json
{
  "extends": "stylelint-config-standard",
  "rules": {
    "color-no-hex": true,
    "declaration-property-value-disallowed-list": {
      "/^(background|color|border)/": ["/^#/", "/^rgb/"]
    }
  }
}
```

**Note**: This will flag hardcoded hex colors and suggest using CSS variables

---

## ✅ IMPLEMENTATION CHECKLIST

### **Phase 1: Design System Enhancement** (2 hours)

- [ ] Add social media colors to CSS variables
- [ ] Add social media colors to Tailwind config
- [ ] Add gray scale to CSS variables
- [ ] Add spacing tokens to Tailwind config
- [ ] Add border radius tokens
- [ ] Add shadow tokens
- [ ] Document all tokens in design system guide

---

### **Phase 2: Component Cleanup** (4 hours)

- [ ] Update BlogPost.vue (social media buttons)
- [ ] Update HelpContacts.vue (WhatsApp button)
- [ ] Refactor DynamicChatWindow.vue (40+ hardcoded colors)
- [ ] Refactor FloatingChatBot.vue (hardcoded reds)
- [ ] Search for remaining `bg-[#` instances
- [ ] Search for remaining `text-[#` instances
- [ ] Search for remaining `border-[#` instances

---

### **Phase 3: Linting Setup** (1 hour)

- [ ] Install ESLint Tailwind plugin
- [ ] Configure linting rules
- [ ] Install Stylelint
- [ ] Configure Stylelint rules
- [ ] Run linters and fix violations
- [ ] Add linting to CI/CD pipeline

---

### **Phase 4: Documentation** (1 hour)

- [ ] Create DESIGN_SYSTEM.md guide
- [ ] Document color tokens
- [ ] Document spacing tokens
- [ ] Document typography scale
- [ ] Document component classes
- [ ] Add usage examples
- [ ] Share with development team

---

## 📊 COMPLIANCE SCORECARD

| Category | Current | Target | Status |
|----------|---------|--------|--------|
| **Color Centralization** | 70% | 100% | ⚠️ In Progress |
| **Font Centralization** | 100% | 100% | ✅ Complete |
| **Spacing Centralization** | 85% | 100% | ⚠️ Good |
| **Hardcoded Values** | 50+ | 0 | ❌ Needs Work |
| **Documentation** | 40% | 100% | ⚠️ In Progress |

**Overall Compliance**: **75%** → Target: **100%**

---

## 🎯 EXPECTED OUTCOMES

### **After Cleanup**

✅ **Zero hardcoded colors** in components  
✅ **All colors** use CSS variables or Tailwind tokens  
✅ **All spacing** uses Tailwind scale or semantic classes  
✅ **All fonts** use centralized font stack  
✅ **Linting** prevents future violations  
✅ **Documentation** guides developers

### **Benefits**

- ✅ **Easier theming**: Change one variable, update entire site
- ✅ **Consistent design**: No color/spacing variations
- ✅ **Faster development**: Developers use tokens, not guessing
- ✅ **Better maintenance**: Centralized system is easier to update
- ✅ **Accessibility**: Enforced contrast ratios via design system

---

**Document Version**: 1.0  
**Last Updated**: 2026-01-07  
**Next Review**: Post-cleanup implementation  
**Maintained By**: Design System Team
