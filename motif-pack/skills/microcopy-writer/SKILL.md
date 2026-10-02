---
name: microcopy-writer
description: Write and rewrite interface text — buttons, CTAs, form labels, helper text, error messages, empty states, tooltips, confirmation dialogs, notifications and onboarding copy — in a consistent product voice. Use when the user asks "what should this button say", wants UX copy, UX writing, error messages, empty state text, or asks to improve the wording of any UI.
license: Commercial — see LICENSE.txt
---

# Microcopy Writer

Good microcopy is clear first, concise second, and on-brand third.

## 1. Establish the voice (once per project)

If no voice guide exists, infer one from the product and state it as 3 traits with "this, not that":

> Confident, not cocky · Plain, not dumbed-down · Warm, not cute

Save it to the conversation and reuse it for every string.

## 2. Rules by component

**Buttons / CTAs**
- Verb + object, describing the outcome: "Create project", "Send invoice", "Start free trial".
- Never "Submit", "OK", "Click here". Max ~3 words.
- Destructive actions name the thing: "Delete 3 files", not "Confirm".

**Form labels & help**
- Labels are nouns, always visible (no placeholder-only labels).
- Helper text explains format or why you're asking ("We'll only use this for receipts").
- Mark optional fields, not required ones, when most are required.

**Errors** — formula: *what happened + how to fix it*, no blame.
- ✗ "Invalid input" → ✓ "Enter a date in DD/MM/YYYY format"
- ✗ "Error 500" → ✓ "We couldn't save your changes. Check your connection and try again."

**Empty states** — formula: *what goes here + why it's useful + one action*.
- "No projects yet. Projects keep your files and team in one place. **Create project**"

**Confirmation dialogs**
- Title asks the specific question: "Delete 'Q3 Report'?"
- Body states the consequence: "This can't be undone. Shared links will stop working."
- Buttons: "Delete report" / "Cancel".

**Success & notifications**
- Say what happened and what's next: "Invoice sent to Dana. We'll notify you when it's paid."
- Toasts ≤ 1 line; include Undo when possible.

**Tooltips** — only for non-obvious things; ≤ 1 sentence; never hide required info.

## 3. Mechanics

- Sentence case everywhere except proper nouns.
- Numerals for numbers ("3 files"), contractions OK unless voice is formal.
- Avoid jargon, double negatives, and "please" overuse.
- Keep strings translation-friendly: no concatenated fragments, allow ~30% expansion.

## 4. Output format

For rewrites, return a table:

| Location | Current | Suggested | Why |
|----------|---------|-----------|-----|

For new copy, provide 2–3 options per key string (e.g., hero CTA) labelled by tone, then recommend one.

If the user shares code, offer to apply the strings directly or export them as a JSON/i18n file.
