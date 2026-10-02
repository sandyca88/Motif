---
name: design-system-starter
description: Generate a starter design system from a brand color, font or reference: color ramps, semantic tokens (light and dark), type scale, spacing, radius, elevation and motion tokens, plus core components (button, input, select, checkbox, card, badge, modal, toast, table) with every state documented. Outputs CSS variables, a Tailwind config, tokens JSON and a living style-guide page. Use when the user asks for a design system, design tokens, theme, style guide, component library foundations or "make my UI consistent".
license: Commercial. See LICENSE.txt
---

# Design System Starter

Turn a few brand inputs into a coherent, documented system the agent (and the team) can build with.

## 1. Inputs

Ask for or infer: primary brand color(s), font preference, product type (marketing / SaaS app / mobile), density (comfortable / compact), and whether dark mode is required (default: yes). If the user has an existing site, extract its current values first and note inconsistencies.

## 2. Foundations

**Color**
- Build a 50–950 ramp (11 steps) for primary and neutral using perceptual (OKLCH) lightness steps; keep hue steady and taper chroma at the ends.
- Add success, warning, danger and info ramps (5 steps each is enough).
- Map to **semantic tokens**; components use ONLY these:
  `--bg`, `--bg-subtle`, `--surface`, `--surface-raised`, `--border`, `--border-strong`, `--text`, `--text-muted`, `--text-inverse`, `--primary`, `--primary-hover`, `--primary-text`, `--focus-ring`, `--danger`, `--success`, `--warning`.
- Provide light and dark values. Verify contrast: text on bg ≥ 4.5:1, muted text ≥ 4.5:1, borders/UI ≥ 3:1. Print a contrast table.

**Type**: scale ratio 1.2 (app) or 1.25–1.333 (marketing). Tokens `--text-xs … --text-5xl` with paired line-heights and tracking. Max 2 families; weights 400/500/600/700.

**Spacing**: 4px base: 0, 1(4), 2(8), 3(12), 4(16), 5(20), 6(24), 8(32), 10(40), 12(48), 16(64), 20(80), 24(96).

**Radius**: `--radius-sm` (controls), `--radius-md` (cards), `--radius-lg` (modals), `--radius-full`.

**Elevation**: 3 levels of layered shadows for light mode; in dark mode use surface lightness + border instead of heavy shadows.

**Motion**: `--dur-fast 120ms`, `--dur-base 200ms`, `--dur-slow 350ms`; `--ease-out cubic-bezier(.2,.8,.2,1)`; reduced-motion rules.

## 3. Components

For each component, document: anatomy, sizes (sm/md/lg), variants, and **all states**: default, hover, focus-visible, active, disabled, loading, error (where relevant). Include do/don't notes and accessibility requirements.

Core set: Button (primary, secondary, ghost, destructive, icon-only), Input (with label, hint, error, prefix/suffix), Select, Checkbox, Radio, Switch, Textarea, Card, Badge, Avatar, Tabs, Tooltip, Modal/Dialog, Toast, Table, Empty state, Skeleton.

## 4. Deliverables

1. `tokens.css`: `:root` + `[data-theme="dark"]` variables.
2. `tailwind.config.js` theme extension mapped to the variables (if Tailwind is used).
3. `tokens.json`: W3C design-tokens format (`$value`, `$type`) for Figma/Tokens Studio.
4. `components/`: implementations in the user's stack (default: plain HTML/CSS + vanilla JS, or React if the project uses it).
5. `styleguide.html`: a living style guide showing every token (swatches with hex + contrast), type specimens, spacing scale, and every component in every state, with a theme toggle.
6. `DESIGN.md`: short rules an AI agent should follow when building with this system (tokens only, no hardcoded hex, spacing from scale, which component to use when).

## Quality bar

- No hardcoded colors or pixel values inside components, only tokens.
- Every interactive component has a visible `:focus-visible` style using `--focus-ring`.
- Dark mode is designed, not inverted: check each semantic token separately.
