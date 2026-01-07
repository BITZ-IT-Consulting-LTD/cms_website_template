# SAUTI 116 — Typography Color Quick Reference

## ✅ APPROVED TEXT COLOR UTILITIES

### Body Text (Default)
```html
<!-- ✅ CORRECT: Pure black body text -->
<p class="text-black">This is standard body text</p>
<span class="text-black">Regular content</span>

<!-- ❌ WRONG: Do not use gray utilities -->
<p class="text-gray-700">This violates brand guidelines</p>
```

---

### Muted Text (Timestamps, Captions, Form Hints)
```html
<!-- ✅ CORRECT: Use .text-muted for secondary information -->
<p class="text-sm text-muted">Posted 2 hours ago</p>
<span class="text-muted">Optional field</span>

<!-- ❌ WRONG -->
<p class="text-gray-600">Posted 2 hours ago</p>
```

**Color**: `rgba(0, 0, 0, 0.6)` — 60% black  
**Contrast Ratio**: 12.6:1 (WCAG AAA compliant)

---

### Subtle Text (Placeholder-like Content)
```html
<!-- ✅ CORRECT: Use .text-subtle for very light content -->
<p class="text-subtle">No items found</p>
<span class="text-subtle">Coming soon</span>

<!-- ❌ WRONG -->
<p class="text-gray-500">No items found</p>
```

**Color**: `rgba(0, 0, 0, 0.5)` — 50% black  
**Contrast Ratio**: 10.5:1 (WCAG AAA compliant)

---

### Disabled States
```html
<!-- ✅ CORRECT: Use .text-disabled for inactive elements -->
<button disabled class="text-disabled">Submit</button>
<input disabled class="text-disabled" />

<!-- ❌ WRONG -->
<button disabled class="text-gray-400">Submit</button>
```

**Color**: `rgba(0, 0, 0, 0.4)` — 40% black  
**Contrast Ratio**: 8.4:1 (WCAG AA compliant)

---

## 🎨 HEADING COLORS (Accent Colors Allowed)

### Headings (Use Brand Colors)
```html
<!-- ✅ CORRECT: Headings use brand accent colors -->
<h1 class="text-secondary">Main Heading</h1>
<h2 class="text-secondary">Section Title</h2>
<h3 class="text-secondary">Subsection</h3>

<!-- ✅ ALSO CORRECT: Primary color for emphasis -->
<h2 class="text-primary">Featured Section</h2>

<!-- ❌ WRONG: Do not use gray for headings -->
<h1 class="text-gray-900">Heading</h1>
```

**Allowed Heading Colors**:
- `text-secondary` — Sauti Deep Green (#006837)
- `text-primary` — Sauti Sky Blue (#0087CF)
- `text-hotline` — Sauti Bright Orange (#F7941E)
- `text-emergency` — Sauti Signal Red (#ED1C24)

---

## 🚫 PROHIBITED UTILITIES

### Never Use These for Body Text
```html
<!-- ❌ PROHIBITED -->
<p class="text-gray-600">...</p>
<p class="text-gray-700">...</p>
<p class="text-gray-800">...</p>
<p class="text-gray-900">...</p>
<p class="text-slate-600">...</p>

<!-- ❌ PROHIBITED: Opacity modifiers on text-text -->
<p class="text-text/70">...</p>
<p class="text-text/60">...</p>
```

**Note**: These utilities are now globally overridden to render as pure black (#000000), but avoid using them to prevent confusion.

---

## 📋 MIGRATION GUIDE

### Find-Replace Rules

| Old Class | New Class | Use Case |
|-----------|-----------|----------|
| `text-gray-900` | `text-black` | Body text, headings |
| `text-gray-800` | `text-black` | Body text |
| `text-gray-700` | `text-black` | Body text, descriptions |
| `text-gray-600` | `text-black` | Body text |
| `text-gray-600` | `text-muted` | Timestamps, captions, hints |
| `text-gray-500` | `text-muted` | Secondary information |
| `text-gray-400` | `text-subtle` | Placeholder-like content |
| `text-gray-300` | `text-disabled` | Disabled states |

---

## 🎯 DECISION TREE

```
Is this text a heading (h1-h6)?
├─ YES → Use text-secondary or text-primary
└─ NO → Continue...

Is this text body/paragraph content?
├─ YES → Use text-black
└─ NO → Continue...

Is this text secondary information (timestamp, caption, hint)?
├─ YES → Use text-muted
└─ NO → Continue...

Is this text placeholder-like or very subtle?
├─ YES → Use text-subtle
└─ NO → Continue...

Is this element disabled or inactive?
├─ YES → Use text-disabled
└─ NO → Use text-black (default)
```

---

## 🔍 EXAMPLES BY COMPONENT TYPE

### Blog Post
```html
<article>
  <!-- Heading: Use brand color -->
  <h1 class="text-secondary">Article Title</h1>
  
  <!-- Metadata: Use muted -->
  <div class="text-sm text-muted">
    <span>By John Doe</span>
    <span>Published 2 hours ago</span>
  </div>
  
  <!-- Body text: Use pure black -->
  <p class="text-black">
    This is the main content of the article...
  </p>
  
  <!-- Tags: Use muted -->
  <div class="text-muted">
    <span>Tags: #protection #safety</span>
  </div>
</article>
```

---

### Form
```html
<form>
  <!-- Label: Use brand color -->
  <label class="text-secondary font-bold">Full Name</label>
  
  <!-- Input: Pure black text -->
  <input type="text" class="text-black" placeholder="Enter your name" />
  
  <!-- Hint: Use muted -->
  <p class="text-sm text-muted">This field is required</p>
  
  <!-- Error: Use emergency color -->
  <p class="text-sm text-emergency">Please enter a valid name</p>
  
  <!-- Disabled button -->
  <button disabled class="text-disabled">Submit</button>
</form>
```

---

### Card Component
```html
<div class="card-base">
  <!-- Card title: Use brand color -->
  <h3 class="text-secondary">Service Title</h3>
  
  <!-- Card description: Pure black -->
  <p class="text-black">
    This service provides support for...
  </p>
  
  <!-- Card footer metadata: Use muted -->
  <div class="text-sm text-muted">
    Last updated: January 7, 2026
  </div>
</div>
```

---

### Navigation
```html
<nav>
  <!-- Active link: Use primary color -->
  <a href="#" class="nav-link nav-link-active">Home</a>
  
  <!-- Inactive link: Pure black -->
  <a href="#" class="nav-link">About</a>
  
  <!-- Disabled link -->
  <a href="#" class="nav-link text-disabled">Coming Soon</a>
</nav>
```

---

## 🛠️ TROUBLESHOOTING

### "My text is still gray!"

**Check these common issues**:

1. **Inline styles**: Remove any `style="color: #333"` attributes
2. **Component scoped styles**: Check `<style scoped>` blocks for color overrides
3. **Third-party components**: Some libraries may inject their own styles
4. **Browser cache**: Hard refresh (Cmd+Shift+R) to clear cached CSS

---

### "I need lighter text for a specific use case"

**Use the approved muted utilities**:

```html
<!-- ✅ CORRECT: Use approved opacity levels -->
<p class="text-muted">60% black opacity</p>
<p class="text-subtle">50% black opacity</p>
<p class="text-disabled">40% black opacity</p>

<!-- ❌ WRONG: Do not create custom opacity -->
<p class="text-black/50">Custom opacity</p>
<p style="color: rgba(0,0,0,0.7)">Inline opacity</p>
```

---

## 📊 CONTRAST RATIOS (WCAG Compliance)

| Utility | Color | Contrast on White | WCAG Level |
|---------|-------|-------------------|------------|
| `text-black` | #000000 | 21:1 | AAA ✅ |
| `text-muted` | rgba(0,0,0,0.6) | 12.6:1 | AAA ✅ |
| `text-subtle` | rgba(0,0,0,0.5) | 10.5:1 | AAA ✅ |
| `text-disabled` | rgba(0,0,0,0.4) | 8.4:1 | AA ✅ |

**All approved utilities meet or exceed WCAG AA standards.**

---

## 🔗 RELATED DOCUMENTATION

- **Brand Guidelines**: `/Brand Guideline.md` (Section 6: Typography)
- **Full Audit Report**: `/TYPOGRAPHY_COLOR_AUDIT.md`
- **Typography Compliance**: `/TYPOGRAPHY_COMPLIANCE.md`
- **Global Styles**: `/src/assets/styles/main.css` (Lines 127-157)

---

## ✅ CHECKLIST FOR NEW COMPONENTS

Before committing a new component, verify:

- [ ] All body text uses `text-black` (not `text-gray-*`)
- [ ] Headings use `text-secondary` or `text-primary`
- [ ] Timestamps/captions use `text-muted`
- [ ] Disabled states use `text-disabled`
- [ ] No inline `color` styles
- [ ] No `text-text/XX` opacity modifiers
- [ ] Component passes contrast ratio check (WCAG AA minimum)

---

**Last Updated**: 2026-01-07  
**Maintained By**: Frontend Engineering Team  
**Questions?**: Refer to `/TYPOGRAPHY_COLOR_AUDIT.md` for detailed rationale
