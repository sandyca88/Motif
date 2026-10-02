# Sales, delivery & release

## Plans (PayPal Payments Standard, one-time `_xclick`)

| Plan | Price | Notes |
|---|---|---|
| Free | $0 | free items + community picks |
| Pro (1 year) | $49 once | 12 months, **no auto-renew** (PayPal subscriptions errored on Sandy's account) |
| Founding Lifetime | $99 once | everything forever |
| Tips | $3 / $5 / $10 | "Buy me a coffee" |

Seller: sandyca88@yahoo.com. Testing: Sandy's Chrome is logged in as the seller, so PayPal shows "can't pay yourself" (CANNOT_PAY_SELF). Test in a private window, logged out, and stop at the login/card screen. The return URL always points to `LIVE_SITE`. Never enter payment or login details for her.

Upgrade path when sales grow: Lemon Squeezy (auto delivery, renewals, tax; fill the `LEMON` links) or Netlify Functions + PayPal webhooks (needs CLI/Git deploys and an email service).

## Delivery (manual, ~2 minutes per sale)

1. PayPal emails "You've got money".
2. Add a row in `~/Downloads/Motif Ops/Motif-Buyer-Tracker.xlsx` (Buyers tab: name, PayPal email, plan, paid date, transaction ID). Status turns red "Send download link".
3. Send the welcome email from `Motif-email-templates.md` (Pro or Lifetime) from tosandy.work@gmail.com, then set "Link sent?" to Yes.
4. Amber "Send renewal reminder" appears 30 days before a Pro expiry; send template 3 and mark it.

**Drive link (Pro bundle):** stored privately in `Motif Ops/Motif-Buyer-Tracker.xlsx` (Settings tab), not in this repo (Anyone with the link, Viewer). Private: never on the website.

## Updating the bundle

1. `python3 motif-pack/build/bundle.py` (rebuilds `dist/motif-pro-bundle.zip`, includes START-HERE.md, claude-app-zips/, assets, examples, prompts).
2. Copy it to `~/Downloads/Motif-Pro-Bundle.zip` (16–17 MB; too big for the 10 MB browser upload tool, so Sandy uploads it herself).
3. Sandy: Drive → right-click the file → File information → **Manage versions → Upload new version**. Same link, buyers get the update.

## Releasing the site (only when Sandy says "push to Netlify")

1. `python3 motif-pack/build/package_site.py`, then run the checks and screenshot key pages in both themes.
2. Netlify → project **sunny-crumble-7de34c** → **Deploys** → drag `motif-site.zip` (or the `motif-site` folder) into the drop area. Sandy is logged in; ask before clicking anything that publishes if she hasn't said go.
3. Verify live: home, prompts, an item page, pricing, guide, thank-you; free zip downloads; PayPal button opens checkout.
4. Contact form: FormSubmit needs one activation email on the first live submission (check tosandy.work@gmail.com).

Domain idea: motifux.com (was available at ~$11/yr; check current price before recommending).
