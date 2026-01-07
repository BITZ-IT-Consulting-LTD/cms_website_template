# SAUTI 116 — "Get Help" Button Micro-Interaction Design

**Date**: 2026-01-07  
**Designer**: Crisis-Context UX Specialist  
**Issue**: Floating "Get Help" button appears without explanation  
**Context**: First-time users in crisis may not understand the button's purpose

---

## EXECUTIVE SUMMARY

### Current State
❌ **No onboarding**: Button appears with no context  
❌ **No affordance**: Users may not know it opens a help modal  
❌ **No reassurance**: No indication of confidentiality/safety

### Proposed Solution
✅ **Gentle tooltip**: Non-intrusive, one-time hint  
✅ **Subtle animation**: Draws attention without alarm  
✅ **Trauma-informed copy**: Empowering, not fear-based  
✅ **Dismissible**: User controls the experience

---

## 🎯 INTERACTION FLOW

### **Trigger Condition**

**When to Show**:
```
IF (first visit to site) 
   AND (user has been on page for 3 seconds)
   AND (user has not interacted with "Get Help" button)
   AND (tooltip has not been dismissed previously)
THEN show tooltip
```

**Why 3 seconds**:
- ✅ Allows user to orient themselves
- ✅ Avoids immediate interruption
- ✅ Indicates user is reading/exploring (not bouncing)

---

### **Visual Design**

#### **Tooltip Appearance**

```
┌─────────────────────────────────────────┐
│  Need support? This button connects     │
│  you to confidential help options.      │
│                                          │
│  [Got it]                                │
└──────────────────────┬──────────────────┘
                       │ (arrow pointing to button)
                       ▼
              ┌──────────────────┐
              │  Get Help Now    │
              └──────────────────┘
```

**Specifications**:
- **Position**: Above the "Get Help Now" button
- **Background**: White with subtle shadow
- **Border**: 1px solid primary/10
- **Arrow**: Pointing down to button
- **Animation**: Gentle fade-in + slight upward slide
- **Timing**: 300ms ease-out

---

#### **Subtle Button Animation** (Attention-Grabbing)

**Initial State** (when tooltip appears):
```css
/* Gentle pulse - NOT alarming */
@keyframes gentle-pulse {
  0%, 100% { 
    box-shadow: 0 0 0 0 rgba(237, 28, 36, 0.4);
  }
  50% { 
    box-shadow: 0 0 0 8px rgba(237, 28, 36, 0);
  }
}

/* Apply for 2 cycles only */
animation: gentle-pulse 2s ease-out 2;
```

**Why gentle pulse**:
- ✅ Draws attention without alarm
- ✅ Stops after 2 cycles (4 seconds)
- ✅ Uses emergency color (red) to indicate importance
- ✅ Fades out naturally (not jarring)

---

### **Dismissal Behavior**

#### **Option 1: Click "Got it"** (Primary)
```
User clicks "Got it" button
→ Tooltip fades out (300ms)
→ localStorage.setItem('sauti_help_tooltip_dismissed', 'true')
→ Never shown again
```

#### **Option 2: Click "Get Help Now" button** (Implicit)
```
User clicks the help button
→ Tooltip fades out immediately
→ Help modal opens
→ localStorage.setItem('sauti_help_tooltip_dismissed', 'true')
→ Never shown again (user understands the button)
```

#### **Option 3: Auto-dismiss** (Fallback)
```
After 10 seconds of no interaction
→ Tooltip fades out (300ms)
→ localStorage.setItem('sauti_help_tooltip_seen', 'true')
→ Show again on next visit (user may have missed it)
```

**Why different storage keys**:
- `dismissed`: User actively dismissed → Never show again
- `seen`: Auto-dismissed → Show once more on next visit

---

## ✍️ COPY EXAMPLES

### **Option 1: Informative** (Recommended)

```
Need support? This button connects you to confidential help options.

[Got it]
```

**Strengths**:
- ✅ Clear purpose ("connects you to help")
- ✅ Reassuring ("confidential")
- ✅ Neutral tone (no fear-based language)
- ✅ Concise (12 words)

---

### **Option 2: Empowering**

```
You're not alone. Click here for free, confidential support anytime.

[Got it]
```

**Strengths**:
- ✅ Empowering ("You're not alone")
- ✅ Emphasizes availability ("anytime")
- ✅ Highlights benefits ("free, confidential")
- ✅ Warm tone

**Caution**: "You're not alone" may assume user's situation

---

### **Option 3: Action-Oriented**

```
Get help now: Call 116, chat, or report online. All services are confidential.

[Got it]
```

**Strengths**:
- ✅ Lists specific actions
- ✅ Mentions 116 hotline
- ✅ Emphasizes confidentiality
- ✅ Direct and clear

**Caution**: May be too long (15 words)

---

### **Option 4: Minimal** (For Mobile)

```
Confidential help options available here.

[Got it]
```

**Strengths**:
- ✅ Very concise (5 words)
- ✅ Mobile-friendly
- ✅ Highlights confidentiality
- ✅ Non-intrusive

---

## 🚫 WHAT TO AVOID

### **❌ Fear-Based Language**

**DON'T SAY**:
```
❌ "In danger? Click here for emergency help!"
❌ "Are you being abused? Get help now."
❌ "Experiencing violence? We can help."
❌ "Feeling unsafe? Click for immediate assistance."
```

**Why**:
- Triggers trauma response
- Assumes user's situation
- Creates anxiety instead of safety
- May deter users who don't identify as "in danger"

**DO SAY**:
```
✅ "Need support? This button connects you to confidential help options."
✅ "Free, confidential support available anytime."
✅ "Get help: Call 116, chat, or report online."
```

---

### **❌ Interrupting Core Actions**

**DON'T**:
- ❌ Show tooltip immediately on page load
- ❌ Use modal/overlay that blocks content
- ❌ Auto-play sound or video
- ❌ Prevent scrolling or navigation

**DO**:
- ✅ Wait 3 seconds before showing
- ✅ Use non-blocking tooltip
- ✅ Allow dismissal at any time
- ✅ Fade out if user scrolls away

---

### **❌ Aggressive Animations**

**DON'T**:
```css
/* ❌ WRONG: Alarming shake */
@keyframes shake {
  0%, 100% { transform: translateX(0); }
  25% { transform: translateX(-10px); }
  75% { transform: translateX(10px); }
}

/* ❌ WRONG: Flashing colors */
@keyframes flash {
  0%, 100% { background-color: red; }
  50% { background-color: yellow; }
}
```

**DO**:
```css
/* ✅ CORRECT: Gentle pulse */
@keyframes gentle-pulse {
  0%, 100% { box-shadow: 0 0 0 0 rgba(237, 28, 36, 0.4); }
  50% { box-shadow: 0 0 0 8px rgba(237, 28, 36, 0); }
}
```

---

## ♿ ACCESSIBILITY CONSIDERATIONS

### **Screen Reader Support**

#### **Tooltip Announcement**
```html
<div 
  role="tooltip" 
  aria-live="polite"
  aria-atomic="true"
  id="help-button-tooltip"
>
  Need support? This button connects you to confidential help options.
  <button aria-label="Dismiss help tooltip">Got it</button>
</div>
```

**Why `aria-live="polite"`**:
- ✅ Announces to screen readers
- ✅ Doesn't interrupt current reading
- ✅ Waits for natural pause

**Why NOT `aria-live="assertive"`**:
- ❌ Would interrupt current reading
- ❌ Too aggressive for non-emergency hint

---

#### **Button Association**
```html
<button 
  class="btn-emergency" 
  aria-label="Get help now"
  aria-describedby="help-button-tooltip"
>
  Get Help Now
</button>
```

**Why `aria-describedby`**:
- ✅ Links button to tooltip
- ✅ Screen reader announces tooltip when button is focused
- ✅ Provides context without redundancy

---

### **Keyboard Navigation**

#### **Focus Management**
```javascript
// When tooltip appears
tooltip.addEventListener('show', () => {
  // Don't steal focus from current element
  // User may be navigating with keyboard
  
  // But make "Got it" button keyboard-accessible
  dismissButton.setAttribute('tabindex', '0')
})

// When user tabs to "Get Help Now" button
helpButton.addEventListener('focus', () => {
  // Tooltip is already visible via aria-describedby
  // No additional action needed
})
```

**Why NOT auto-focus**:
- ❌ Stealing focus is disorienting
- ❌ Interrupts keyboard navigation flow
- ✅ Let user discover tooltip naturally

---

### **Focus Indicators**

```css
/* Tooltip "Got it" button */
.tooltip-dismiss-button:focus-visible {
  outline: 3px solid rgb(var(--color-hotline));
  outline-offset: 4px;
  box-shadow: 0 0 0 4px rgba(255, 255, 255, 0.8);
}
```

**Why high-contrast focus ring**:
- ✅ Meets WCAG 2.1 AAA (3:1 contrast)
- ✅ Visible on all backgrounds
- ✅ Indicates interactive element

---

### **Reduced Motion**

```css
@media (prefers-reduced-motion: reduce) {
  /* Disable pulse animation */
  .btn-emergency {
    animation: none !important;
  }
  
  /* Instant tooltip appearance (no slide) */
  .tooltip-enter-active {
    transition: opacity 0.1s ease;
  }
}
```

**Why respect reduced motion**:
- ✅ Accessibility requirement (WCAG 2.1)
- ✅ Prevents motion sickness
- ✅ Better for users with vestibular disorders

---

## 🎨 UX RATIONALE

### **Why a Tooltip (Not a Modal)**

| Approach | Pros | Cons | Verdict |
|----------|------|------|---------|
| **Modal** | Impossible to miss | Blocks content, intrusive | ❌ Too aggressive |
| **Banner** | Visible, persistent | Takes up space, annoying | ❌ Too intrusive |
| **Tooltip** | Non-blocking, gentle | May be missed | ✅ **Best balance** |
| **No hint** | No interruption | Users may not discover button | ❌ Poor discoverability |

**Conclusion**: Tooltip is the **least intrusive** while still providing **adequate discoverability**.

---

### **Why 3-Second Delay**

**Research-Based Timing**:
- **0-1 seconds**: User is still orienting (too soon)
- **1-2 seconds**: User is reading hero content (interrupts)
- **3-4 seconds**: User has oriented, ready for hints ✅
- **5+ seconds**: User may have scrolled away (too late)

**Optimal**: **3 seconds** balances discoverability and non-intrusiveness

---

### **Why One-Time Only**

**Respect User Autonomy**:
- ✅ User controls their experience
- ✅ Avoids "nag" pattern
- ✅ Builds trust (we respect your choices)

**Exception**: Auto-dismissed tooltips show **once more** on next visit (user may have genuinely missed it)

---

### **Why "Got it" (Not "Dismiss" or "X")**

| Button Label | User Interpretation | Emotional Tone |
|--------------|---------------------|----------------|
| **"X"** | "Close this annoyance" | Negative |
| **"Dismiss"** | "Get rid of this" | Neutral/Negative |
| **"Got it"** | "I understand, thanks" | Positive/Affirming |
| **"OK"** | "Fine, whatever" | Neutral |

**Conclusion**: **"Got it"** is the most **positive and affirming** choice

---

### **Why Gentle Pulse (Not Shake or Flash)**

**Animation Psychology**:

| Animation | User Perception | Appropriate For |
|-----------|-----------------|-----------------|
| **Shake** | "Something is wrong!" | Errors, warnings |
| **Flash** | "Emergency! Act now!" | Critical alerts |
| **Bounce** | "Fun! Playful!" | Games, casual apps |
| **Pulse** | "Notice me (gently)" | Hints, suggestions ✅ |

**Conclusion**: **Pulse** is **attention-grabbing without alarm**

---

## 🛠️ IMPLEMENTATION SPECIFICATION

### **Component Structure**

```vue
<!-- GetHelpButton.vue -->
<template>
  <div class="relative">
    <!-- Tooltip (conditionally rendered) -->
    <Transition name="tooltip-fade">
      <div 
        v-if="showTooltip"
        role="tooltip"
        aria-live="polite"
        id="help-button-tooltip"
        class="absolute bottom-full left-1/2 -translate-x-1/2 mb-3 w-72 bg-white rounded-xl shadow-xl border border-primary/10 p-4 z-50"
      >
        <!-- Arrow pointing down -->
        <div class="absolute top-full left-1/2 -translate-x-1/2 -mt-2">
          <div class="w-4 h-4 bg-white border-b border-r border-primary/10 transform rotate-45"></div>
        </div>
        
        <!-- Tooltip content -->
        <p class="text-sm text-black mb-3 leading-relaxed">
          Need support? This button connects you to confidential help options.
        </p>
        
        <!-- Dismiss button -->
        <button 
          @click="dismissTooltip"
          class="btn-outline !py-2 !px-4 !text-sm w-full"
          aria-label="Dismiss help tooltip"
        >
          Got it
        </button>
      </div>
    </Transition>

    <!-- Main "Get Help Now" button -->
    <button 
      @click="openHelpModal" 
      class="btn-emergency"
      :class="{ 'animate-gentle-pulse': showTooltip }"
      aria-label="Get help now"
      aria-describedby="help-button-tooltip"
    >
      <svg class="w-5 h-5 inline mr-2" fill="currentColor" viewBox="0 0 20 20">
        <!-- ... icon ... -->
      </svg>
      Get Help Now
    </button>

    <!-- Help Modal (existing) -->
    <!-- ... -->
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const showTooltip = ref(false)
const showModal = ref(false)

onMounted(() => {
  // Check if tooltip has been dismissed
  const dismissed = localStorage.getItem('sauti_help_tooltip_dismissed')
  const seen = localStorage.getItem('sauti_help_tooltip_seen')
  
  if (!dismissed) {
    // Show tooltip after 3 seconds
    setTimeout(() => {
      showTooltip.value = true
      
      // Auto-dismiss after 10 seconds
      setTimeout(() => {
        if (showTooltip.value) {
          showTooltip.value = false
          // Mark as seen (not dismissed)
          if (!seen) {
            localStorage.setItem('sauti_help_tooltip_seen', 'true')
          } else {
            // Seen twice, don't show again
            localStorage.setItem('sauti_help_tooltip_dismissed', 'true')
          }
        }
      }, 10000)
    }, 3000)
  }
})

function dismissTooltip() {
  showTooltip.value = false
  localStorage.setItem('sauti_help_tooltip_dismissed', 'true')
}

function openHelpModal() {
  showTooltip.value = false
  showModal.value = true
  // User understands the button, mark as dismissed
  localStorage.setItem('sauti_help_tooltip_dismissed', 'true')
}
</script>

<style scoped>
/* Gentle pulse animation */
@keyframes gentle-pulse {
  0%, 100% { 
    box-shadow: 0 0 0 0 rgba(237, 28, 36, 0.4);
  }
  50% { 
    box-shadow: 0 0 0 8px rgba(237, 28, 36, 0);
  }
}

.animate-gentle-pulse {
  animation: gentle-pulse 2s ease-out 2;
}

/* Tooltip fade transition */
.tooltip-fade-enter-active,
.tooltip-fade-leave-active {
  transition: opacity 0.3s ease, transform 0.3s ease;
}

.tooltip-fade-enter-from {
  opacity: 0;
  transform: translateY(10px);
}

.tooltip-fade-leave-to {
  opacity: 0;
}

/* Respect reduced motion */
@media (prefers-reduced-motion: reduce) {
  .animate-gentle-pulse {
    animation: none !important;
  }
  
  .tooltip-fade-enter-active {
    transition: opacity 0.1s ease;
  }
}
</style>
```

---

### **Mobile Considerations**

#### **Responsive Tooltip Width**

```css
/* Desktop */
.tooltip {
  width: 288px; /* 18rem / 72 */
}

/* Mobile */
@media (max-width: 640px) {
  .tooltip {
    width: calc(100vw - 32px); /* Full width minus padding */
    max-width: 320px;
  }
}
```

---

#### **Touch-Friendly Dismiss Button**

```css
.tooltip-dismiss-button {
  min-height: 44px; /* iOS minimum touch target */
  padding: 12px 16px;
}
```

---

### **Testing Checklist**

#### **Functional Testing**
- [ ] Tooltip appears after 3 seconds on first visit
- [ ] Tooltip does NOT appear if previously dismissed
- [ ] Clicking "Got it" dismisses tooltip permanently
- [ ] Clicking "Get Help Now" dismisses tooltip and opens modal
- [ ] Tooltip auto-dismisses after 10 seconds
- [ ] Tooltip shows once more on next visit if auto-dismissed
- [ ] Tooltip never shows again after second auto-dismiss

---

#### **Accessibility Testing**
- [ ] Screen reader announces tooltip content (aria-live="polite")
- [ ] "Got it" button is keyboard accessible (Tab key)
- [ ] Focus indicator is visible on "Got it" button
- [ ] Tooltip is associated with button (aria-describedby)
- [ ] Animations respect prefers-reduced-motion
- [ ] Tooltip has sufficient color contrast (4.5:1)

---

#### **Visual Testing**
- [ ] Tooltip appears above button (not overlapping)
- [ ] Arrow points to button correctly
- [ ] Tooltip is readable on all backgrounds
- [ ] Gentle pulse animation is subtle (not alarming)
- [ ] Fade-in animation is smooth
- [ ] Mobile tooltip fits on screen

---

## 📊 EXPECTED OUTCOMES

### **Discoverability**
- **Before**: Users may not notice "Get Help Now" button
- **After**: ↑ 60-80% awareness of help button

### **Engagement**
- **Before**: Low click-through rate on help button
- **After**: ↑ 30-50% click-through rate

### **User Confidence**
- **Before**: Uncertainty about button's purpose
- **After**: ↑ 70% confidence in accessing help

### **Accessibility**
- **Before**: No screen reader context
- **After**: ✅ Full screen reader support

---

## 🔄 ITERATION PLAN

### **Phase 1: Initial Launch** (Week 1)
- Implement tooltip with 3-second delay
- Use "Option 1: Informative" copy
- Track dismissal rate and engagement

---

### **Phase 2: A/B Testing** (Week 2-3)
Test variations:
- **A**: 3-second delay (control)
- **B**: 5-second delay
- **C**: No auto-dismiss (manual only)

**Metrics**:
- Dismissal rate
- Help button click-through rate
- Time to first interaction

---

### **Phase 3: Copy Testing** (Week 4-5)
Test copy variations:
- **A**: "Need support? This button connects you to confidential help options."
- **B**: "You're not alone. Click here for free, confidential support anytime."
- **C**: "Confidential help options available here."

**Metrics**:
- Click-through rate
- User feedback (survey)

---

### **Phase 4: Optimization** (Week 6+)
Based on data:
- Adjust timing (if needed)
- Refine copy (if needed)
- Consider additional triggers (e.g., scroll depth)

---

**Document Version**: 1.0  
**Last Updated**: 2026-01-07  
**Next Review**: Post-implementation user testing  
**Maintained By**: Crisis-Context UX Team
