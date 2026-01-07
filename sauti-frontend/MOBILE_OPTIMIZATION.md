# Sauti 116 Mobile-First & Low-Bandwidth Strategy

To ensure Sauti 116 is accessible to all Ugandans, including those on legacy mobile hardware and low-bandwidth EDGE/3G networks, we adhere to the following optimization principles.

## 1. Core Mobile UX Principles
- **Thumb-Confidence**: All interactive elements (buttons, links) must have a minimum height of **52px** to account for the "shaky hand" or "distressed user" context.
- **Priority Loading**: Crucial text and emergency action buttons (Call 116) must render before any decorative content.
- **Cognitive Ease**: Use single-column layouts on mobile to reduce visual scanning effort. Never hide critical information behind "hover" states.
- **Input Optimization**: Use appropriate HTML5 input types (`tel`, `email`, `number`) to trigger the correct mobile keyboards automatically.

## 2. Component-Specific Redesigns
### The "Flash" Header
- **Dynamic Action**: On mobile, the header collapses to show only the Sauti Logo and a high-contrast "CALL 116" bubble.
- **Menu Efficiency**: The mobile menu uses a "full-screen takeover" with extra-large vertical links to prevent mis-taps.

### The "Step-by-Step" Reporting Form
- **Narrative First**: Instead of a complex long-form, reports are handled via a chat-like interface that saves progress on every message.
- **Zero-Deadweight**: We avoid heavy date pickers or file uploaders unless explicitly required for the case.

### Hero Section Optimization
- **CSS Over Images**: We use brand-colored gradients and CSS-based patterns for backgrounds rather than high-resolution hero images to save 200KB+ per page load.
- **Content Visibility**: We use the `content-visibility: auto` CSS property to postpone the rendering of sections that are below the fold.

## 3. Performance Improvement Checklist
- [x] **WebP Conversions**: All images must be in WebP format (typically 30% smaller than JPEG).
- [x] **Reduced Motion**: Respect the `prefers-reduced-motion` browser setting to save battery and reduce CPU strain on older Android/iOS devices.
- [x] **Font Optimization**: We use standard system fonts as fallbacks for the 'Roboto' brand font to ensure text is readable immediately while the custom font loads.
- [x] **Lazy Loading**: Native `loading="lazy"` attribute applied to all images below the hero section.

---
**Goal**: Sub-2s initial load time on 3G (East Africa standard) and 100% functional parity on devices with 2GB RAM.
