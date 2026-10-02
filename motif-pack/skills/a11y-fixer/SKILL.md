---
name: a11y-fixer
description: Find and directly fix accessibility issues in HTML, JSX/TSX, Vue or Svelte code against WCAG 2.2 AA (contrast, semantics, landmarks, headings, labels, focus management, keyboard support, ARIA, target size, motion, alt text, forms, modals, menus), then report every change with the success criterion it satisfies. Use when the user asks to make something accessible, fix a11y, pass an accessibility audit, support screen readers or keyboard users, or prepare for WCAG/ADA/EAA compliance.
license: Commercial. See LICENSE.txt
---

# A11y Fixer

Fix first, explain second. The goal is working, accessible code, not a lecture.

## 1. Scan

Read the files and check each area. Run available tooling if the project has it (`axe`, `eslint-plugin-jsx-a11y`, `pa11y`, Lighthouse); otherwise inspect manually.

| Area | Check | WCAG |
|------|-------|------|
| Contrast | text ≥ 4.5:1 (large ≥ 3:1), UI components & focus indicators ≥ 3:1 | 1.4.3, 1.4.11 |
| Semantics | real `<button>`/`<a>`, lists, tables with headers, one `<h1>`, no skipped heading levels | 1.3.1, 2.4.6 |
| Landmarks | `header`, `nav`, `main`, `footer`; skip link to main | 1.3.1, 2.4.1 |
| Images | meaningful `alt`; decorative `alt=""`; SVG icons `aria-hidden` + labelled parent | 1.1.1 |
| Forms | visible `<label for>`, grouped radios in `fieldset/legend`, errors linked with `aria-describedby`, `autocomplete` | 1.3.5, 3.3.1–3.3.3 |
| Keyboard | everything operable by keyboard, logical tab order, no traps, no positive `tabindex` | 2.1.1, 2.4.3 |
| Focus | visible `:focus-visible` style, not obscured by sticky headers | 2.4.7, 2.4.11 |
| Dialogs | focus moves in, trapped, `Esc` closes, focus returns to trigger, `aria-modal`, labelled | 2.4.3, 4.1.2 |
| Menus / tabs / accordions | correct ARIA pattern + arrow-key support (per ARIA APG) | 4.1.2 |
| Dynamic updates | `aria-live` for toasts, errors, async results | 4.1.3 |
| Target size | ≥ 24×24px (aim 44×44 on touch) | 2.5.8 |
| Motion | `prefers-reduced-motion` respected; no auto-playing motion > 5s without pause | 2.2.2, 2.3.3 |
| Language & titles | `lang` on `<html>`, unique `<title>` per page | 3.1.1, 2.4.2 |
| Reflow & zoom | usable at 320px width and 200% text zoom | 1.4.10, 1.4.4 |

## 2. Fix

- Edit the code directly with minimal, idiomatic changes. Prefer native HTML over ARIA ("no ARIA is better than bad ARIA").
- When a color must change, pick the closest on-brand color that passes, and show old → new with ratios.
- Add small reusable utilities where they help (`.sr-only`, a focus-trap hook, a `VisuallyHidden` component).
- Never remove functionality or visual design without saying so.

## 3. Report

Return:

1. **Summary**: issues found / fixed / needs human decision.
2. **Change log table**: File:line · Issue · Fix · WCAG SC · Severity (Critical / Serious / Moderate / Minor).
3. **Needs human input**: e.g. alt text that requires content knowledge, captions for video, color choices affecting brand.
4. **Manual test script**: 5-minute keyboard + screen-reader (VoiceOver/NVDA) walkthrough for the changed flows.

Note: automated checks catch only part of WCAG issues. Always recommend a manual screen-reader pass before claiming compliance.
