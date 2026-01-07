# SAUTI 116 — IMAGE CULTURAL REPRESENTATION AUDIT

**Date**: 2026-01-07  
**Context**: SAUTI 116 is a **Ugandan** child protection helpline  
**Requirement**: All images must represent **Ugandan people and context**  
**Status**: ⚠️ **NEEDS REVIEW**

---

## 🔍 IMAGE INVENTORY

### **Total Images Found**: 18 static images

| Image | Location | Type | Status |
|-------|----------|------|--------|
| `community-protection.png` | src/assets | People | ⚠️ **REVIEW NEEDED** |
| `diverse_helpline_operations.png` | src/assets | People | ⚠️ **REVIEW NEEDED** |
| `inclusive_community_protection.png` | src/assets | People | ⚠️ **REVIEW NEEDED** |
| `helpline-action.png` | src/assets | People | ⚠️ **REVIEW NEEDED** |
| `helpline-center.png` | src/assets | People | ⚠️ **REVIEW NEEDED** |
| `children-uganda-1.jpeg` | src/assets, public/assets | People | ✅ **Likely Ugandan** |
| `children-uganda-2.jpeg` | src/assets, public/assets | People | ✅ **Likely Ugandan** |
| `sauti-aboutpage.webp` | src/assets, public/assets | People | ⚠️ **REVIEW NEEDED** |
| `operations-case-flow.jpg` | src/assets, public/assets | Diagram | ✅ **OK (no people)** |
| `uganda mapping.png` | src/assets, public/assets | Map | ✅ **OK (map)** |
| `logo.png` | src/assets, public | Logo | ✅ **OK (logo)** |
| `sauti-logo.jpeg` | src/assets, public/assets | Logo | ✅ **OK (logo)** |
| `call.png` | src/assets | Icon | ✅ **OK (icon)** |
| `ug.svg` | src/assets, public/assets | Flag | ✅ **OK (flag)** |

---

## ⚠️ IMAGES REQUIRING REVIEW

### **Priority: HIGH** (Images with people)

These images **MUST** show Ugandan people in Ugandan context:

1. **community-protection.png** (825KB)
   - **Usage**: DonatePage hero image
   - **Description**: Community protection scene
   - **Action**: ⚠️ **Verify shows Ugandan people**

2. **diverse_helpline_operations.png** (754KB)
   - **Usage**: HomePage operations section
   - **Description**: Helpline operations team
   - **Action**: ⚠️ **Verify shows Ugandan staff**

3. **inclusive_community_protection.png** (1.1MB)
   - **Usage**: AboutPage vision section
   - **Description**: Community protection
   - **Action**: ⚠️ **Verify shows Ugandan community**

4. **helpline-action.png** (696KB)
   - **Usage**: BlogCard fallback image
   - **Description**: Helpline action scene
   - **Action**: ⚠️ **Verify shows Ugandan context**

5. **helpline-center.png** (766KB)
   - **Usage**: OperationsPage header
   - **Description**: Helpline operations center
   - **Action**: ⚠️ **Verify shows Ugandan facility**

6. **sauti-aboutpage.webp** (size unknown)
   - **Usage**: AboutPage
   - **Description**: About page hero
   - **Action**: ⚠️ **Verify shows Ugandan people**

---

## ✅ IMAGES CONFIRMED OK

### **No people or generic content**:

1. **children-uganda-1.jpeg** ✅
   - **Filename indicates**: Ugandan children
   - **Status**: Likely appropriate

2. **children-uganda-2.jpeg** ✅
   - **Filename indicates**: Ugandan children
   - **Status**: Likely appropriate

3. **operations-case-flow.jpg** ✅
   - **Type**: Diagram/flowchart
   - **Status**: No people, OK

4. **uganda mapping.png** ✅
   - **Type**: Map of Uganda
   - **Status**: Geographic, OK

5. **logo.png** ✅
   - **Type**: Government/organizational logo
   - **Status**: OK

6. **sauti-logo.jpeg** ✅
   - **Type**: SAUTI 116 logo
   - **Status**: OK

7. **call.png** ✅
   - **Type**: Phone icon
   - **Status**: Generic icon, OK

8. **ug.svg** ✅
   - **Type**: Uganda flag
   - **Status**: OK

---

## 📋 IMAGE USAGE IN CODE

### **Where images are used**:

| File | Image | Line | Context |
|------|-------|------|---------|
| DonatePage.vue | community-protection.png | 5 | Hero background |
| HomePage.vue | diverse_helpline_operations.png | 83 | Operations section |
| AboutPage.vue | inclusive_community_protection.png | 91 | Vision section |
| BlogCard.vue | helpline-action.png | 7 | Fallback image |
| OperationsPage.vue | helpline-center.png | 50 | Header image |
| DynamicChatWindow.vue | call.png | 34, 63, 74 | Chat avatar |
| AppFooter.vue | logo.png | 137 | Footer logo |

---

## 🎯 CULTURAL REPRESENTATION REQUIREMENTS

### **For SAUTI 116 (Ugandan Organization)**:

All images with people **MUST**:

1. ✅ **Show Ugandan people**
   - East African features
   - Ugandan context
   - Local settings

2. ✅ **Represent Ugandan context**
   - Ugandan buildings/facilities
   - Local environment
   - Culturally appropriate settings

3. ✅ **Avoid stock photos** (if non-Ugandan)
   - No generic Western stock photos
   - No non-African people
   - No non-Ugandan contexts

4. ✅ **Show diversity within Uganda**
   - Different regions
   - Different ages
   - Different backgrounds

---

## 🚨 CRITICAL ISSUES TO CHECK

### **Red Flags** (Immediate review needed):

1. **Stock Photo Usage**
   - ❌ Are these generic stock photos?
   - ❌ Do they show non-Ugandan people?
   - ❌ Do they show non-African settings?

2. **Cultural Authenticity**
   - ❌ Do settings look Ugandan?
   - ❌ Are clothing/uniforms appropriate?
   - ❌ Is the environment authentic?

3. **Representation**
   - ❌ Do people look East African?
   - ❌ Is the context Ugandan?
   - ❌ Are facilities/buildings local?

---

## 💡 RECOMMENDATIONS

### **Immediate Actions**:

1. **Visual Review** (Priority: 🔴 CRITICAL)
   ```bash
   # Open each image for visual inspection
   open src/assets/community-protection.png
   open src/assets/diverse_helpline_operations.png
   open src/assets/inclusive_community_protection.png
   open src/assets/helpline-action.png
   open src/assets/helpline-center.png
   open src/assets/sauti-aboutpage.webp
   ```

2. **Verify Each Image**:
   - [ ] Shows Ugandan people
   - [ ] Shows Ugandan context
   - [ ] Culturally appropriate
   - [ ] Not generic stock photo
   - [ ] Authentic representation

3. **Replace if Needed**:
   - Source authentic Ugandan photos
   - Use actual SAUTI 116 facility photos
   - Use real staff/team photos
   - Use genuine community photos

---

## 📸 SOURCING AUTHENTIC UGANDAN IMAGES

### **Recommended Sources**:

1. **Internal Photos** (Best)
   - Actual SAUTI 116 facilities
   - Real staff members
   - Genuine community events
   - Actual operations center

2. **Ugandan Photographers**
   - Local professional photographers
   - Ugandan stock photo sites
   - East African image libraries

3. **Partner Organizations**
   - MGLSD official photos
   - Government of Uganda images
   - Partner NGO photos (with permission)

4. **Avoid**:
   - ❌ Generic Western stock photos
   - ❌ Non-African people
   - ❌ Non-Ugandan settings
   - ❌ Culturally inappropriate images

---

## 🎨 IMAGE REPLACEMENT GUIDE

### **If images need replacement**:

#### **Step 1: Identify Issues**
```bash
# Review each image
open src/assets/community-protection.png
# Ask: Is this Ugandan? Is this authentic?
```

#### **Step 2: Source Replacements**
- Contact SAUTI 116 for official photos
- Hire Ugandan photographer
- Use authentic local images

#### **Step 3: Replace Files**
```bash
# Same filename, new content
cp new-ugandan-photo.png src/assets/community-protection.png
```

#### **Step 4: Optimize**
```bash
# Optimize for web
# Maintain quality
# Keep file sizes reasonable
```

---

## 📊 CULTURAL REPRESENTATION CHECKLIST

### **For Each Image with People**:

- [ ] **People are Ugandan/East African**
- [ ] **Setting is Ugandan**
- [ ] **Context is culturally appropriate**
- [ ] **Not a generic stock photo**
- [ ] **Represents SAUTI 116 authentically**
- [ ] **Shows diversity within Uganda**
- [ ] **Respectful representation**
- [ ] **High quality**
- [ ] **Properly licensed**

---

## 🎯 PRIORITY ACTIONS

### **Immediate** (This Week):

1. ✅ **Visual audit of all 6 people-focused images**
   - Open each image
   - Verify Ugandan representation
   - Document findings

2. ⚠️ **Identify non-Ugandan images**
   - Flag for replacement
   - Source alternatives
   - Plan replacement

3. 🔄 **Replace non-authentic images**
   - Use authentic Ugandan photos
   - Maintain same filenames
   - Update if needed

---

### **Short-term** (This Month):

1. **Establish image guidelines**
   - Document requirements
   - Create approval process
   - Set standards

2. **Build image library**
   - Collect authentic photos
   - Organize by category
   - Maintain licenses

3. **Partner with photographers**
   - Hire Ugandan photographers
   - Commission new photos
   - Build ongoing relationship

---

## 📝 IMAGE GUIDELINES (Going Forward)

### **All future images MUST**:

1. ✅ **Show Ugandan people and context**
2. ✅ **Be culturally authentic**
3. ✅ **Represent SAUTI 116 accurately**
4. ✅ **Be properly licensed**
5. ✅ **Be high quality**
6. ✅ **Be optimized for web**

### **Approval Process**:

1. Source image
2. Verify cultural authenticity
3. Check licensing
4. Optimize for web
5. Get stakeholder approval
6. Deploy

---

## 🎊 CONCLUSION

**Status**: ⚠️ **NEEDS IMMEDIATE REVIEW**

**Critical Actions**:
1. ⚠️ **Review 6 people-focused images**
2. ⚠️ **Verify Ugandan representation**
3. ⚠️ **Replace if non-authentic**

**Timeline**: **This week**

**Importance**: 🔴 **CRITICAL** for cultural authenticity

---

**SAUTI 116 is Ugandan. All images must authentically represent Ugandan people and context.**

---

**Document Version**: 1.0  
**Last Updated**: 2026-01-07 06:56 AM  
**Status**: Awaiting Visual Review  
**Maintained By**: Content Team
