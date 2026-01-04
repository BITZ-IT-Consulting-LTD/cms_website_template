# SAUTI 116 - Brand Compliance Checklist

This document provides a checklist for developers and designers to ensure all new and existing work on the SAUTI 116 website complies with the official brand guidelines.

## 1. Colour

- [x] **Use Only Approved Colours:** All colours used must be from the official brand palette.
  - `blue`: `#007BBF` (Trust, authority, headers)
  - `yellow`: `#FFF200` (Awareness, highlights)
  - `orange`: `#FF9933` (Action, response, secondary CTAs)
  - `darkGreen`: `#006633` (Protection, seriousness)
  - `lightGreen`: `#8CC63F` (Care, healing, community support)
  - `red`: `#ED1C24` (Emergency, violence reporting, primary CTA)
  - `black`: `#000000`
  - `white`: `#FFFFFF`

- [x] **Use Tailwind CSS Variables:** All colours must be applied using the `*` utility classes defined in `tailwind.config.js` (e.g., `bg-blue`, `text-red`).

- [ ] **No Hardcoded Colours:** There must be no hardcoded hex codes, RGB values, or other color definitions in the codebase.

- [x] **No Gradients:** Gradients are not permitted. Use solid colours only.

## 2. Typography

- [x] **Primary Typeface:** The primary typeface for all body text and most headings is **Cronos Pro**. This is applied via the `font-sans` utility class.

- [ ] **Campaign Headers:** **Helvetica Neue (Bold / Condensed Black)** may be used for special campaign headers. This is applied via the `font-display` utility class.

- [x] **Font Files:** The official font files (`.woff2` format) must be present in the `frontend/src/assets/fonts/` directory.

- [ ] **Consistent Hierarchy:** Use a consistent and clear type scale for headings and paragraphs. Do not manually set font sizes with hardcoded values.

## 3. Logo

- [x] **Use Official Logo:** Only the official SAUTI 116 master logo files must be used. The logo should be loaded dynamically from the CMS.

- [ ] **No Improvised Logos:** Do not create or use any improvised logos, such as text-based fallbacks or single-letter representations.

- [ ] **No Stretching or Distortion:** The logo must always be displayed at its correct aspect ratio. Use `object-contain` where necessary.

- [ ] **Favicon:** The site favicon must be a simplified, on-brand version of the official logo.

## 4. Messaging & Tone of Voice

- [x] **Action-Oriented:** Copy should be direct and encourage action (e.g., "Report Violence," "Call 116").

- [x] **Compassionate:** Language should be warm, supportive, and empathetic.

- [x] **Clear and Authoritative:** Messaging should be easy to understand and convey the authority of a national helpline.

- [x] **Core CTA:** The primary call to action, "Report any form of violence. Call 116," should be reinforced consistently.

## 5. Imagery & Visual Style

- [x] **Use Real Imagery:** All images should be of real people, places, and situations in Uganda.

- [ ] **No Stock Photography:** Do not use staged, generic, or decorative stock photography. Placeholder services like `picsum.photos` are strictly forbidden.

- [ ] **Harmonious Overlays:** Any color overlays on images must use colors from the approved brand palette.

## 6. Layout & UI Consistency

- [x] **Consistent Spacing:** Use the spacing scale defined in Tailwind for consistent margins, paddings, and gaps.

- [x] **Consistent Components:** Reuse common components like buttons (`BaseCTA`) and ensure they are styled consistently across the site.

- [ ] **Dominant "116":** The number "116" should be visually dominant in emergency contexts.
