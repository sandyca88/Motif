---
name: onboarding-flow-designer
description: Design user onboarding that drives activation — sign-up, first-run experience, setup checklists, product tours, empty states and activation emails — and optionally build the screens. Use when the user asks about onboarding, first-time user experience (FTUE), sign-up flow, activation, "users drop off after sign up", welcome screens, setup wizards or product tours.
license: Commercial — see LICENSE.txt
---

# Onboarding Flow Designer

Onboarding is not a tour; it is the shortest path to the user's first real success (the "aha moment").

## 1. Define activation

Ask or infer:

- **Product & user type** (e.g., B2B analytics tool for marketing managers).
- **Aha moment** — the first moment of real value (e.g., "sees their first report with their own data").
- **Activation event** — a measurable action that predicts retention (e.g., "connected 1 data source and viewed a report within 24h").

Write these three lines in an "Activation brief" before designing.

## 2. Map the current and ideal path

Produce a step table:

| Step | Screen / touchpoint | User goal | Required? | Friction risk | Fix |
|------|---------------------|-----------|-----------|---------------|-----|

Then cut: every step that is not required for the aha moment gets deferred, made optional, or auto-filled. Target ≤ 5 steps from sign-up to aha.

## 3. Pattern toolkit (pick what fits)

- **Sign-up**: SSO first (Google/Microsoft/GitHub), email as fallback; ask only for email + password; defer profile questions.
- **Welcome survey**: max 3 questions, each one must change what the user sees next (personalization), show progress.
- **Templates / sample data**: let users experience value before doing setup work.
- **Setup checklist**: 3–5 items, first item pre-completed ("Create account ✓") for momentum, progress bar, dismissible, persists across sessions.
- **Contextual tips**: triggered by user action, never a 7-step forced tour. One tip per screen, always skippable.
- **Empty states**: headline explaining the value + one primary action + optional "see an example". Never a blank table.
- **Celebrate**: light, brief success moment at the aha event, then the next suggested step.
- **Re-engagement**: 3-email sequence (Day 0 welcome + single CTA, Day 2 help on the stuck step, Day 5 social proof/use case).

## 4. Writing rules

- Speak in the user's outcome, not your features ("See which campaigns make money" vs. "Explore analytics").
- Buttons say what happens next ("Connect Google Ads").
- Every screen answers: Where am I? What do I do? Why should I?

## 5. Deliverables

Return, in order:

1. Activation brief
2. Ideal flow table + a Mermaid flowchart of the path (include skip/error branches)
3. Screen-by-screen spec: purpose, content, primary/secondary action, copy
4. Metrics to track: sign-up conversion, time-to-aha, activation rate, checklist completion, Day-7 retention
5. If asked (or if the user is building), implement the screens in their stack, including loading/error states and a persisted checklist component

## Quality bar

- No step exists "because we need the data" without a reason for the user.
- Every optional step has a visible skip.
- Mobile flow tested at 375px; inputs use correct `type` and `autocomplete`.
