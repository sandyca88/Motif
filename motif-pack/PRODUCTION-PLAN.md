# Motif: going live with Google login, Pro access and payments

The storefront file is a **prototype**: login and Pro are simulated in memory. A static HTML page can't truly protect paid files (anyone can view source), so production needs a small backend. Here's the simplest setup that works well for a solo creator.

## Recommended stack

| Need | Recommendation | Why |
|------|----------------|-----|
| Site | **Next.js** on **Vercel** | Easy deploy, free tier is plenty to start, API routes built in |
| Google login + user database | **Supabase** (Auth + Postgres + Storage) | Google sign-in in a few clicks, row-level security, private file storage with expiring links |
| Payments | **Lemon Squeezy** *(or Stripe)* | Lemon Squeezy is a *merchant of record*: it handles global sales tax/VAT for you, and supports subscriptions, lifetime, license keys and a customer portal. Stripe is cheaper and more flexible, but you handle tax setup yourself |
| Tips | **Buy Me a Coffee** or **Ko-fi** link | Good as a "say thanks" tip jar. Not ideal for gating Pro access |
| PayPal | Enable PayPal *inside* Lemon Squeezy/Stripe checkout | Customers get PayPal as an option, and you keep one system for entitlements instead of two |

**My pick for you:** Supabase + Lemon Squeezy (with PayPal enabled at checkout) + a Buy Me a Coffee tip link.

## How access works

```
User clicks "Sign in with Google"  →  Supabase Auth creates/loads the user
User clicks "Go Pro"               →  Lemon Squeezy hosted checkout (card / Apple Pay / PayPal)
Payment succeeds                   →  Lemon Squeezy webhook → /api/webhooks/billing
Webhook (signature verified)       →  sets profiles.plan = 'pro' (or 'lifetime'), stores period_end
User opens a Pro item              →  server checks plan → returns a signed download URL (expires in 60s)
Subscription cancelled/expired     →  webhook sets plan = 'free' after period_end
```

**Key rules**
- Paid prompt text and skill zips live **only** in private Supabase Storage / the database, never in the public page bundle. The page shows a teaser; the full text comes from an authenticated API.
- Free items can stay public (good for SEO).
- Always verify webhook signatures; never trust "I'm Pro" from the browser.

## Data model (Supabase)

```sql
profiles (id uuid pk = auth.users.id, email text, name text, avatar_url text,
          plan text default 'free' check (plan in ('free','pro','lifetime')),
          period_end timestamptz, billing_customer_id text, created_at timestamptz)

items    (slug text pk, kind text, title text, category text, tags text[],
          is_free bool, description text, preview_html text, published_at timestamptz)

item_files (slug text references items, storage_path text, content text)  -- private, RLS: only pro/lifetime or is_free

downloads (user_id uuid, slug text, created_at timestamptz)                -- "My library" + popularity counts
```

## Site structure (matches the prototype)

| Page | URL | Purpose |
|------|-----|---------|
| Home | `/` | Hero, category tiles, editor's picks, new drops, free picks, Pro teaser |
| Skills | `/skills` | Sub-filters: UX, AI, research, brand, systems, career… |
| Decks | `/decks` | 8 deck styles, filters by use (business, teaching, launch…) |
| Prompts | `/prompts` | Filters: landing, hero, app, SaaS, sections, portfolio… |
| Free | `/free` | Free items + community open-source picks |
| Item | `/item/[slug]` | Big preview, description, what's included, copy/download or unlock, related items |
| Pricing | `/pricing` | Plans, checkout buttons, tip jar, FAQ |
| Account | `/account` | Plan, billing portal, unlocked library, download history |

Separate pages make sense at this size (41 items and growing). Each page stays scannable, gets its own search ranking, and filters stay relevant to that type. Add "Load more" at 12 items per page, and an item detail page so each product has a shareable URL.

## Build steps (about 1–2 weekends)

1. Create Supabase project → enable Google provider (Google Cloud OAuth client, add redirect URL).
2. Create Lemon Squeezy store → products: Pro Yearly ($49), Founding Lifetime ($99); enable PayPal; set webhook to `/api/webhooks/billing`.
3. Scaffold Next.js app; port the prototype's CSS/markup into components (Nav, Card, LibraryPage, ItemPage, Pricing, Account).
4. Import items into `items`; upload zips/prompt text to private storage.
5. Implement `/api/items/[slug]/content` (auth + plan check → content or signed URL).
6. Implement webhook handler → update `profiles.plan`.
7. Add legal pages (Terms incl. license + refund policy, Privacy), then launch.

## Notes

- If you build this on an Equinix-managed machine, pull npm packages through the Equinix Nexus registry (`https://nexus.equinix.com/repository/Equinix-NPM-Release/`) per company policy.
- This is a side business, so check Equinix's outside-activity policy before you launch paid plans.
- Before choosing, compare current fees and payout terms on each provider's pricing page. They change.
