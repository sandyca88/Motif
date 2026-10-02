# End-result thumbnails (1280x800), part A: prompts 01-06
BASE = """<style>*{box-sizing:border-box;margin:0;padding:0}html,body{width:1280px;height:800px;overflow:hidden}
body{font-family:-apple-system,BlinkMacSystemFont,Inter,'Segoe UI',sans-serif;-webkit-font-smoothing:antialiased}
.serif{font-family:'Iowan Old Style','Palatino Linotype',Georgia,serif}.mono{font-family:ui-monospace,Menlo,monospace}
@keyframes fl{to{transform:translate(90px,60px) scale(1.15)}}@keyframes up{from{opacity:0;transform:translateY(30px)}}
@keyframes spin{to{transform:rotate(360deg)}}@keyframes blink{50%{opacity:0}}@keyframes grow{from{transform:scaleY(.2)}}
@keyframes pulse{0%{transform:scale(.6);opacity:1}100%{transform:scale(2.4);opacity:0}}@keyframes marq{to{transform:translateX(-50%)}}
@keyframes bob{50%{transform:translateY(-14px)}}@keyframes shim{to{transform:translateX(100%)}}
</style>"""

T = {}

T["aurora"] = BASE + """<style>
body{background:#07070b;color:#fff;position:relative}
.o{position:absolute;border-radius:50%;filter:blur(90px);opacity:.55;animation:fl 9s ease-in-out infinite alternate}
nav{position:relative;display:flex;justify-content:space-between;align-items:center;padding:28px 56px;font-size:15px;color:#a3a3b5}
nav b{color:#fff;font-size:20px;display:flex;gap:10px;align-items:center}nav b i{width:24px;height:24px;border-radius:7px;background:conic-gradient(#8b5cf6,#22d3ee,#f472b6,#8b5cf6)}
nav .l{display:flex;gap:34px}.pill{padding:10px 20px;border-radius:99px;background:#fff;color:#000;font-weight:600}
.c{position:relative;text-align:center;margin-top:84px}
.an{display:inline-flex;gap:8px;align-items:center;padding:8px 16px;border:1px solid rgba(255,255,255,.15);border-radius:99px;font-size:14px;color:#c9c9d6;background:rgba(255,255,255,.04)}
.an i{width:8px;height:8px;border-radius:50%;background:#34d399}
h1{font-size:104px;letter-spacing:-.05em;line-height:.98;margin:30px 0 24px;font-weight:700;animation:up 1s both}
h1 span{background:linear-gradient(90deg,#a78bfa,#22d3ee,#f472b6);-webkit-background-clip:text;color:transparent}
p{font-size:21px;color:#a3a3b5;max-width:640px;margin:0 auto 36px}
.b{display:flex;gap:14px;justify-content:center}.b a{padding:16px 30px;border-radius:99px;font-weight:600;font-size:17px}
.logos{position:absolute;bottom:50px;left:0;right:0;display:flex;justify-content:center;gap:70px;font-weight:700;font-size:22px;color:rgba(255,255,255,.35);letter-spacing:-.02em}
</style>
<div class="o" style="width:620px;height:520px;left:-120px;top:-60px;background:#7c3aed"></div>
<div class="o" style="width:560px;height:480px;right:-100px;top:120px;background:#0891b2;animation-delay:-4s"></div>
<div class="o" style="width:380px;height:320px;left:480px;top:380px;background:#db2777;animation-delay:-6s"></div>
<nav><b><i></i>Relay</b><div class="l"><span>Product</span><span>Agents</span><span>Pricing</span><span>Docs</span></div><span class="pill">Get started</span></nav>
<div class="c"><span class="an"><i></i>Relay Agents 2.0 is live →</span>
<h1>Your pipeline on<br><span>autopilot.</span></h1>
<p>AI agents that qualify leads, book meetings and update your CRM — while you sleep.</p>
<div class="b"><a style="background:#fff;color:#000;box-shadow:0 10px 40px rgba(139,92,246,.5)">Start free</a><a style="border:1px solid rgba(255,255,255,.2)">Watch demo ▶</a></div></div>
<div class="logos"><span>Northwind</span><span>Acme</span><span>Globex</span><span>Umbrella</span><span>Initech</span><span>Hooli</span></div>"""

T["ledger"] = BASE + """<style>
body{background:#0a0a0b;color:#ececf1;display:flex;font-size:14px}
.sb{width:230px;border-right:1px solid rgba(255,255,255,.07);padding:24px 16px}
.sb b{display:flex;gap:10px;align-items:center;font-size:17px;margin-bottom:32px;padding-left:8px}.sb b i{width:22px;height:22px;border-radius:6px;background:#7c5cff}
.sb div{padding:10px 12px;border-radius:8px;color:#8b8b98;margin-bottom:4px}.sb .on{background:rgba(124,92,255,.14);color:#fff;box-shadow:inset 3px 0 #7c5cff}
.m{flex:1;padding:24px 32px}.top{display:flex;justify-content:space-between;align-items:center;margin-bottom:24px}
.top h2{font-size:24px;letter-spacing:-.02em}.seg{display:flex;gap:4px;background:#111114;border:1px solid rgba(255,255,255,.07);border-radius:9px;padding:3px}
.seg span{padding:6px 12px;border-radius:6px;color:#8b8b98}.seg .on{background:#222228;color:#fff}
.k{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-bottom:16px}
.card{background:#111114;border:1px solid rgba(255,255,255,.07);border-radius:14px;padding:18px}
.k .v{font-size:30px;font-weight:600;letter-spacing:-.02em;margin:6px 0;font-variant-numeric:tabular-nums}
.d{font-size:12px;padding:2px 7px;border-radius:99px}.up{background:rgba(52,211,153,.14);color:#34d399}.dn{background:rgba(248,113,113,.14);color:#f87171}
.mut{color:#8b8b98}.r2{display:grid;grid-template-columns:2fr 1fr;gap:16px;margin-bottom:16px}
.bar{display:flex;align-items:center;gap:10px;margin:12px 0}.bar i{height:10px;border-radius:5px;background:#7c5cff;animation:grow 1s both;transform-origin:left}
.bar span{width:70px;color:#8b8b98}.row{display:grid;grid-template-columns:2fr 1fr 1fr 1fr;padding:11px 0;border-top:1px solid rgba(255,255,255,.06);align-items:center}
.bd{font-size:12px;padding:3px 9px;border-radius:99px;width:max-content}
</style>
<div class="sb"><b><i></i>Ledger</b><div class="on">▦ Overview</div><div>◷ Revenue</div><div>◉ Customers</div><div>✦ Campaigns</div><div>▤ Reports</div><div>⚙ Settings</div></div>
<div class="m"><div class="top"><h2>Overview</h2><div class="seg"><span>Today</span><span>7D</span><span class="on">30D</span><span>QTD</span></div></div>
<div class="k">
<div class="card"><div class="mut">Revenue</div><div class="v">$482.1k</div><span class="d up">▲ 12.4%</span></div>
<div class="card"><div class="mut">Active customers</div><div class="v">3,904</div><span class="d up">▲ 4.1%</span></div>
<div class="card"><div class="mut">Conversion</div><div class="v">3.82%</div><span class="d up">▲ 0.6pt</span></div>
<div class="card"><div class="mut">Churn</div><div class="v">1.9%</div><span class="d dn">▼ 0.3pt</span></div></div>
<div class="r2"><div class="card"><div style="display:flex;justify-content:space-between"><b>Revenue</b><span class="mut">This period vs previous</span></div>
<svg viewBox="0 0 600 200" style="width:100%;height:210px;margin-top:10px"><defs><linearGradient id="g" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#7c5cff" stop-opacity=".45"/><stop offset="1" stop-color="#7c5cff" stop-opacity="0"/></linearGradient></defs>
<g stroke="rgba(255,255,255,.06)"><line x1="0" y1="50" x2="600" y2="50"/><line x1="0" y1="100" x2="600" y2="100"/><line x1="0" y1="150" x2="600" y2="150"/></g>
<path d="M0 150 C60 140 90 120 140 125 S220 90 260 110 S330 140 370 100 S460 60 520 55 S580 35 600 30" stroke="#6b6b78" stroke-dasharray="5 6" fill="none" stroke-width="2" transform="translate(0,25)"/>
<path d="M0 150 C60 140 90 120 140 125 S220 90 260 110 S330 140 370 100 S460 60 520 55 S580 35 600 30 V200 H0Z" fill="url(#g)"/>
<path d="M0 150 C60 140 90 120 140 125 S220 90 260 110 S330 140 370 100 S460 60 520 55 S580 35 600 30" stroke="#7c5cff" fill="none" stroke-width="3"/><circle cx="520" cy="55" r="6" fill="#fff" stroke="#7c5cff" stroke-width="3"/></svg></div>
<div class="card"><b>Revenue by channel</b><div class="bar"><span>Organic</span><i style="width:78%"></i></div><div class="bar"><span>Paid</span><i style="width:61%;opacity:.8"></i></div><div class="bar"><span>Referral</span><i style="width:44%;opacity:.6"></i></div><div class="bar"><span>Email</span><i style="width:30%;opacity:.45"></i></div><div class="bar"><span>Social</span><i style="width:18%;opacity:.3"></i></div></div></div>
<div class="card"><b>Needs attention</b>
<div class="row mut" style="border:0;font-size:12px"><span>ACCOUNT</span><span>STATUS</span><span>MRR</span><span>LAST ACTIVITY</span></div>
<div class="row"><span>Northwind Traders</span><span class="bd" style="background:rgba(248,113,113,.14);color:#f87171">At risk</span><span>$4,200</span><span class="mut">12 days ago</span></div>
<div class="row"><span>Globex Corp</span><span class="bd" style="background:rgba(251,191,36,.14);color:#fbbf24">Overdue</span><span>$2,850</span><span class="mut">3 days ago</span></div></div></div>"""

T["hairline"] = BASE + """<style>
body{background:#060607;color:#f2f2f2;background-image:linear-gradient(rgba(255,255,255,.045) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.045) 1px,transparent 1px);background-size:32px 32px}
body::before{content:"";position:absolute;inset:0;background:radial-gradient(circle at 30% 40%,transparent 0,#060607 60%)}
nav{position:relative;display:flex;justify-content:space-between;padding:28px 64px;font-size:14px;color:#8a8a8a}nav b{color:#fff;font-size:18px}
.w{position:relative;display:grid;grid-template-columns:1fr 1fr;gap:50px;padding:90px 64px 0;align-items:center}
.eb{font-size:13px;color:#c6ff3d;border:1px solid rgba(198,255,61,.3);padding:6px 12px;border-radius:6px;display:inline-block}
h1{font-size:76px;letter-spacing:-.045em;line-height:1;margin:26px 0 22px;font-weight:700}
p{font-size:19px;color:#9a9a9a;max-width:470px;margin-bottom:34px}
.cmd{display:inline-flex;gap:18px;align-items:center;padding:16px 20px;border:1px solid rgba(255,255,255,.14);border-radius:10px;background:#0e0e10;font-size:16px}
.cmd b{color:#c6ff3d;font-weight:400}.cmd span{font-size:12px;padding:4px 9px;border-radius:5px;background:#c6ff3d;color:#000}
.t{border:1px solid rgba(255,255,255,.12);border-radius:14px;background:#0c0c0e;box-shadow:0 40px 80px rgba(0,0,0,.6),0 0 0 1px rgba(198,255,61,.05)}
.t .h{display:flex;gap:8px;padding:14px 16px;border-bottom:1px solid rgba(255,255,255,.08)}.t .h i{width:11px;height:11px;border-radius:50%;background:#333}
.t pre{padding:22px;font-size:15px;line-height:1.9;color:#cfcfcf}.g{color:#c6ff3d}.mu{color:#666}.c{display:inline-block;width:9px;height:17px;background:#c6ff3d;vertical-align:-3px;animation:blink 1s steps(1) infinite}
</style>
<nav class="mono"><b>▲ tracer</b><span>docs &nbsp; changelog &nbsp; github ★ 18.2k &nbsp; pricing</span></nav>
<div class="w"><div><span class="eb mono">v2.0 — zero-config tracing</span><h1>See every request. Change nothing.</h1><p>Drop-in distributed tracing for Node, Go and Python. One line, no agents, no YAML.</p><div class="cmd mono"><b>$</b> npm i @tracer/node <span>COPY</span></div></div>
<div class="t mono"><div class="h"><i></i><i></i><i></i></div><pre><span class="g">$</span> npx tracer init
<span class="mu">✓ detected express@5, pg, redis</span>
<span class="mu">✓ instrumented 14 routes</span>
<span class="g">$</span> npm run dev
<span class="mu">→ trace</span> GET /checkout  <span class="g">42ms</span>
   ├─ pg.query      <span class="g">11ms</span>
   ├─ redis.get     <span class="g">2ms</span>
   └─ stripe.charge <span style="color:#ff6b6b">28ms ⚠</span>
<span class="g">$</span> <span class="c"></span></pre></div></div>"""

T["folio"] = BASE + """<style>
body{background:#f6f3ee;color:#141414}
nav{display:flex;justify-content:space-between;padding:32px 64px;font-size:15px}nav span{display:flex;gap:30px}
.av{display:inline-flex;gap:8px;align-items:center;font-size:14px;padding:6px 14px;border:1px solid rgba(0,0,0,.15);border-radius:99px}.av i{width:8px;height:8px;border-radius:50%;background:#2fb46b}
h1{font-size:118px;line-height:.95;letter-spacing:-.035em;font-weight:400;padding:40px 64px 0;animation:up 1s both}
h1 em{color:#e4572e}.meta{display:flex;gap:40px;padding:26px 64px;font-size:15px;color:#6b6b6b}
.cards{position:absolute;bottom:-60px;left:64px;right:64px;display:grid;grid-template-columns:1.3fr 1fr 1fr;gap:20px;align-items:end}
.cd{border-radius:14px;height:260px;position:relative;overflow:hidden}.cd span{position:absolute;left:16px;bottom:16px;font-size:13px;background:#fff;padding:6px 12px;border-radius:99px}
</style>
<nav><b class="serif" style="font-size:22px">Maya Lin·Park</b><span>Work About Contact</span></nav>
<div style="padding:0 64px"><span class="av"><i></i>Available from November</span></div>
<h1 class="serif">I design onboarding<br>that people <em><i>finish.</i></em></h1>
<div class="meta"><span>Senior UX Designer</span><span>Seoul · GMT+9</span><span>Previously at Fintech Co, Studio North</span></div>
<div class="cards">
<div class="cd" style="background:linear-gradient(135deg,#ffcfb8,#e4572e);height:300px"><span>Brightpay — +32% activation</span></div>
<div class="cd" style="background:linear-gradient(135deg,#cfd9c8,#5c7a5a)"><span>Habitly — Onboarding</span></div>
<div class="cd" style="background:linear-gradient(135deg,#d9d2f5,#5b4bb7);height:220px"><span>Loop — Design system</span></div></div>"""

T["tiers"] = BASE + """<style>
body{background:#09090d;color:#f4f4f7;text-align:center;padding-top:56px}
h2{font-size:58px;letter-spacing:-.04em}h2 em{font-weight:400}p{color:#9a9aab;font-size:18px;margin:12px 0 26px}
.tg{display:inline-flex;padding:5px;border:1px solid rgba(255,255,255,.1);border-radius:99px;font-size:15px;gap:4px}
.tg span{padding:9px 20px;border-radius:99px;color:#9a9aab}.tg .on{background:#fff;color:#000}.tg b{font-size:11px;background:#34d399;color:#022;padding:2px 7px;border-radius:99px;margin-left:6px}
.pl{display:grid;grid-template-columns:repeat(3,330px);gap:22px;justify-content:center;margin-top:40px;text-align:left}
.p{padding:30px;border-radius:22px;border:1px solid rgba(255,255,255,.09);background:#111118;position:relative}
.p.hot{border:1px solid transparent;background:linear-gradient(#111118,#111118) padding-box,linear-gradient(135deg,#8b5cf6,#22d3ee,#f472b6) border-box;transform:translateY(-12px);box-shadow:0 30px 80px -20px rgba(139,92,246,.5)}
.rb{position:absolute;top:-12px;left:30px;font-size:11px;font-weight:700;padding:4px 10px;border-radius:99px;background:linear-gradient(90deg,#8b5cf6,#f472b6)}
.a{font-size:52px;font-weight:700;letter-spacing:-.04em;margin:10px 0 0}.a small{font-size:16px;color:#9a9aab;font-weight:400}
ul{list-style:none;margin:22px 0;display:grid;gap:11px;font-size:15px;color:#cfcfdc}li::before{content:"✓  ";color:#34d399}
.bt{display:block;text-align:center;padding:13px;border-radius:99px;font-weight:600;border:1px solid rgba(255,255,255,.2)}
</style>
<h2>Pricing that <em class="serif"><i>scales</i></em> with you</h2><p>Start free. Upgrade when your team does.</p>
<div class="tg"><span>Monthly</span><span class="on">Yearly<b>SAVE 20%</b></span></div>
<div class="pl"><div class="p"><div style="color:#9a9aab">Starter</div><div class="a">$0<small> /mo</small></div><ul><li>3 projects</li><li>Basic analytics</li><li>Community support</li></ul><span class="bt">Start free</span></div>
<div class="p hot"><span class="rb">MOST POPULAR</span><div style="color:#9a9aab">Pro</div><div class="a">$24<small> /mo</small></div><ul><li>Unlimited projects</li><li>Advanced analytics</li><li>Priority support</li><li>Custom domains</li></ul><span class="bt" style="background:#fff;color:#000;border:0">Start 14-day trial</span></div>
<div class="p"><div style="color:#9a9aab">Team</div><div class="a">$59<small> /mo</small></div><ul><li>Everything in Pro</li><li>SSO & roles</li><li>Audit log</li></ul><span class="bt">Contact sales</span></div></div>"""

T["bento"] = BASE + """<style>
body{background:#07070a;color:#f4f4f7;padding:44px 56px}
h2{font-size:46px;letter-spacing:-.035em;margin-bottom:28px}h2 span{color:#5e5e6e}
.g{display:grid;grid-template-columns:repeat(4,1fr);grid-template-rows:260px 260px;gap:16px}
.t{background:#0e0e14;border:1px solid rgba(255,255,255,.08);border-radius:24px;padding:24px;position:relative;overflow:hidden}
.t small{color:#22d3ee;font-size:12px;letter-spacing:.12em}.t h3{font-size:20px;margin-top:6px;letter-spacing:-.01em}
.ui{position:absolute;left:24px;right:24px;bottom:24px;top:110px;display:grid;grid-template-columns:90px 1fr;gap:10px}
.ui i{background:rgba(255,255,255,.06);border-radius:8px;position:relative;overflow:hidden}.ui i::after{content:"";position:absolute;inset:0;background:linear-gradient(90deg,transparent,rgba(255,255,255,.1),transparent);transform:translateX(-100%);animation:shim 2s infinite}
.orb{position:absolute;right:30px;top:20px;width:210px;height:210px;border:1px dashed rgba(255,255,255,.15);border-radius:50%;animation:spin 14s linear infinite}
.orb i{position:absolute;width:30px;height:30px;border-radius:9px;background:#1c1c28;border:1px solid rgba(255,255,255,.15)}
.bars{position:absolute;right:24px;bottom:24px;display:flex;gap:8px;align-items:end;height:150px}.bars i{width:22px;border-radius:5px 5px 0 0;background:linear-gradient(#22d3ee,#8b5cf6);animation:grow 1.4s both;transform-origin:bottom}
.big{font-size:64px;font-weight:700;letter-spacing:-.04em;margin-top:40px}
.ring{position:absolute;left:50%;top:60%;width:60px;height:60px;margin:-30px;border-radius:50%;border:2px solid #f472b6;animation:pulse 2.2s infinite}
</style>
<h2>Everything you need. <span>Nothing you don't.</span></h2>
<div class="g">
<div class="t" style="grid-column:span 2;grid-row:span 2"><small>WORKSPACE</small><h3>One place for every project</h3><div class="ui"><i style="grid-row:span 4"></i><i></i><i style="background:rgba(139,92,246,.25)"></i><i></i><i></i></div></div>
<div class="t" style="grid-column:span 2"><small>INTEGRATIONS</small><h3>Plugs into 120+ tools</h3><div class="orb"><i style="left:-15px;top:90px"></i><i style="left:90px;top:-15px;background:#2a1f4d"></i><i style="right:-15px;top:90px"></i><i style="left:90px;bottom:-15px;background:#0f3240"></i></div></div>
<div class="t"><small>SPEED</small><h3>Blazing fast</h3><div class="big">38ms</div><div style="color:#5e5e6e">p95 latency</div></div>
<div class="t"><small>SECURITY</small><h3>SOC 2 Type II</h3><div class="ring"></div><div style="position:absolute;left:50%;top:60%;transform:translate(-50%,-50%);"><svg width="34" height="34" viewBox="0 0 24 24" fill="none" stroke="#f472b6" stroke-width="1.6"><rect x="4" y="11" width="16" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/></svg></div></div></div>"""
