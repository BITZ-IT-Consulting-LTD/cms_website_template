# SAUTI 116 — Typography Color Visual Test Checklist

**Purpose**: Verify that body text color enforcement is working correctly across all pages and components.

**Date**: 2026-01-07  
**Tester**: _________________  
**Browser**: _________________  
**Device**: _________________

---

## 🎯 TESTING METHODOLOGY

### Color Verification Tools

1. **Browser DevTools**:
   - Right-click on text → Inspect
   - Check "Computed" tab → Look for `color` property
   - Should show: `rgb(0, 0, 0)` or `#000000`

2. **Color Picker Extension**:
   - Use ColorZilla or similar
   - Click on text to get exact color value
   - Body text should be: `#000000`

3. **Contrast Checker**:
   - Use WebAIM Contrast Checker
   - Verify WCAG AAA compliance (21:1 ratio)

---

## 📄 PAGE-BY-PAGE CHECKLIST

### ✅ Homepage (`/`)

| Element | Expected Color | Actual Color | Status |
|---------|----------------|--------------|--------|
| Hero section body text | #000000 | _______ | ☐ |
| Service descriptions | #000000 | _______ | ☐ |
| Testimonial text | #000000 | _______ | ☐ |
| Footer text | #000000 | _______ | ☐ |
| **Headings** (h1-h3) | #006837 (Deep Green) | _______ | ☐ |
| **CTA buttons** | Brand colors | _______ | ☐ |

**Notes**: _________________________________________________________________

---

### ✅ About Page (`/about`)

| Element | Expected Color | Actual Color | Status |
|---------|----------------|--------------|--------|
| Mission statement | #000000 | _______ | ☐ |
| Timeline descriptions | #000000 | _______ | ☐ |
| Team member bios | #000000 | _______ | ☐ |
| **Timestamps** | rgba(0,0,0,0.6) | _______ | ☐ |
| **Headings** | #006837 | _______ | ☐ |

**Notes**: _________________________________________________________________

---

### ✅ Services Page (`/services`)

| Element | Expected Color | Actual Color | Status |
|---------|----------------|--------------|--------|
| Service descriptions | #000000 | _______ | ☐ |
| Help steps text | #000000 | _______ | ☐ |
| FAQ answers | #000000 | _______ | ☐ |
| **Headings** | #006837 | _______ | ☐ |

**Notes**: _________________________________________________________________

---

### ✅ Blog Page (`/blog`)

| Element | Expected Color | Actual Color | Status |
|---------|----------------|--------------|--------|
| Blog post excerpts | #000000 | _______ | ☐ |
| Article body text | #000000 | _______ | ☐ |
| Comment text | #000000 | _______ | ☐ |
| **Post metadata** (date, author) | rgba(0,0,0,0.6) | _______ | ☐ |
| **Headings** | #006837 | _______ | ☐ |
| **Tags** | rgba(0,0,0,0.6) | _______ | ☐ |

**Notes**: _________________________________________________________________

---

### ✅ Contact Page (`/contact`)

| Element | Expected Color | Actual Color | Status |
|---------|----------------|--------------|--------|
| Form labels | #006837 (secondary) | _______ | ☐ |
| Form input text | #000000 | _______ | ☐ |
| Form hints | rgba(0,0,0,0.6) | _______ | ☐ |
| Contact info text | #000000 | _______ | ☐ |
| **Placeholder text** | rgba(0,0,0,0.5) | _______ | ☐ |

**Notes**: _________________________________________________________________

---

### ✅ Resources Page (`/resources`)

| Element | Expected Color | Actual Color | Status |
|---------|----------------|--------------|--------|
| Resource descriptions | #000000 | _______ | ☐ |
| Download links | #000000 | _______ | ☐ |
| Category labels | #000000 | _______ | ☐ |
| **Headings** | #006837 | _______ | ☐ |

**Notes**: _________________________________________________________________

---

## 🧩 COMPONENT-BY-COMPONENT CHECKLIST

### ✅ Navigation Header

| Element | Expected Color | Actual Color | Status |
|---------|----------------|--------------|--------|
| Nav links (inactive) | #000000 | _______ | ☐ |
| Nav links (hover) | #0087CF (primary) | _______ | ☐ |
| Nav links (active) | #0087CF (primary) | _______ | ☐ |

**Notes**: _________________________________________________________________

---

### ✅ Footer

| Element | Expected Color | Actual Color | Status |
|---------|----------------|--------------|--------|
| Footer text | #000000 | _______ | ☐ |
| Footer links | #000000 | _______ | ☐ |
| Copyright text | rgba(0,0,0,0.6) | _______ | ☐ |

**Notes**: _________________________________________________________________

---

### ✅ Cards (Service Cards, Blog Cards, etc.)

| Element | Expected Color | Actual Color | Status |
|---------|----------------|--------------|--------|
| Card title | #006837 (secondary) | _______ | ☐ |
| Card body text | #000000 | _______ | ☐ |
| Card metadata | rgba(0,0,0,0.6) | _______ | ☐ |

**Notes**: _________________________________________________________________

---

### ✅ Forms

| Element | Expected Color | Actual Color | Status |
|---------|----------------|--------------|--------|
| Input text (typed) | #000000 | _______ | ☐ |
| Placeholder text | rgba(0,0,0,0.5) | _______ | ☐ |
| Label text | #006837 (secondary) | _______ | ☐ |
| Helper text | rgba(0,0,0,0.6) | _______ | ☐ |
| Error text | #ED1C24 (emergency) | _______ | ☐ |
| Disabled input text | rgba(0,0,0,0.4) | _______ | ☐ |

**Notes**: _________________________________________________________________

---

### ✅ Buttons

| Element | Expected Color | Actual Color | Status |
|---------|----------------|--------------|--------|
| Primary button text | #FFFFFF (white) | _______ | ☐ |
| Secondary button text | #FFFFFF (white) | _______ | ☐ |
| Emergency button text | #FFFFFF (white) | _______ | ☐ |
| Disabled button text | rgba(0,0,0,0.4) | _______ | ☐ |

**Notes**: _________________________________________________________________

---

### ✅ Modals/Dialogs

| Element | Expected Color | Actual Color | Status |
|---------|----------------|--------------|--------|
| Modal title | #006837 (secondary) | _______ | ☐ |
| Modal body text | #000000 | _______ | ☐ |
| Modal close button | #000000 | _______ | ☐ |

**Notes**: _________________________________________________________________

---

### ✅ Partner Carousel

| Element | Expected Color | Actual Color | Status |
|---------|----------------|--------------|--------|
| Partner name | #000000 | _______ | ☐ |
| Partner description | #000000 | _______ | ☐ |
| Empty state text | rgba(0,0,0,0.6) | _______ | ☐ |

**Notes**: _________________________________________________________________

---

### ✅ Video Player

| Element | Expected Color | Actual Color | Status |
|---------|----------------|--------------|--------|
| Video title | #006837 (secondary) | _______ | ☐ |
| Video description | #000000 | _______ | ☐ |
| Video metadata | rgba(0,0,0,0.6) | _______ | ☐ |

**Notes**: _________________________________________________________________

---

## 📱 RESPONSIVE TESTING

### Desktop (1920px)

| Page | Body Text Color | Heading Color | Status |
|------|-----------------|---------------|--------|
| Homepage | #000000 | #006837 | ☐ |
| About | #000000 | #006837 | ☐ |
| Services | #000000 | #006837 | ☐ |
| Blog | #000000 | #006837 | ☐ |
| Contact | #000000 | #006837 | ☐ |

**Notes**: _________________________________________________________________

---

### Tablet (768px)

| Page | Body Text Color | Heading Color | Status |
|------|-----------------|---------------|--------|
| Homepage | #000000 | #006837 | ☐ |
| About | #000000 | #006837 | ☐ |
| Services | #000000 | #006837 | ☐ |
| Blog | #000000 | #006837 | ☐ |
| Contact | #000000 | #006837 | ☐ |

**Notes**: _________________________________________________________________

---

### Mobile (375px)

| Page | Body Text Color | Heading Color | Status |
|------|-----------------|---------------|--------|
| Homepage | #000000 | #006837 | ☐ |
| About | #000000 | #006837 | ☐ |
| Services | #000000 | #006837 | ☐ |
| Blog | #000000 | #006837 | ☐ |
| Contact | #000000 | #006837 | ☐ |

**Notes**: _________________________________________________________________

---

## 🔍 BROWSER COMPATIBILITY

### Chrome

| Page | Body Text | Headings | Forms | Status |
|------|-----------|----------|-------|--------|
| All pages | #000000 | #006837 | #000000 | ☐ |

**Version**: _________________  
**Notes**: _________________________________________________________________

---

### Safari

| Page | Body Text | Headings | Forms | Status |
|------|-----------|----------|-------|--------|
| All pages | #000000 | #006837 | #000000 | ☐ |

**Version**: _________________  
**Notes**: _________________________________________________________________

---

### Firefox

| Page | Body Text | Headings | Forms | Status |
|------|-----------|----------|-------|--------|
| All pages | #000000 | #006837 | #000000 | ☐ |

**Version**: _________________  
**Notes**: _________________________________________________________________

---

### Edge

| Page | Body Text | Headings | Forms | Status |
|------|-----------|----------|-------|--------|
| All pages | #000000 | #006837 | #000000 | ☐ |

**Version**: _________________  
**Notes**: _________________________________________________________________

---

## ♿ ACCESSIBILITY TESTING

### Contrast Ratio Verification

| Element | Foreground | Background | Ratio | WCAG Level | Status |
|---------|------------|------------|-------|------------|--------|
| Body text | #000000 | #FFFFFF | 21:1 | AAA | ☐ |
| Muted text | rgba(0,0,0,0.6) | #FFFFFF | 12.6:1 | AAA | ☐ |
| Subtle text | rgba(0,0,0,0.5) | #FFFFFF | 10.5:1 | AAA | ☐ |
| Disabled text | rgba(0,0,0,0.4) | #FFFFFF | 8.4:1 | AA | ☐ |

**Tool Used**: _________________  
**Notes**: _________________________________________________________________

---

### Screen Reader Testing

| Page | Text Readability | Status |
|------|------------------|--------|
| Homepage | ☐ Clear | ☐ |
| About | ☐ Clear | ☐ |
| Services | ☐ Clear | ☐ |
| Blog | ☐ Clear | ☐ |
| Contact | ☐ Clear | ☐ |

**Screen Reader**: _________________  
**Notes**: _________________________________________________________________

---

## 🐛 KNOWN ISSUES

### Issue 1
**Description**: _________________________________________________________________  
**Severity**: ☐ Critical  ☐ High  ☐ Medium  ☐ Low  
**Affected Pages**: _________________________________________________________________  
**Status**: ☐ Open  ☐ In Progress  ☐ Resolved

---

### Issue 2
**Description**: _________________________________________________________________  
**Severity**: ☐ Critical  ☐ High  ☐ Medium  ☐ Low  
**Affected Pages**: _________________________________________________________________  
**Status**: ☐ Open  ☐ In Progress  ☐ Resolved

---

### Issue 3
**Description**: _________________________________________________________________  
**Severity**: ☐ Critical  ☐ High  ☐ Medium  ☐ Low  
**Affected Pages**: _________________________________________________________________  
**Status**: ☐ Open  ☐ In Progress  ☐ Resolved

---

## ✅ FINAL SIGN-OFF

### Testing Summary

- **Total Pages Tested**: _______
- **Total Components Tested**: _______
- **Issues Found**: _______
- **Critical Issues**: _______
- **Overall Status**: ☐ PASS  ☐ FAIL  ☐ PASS WITH ISSUES

---

### Approvals

**Frontend Engineer**: _________________  
**Date**: _________________  
**Signature**: _________________

**UX Auditor**: _________________  
**Date**: _________________  
**Signature**: _________________

**Brand Team (MGLSD)**: _________________  
**Date**: _________________  
**Signature**: _________________

---

## 📋 DEPLOYMENT DECISION

☐ **APPROVED FOR PRODUCTION** — All tests passed, no critical issues  
☐ **APPROVED WITH MINOR ISSUES** — Non-critical issues documented, can be fixed post-deployment  
☐ **REJECTED** — Critical issues found, requires fixes before deployment

**Decision Date**: _________________  
**Deployment Date**: _________________

---

**Test Report Generated**: 2026-01-07  
**Document Version**: 1.0  
**Next Review**: 30 days post-deployment
