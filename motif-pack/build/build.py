import json, re, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from thumbs_a import T as A
from thumbs_b import T as B
from thumbs_c import T as C
from thumbs_d import T as D
from thumbs_e import T as E
from thumbs_f import T as F
from thumbs_g import T as G
from thumbs_h import T as H
from thumbs_i import T as I
from thumbs_j import T as J
from thumbs_k import T as K
from thumbs_l import T as L
from thumbs_m import T as M
TH = {**A, **B, **C, **D, **E, **F, **G, **H, **I, **J, **K, **L, **M}
ROOT = os.path.dirname(os.path.dirname(__file__))
md = open(os.path.join(ROOT, "prompts/motif-website-prompts.md")).read()
blocks = re.findall(r"## (\d\d) · (.+?)  `(FREE|PRO)`\n\n```\n(.*?)```", md, re.S)
P = {num: (name, tier, body.strip()) for num, name, tier, body in blocks}

items = [
 # key, title, category, kind, tags, free, prompt#, desc, zip
 ("aurora","Aurora","AI SaaS Hero","prompt",["hero","landing","saas"],True,"01","Cinematic dark hero with drifting aurora, rotating gradient word and logo marquee.",None),
 ("ledger","Ledger","Analytics Dashboard","prompt",["dashboard","app","saas"],False,"02","Question-first dark dashboard: KPI tiles, trend chart, channel bars, action table, all states.",None),
 ("taste","Taste Layer","Flagship · Design taste","skill",["skill"],False,None,"Makes anything your agent builds look designed: direction, tokens, layout breaks, detail pass, motion, self-check.","taste-layer"),
 ("hairline","Hairline","Dev Tool Landing","prompt",["landing","saas"],False,"03","Precision-style landing with drifting grid, typing terminal and copyable install command.",None),
 ("folio","Folio","Editorial UX Portfolio","prompt",["portfolio","landing"],True,"04","Serif editorial portfolio for designers with staggered case-study cards and a case study template.",None),
 ("audit","UX Heuristic Audit","Usability + accessibility","skill",["skill"],True,None,"Scores any UI across 8 UX + WCAG lenses and returns P0–P2 findings with copy-paste code fixes.","ux-heuristic-audit"),
 ("bento","Bento","Feature Grid Section","prompt",["sections","saas"],False,"06","Mixed-span bento grid with live mini-visuals, cursor spotlight and tilt.",None),
 ("vault","Vault","Fintech App Landing","prompt",["landing","app"],False,"08","Soft-product fintech page with floating phone mockup, pop-out chips and savings calculator.",None),
 ("motionhero","Motion Hero Builder","Animated heroes","skill",["skill"],False,None,"Builds cinematic animated heroes from a concept menu, with performance budget and tuning knobs.","motion-hero-builder"),
 ("tiers","Tiers","Pricing Section","prompt",["sections","saas"],True,"05","Monthly/yearly toggle, gradient-border popular plan, comparison table and billing FAQ.",None),
 ("studio","Northwall","Agency · Kinetic Type","prompt",["landing","portfolio"],False,"09","Bold brutal agency homepage: viewport-wide kinetic type, hover-preview work list, marquee.",None),
 ("dash","Dashboard Architect","Data & dashboards","skill",["skill","dashboard"],False,None,"Turns audience + questions into the right KPIs, charts, layout and loading/empty/error states.","dashboard-architect"),
 ("waitlist","Waitlist","Launch Countdown Page","prompt",["landing","hero"],True,"07","One-viewport pre-launch page with gradient mesh, morphing email form and countdown.",None),
 ("drop","Drop","Single-Product Store","prompt",["landing","app"],False,"10","Product-as-hero store: swatches recolor the page, hotspots, sticky buy bar, cart drawer.",None),
 ("onboard","Onboarding Flow Designer","Activation & onboarding","skill",["skill"],False,None,"Maps sign-up → aha in ≤ 5 steps, with checklists, empty states, emails and metrics.","onboarding-flow-designer"),
 ("summit","Summit","Conference / Event","prompt",["landing","hero"],False,"11","Event site with rotating rings, condensed display type, speakers, schedule tabs and tickets.",None),
 ("micro","Microcopy Writer","UX writing","skill",["skill"],True,None,"Buttons, errors, empty states and dialogs rewritten in one consistent product voice.","microcopy-writer"),
 ("horizon","Horizon","Cinematic Footer + CTA","prompt",["sections"],False,"12","A finale CTA with a rising horizon glow, twinkling stars and a giant clipped wordmark.",None),
 # ---- batch 2: decks + brand ----
 ("d_marker","Marker Margin","Sketchnote deck","deck",["slides","teaching"],True,None,"Hand-drawn sketchnote decks: marker headlines, highlighter swipes, doodled arrows on warm dotted paper.","deck-marker-margin"),
 ("d_kraft","Kraft Journal","Field-notes research deck","deck",["slides","research"],True,None,"Researcher's notebook look: grid paper, taped polaroids, rubber stamps and red margin insights.","deck-kraft-journal"),
 ("d_board","Boardroom Storyline","Consulting / exec deck","deck",["slides","business"],False,None,"Action titles, pyramid-principle storyline, exec summary, clean charts with callouts and a clear ask.","deck-boardroom-storyline"),
 ("d_grid","Grid Signal","Swiss system deck","deck",["slides","business"],False,None,"Strict 12-column Swiss layouts, bold grotesk, one cobalt signal color, giant numerals.","deck-grid-signal"),
 ("d_serif","Serif Quarterly","Editorial magazine deck","deck",["slides","brand"],False,None,"Magazine-grade serif storytelling: mastheads, pull quotes, drop caps and photo essays.","deck-serif-quarterly"),
 ("d_frost","Frost","Glassmorphism keynote","deck",["slides","launch"],False,None,"Frosted glass panels over drifting pastel skies for product launches and vision keynotes.","deck-frost"),
 ("d_riso","Pop Riso","Riso print event deck","deck",["slides","launch"],False,None,"Two-color overprint, halftones, misregistered stacked type and confetti energy.","deck-pop-riso"),
 ("d_collage","Paper Collage","Cut-paper story deck","deck",["slides","teaching"],False,None,"Layered cut-paper scenes with diverse paper figures, torn banners and warm handmade texture.","deck-paper-collage"),
 ("avatar","Bloblings Avatar Set","Brand assets · SVG","skill",["brand"],False,None,"A consistent family of original SVG avatars from one construction system, plus sheet, JSON and seeded React avatar.","mascot-avatar-set"),
 ("pinboard","Pinboard","Scrapbook Résumé Site","prompt",["portfolio"],True,"13","A memorable pinboard résumé: pinned cards, polaroids, stickers, and a clean 1-page print version.",None),
 ("spread","Spread","Scattered-Card Magazine","prompt",["landing","editorial"],False,"14","Editorial homepage with a scattered collage of story cards that straighten on hover and re-sort with FLIP.",None),
 # ---- batch 3 ----
 ("gate","Gate","Login & Sign-up Screens","prompt",["app","saas"],True,"15","Five auth screens with SSO-first layout, strength meter, OTP inputs and every error state.",None),
 ("console","Console","Settings & Account Page","prompt",["app","saas"],False,"16","Settings with notification matrix, team roles, billing, API keys, danger zone and unsaved-changes bar.",None),
 ("parley","Parley","AI Chat Interface","prompt",["app","ai"],False,"17","Production AI chat: history, streaming, tool steps, citations, code blocks and a rich composer.",None),
 ("manual","Manual","Docs Site","prompt",["landing","saas"],False,"18","Three-column docs with ⌘K search, code tabs, callouts, API blocks and scroll-spy TOC.",None),
 ("lost","Lost & Found","404 + Empty States","prompt",["sections"],False,"19","Seven useful error and empty states with small looping SVG illustrations and warm copy.",None),
 ("pocket","Pocket","Mobile App Onboarding","prompt",["app","mobile"],False,"20","Mobile onboarding to first success in under 60 seconds: carousel, chips, permission priming, coach marks.",None),
 ("dsys","Design System Starter","Tokens + components","skill",["ux","systems"],False,None,"Brand color → OKLCH ramps, semantic light/dark tokens, type scale, components in every state and a living style guide.","design-system-starter"),
 ("casestudy","Case Study Writer","Portfolio & career","skill",["ux","career"],True,None,"Turns messy project notes into an outcome-first UX case study, a 30-second version and a 5-slide interview deck.","case-study-writer"),
 ("form","Form UX Optimizer","Conversion & forms","skill",["ux"],False,None,"Field inventory, cuts, autofill, validation timing and error recovery, then rebuilds the form.","form-ux-optimizer"),
 ("a11y","A11y Fixer","Accessibility · WCAG 2.2","skill",["ux","a11y"],False,None,"Fixes accessibility issues directly in code and logs every change with its WCAG success criterion.","a11y-fixer"),
 ("usability","Usability Test Kit","Research","skill",["ux","research"],False,None,"Plan, screener, task script, note template, affinity synthesis and a stakeholder-ready readout.","usability-test-kit"),
 ("aiux","AI Product UX","AI & agent UX patterns","skill",["ux","ai"],False,None,"Patterns for chat, copilots and agents: progress, citations, approvals, undo, errors and feedback.","ai-product-ux"),
 # ---- batch 4 ----
 ("d_obsidian","Obsidian","Premium keynote deck · sample included","deck",["slides","business","launch"],True,None,"Flagship dark keynote style with luminous gradient accents, glass cards and big numbers. Includes a complete 10-slide investor deck you can open, present and adapt.","deck-obsidian"),
 ("vprompt","Video Prompt Director","AI video prompts","skill",["video","ai"],True,None,"Model-ready prompts for Veo, Sora, Kling, Runway and more: the 8-part shot formula, shot lists, image-to-video and per-model tips.","video-prompt-director"),
 ("storyboard","Launch Video Storyboard","Launch & promo videos","skill",["video","brand"],False,None,"Hook-to-CTA launch video plan: script, storyboard, screen-recording list, AI B-roll prompts, audio cues, captions and cut-downs.","launch-video-storyboard"),
 # ---- batch 5 ----
 ("d_clearview","Clearview","Minimal product keynote · sample included","deck",["slides","launch","business"],True,None,"Bright, minimal product-keynote style: huge centered headlines, floating product heroes and one crisp blue accent. Includes an 8-slide launch deck you can present today.","deck-clearview"),
 ("d_toybox","Toybox Bots","Playful 3D mascot deck","deck",["slides","teaching","brand"],False,None,"A cast of original clay-style robot mascots with poses, candy colors and sticker UI: explainers, onboarding and fun all-hands.","deck-toybox-bots"),
 ("d_chroma","Chroma Launch","Gradient hype launch deck","deck",["slides","launch"],False,None,"Saturated gradient-mesh backgrounds, huge tight type, glossy product reveals and counters for launch day.","deck-chroma-launch"),
 # ---- batch 6: prompts 21-44 ----
 ('halo','Halo','Wearable / AR Hardware Launch',"prompt",['landing', 'hero'],False,'21','Cinematic device launch: reflective hero, scroll-driven exploded view, day-in-the-life UI overlays and pre-order bar.',None),
 ('maison','Maison','Luxury Fashion Store',"prompt",['ecommerce', 'editorial'],False,'22','Quiet-luxury storefront and product page: editorial grid, second-angle hovers, sticky gallery and cart drawer.',None),
 ('ember','Ember & Oak','Restaurant Site',"prompt",['landing', 'mobile'],True,'23','Warm restaurant site with live open/closed status, tabbed menu, reservations and a sticky mobile Call/Book bar.',None),
 ('stride','Stride','Fitness & Wellness App',"prompt",['landing', 'app', 'mobile'],False,'24','Energetic app landing with animated activity rings, filterable plans, coaches and inclusive, honest results.',None),
 ('wander','Wander','Travel Booking',"prompt",['landing', 'ecommerce'],False,'25','Travel homepage with an accessible search bar, date-range pricing, category filters and a list/map split view.',None),
 ('stage','Stage','Musician / Artist Site',"prompt",['portfolio', 'landing'],False,'26','Release-driven artist site: album-colored hero, preview player, tour dates, video and merch.',None),
 ('care','Care','Clinic & Healthcare',"prompt",['landing', 'app'],False,'27','Calm, trustworthy clinic site with a full booking flow, clinician picker and strict accessibility.',None),
 ('haven','Haven','Real Estate Listings',"prompt",['landing', 'app'],False,'28','Search-first real-estate site with listing cards, photo mosaic, sticky viewing card and mortgage calculator.',None),
 ('learn','Learn','Online Course / Cohort',"prompt",['landing', 'saas'],False,'29','Course sales page with honest seats-left bar, curriculum accordion, outcomes and pricing tiers.',None),
 ('kindred','Kindred','Nonprofit & Donations',"prompt",['landing'],False,'30','Hopeful nonprofit site with goal progress, outcome-mapped donation amounts and monthly-first giving.',None),
 ('shipped','Shipped','Changelog & Roadmap',"prompt",['sections', 'saas'],False,'31','Public changelog timeline with filters and permalinks, plus an upvotable roadmap board.',None),
 ('dispatch','Dispatch','Creator Newsletter',"prompt",['landing', 'editorial'],True,'32','Editorial newsletter landing with a single-field signup, recent issues and reader quotes.',None),
 ('blockhaus','Blockhaus','Neo-Brutalist SaaS',"prompt",['landing', 'saas'],False,'33','Loud neo-brutalist SaaS page: thick borders, hard shadows, sticker pricing and a tabbed demo.',None),
 ('tiles','Tiles','Bento Personal Site',"prompt",['portfolio'],True,'34','One-page bento-grid personal site: intro, socials, map, music, projects and a copy-email tile.',None),
 ('configure','Configure','3D Product Configurator',"prompt",['ecommerce', 'app'],False,'35','Customize-and-buy configurator: live recolor, materials, monogram preview and shareable design URL.',None),
 ('daybreak','Daybreak','Light AI Agent Startup',"prompt",['landing', 'ai', 'saas'],False,'36','Bright sunrise-themed AI agent landing with a live task card, approvals and honest AI copy.',None),
 ('formvoid','Form & Void','Architecture Studio',"prompt",['portfolio', 'editorial'],False,'37','Monochrome architecture portfolio with slideshow hero, hover-preview project index and project template.',None),
 ('roast','Roast','DTC Coffee Brand',"prompt",['ecommerce', 'landing'],False,'38','Playful coffee DTC store with a taste quiz, roast-level cards and a subscription builder.',None),
 ('encore','Encore','Event Ticketing',"prompt",['app', 'ecommerce'],False,'39','Ticketing flow with discovery, event page, seat map, hold timer and fees shown upfront.',None),
 ('counsel','Counsel','Law & Professional Services',"prompt",['landing'],False,'40','Established-but-modern firm site with practice pages, team filters and a confidential consult form.',None),
 ('tides','Tides','Boutique Hotel & Resort',"prompt",['landing', 'editorial'],False,'41','Slow-luxury hotel site with sticky booking bar, room cards, experiences and packages.',None),
 ('onair','On Air','Podcast Site',"prompt",['landing'],False,'42','Podcast site with chaptered player, persistent mini player, episode list and searchable transcripts.',None),
 ('nest','Nest','Interior Design Studio',"prompt",['portfolio'],False,'43','Warm interior studio site with arch-masked imagery, mood boards, before/after and multi-step inquiry.',None),
 ('signal','Signal','Live Analytics Hero',"prompt",['hero', 'saas'],False,'44','Hero built around a live streaming chart, ticking counters and floating event chips, performance-first.',None),
 ('ronin','Ronin Dawn','Game Launch Landing',"prompt",['landing','hero'],False,'45','Cinematic game launch page: layered parallax key art with the title behind the hero, particles, trailer, character selector and editions.',None),
 ('nova','Nova','Coral AI Assistant Landing',"prompt",['landing','ai','saas'],False,'46','Bold single-color AI assistant hero with a glossy original 3D object, floating UI chips and a scroll hint row.',None),
 ('tidewater','Tidewater','Outdoor Build & Design Services',"prompt",['landing','portfolio'],False,'47','Premium pool & landscape builder site with a hand-drawn architectural sketch hero, before/after projects and a quote flow.',None),
 ('meridian','Meridian','City Residences · Ink Sketch',"prompt",['landing','editorial'],False,'48','Luxury residential tower site with a hand-drawn skyscraper ink-sketch hero, residence tabs, amenities, availability table and viewing form.',None),
 ('jade','Jade Pavilion','Wuxia Game Launch',"prompt",['landing','hero'],False,'49','Painterly game launch page: an original heroine in silk hanfu at a mountain temple, calligraphy title layered behind her, petals and ink-wash transitions. Includes the hero image prompt.',None),
 ('aero','Aero','Smart Glasses Launch · Sky',"prompt",['landing','hero','ecommerce'],False,'50','Bright sky-blue launch page for original smart glasses: floating product, feature chips, scroll hotspots and style swatches. Includes the product image prompt.',None),
 ('lumenfold','Lumen Fold','Minimal Product Keynote',"prompt",['landing','hero','ecommerce'],False,'51','Clean consumer-tech keynote page: centered type, blue pill buttons and an original foldable phone held in two hands. Includes the hero image prompt.',None),
 ('ember1','Ember One','Coral Smartphone Launch',"prompt",['landing','hero','ecommerce'],False,'52','Bold coral phone launch: tight white headline, glossy original phone on a pedestal, floating chips and spheres, scroll hint bar. Includes the hero image prompt.',None),
 ('lumora','Lumora','3D Orb Motion Hero · Video',"prompt",['hero','landing','ai'],False,'53','Motion-first hero with a looping cinematic video of an iridescent orb above pastel clouds, word-by-word headline reveal and particle parallax. Includes the video prompt and a ready-made background loop in the Pro bundle.',None),
 ('softwork','Softwork','Eye-Tracking Mascot Studio',"prompt",['landing','portfolio','hero'],False,'54','A fuzzy original mascot fills the screen and its eyes follow your cursor (blinks, idle wander, touch). Includes the image prompt and the exact eye-tracking math. Live demo included.',None),
 ('concord','Concord','Human + Robot Motion Hero · Video',"prompt",['hero','landing','ai'],False,'55','Looping video of a human hand and a robot hand holding a glowing sphere, with a calm centered headline and pill UI. Includes the video prompt; the original loop ships in the Pro bundle.',None),
 ('aipipe','AI Art Direction Pipeline','Pro skill · Gemini image & video',"skill",['ai','brand','video'],False,None,'The exact workflow behind our Gemini thumbnails: reference style analysis, prompt formulas, image & video generation, eye detection, UI overlays, animated thumbnails and compression, with 5 working scripts and an eye-tracking example.','ai-art-direction-pipeline'),
 ('uupm','UI UX Pro Max','Free pick · by nextlevelbuilder',"skill",['ux','systems'],True,None,'Open-source design intelligence skill: a searchable database of UI styles, color palettes, font pairings, chart types and UX guidelines. MIT-licensed, made by nextlevelbuilder; featured here with credit.',None),
 ('mascotkit','Animated Mascot Logo Kit','Pro skill · logo with eyes',"skill",['brand','ux'],False,None,'Make any logo come alive: a mark that looks at the cursor, blinks, breathes and squishes; shape-morphing; and a hopping family of avatars. Pure CSS/JS, plus favicon/app-icon and animated MP4/GIF export recipes.','animated-mascot-logo'),
 ('northbound','Northbound','Polar Expedition Travel',"prompt",['landing','editorial'],False,'56','Quiet luxury expedition site: chart-style coordinates, animated polar route map, journal entries, deck-plan suite picker and honest scarcity. Includes the hero image prompt.',None),
 ('prismbench','Prism Bench','Optics Lab Instrument Maker',"prompt",['landing','ecommerce','saas'],False,'57','Dark precision-instrument site with an interactive prism ray simulator (real refraction math), parts grid and live bench configurator.',None),
 ('wobble','Wobble Co.','Squishy Toy & Slime Shop',"prompt",['ecommerce','landing'],False,'58','Candy-bright DTC store with a jiggly soft-body hero blob, texture picker, poke-to-preview products and a build-a-slime jar.',None),
 ('duotone','Duotone Press','Riso Print Studio',"prompt",['portfolio','landing'],True,'59','Printed-look studio site: two inks with real overprint blending, misregistered headline that follows the cursor, live ink-combo preview and price calculator.',None),
 ('fallline','Fall Line','Downhill Ski Race Event',"prompt",['landing','hero'],False,'60','Race-day event site: slanted sports type, flip-digit countdown, scroll-driven course elevation profile and a live timing board.',None),
 ('staticfm','Static FM','Independent Internet Radio',"prompt",['landing','editorial'],True,'61','Late-night radio station with a persistent live player, Web Audio visualizer, time-zone-aware schedule and a playable archive.',None),
 ('halden','Halden','Quiet Fashion Store',"prompt",['ecommerce','editorial'],False,'62','Calm editorial fashion store: giant serif, asymmetric photo grid, shoppable lookbook, filterable products and a complete product page.',None),
 ('facet','Facet','Fine Jewelry Configurator',"prompt",['ecommerce','landing'],False,'63','Velvet-black ring configurator: rotating render with sparkles, step-by-step stone/cut/metal/band builder with running price, and the 4Cs explained.',None),
 ('lattice','Lattice','Particle Sphere Intelligence Hero · Video',"prompt",['hero','landing','ai','saas'],False,'64','Dark AI-platform hero with a living particle sphere, travelling data signals and orbit rings. Build it in canvas (full spec included) or use the Gemini video loop. Includes the video and poster prompts.',None),
 # credited free picks from the aura.build/skills directory (all MIT, link out, never re-hosted)
 ('af_mengto','Aura Web Design Skills','Free pick · by Meng To',"skill",['ux','motion','landing'],True,None,'The skill set behind Aura: high-conversion landing pages, GSAP, Vanta.js backgrounds, progressive blur, pricing pages, CSS border gradients, cobe.js globes, Matter.js physics and CSS alpha masking. MIT, by Meng To.',None),
 ('af_frontend','Frontend Design','Free pick · by Anthropic',"skill",['ux','brand'],True,None,"Anthropic's official skill for distinctive, production-grade frontends that avoid the generic AI look: bold direction, typography, color, motion. Apache-2.0.",None),
 ('af_taste','Taste Skill','Free pick · by Leonxlnx',"skill",['ux','motion'],True,None,'High-agency frontend and image art direction with adjustable variance, motion and density dials. MIT, by Leonxlnx.',None),
 ('af_vercel','Web Interface Guidelines','Free pick · by Vercel Labs',"skill",['ux','a11y'],True,None,'Concise rules for interfaces that feel right: interactions, forms, focus, animation, layout, content and performance. Great as a review checklist. MIT, by Vercel Labs.',None),
 ('af_ccui','UI Design System','Free pick · by Daniel Ávila',"skill",['ux','systems'],True,None,'Design-system skill from the Claude Code Templates collection: components, tokens, spacing and accessible patterns. MIT, by Daniel Ávila (davila7).',None),
 ('af_wsh','Tailwind v4 & Responsive Design','Free pick · by Seth Hobson',"skill",['ux','systems'],True,None,'Tailwind CSS v4 design-system, interaction-design and responsive-design skills from the wshobson/agents collection. MIT, by Seth Hobson.',None),
 ('af_three','Three.js Skills','Free pick · by CloudAI-X',"skill",['motion','3d'],True,None,'Ten focused Three.js skills: fundamentals, geometry, materials, lighting, textures, animation, loaders, shaders, post-processing and interaction. MIT, by CloudAI-X.',None),
 ('af_anime','Anime.js v4 Skill','Free pick · by BowTiedSwan',"skill",['motion'],True,None,'Full Anime.js v4 knowledge for agents: timelines, stagger, SVG morphing and line drawing, scroll-triggered motion, draggables and springs. MIT, by BowTiedSwan.',None),
 ('af_webrev','Web Design Reviewer','Free pick · by GitHub',"skill",['ux','a11y'],True,None,'Visual QA skill from GitHub\'s awesome-copilot: inspects a running site, finds layout, contrast and responsive issues, and proposes fixes. MIT, by GitHub.',None),
 ('af_corey','Marketing Skills','Free pick · by Corey Haines',"skill",['marketing'],True,None,'Copywriting, marketing psychology, analytics tracking, CRO and more for agents. Pairs well with landing-page prompts. MIT, by Corey Haines.',None),
 ('af_kostja','Marketing Skills Pack','Free pick · by kostja94',"skill",['marketing'],True,None,'A broad marketing skill pack: SEO, content, landing pages and growth playbooks. MIT, by kostja94.',None),
]
out = []
for i,(k,t,c,kind,tags,free,pn,desc,z) in enumerate(items):
    d = dict(k=k,t=t,c=c,kind=kind,tags=tags+(["free"] if free else []),free=free,desc=desc,html=TH[k],new=i>=18,order=i)
    if pn:
        d["prompt"] = P[pn][2] if free else P[pn][2][:420]
        m=re.search(r'((?:HERO IMAGE PROMPT|VIDEO PROMPT)[^\n]*:\n.*)$',P[pn][2],re.S)
        if m: d['artprompt']=m.group(1).strip()
    if z: d["zip"] = f"motif-pack/dist/{z}.zip"
    for ext in ('webp','jpg','png'):
        ip=os.path.join(os.path.dirname(__file__),'thumb-images',f'{k}.{ext}')
        if os.path.exists(ip): d['img']=f'thumbs/{k}.{ext}'; break
    vp=os.path.join(os.path.dirname(__file__),'thumb-images',f'{k}.mp4')
    if os.path.exists(vp): d['vid']=f'thumbs/{k}.mp4'
    PO=('jade','meridian','concord','lattice','lumora','aipipe','d_obsidian','mascotkit','softwork','d_clearview','taste','aurora','ledger','parley','a11y','studio','d_board');d['pick'] = (PO.index(k)+1) if k in PO else 0
    if k=='d_obsidian': d['sample']='samples/obsidian-sample-deck.html'
    if k=='d_clearview': d['sample']='samples/clearview-sample-deck.html'
    if k=='mascotkit': d['sample']='samples/mascot-concepts.html'; d['samplelabel']='Try the live mascot demo'
    if k=='lattice': d['sample']='samples/lattice/index.html'; d['samplelabel']='Try the live particle-sphere demo'
    if k=='softwork': d['sample']='samples/softwork/index.html'; d['samplelabel']='Try the live eye-tracking demo'
    if k=='uupm': d['tags'].append('open-source'); d['lic']='MIT'; d['ext']='https://github.com/nextlevelbuilder/ui-ux-pro-max-skill'; d['site']='https://uupm.cc/#styles'
    EXT={'af_mengto':'https://github.com/MengTo/Skills','af_frontend':'https://github.com/anthropics/skills/tree/main/skills/frontend-design','af_taste':'https://github.com/Leonxlnx/taste-skill','af_vercel':'https://github.com/vercel-labs/web-interface-guidelines','af_ccui':'https://github.com/davila7/claude-code-templates','af_wsh':'https://github.com/wshobson/agents','af_three':'https://github.com/CloudAI-X/threejs-skills','af_anime':'https://github.com/BowTiedSwan/animejs-skills','af_webrev':'https://github.com/github/awesome-copilot','af_corey':'https://github.com/coreyhaines31/marketingskills','af_kostja':'https://github.com/kostja94/marketing-skills'}
    if k in EXT: d['ext']=EXT[k]; d['lic']='Apache-2.0' if k=='af_frontend' else 'MIT'; d['tags'].append('open-source')
    if k=='af_mengto': d['site']='https://www.aura.build/skills'
    out.append(d)

tpl = open(os.path.join(os.path.dirname(__file__), "storefront_template.html")).read()
html = tpl.replace("/*__DATA__*/[]", json.dumps(out).replace("</", "<\\/"))
open(os.path.join(os.path.dirname(ROOT), "motif-storefront.html"), "w").write(html)
print("ok", len(out), "items", len(html)//1024, "KB")
