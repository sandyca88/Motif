---
name: dashboard-architect
description: Design and build clear, decision-focused dashboards and admin/analytics screens — from choosing KPIs and chart types to layout, filters, empty/loading states and responsive behavior. Use when the user asks for a dashboard, admin panel, analytics page, KPI view, reporting screen, internal tool, or wants to "visualize this data" in an app UI.
license: Commercial — see LICENSE.txt
---

# Dashboard Architect

Most dashboards fail because they show everything. A good dashboard answers 3–5 questions for one audience, fast.

## 1. Frame it (before any layout)

Establish, from the request or by asking at most one question:

1. **Audience** — exec, operator, analyst, or customer?
2. **Top questions** — list 3–5 questions the screen must answer ("Are we on track for revenue this month?").
3. **Cadence** — glanced at live, daily, or weekly?

State these back in a short "Dashboard brief" block before building.

## 2. Map questions → components

| Question type | Component |
|---------------|-----------|
| "How are we doing right now?" | KPI tile: value, delta vs. previous period, sparkline, target |
| Trend over time | Line chart (≤ 4 series) or area for cumulative |
| Compare categories | Horizontal bar, sorted descending |
| Part of whole | Stacked bar or 100% bar. Donut only if ≤ 4 slices |
| Distribution | Histogram / box plot |
| Correlation | Scatter |
| "What needs my attention?" | Alert list / table with status badges, sorted by urgency |
| Detail lookup | Data table with search, sort, sticky header, row actions |

Never use: 3D charts, pie with > 5 slices, dual y-axes (split into two charts instead), gauges for non-bounded metrics.

## 3. Layout

- **F-pattern**: most important KPI top-left. Row 1 = 3–5 KPI tiles. Row 2 = primary trend chart (spans 8/12) + breakdown (4/12). Row 3 = actionable table.
- 12-col grid, 16–24px gutters, cards with consistent internal padding (20–24px).
- Global filters (date range, segment) in a sticky toolbar top-right; show active filters as removable chips.
- Sidebar nav 240px, collapsible to 64px icons; highlight the current route.
- Density toggle (comfortable / compact) for operator dashboards.

## 4. Data-viz styling

- One accent color for the "hero" series; others in neutral greys. Use semantic colors only for meaning (up/down, status).
- Deltas: green ▲ / red ▼, but always also show the sign and % (color-blind safe).
- Gridlines faint (6–10% alpha), no chart borders, axis labels 12px muted, direct labels over legends when possible.
- Numbers: `tabular-nums`, abbreviate (12.4k, $1.2M), consistent decimals per metric.
- Tooltips show the exact value, date and comparison.

## 5. States (required)

Build all of these, not just the happy path:

- **Loading** — skeletons that match final layout (no spinners on whole page).
- **Empty** — explain why it's empty and give the next action ("Connect a data source").
- **Error** — what failed + retry button; keep other widgets working.
- **Partial / stale data** — "Updated 12 min ago" timestamp on each widget.

## 6. Build

- Default stack if unspecified: React + Tailwind + Recharts (or Chart.js for plain HTML). Use realistic mock data with believable seasonality, not random noise.
- Responsive: tiles become a 2-col grid on tablet, horizontal scroll carousel on mobile; tables become stacked cards < 640px.
- Dark and light theme via CSS variables.
- Accessibility: charts have an accessible summary (`aria-label` / visually hidden table), keyboard-reachable filters, 3:1 contrast for chart lines against background.

## 7. Deliver

Return: the dashboard brief, the code, and a short "Next iterations" list (e.g., drill-down views, saved filters, alerts).
