---
name: form-ux-optimizer
description: Audit and rebuild web and mobile forms for higher completion: field reduction, layout, labels, input types, autofill, validation timing, error recovery, multi-step flows, checkout and sign-up patterns, and accessibility. Use when the user shares a form, checkout, sign-up, booking, survey, onboarding questionnaire or settings form, or says users abandon a form, or asks to improve conversion of a form.
license: Commercial. See LICENSE.txt
---

# Form UX Optimizer

Every field is a cost. The best form asks for the least, in the right order, and recovers gracefully from mistakes.

## 1. Field inventory

List every field in a table:

| Field | Required? | Why we need it | Can we infer / defer / remove? | Input type | autocomplete |
|-------|-----------|----------------|--------------------------------|------------|--------------|

Then apply cuts: remove unneeded fields, defer to later (profile completion), infer (city from postal code, card type from number), or merge (single "Full name" unless the locale needs split names).

## 2. Layout rules

- Single column. Exception: short related pairs (City + Postal code, Expiry + CVC).
- Labels above inputs, always visible. Placeholders only for format examples.
- Group related fields with headings; ≤ 7 fields per group/step.
- Field width hints at expected length (postal code short, address long).
- Primary action left-aligned under the last field, labelled with the outcome ("Create account", "Pay $49").
- Mark optional fields "(optional)" instead of asterisks on required ones when most are required.

## 3. Input correctness (checklist)

- `type`: email, tel, url, number (only for true quantities), date where appropriate.
- `inputmode` for numeric codes (`inputmode="numeric"` for card, OTP, postal).
- `autocomplete` tokens: name, email, tel, street-address, address-line1, postal-code, country, cc-number, cc-exp, cc-csc, one-time-code, new-password, current-password.
- Don't block paste. Don't split phone numbers or dates into multiple inputs (OTP excepted, with paste support).
- Sensible defaults (country from locale), but never pre-check marketing consent.

## 4. Validation & errors

- Validate on blur; re-validate on input only after a field has shown an error.
- Error text below the field, tied with `aria-describedby`, starting with what to do: "Enter a 5-digit ZIP code".
- On submit with errors: focus the first invalid field, show an error summary at top with anchor links (for long forms).
- Preserve all entered data on error or back navigation. Never clear passwords silently without saying so.
- Server errors are mapped to the right field when possible.

## 5. Multi-step flows

- Use steps when > ~10 fields or logically distinct phases. Show a progress indicator with step names.
- Easiest questions first; commitment-heavy ones (payment) last.
- Back button that keeps data; save progress for long forms.
- Review step before irreversible submits.

## 6. Output

1. **Audit**: findings table (Issue · Impact · Fix) prioritized P0–P2, plus the field inventory with proposed cuts and the estimated field reduction ("14 → 8 fields").
2. **Rebuilt form**: code in the user's stack with all the above, including loading, success and error states.
3. **Measurement plan**: events to track (start, field-level drop-off, error rate per field, completion time, completion rate).
