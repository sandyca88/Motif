# Launch Motif with PayPal (about 30–45 minutes, $0)

**Live site:** https://sunny-crumble-7de34c.netlify.app (Netlify project: sunny-crumble-7de34c). To update it, open the project's Deploys page and drop a new `motif-site.zip`.

## What's in the launch kit

- `motif-site/`: **the public website.** Upload this folder. It contains only free downloads; Pro files are NOT in it.
- `motif-pack/dist/motif-pro-bundle.zip`: **private.** Never upload this to the website. Share it only by private link to buyers.
- `motif-pack/`: your source files (skills, prompts, build scripts). Keep this safe.

---

## Step 1: Set up PayPal (10 min)

1. Log in to PayPal with **sandyca88@yahoo.com**.
2. Upgrade to a **Business account** (free): Settings → Account type → Upgrade. This avoids selling limits on personal accounts and lets buyers pay by card without a PayPal account.
3. Make sure your email is **confirmed** and a bank account is linked for withdrawals.
4. Optional: turn on **email notifications for payments received** (you'll use these to deliver files).

## Step 2: Put the Pro bundle somewhere private (5 min)

1. Upload `motif-pack/dist/motif-pro-bundle.zip` to Google Drive (or Dropbox).
2. Set sharing to **"Anyone with the link"**, then copy the link.
3. Paste that link into the delivery email template below.
4. When you add new items later, replace the file in Drive (same link keeps working).

## Step 3: Put the site online (5–10 min, free)

**Easiest: Netlify Drop**
1. Go to app.netlify.com/drop and create a free account.
2. Drag the whole **`motif-site`** folder onto the page.
3. You get a live URL like `https://random-name.netlify.app`. Rename it in Site settings (e.g. `motif-ux.netlify.app`).

Alternatives: Vercel, Cloudflare Pages or GitHub Pages. All free.

Optional later: buy a domain (e.g. motif.design) and connect it in Netlify → Domain settings.

## Step 4: Test a real payment (5 min)

1. Open your live site → Pricing → **Buy me a coffee → $3** (cheapest test).
2. Pay with a different PayPal account or a card (ask a friend or use a family account).
3. Confirm: you're returned to the **Thank you** page, and PayPal emails you "You've got money".
4. Refund the test in PayPal (Activity → the payment → Refund) if you want.

## Step 5: Deliver each order

When PayPal emails you a payment for **Motif Pro** or **Founding Lifetime**, reply to the buyer's PayPal email with the template below. Aim for the same day. The site promises within 24 hours.

For **subscriptions**, PayPal also emails you when someone cancels. Stop sending them new drops after their paid period ends.

---

## Delivery email template

**Subject:** Your Motif Pro library is ready 🎉

> Hi {first name},
>
> Thank you for joining Motif Pro! Here's your full library:
>
> **Download:** {your Google Drive link}
>
> **What's inside:** 21 agent skills (13 UX & AI skills + 8 deck styles), 20 website prompts, and reference libraries (palettes, font pairings, UX laws).
>
> **Install a skill:** unzip, then add the skill folder to Claude (Settings → Capabilities → Skills), or put it in `.claude/skills/` for Claude Code / your agent's skills folder. For prompts, open `motif-website-prompts.md` and copy any prompt into Lovable, Bolt, v0 or Cursor.
>
> {For subscribers:} New drops arrive by email every week. You can cancel anytime in PayPal → Settings → Payments → Automatic payments.
>
> Your license covers your own and client projects. Please don't share or resell the files.
>
> Questions? Just reply to this email.
>
> Sandy
> Motif

---

## Before you share the link publicly

- [ ] PayPal Business upgrade done, test payment successful
- [ ] Pro bundle uploaded to Drive; link pasted into the email template
- [ ] Footer contact email changed from `hello@motif.design` to one you check (in `motif-site/index.html`, search for `mailto:`)
- [ ] Read the License / Refunds / Terms / Privacy pages on the site and adjust if needed
- [ ] Checked Equinix's outside-activity policy
- [ ] Record 5–8 second screen captures of a few results for social posts

## When to upgrade

When you're getting a few sales a week, or selling outside the US, add Lemon Squeezy for automatic delivery and tax handling. See `motif-pack/PAYMENTS-SETUP.md`. PayPal stays as a backup.
