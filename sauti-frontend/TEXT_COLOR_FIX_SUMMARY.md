# SAUTI 116 — Text Color Compliance Fix Summary

**Date**: 2026-01-07  
**Status**: 🔄 **In Progress**  
**Completed**: 20+ violations fixed  
**Remaining**: 350+ violations to fix

---

## ✅ COMPLETED FIXES

### **Files Fixed** (3 files)

#### **1. ReportPage.vue** ✅
**Violations Fixed**: 5

| Line | Before | After |
|------|--------|-------|
| 42 | `text-secondary/60` | `text-muted` |
| 55 | `text-secondary` | `text-black` |
| 82 | `text-secondary` | `text-black` |
| 112 | `text-secondary/40` | `text-black/40` |
| 113 | `text-secondary` | `text-black` |

---

#### **2. AppServiceCard.vue** ✅
**Violations Fixed**: 1

| Line | Before | After |
|------|--------|-------|
| 13 | `text-secondary/60` | `text-muted` |

---

#### **3. ReportForm.vue** ✅
**Violations Fixed**: 4

| Line | Before | After |
|------|--------|-------|
| 163 | `text-secondary` (input) | `text-black` |
| 167 | `text-secondary/30` (disabled) | `text-black/30` |
| 187 | `text-secondary` (label) | `text-black` |
| 189 | `text-secondary` (textarea) | `text-black` |

---

## 🔄 REMAINING WORK

### **High Priority Files** (Still Need Fixing)

| File | Violations | Priority |
|------|------------|----------|
| `/views/OperationsPage.vue` | 40+ | 🔴 Critical |
| `/views/AccessibilityPage.vue` | 30+ | 🔴 Critical |
| `/views/ReportsInsightsPage.vue` | 25+ | 🔴 Critical |
| `/views/PartnersPage.vue` | 20+ | 🔴 Critical |
| `/views/NewsPage.vue` | 15+ | 🟡 High |
| `/views/BlogPage.vue` | 10+ | 🟡 High |
| Other components | 200+ | 🟢 Medium |

---

## 🛠️ AUTOMATED FIX SCRIPT

### **For Remaining Files**

Use this VS Code search & replace pattern:

#### **Pattern 1: Body Paragraphs with text-secondary**
```regex
Find: (<p[^>]*class="[^"]*)(text-secondary)([^"]*"[^>]*>)
Replace: $1text-black$3
```

**Note**: Manually verify each replacement to ensure it's not a heading

---

#### **Pattern 2: Muted Text (60% opacity)**
```regex
Find: text-secondary/60
Replace: text-muted
```

---

#### **Pattern 3: Subtle Text (70% opacity)**
```regex
Find: text-secondary/70
Replace: text-black/70
```

---

#### **Pattern 4: Form Labels**
```regex
Find: (<label[^>]*class="[^"]*)(text-secondary)([^"]*"[^>]*>)
Replace: $1text-black$3
```

---

## 📋 MANUAL FIX CHECKLIST

### **OperationsPage.vue** (40+ violations)

- [ ] Lines 27, 32, 37: Feature descriptions (`text-secondary/60` → `text-muted`)
- [ ] Line 67: Path subtitle (`text-secondary` → `text-black`)
- [ ] Lines 101, 132: Step descriptions (`text-secondary/70` → `text-black/70`)
- [ ] Line 161: Metrics title (`text-secondary-light` → Keep as is - this is a heading)
- [ ] Lines 26, 31, 36: Feature titles (Keep `text-secondary` - these are headings)

---

### **AccessibilityPage.vue** (30+ violations)

- [ ] Lines 28, 33, 38: Feature descriptions (`text-secondary` → `text-black`)
- [ ] Line 50: Commitment description (`text-secondary/70` → `text-black/70`)
- [ ] Line 70: Feature list items (`text-secondary` → `text-black`)
- [ ] Line 87: Method names (`text-secondary` → `text-black`)
- [ ] Lines 21, 46, 59, 77, 94: Section headings (Keep `text-secondary` - these are H2/H3)

---

### **ReportsInsightsPage.vue** (25+ violations)

- [ ] Lines 27, 32, 37: Stats descriptions (`text-secondary/60` → `text-muted`)
- [ ] Lines 107, 130, 162: Content descriptions (`text-secondary` → `text-black`)
- [ ] Line 65: Select text (`text-secondary` → `text-black`)
- [ ] Lines 20, 97, 126, 143, 158, 171, 182: Section headings (Keep `text-secondary` - these are H2/H3)

---

### **PartnersPage.vue** (20+ violations)

- [ ] Lines 26, 31, 36: Feature descriptions (`text-secondary/60` → `text-muted`)
- [ ] Lines 25, 30, 35: Feature titles (`text-secondary` → `text-black`)
- [ ] Line 86: Collaboration description (`text-secondary/60` → `text-muted`)
- [ ] Line 77: No partners message (`text-secondary/40` → `text-black/40`)
- [ ] Lines 19, 46, 85: Section headings (Keep `text-secondary` - these are H2/H3)

---

## ✅ VERIFICATION CHECKLIST

After fixing each file:

- [ ] **Headings still green**: All `<h1>`, `<h2>`, `<h3>`, `<h4>` should keep `text-secondary`
- [ ] **Body text now black**: All `<p>`, `<span>`, `<div>` body text should use `text-black` or `text-muted`
- [ ] **Form inputs black**: All `<input>`, `<textarea>`, `<select>` should use `text-black`
- [ ] **Icons unchanged**: Icons can keep brand colors (`text-secondary`, `text-primary`)
- [ ] **Labels/Tags unchanged**: Small labels/tags can keep brand colors

---

## 🎯 QUICK REFERENCE

### **What to Change**

```vue
<!-- ❌ WRONG -->
<p class="text-secondary">Body text</p>
<p class="text-secondary/60">Muted text</p>
<p class="text-secondary/70">Subtle text</p>
<input class="text-secondary" />
<label class="text-secondary">Label</label>
```

### **What to Keep**

```vue
<!-- ✅ CORRECT - Keep these -->
<h1 class="text-secondary">Heading</h1>
<h2 class="text-secondary">Subheading</h2>
<h3 class="text-secondary">Section</h3>
<h4 class="campaign-header text-secondary">Campaign Header</h4>
<ShieldCheckIcon class="text-secondary" />
<span class="campaign-header text-secondary">LABEL</span>
```

### **Corrected Version**

```vue
<!-- ✅ CORRECT -->
<p class="text-black">Body text</p>
<p class="text-muted">Muted text</p>
<p class="text-black/70">Subtle text</p>
<input class="text-black" />
<label class="text-black">Label</label>
```

---

## 📊 PROGRESS TRACKER

| Category | Total | Fixed | Remaining | % Complete |
|----------|-------|-------|-----------|------------|
| **Views** | 250+ | 5 | 245+ | 2% |
| **Components** | 128+ | 5 | 123+ | 4% |
| **Total** | 378+ | 10 | 368+ | **3%** |

---

## 🚀 NEXT STEPS

### **Immediate** (Next 2-3 hours)

1. **Fix OperationsPage.vue** (40+ violations)
   - Use search & replace patterns above
   - Manually verify headings stay green
   - Test visual appearance

2. **Fix AccessibilityPage.vue** (30+ violations)
   - Use search & replace patterns
   - Verify compliance

3. **Fix ReportsInsightsPage.vue** (25+ violations)
   - Use search & replace patterns
   - Verify compliance

---

### **Follow-up** (Next 4-6 hours)

4. **Fix PartnersPage.vue** (20+ violations)
5. **Fix NewsPage.vue** (15+ violations)
6. **Fix BlogPage.vue** (10+ violations)
7. **Fix remaining components** (200+ violations)

---

### **Final QA** (1-2 hours)

8. **Visual review** of all pages
9. **Accessibility testing** (contrast ratios)
10. **Brand compliance verification**

---

## 📝 NOTES

### **Helper Classes Available**

```css
/* Already defined in main.css */
.text-muted {
  color: rgba(0, 0, 0, 0.6) !important; /* 60% black */
}

.text-subtle {
  color: rgba(0, 0, 0, 0.5) !important; /* 50% black */
}

.text-disabled {
  color: rgba(0, 0, 0, 0.4) !important; /* 40% black */
}
```

### **When to Use Each**

- **`text-black`**: Standard body text, form inputs, labels
- **`text-muted`**: Secondary information, descriptions, captions (60% opacity)
- **`text-black/70`**: Subtle text, step descriptions (70% opacity)
- **`text-black/40`**: Disabled states, very subtle text (40% opacity)

---

**Document Version**: 1.0  
**Last Updated**: 2026-01-07  
**Next Update**: After completing high-priority files  
**Maintained By**: Brand Compliance Team
