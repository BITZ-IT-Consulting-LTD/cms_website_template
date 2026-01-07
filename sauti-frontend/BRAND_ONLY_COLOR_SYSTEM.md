# SAUTI 116 — BRAND-ONLY COLOR SYSTEM

**Date**: 2026-01-07  
**Approach**: Strict brand colors only (no generic grays)  
**Total Colors**: 16 (down from 29)

---

## 🎨 BRAND-ONLY COLOR PALETTE

### **Total**: 16 colors (all brand-specific)

---

## 📊 BREAKDOWN

### **1. Core Brand Colors** (7 colors) ✅

| Color | Token | Hex | Purpose |
|-------|-------|-----|---------|
| **Sky Blue** | `--color-primary` | #0087CF | Primary brand color |
| **Dark Blue** | `--color-primary-dark` | #0069A5 | WCAG AA contrast |
| **Deep Green** | `--color-secondary` | #006837 | Secondary brand |
| **Leaf Green** | `--color-secondary-light` | #9DC83E | Hope & growth |
| **Orange** | `--color-hotline` | #F7941E | Call-to-action |
| **Red** | `--color-emergency` | #ED1C24 | Urgency & alerts |
| **Yellow** | `--color-accent-yellow` | #FFF200 | Highlights |

**Source**: Official Sauti 116 Brand Guidelines

---

### **2. Neutral Colors** (4 colors) ✅

| Color | Token | Hex | Purpose |
|-------|-------|-----|---------|
| **Black** | `--color-text` | #000000 | Body text |
| **Dark Slate** | `--color-neutral-black` | #0F172A | Headers |
| **White** | `--color-neutral-white` | #FFFFFF | Backgrounds |
| **Off-white** | `--color-neutral-offwhite` | #F8FAFC | Subtle backgrounds |

**Source**: Brand typography & backgrounds

---

### **3. Social Media Colors** (5 colors) ✅

| Color | Token | Hex | Purpose |
|-------|-------|-----|---------|
| **WhatsApp** | `--color-whatsapp` | #25D366 | WhatsApp button |
| **WhatsApp Hover** | `--color-whatsapp-hover` | #20BD5A | Hover state |
| **Facebook** | `--color-facebook` | #1877F2 | Facebook button |
| **Facebook Hover** | `--color-facebook-hover` | #1664D9 | Hover state |
| **Twitter/X** | `--color-twitter` | #000000 | Twitter button |

**Source**: Social media brand guidelines

---

## ❌ WHAT TO REMOVE

### **Remove All Generic Grays** (10 colors)

```css
/* ❌ REMOVE THESE */
--color-gray-50: 248 250 252;
--color-gray-100: 241 245 249;
--color-gray-200: 226 232 240;
--color-gray-300: 203 213 225;
--color-gray-400: 148 163 184;
--color-gray-500: 100 116 139;
--color-gray-600: 71 85 105;
--color-gray-700: 51 65 85;
--color-gray-800: 30 41 59;
--color-gray-900: 15 23 42;
```

**Why**: Not part of Sauti 116 brand palette

---

### **Remove Legacy/Unused** (3 colors)

```css
/* ❌ REMOVE THESE */
--color-accent-orange (duplicate of hotline)
--color-surface-warm (not defined)
(any other non-brand colors)
```

---

## 🎯 HOW TO HANDLE UI NEEDS

### **Problem**: What about borders, disabled states, muted text?

### **Solution**: Use brand colors with opacity

---

### **Borders** (use primary/secondary with opacity)

```css
/* Instead of gray-300 */
border: 1px solid rgb(var(--color-primary) / 0.2);
border: 1px solid rgb(var(--color-secondary) / 0.15);
```

```vue
<!-- Tailwind -->
<div class="border-2 border-primary/20">
<div class="border-2 border-secondary/15">
```

---

### **Disabled States** (use black with opacity)

```css
/* Instead of gray-400 */
color: rgb(var(--color-text) / 0.4);
```

```vue
<!-- Tailwind -->
<button class="text-black/40 cursor-not-allowed">
```

---

### **Muted Text** (use black with opacity)

```css
/* Instead of gray-600 */
color: rgb(var(--color-text) / 0.6);
```

```vue
<!-- Tailwind -->
<p class="text-black/60">
<p class="text-muted"> <!-- using helper class -->
```

---

### **Subtle Backgrounds** (use brand colors with opacity)

```css
/* Instead of gray-100 */
background: rgb(var(--color-primary) / 0.05);
background: rgb(var(--color-secondary) / 0.05);
```

```vue
<!-- Tailwind -->
<div class="bg-primary/5">
<div class="bg-secondary/5">
```

---

## 📋 BRAND-ONLY SYSTEM

### **Final Color Palette**: 16 colors

```css
:root {
  /* Core Brand (7) */
  --color-primary: 0 135 207;
  --color-primary-dark: 0 105 165;
  --color-secondary: 0 104 55;
  --color-secondary-light: 157 200 62;
  --color-hotline: 247 148 30;
  --color-emergency: 237 28 36;
  --color-accent-yellow: 255 242 0;
  
  /* Neutrals (4) */
  --color-text: 0 0 0;
  --color-neutral-black: 15 23 42;
  --color-neutral-white: 255 255 255;
  --color-neutral-offwhite: 248 250 252;
  
  /* Social Media (5) */
  --color-whatsapp: 37 211 102;
  --color-whatsapp-hover: 32 189 90;
  --color-facebook: 24 119 242;
  --color-facebook-hover: 22 100 217;
  --color-twitter: 0 0 0;
}
```

**Total**: **16 colors** (all brand-specific)

---

## 🎨 USAGE EXAMPLES

### **Borders**

```vue
<!-- Light border -->
<div class="border-2 border-primary/10">

<!-- Medium border -->
<div class="border-2 border-secondary/20">

<!-- Strong border -->
<div class="border-2 border-primary">
```

---

### **Backgrounds**

```vue
<!-- Subtle background -->
<div class="bg-primary/5">
<div class="bg-secondary/5">

<!-- Light background -->
<div class="bg-neutral-offwhite">

<!-- Colored background -->
<div class="bg-primary">
<div class="bg-secondary">
```

---

### **Text**

```vue
<!-- Body text -->
<p class="text-black">

<!-- Muted text -->
<p class="text-black/60">
<p class="text-muted">

<!-- Disabled text -->
<p class="text-black/40">

<!-- Brand text -->
<h2 class="text-secondary">
<span class="text-primary">
```

---

### **Interactive States**

```vue
<!-- Button -->
<button class="bg-primary hover:bg-primary-dark text-white">

<!-- Link -->
<a class="text-primary hover:text-primary-dark">

<!-- Disabled -->
<button class="bg-black/10 text-black/40 cursor-not-allowed">
```

---

## ✅ BENEFITS OF BRAND-ONLY

### **1. Pure Brand Compliance** ✅
- Every color is from the brand palette
- No generic grays diluting brand identity
- 100% alignment with brand guidelines

### **2. Stronger Brand Identity** ✅
- More distinctive visual language
- Consistent brand presence
- Memorable color associations

### **3. Simpler System** ✅
- Only 16 colors to remember
- Clear purpose for each color
- Less decision fatigue

### **4. Better Performance** ✅
- Fewer CSS variables
- Smaller bundle size
- Faster color calculations

---

## ⚠️ CONSIDERATIONS

### **Potential Challenges**

1. **Limited Neutral Options**
   - **Solution**: Use opacity variants
   - Example: `text-black/60` instead of `text-gray-600`

2. **Accessibility Concerns**
   - **Solution**: Test all opacity combinations
   - Ensure WCAG AA compliance
   - Use `primary-dark` for better contrast

3. **Designer Expectations**
   - **Solution**: Document opacity system
   - Provide clear examples
   - Train team on new approach

---

## 🚀 MIGRATION PLAN

### **Phase 1: Audit Current Usage** (1 hour)

```bash
# Find all gray usage
grep -r "gray-" src/ --include="*.vue" | wc -l
grep -r "bg-gray" src/ --include="*.vue"
grep -r "text-gray" src/ --include="*.vue"
grep -r "border-gray" src/ --include="*.vue"
```

---

### **Phase 2: Create Opacity Mappings** (30 min)

```css
/* Map grays to brand colors with opacity */
/* gray-50  → primary/5 or secondary/5 */
/* gray-100 → primary/10 or secondary/10 */
/* gray-200 → primary/15 or secondary/15 */
/* gray-300 → primary/20 or secondary/20 */
/* gray-400 → black/40 */
/* gray-600 → black/60 */
```

---

### **Phase 3: Replace Grays** (3 hours)

```vue
<!-- Before -->
<div class="bg-gray-100 border-gray-300 text-gray-600">

<!-- After -->
<div class="bg-primary/10 border-primary/20 text-black/60">
```

---

### **Phase 4: Remove Gray Tokens** (15 min)

1. Delete gray definitions from `main.css`
2. Remove gray mappings from `tailwind.config.js`
3. Test thoroughly
4. Update documentation

---

## 📊 COMPARISON

| Approach | Colors | Brand Purity | Complexity | Flexibility |
|----------|--------|--------------|------------|-------------|
| **Current (29)** | 29 | 55% | High | High |
| **Optimized (21)** | 21 | 76% | Medium | High |
| **Brand-Only (16)** | 16 | **100%** | Low | Medium |

---

## 🎯 RECOMMENDATION

### **For Sauti 116**: ⭐ **Brand-Only (16 colors)**

**Why**:
- ✅ Government/institutional brand
- ✅ Strong brand identity needed
- ✅ Official brand guidelines exist
- ✅ Professional appearance
- ✅ Distinctive visual language

**How**:
- Use 16 brand colors
- Use opacity for UI states
- Remove all generic grays
- Document opacity system

---

## 📋 IMPLEMENTATION CHECKLIST

### **Step 1: Update main.css**

```css
:root {
  /* Keep only these 16 colors */
  
  /* Brand (7) */
  --color-primary: 0 135 207;
  --color-primary-dark: 0 105 165;
  --color-secondary: 0 104 55;
  --color-secondary-light: 157 200 62;
  --color-hotline: 247 148 30;
  --color-emergency: 237 28 36;
  --color-accent-yellow: 255 242 0;
  
  /* Neutrals (4) */
  --color-text: 0 0 0;
  --color-neutral-black: 15 23 42;
  --color-neutral-white: 255 255 255;
  --color-neutral-offwhite: 248 250 252;
  
  /* Social Media (5) */
  --color-whatsapp: 37 211 102;
  --color-whatsapp-hover: 32 189 90;
  --color-facebook: 24 119 242;
  --color-facebook-hover: 22 100 217;
  --color-twitter: 0 0 0;
  
  /* Remove all gray-* tokens */
}
```

---

### **Step 2: Update tailwind.config.js**

```javascript
colors: {
  // Brand colors (7)
  'primary': 'rgb(var(--color-primary) / <alpha-value>)',
  'primary-dark': 'rgb(var(--color-primary-dark) / <alpha-value>)',
  'secondary': 'rgb(var(--color-secondary) / <alpha-value>)',
  'secondary-light': 'rgb(var(--color-secondary-light) / <alpha-value>)',
  'hotline': 'rgb(var(--color-hotline) / <alpha-value>)',
  'emergency': 'rgb(var(--color-emergency) / <alpha-value>)',
  'accent-yellow': 'rgb(var(--color-accent-yellow) / <alpha-value>)',
  
  // Neutrals (4)
  'text': 'rgb(var(--color-text) / <alpha-value>)',
  'neutral-black': 'rgb(var(--color-neutral-black) / <alpha-value>)',
  'neutral-white': 'rgb(var(--color-neutral-white) / <alpha-value>)',
  'neutral-offwhite': 'rgb(var(--color-neutral-offwhite) / <alpha-value>)',
  
  // Social Media (5)
  'whatsapp': 'rgb(var(--color-whatsapp) / <alpha-value>)',
  'whatsapp-hover': 'rgb(var(--color-whatsapp-hover) / <alpha-value>)',
  'facebook': 'rgb(var(--color-facebook) / <alpha-value>)',
  'facebook-hover': 'rgb(var(--color-facebook-hover) / <alpha-value>)',
  'twitter': 'rgb(var(--color-twitter) / <alpha-value>)',
  
  // Remove all gray-* mappings
}
```

---

### **Step 3: Replace Gray Usage**

Use search & replace:

```bash
# Backgrounds
bg-gray-50  → bg-primary/5
bg-gray-100 → bg-primary/10
bg-gray-200 → bg-secondary/10

# Borders
border-gray-200 → border-primary/15
border-gray-300 → border-primary/20

# Text
text-gray-400 → text-black/40
text-gray-600 → text-black/60
```

---

## 🎊 FINAL ANSWER

### **If you want to stick to brand colors only**:

**Use**: **16 colors** (all brand-specific)
- 7 core brand colors
- 4 neutrals
- 5 social media

**Remove**: **13 colors** (all generic)
- 10 gray scale
- 3 legacy/unused

**Replace grays with**: Brand colors + opacity
- `bg-gray-100` → `bg-primary/10`
- `text-gray-600` → `text-black/60`
- `border-gray-300` → `border-primary/20`

**Result**: **100% brand compliance** ⭐

---

**Document Version**: 1.0  
**Last Updated**: 2026-01-07 06:37 AM  
**Recommendation**: Brand-only system (16 colors)  
**Maintained By**: Design System Team
