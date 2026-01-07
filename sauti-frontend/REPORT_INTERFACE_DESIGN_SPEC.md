# SAUTI 116: REPORT A CASE - INTERFACE DESIGN SPECIFICATION

**Version**: 1.0  
**Status**: APPROVED FOR IMPLEMENTATION  
**Type**: SAFETY-CRITICAL / GOVERNMENT-ADJACENT

---

## 1. VISUAL VISUAL PRINCIPLES
The design prioritizes **Clarity, Stability, and Speed**. The interface must behave less like a "friend" (chatbot) and more like a **digital intake officer**—efficient, non-judgmental, and secure.

*   **Principle 1: Radical Neutrality**  
    The interface has no "personality." It does not try to comfort via cute graphics; it comforts via *competence* and *predictability*.
*   **Principle 2: High Contrast & Legibility**  
    Safety information must never be ambiguous. All text is #000000. All active elements are clearly bordered.
*   **Principle 3: The "Ledger" Metaphor**  
    Instead of floating "chat bubbles," the UI acts as a **Progressive Ledger**. It feels like a digital form that reveals itself one question at a time. History is static; the current step is active.

---

## 2. VISUAL METAPHOR: "THE PROGRESSIVE LEDGER"

### Concept
The interface resembles a clean, reliable paper logbook shifting into a digital state. 
- **No Avatar**: Who is speaking? The "Service."
- **No Orientation**: Questions and Answers are **Left-Aligned**. This removes the "back-and-forth" chat tennis match feel and replaces it with a linear "filling out a record" feel.
- **History**: Past answers become static "entries" in the ledger.

---

## 3. LAYOUT SYSTEM

### Container & Grid
*   **Max-Width**: `640px` (Optimal reading length).
*   **Alignment**: Left-aligned content. Centered container on viewport.
*   **Background**: White (`#FFFFFF`).
*   **Padding**: `24px` (Mobile), `48px` (Desktop).

### Vertical Rhythm (Spacing)
*   **Between Q&A Pairs**: `48px` (Distinct separation).
*   **Between Question & Input**: `16px`.
*   **Between Input & Action**: `24px`.

### Mobile vs Desktop
*   **Mobile**: Full width. Inputs are `48px` height (min).
*   **Desktop**: Centered column. Inputs are `56px` height.

---

## 4. MESSAGE & CONTAINER DESIGN
*Strict rule: No speech bubbles.*

### The Question (System)
*   **Typography**: `Roboto Sans`, **Bold**, 18px (Mobile) / 20px (Desktop).
*   **Color**: `#000000`.
*   **Shape**: Text block. No container.
*   **Iconography**: None.

### The Answer (User - History State)
*   **Typography**: `Roboto Sans`, Regular, 16px.
*   **Color**: `#000000`.
*   **Styling**: 
    *   **Border-Left**: 4px solid **Blue**.
    *   **Padding-Left**: 16px.
    *   **Background**: None (High contrast).
*   **Editability**: A small, text-only "Edit" link (Underlined, Blue) appears on hover/focus.

---

## 5. USER RESPONSE COMPONENTS

### Input Fields (Text)
*   **Shape**: Rectangular. `4px` border radius (Subtle).
*   **Border**: `2px` solid **Black** (Default). `2px` solid **Blue** (Focus).
*   **Background**: White.
*   **Text**: `#000000`.
*   **Placeholder**: `#000000` (Opacity 60%).

### Choice Buttons (Options)
*   **Layout**: Stacked vertical list (never horizontal scroll).
*   **Shape**: Rectangular. `4px` border radius.
*   **State - Default**: 
    *   Border: `2px` solid **Black**.
    *   Text: **Black**, Bold.
    *   Background: White.
*   **State - Hover/Focus**:
    *   Border: `2px` solid **Blue**.
    *   Background: **Blue** (10% tint if possible, otherwise White).
    *   Text: **Black**.
*   **State - Selected**:
    *   Background: **Blue**.
    *   Text: White.
    *   Border: **Blue**.
    *   *Icon*: Checkmark (White) on the right.

---

## 6. PROGRESS FEEDBACK

### Step Indicator
*   **Placement**: Top Left (Sticky).
*   **Style**: Plain Text. `Step 1 of 5`.
*   **Typography**: `Roboto Sans`, Bold, 12px, **Black**.
*   **Visual Bar**: None. The text is sufficient and calm.

### Loading State
*   **No Typography** ("Typing...").
*   **Visual**: A simple, non-animating status text: "Processing..." appearing in **Green** text.
*   **Transition**: Instant replacement.

---

## 7. MICRO-INTERACTIONS

### Entrance
*   **Motion**: Fade In + Slide Up (`10px`).
*   **Timing**: `200ms` (Fast, efficient).
*   **Ease**: `ease-out`.
*   **Typing Effect**: **BANNED**. Text appears instantly.

### Scrolling
*   **Behavior**: When a new question appears, the page smoothly scrolls to place the new question at the **optical center** of the screen, not the bottom.

---

## 8. ERROR & VALIDATION STATES

### Visual Tone
Errors are helpful signposts, not alarms.

### Design
*   **Color**: **Red**.
*   **Icon**: Simple "!" in a circle.
*   **Border**: Input border turns **Red** (`2px`).
*   **Message**: 
    *   Placed *below* the input.
    *   `Roboto Sans`, Bold, 14px.
    *   Text: **Red**.

---

## 9. COLOR APPLICATION MAP (STRICT)

| UI Element | Color Name | Hex Code (Approx) | Role |
| :--- | :--- | :--- | :--- |
| **Background** | White | `#FFFFFF` | Canvas |
| **Body Text** | Black | `#000000` | Legibility |
| **Primary Action** | Sauti Blue | `#005691`* | Buttons, Selected States, Focus |
| **Secondary Action** | Sauti Green | `#006837`* | Success messages, "Safe" indicators |
| **Borders** | Black | `#000000` | Inputs, Cards (Unselected) |
| **Errors** | Emergency Red | `#D32F2F`* | Validation |
| **Separators** | Light Gray | `#E0E0E0` | Section breaks |

*(Note: Use exact brand hex codes where mapped: Sauti Sky Blue or Trust Blue for 'Sauti Blue')*

---

## 10. ACCESSIBILITY VISUAL RULES
1.  **Focus States**: **Double Border** or **Thick Blue Outline** (`3px`) on all interactive elements.
2.  **Touch Targets**: Minimum `48px` height for all buttons and inputs.
3.  **Contrast**: All text is Black on White (Ratio 21:1). Button text is White on Dark Blue (Ratio > 4.5:1).
4.  **No reliance on color**: Selected states use both Color change and Icon (Checkmark).

---

## 11. FRONTEND IMPLEMENTATION NOTES (Vue.js)

1.  **Remove Avatars**: Delete all `<img src="avatar">` or icon containers next to messages.
2.  **Remove Chat Bubbles**: Remove `bg-gray-100`, `rounded-2xl`, `rounded-tl-none` classes.
3.  **Refactor Layout**: 
    *   Use a single vertical stack layout. 
    *   `v-for` loop should render "CompletedEntry" component (static) vs "CurrentStep" component (active).
4.  **Fonts**: Force `font-family: 'Roboto', sans-serif;` on the reporting container.
5.  **Icons**: Remove emoji icons from the category selection. Use simple SVG icons (outline style) or no icons.

---
**DESIGN COMPLETE.**
