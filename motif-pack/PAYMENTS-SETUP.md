# Payments setup (about 30 minutes)

The storefront already works with **PayPal** (payments go to sandyca88@yahoo.com). Add **Lemon Squeezy** for card, Apple Pay and PayPal checkout with **automatic file delivery**, plus an optional **Buy Me a Coffee** page.

All settings live at the top of the `<script>` in `motif-storefront.html`. Search for `LEMON=`.

```js
const LEMON={month:"", pro:"", life:"", tip:""};   // paste checkout links
const BMC_URL="";                                   // paste your Buy Me a Coffee page
```

Empty values fall back to PayPal automatically, so the site never has a dead button.

---

## 1. Lemon Squeezy (recommended main checkout)

1. Sign up at lemonsqueezy.com → create a store (name: Motif).
2. **Settings → Payouts**: connect your bank or PayPal to receive money. Complete identity verification. Your store needs approval before it can take live payments.
3. **Products → New product**, create these four:

| Product | Pricing | File to attach |
|---------|---------|----------------|
| Motif Pro (1 year) | Single payment · $49 (12 months, no auto-renew) | `dist/motif-pro-bundle.zip` |
| Motif Founding Lifetime | Single payment · $99 | `dist/motif-pro-bundle.zip` |
| Motif Free Starter *(optional, $0)* | Free, "pay what you want" off | `dist/motif-free-bundle.zip` (collects emails for your newsletter) |

   Attach the zip under the product's **Files** section so buyers get a download link in their receipt email. Before launch, confirm in your dashboard that file delivery is enabled for subscription products too.
4. For each product: **Share → Checkout link** → copy the URL (looks like `https://motif.lemonsqueezy.com/buy/…`) and paste it into `LEMON` (`month`, `pro`, `life`).
5. **Settings → Checkout**: set the confirmation redirect to `https://YOUR-SITE/#/thanks/pro` (after you host the site) and add your logo and brand color `#8B5CF6`.
6. Turn on PayPal as a payment method in your payment settings if it's offered for your region.
7. Test with **Test mode** on before going live.

**Weekly drops for subscribers:** each time you add items, rebuild the bundle (see below), upload the new file to the three Pro products, and send an email to customers from Lemon Squeezy.

## 2. Buy Me a Coffee (tips)

1. Create a page at buymeacoffee.com and connect your payout method.
2. Paste the URL into `BMC_URL`, e.g. `"https://buymeacoffee.com/sandyux"`.
3. The "Buy me a coffee" buttons (pricing page and footer) will open your page. If `BMC_URL` is left empty, they show the $3 / $5 / $10 PayPal tip picker instead.

## 3. PayPal (already live; backup and "pay directly" option)

- Buttons use PayPal's standard checkout: monthly/yearly subscriptions, lifetime and tips. No API keys needed.
- **Delivery is manual** for PayPal-direct orders. PayPal emails you each payment, and you reply with the download link (upload `motif-pro-bundle.zip` to Google Drive/Dropbox with link access). The site tells buyers "within 24 hours".
- Optional: in PayPal, create **hosted buttons** so your email isn't visible in the page source, then swap them in.
- Receiving business payments on a personal PayPal account may be limited. Consider upgrading it to a free **Business** account.

## 4. Put the site online

Any static host works because it's one HTML file: Netlify Drop (drag and drop), Vercel, GitHub Pages or Cloudflare Pages. Keep `motif-pack/dist/` next to it so the free downloads work. Buy a domain (e.g. motif.design) and update the `mailto:` contact address in the footer.

## 5. Rebuild after adding items

```bash
cd motif-pack/build && python3 build.py      # regenerates motif-storefront.html
```

Re-zip `skills/` and prompts into `dist/motif-pro-bundle.zip` (and the free bundle) and re-upload to Lemon Squeezy.

## Checklist before launch

- [ ] Lemon Squeezy store approved, test purchase done, links pasted
- [ ] PayPal upgraded to Business (recommended)
- [ ] Contact email updated in the footer
- [ ] License / Refund / Terms / Privacy pages reviewed (plain-language drafts are included; have them checked for your country)
- [ ] Equinix outside-activity policy checked
