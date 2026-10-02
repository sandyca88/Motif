# part E: prompts 13-20
from thumbs_a import BASE
T = {}

T["pinboard"] = BASE + """<style>
body{background:#EFE6D8;color:#1D1B18;position:relative}
.c{position:absolute;background:#fff;box-shadow:0 10px 24px rgba(60,40,20,.16);padding:22px}
.pin{position:absolute;top:-10px;left:50%;width:22px;height:22px;border-radius:50%;background:#E4572E;box-shadow:inset -3px -3px 0 rgba(0,0,0,.2)}
.tp{position:absolute;width:90px;height:26px;background:rgba(244,197,66,.6);top:-12px}
.mono{font-family:'Courier New',monospace}
h1{font-size:64px;letter-spacing:-.04em;line-height:.95}
.st{display:inline-block;margin-top:14px;border:3px solid #6CA6E0;color:#3f7fc0;padding:4px 10px;font:700 14px 'Courier New',monospace;transform:rotate(-3deg)}
.btn{display:inline-block;margin:16px 8px 0 0;padding:9px 14px;border-radius:99px;background:#1D1B18;color:#fff;font-size:14px}
.pol{padding:12px 12px 44px}.pol div{width:220px;height:170px}.pol span{position:absolute;left:16px;bottom:12px;font:22px 'Bradley Hand','Segoe Print',cursive}
.chip{display:inline-block;padding:7px 12px;border-radius:99px;margin:4px;font-size:14px;font-weight:600}
</style>
<div class="c" style="left:70px;top:60px;width:520px;transform:rotate(-1.5deg)"><i class="pin"></i><h1>Jun Seo<br>Kim</h1><div style="margin-top:10px;font-size:18px">Product Designer · Busan → Remote</div><span class="st">AVAILABLE FROM JAN</span><br><span class="btn">Email</span><span class="btn" style="background:#fff;color:#1D1B18;border:1px solid #1D1B18">Download PDF</span></div>
<div class="c" style="left:660px;top:70px;width:250px;transform:rotate(2deg)"><i class="tp" style="left:80px"></i><div class="mono" style="font-size:13px;color:#888">2023 — NOW</div><b style="font-size:20px">Lead Designer, Tidal Pay</b><div style="font-size:14px;margin-top:8px">• Cut checkout steps 7 → 3<br>• +19% conversion</div></div>
<div class="c pol" style="left:960px;top:90px;transform:rotate(4deg)"><i class="pin" style="background:#6CA6E0"></i><div style="background:linear-gradient(135deg,#F4C542,#E4572E)"></div><span>Tidal checkout</span></div>
<div class="c pol" style="left:120px;top:430px;transform:rotate(-3deg)"><i class="tp" style="left:70px"></i><div style="background:linear-gradient(135deg,#6CA6E0,#2f4b8a)"></div><span>Harbor app</span></div>
<div class="c" style="left:430px;top:440px;width:360px;transform:rotate(1deg)"><div class="mono" style="font-size:13px;color:#888;margin-bottom:8px">SKILLS</div><span class="chip" style="background:#FDE7C0">Research</span><span class="chip" style="background:#D6E8FA">Prototyping</span><span class="chip" style="background:#FAD4CB">Design systems</span><span class="chip" style="background:#E3F1D9">Figma</span><span class="chip" style="background:#EEE">Workshops</span></div>
<div class="c" style="left:850px;top:470px;width:300px;background:#FFF3A8;transform:rotate(-2deg);font:22px/1.3 'Bradley Hand','Segoe Print',cursive">"Jun turns messy problems into calm products." <div style="font-size:16px;margin-top:8px">— Head of Product</div></div>"""

T["spread"] = BASE + """<style>
body{background:#F6F4EF;color:#151515;font-family:Georgia,serif;position:relative}
.m{position:absolute;left:50px;right:50px;top:24px;border-bottom:3px double #151515;display:flex;justify-content:space-between;align-items:end;padding-bottom:8px}
.m b{font:700 78px/1 'Didot','Bodoni 72',Georgia,serif;letter-spacing:-.03em}.m span{font:600 13px -apple-system,sans-serif;letter-spacing:.18em}
.c{position:absolute;background:#fff;box-shadow:0 14px 30px rgba(0,0,0,.12);padding:12px}
.c .im{background:#2B50FF;mix-blend-mode:normal}.c .im::after{content:"";display:block;height:100%;background:linear-gradient(135deg,rgba(255,255,255,.35),rgba(0,0,0,.25))}
.k{font:700 11px -apple-system,sans-serif;letter-spacing:.18em;color:#2B50FF;margin-top:10px}.c h3{font-size:24px;line-height:1.05;margin-top:4px;letter-spacing:-.01em}
</style>
<div class="m"><b>Almanac</b><span>ISSUE 12 · OBJECTS · OCTOBER 2026</span></div>
<div class="c" style="left:70px;top:170px;width:470px;transform:rotate(-2deg);z-index:3"><div class="im" style="height:300px;background:linear-gradient(135deg,#c9b79c,#6b5a45)"></div><div class="k">LEAD STORY</div><h3 style="font-size:38px">The last chair makers of the valley</h3></div>
<div class="c" style="left:500px;top:150px;width:280px;transform:rotate(3deg)"><div class="im" style="height:180px;background:linear-gradient(135deg,#9fb3c8,#2B50FF)"></div><div class="k">PLACES</div><h3>A library that only lends tools</h3></div>
<div class="c" style="left:820px;top:170px;width:380px;transform:rotate(-1deg)"><div class="im" style="height:220px;background:linear-gradient(135deg,#e7c6b0,#b05b3b)"></div><div class="k">PEOPLE</div><h3>She repairs 400 radios a year</h3></div>
<div class="c" style="left:560px;top:440px;width:300px;transform:rotate(-3deg);z-index:2"><div class="im" style="height:170px;background:linear-gradient(135deg,#d7dcc8,#56624a)"></div><div class="k">IDEAS</div><h3>Why objects outlive their makers</h3></div>
<div class="c" style="left:900px;top:500px;width:280px;transform:rotate(2deg)"><div class="k" style="margin:0">IN FOCUS</div><h3 style="font-size:30px;font-style:italic">"Nothing is thrown away, only forgotten."</h3></div>"""

T["gate"] = BASE + """<style>
body{display:grid;grid-template-columns:45% 55%;background:#fff;color:#0f1115}
.l{position:relative;background:#0b1020;color:#fff;padding:50px;overflow:hidden}
.l::before{content:"";position:absolute;inset:-20%;background:radial-gradient(40% 40% at 30% 30%,#4f46e5,transparent),radial-gradient(40% 40% at 70% 70%,#0ea5e9,transparent);filter:blur(30px);opacity:.8}
.l>*{position:relative}.q{position:absolute;left:50px;right:50px;bottom:60px;font-size:24px;line-height:1.4}
.r{display:grid;place-items:center}.f{width:400px}
h2{font-size:34px;letter-spacing:-.03em}.mu{color:#6b7280;font-size:15px;margin:6px 0 24px}
.sso{display:flex;align-items:center;justify-content:center;gap:10px;border:1px solid #e5e7eb;border-radius:12px;height:46px;margin-bottom:10px;font-weight:600;font-size:15px}
.or{display:flex;align-items:center;gap:12px;color:#9ca3af;font-size:13px;margin:18px 0}.or::before,.or::after{content:"";flex:1;height:1px;background:#e5e7eb}
label{font-size:14px;font-weight:600;display:block;margin-bottom:6px}.in{height:46px;border:1px solid #d1d5db;border-radius:12px;padding:0 14px;display:flex;align-items:center;justify-content:space-between;color:#111;font-size:15px;margin-bottom:6px}
.in.foc{border:2px solid #4f46e5;box-shadow:0 0 0 4px rgba(79,70,229,.15)}.hint{font-size:13px;color:#16a34a;margin-bottom:14px}
.meter{display:flex;gap:4px;margin:8px 0 4px}.meter i{flex:1;height:5px;border-radius:3px;background:#16a34a}.meter i:last-child{background:#e5e7eb}
.btn{height:48px;border-radius:12px;background:#4f46e5;color:#fff;display:grid;place-items:center;font-weight:700;margin-top:18px}
</style>
<div class="l"><b style="font-size:22px">◆ Northstar</b><div class="q">"Setup took four minutes. Our whole team was in before lunch."<div style="font-size:15px;opacity:.7;margin-top:10px">Priya N., Ops Lead at Fernway</div></div></div>
<div class="r"><div class="f"><h2>Create your account</h2><div class="mu">Free for 14 days. No card needed.</div>
<div class="sso">G &nbsp;Continue with Google</div><div class="sso">▦ &nbsp;Continue with Microsoft</div><div class="or">or continue with email</div>
<label>Work email</label><div class="in">dana@fernway.com</div><div class="hint">✓ Looks good</div>
<label>Password</label><div class="in foc">•••••••••••<span style="font-size:13px;color:#4f46e5;font-weight:600">Show</span></div>
<div class="meter"><i></i><i></i><i></i><i></i></div><div style="font-size:13px;color:#6b7280">Strong password · ✓ 8+ characters ✓ number ✓ symbol</div>
<div class="btn">Create account</div></div></div>"""

T["console"] = BASE + """<style>
body{background:#fafafa;color:#111;display:flex;font-size:14px}
.nav{width:240px;padding:34px 20px;border-right:1px solid #eee;background:#fff}.nav b{display:block;font-size:18px;margin-bottom:24px}
.nav div{padding:9px 12px;border-radius:8px;color:#666;margin-bottom:2px}.nav .on{background:#f1f0ff;color:#4f46e5;font-weight:600}.nav .dz{color:#dc2626}
.c{flex:1;padding:34px 60px;position:relative}.card{background:#fff;border:1px solid #eee;border-radius:14px;padding:22px 24px;margin-bottom:16px;max-width:760px}
h3{font-size:17px}.mu{color:#777;margin:4px 0 16px}
table{width:100%;border-collapse:collapse}td,th{padding:10px 6px;text-align:left;border-top:1px solid #f0f0f0}th{font-size:12px;color:#888;font-weight:600;border:0}
.sw{width:36px;height:20px;border-radius:99px;background:#4f46e5;position:relative;display:inline-block}.sw::after{content:"";position:absolute;right:2px;top:2px;width:16px;height:16px;border-radius:50%;background:#fff}.sw.off{background:#ddd}.sw.off::after{right:auto;left:2px}
.bar{position:absolute;left:60px;right:60px;bottom:26px;max-width:760px;background:#111;color:#fff;border-radius:14px;padding:14px 18px;display:flex;justify-content:space-between;align-items:center;box-shadow:0 16px 40px rgba(0,0,0,.2)}
.bar span{padding:8px 14px;border-radius:9px}
</style>
<div class="nav"><b>Settings</b><div>Profile</div><div>Account & security</div><div class="on">Notifications</div><div>Team members</div><div>Billing</div><div>API keys</div><div class="dz">Danger zone</div></div>
<div class="c"><div class="card"><h3>Notifications</h3><div class="mu">Choose how you hear about activity in Fernway.</div>
<table><tr><th>EVENT</th><th>EMAIL</th><th>PUSH</th><th>IN-APP</th></tr>
<tr><td>Mentions & replies</td><td><i class="sw"></i></td><td><i class="sw"></i></td><td><i class="sw"></i></td></tr>
<tr><td>Task assigned to me</td><td><i class="sw"></i></td><td><i class="sw off"></i></td><td><i class="sw"></i></td></tr>
<tr><td>Weekly summary</td><td><i class="sw"></i></td><td><i class="sw off"></i></td><td><i class="sw off"></i></td></tr>
<tr><td>Billing & invoices</td><td><i class="sw"></i></td><td><i class="sw off"></i></td><td><i class="sw off"></i></td></tr></table></div>
<div class="card" style="border-color:#fecaca"><h3 style="color:#dc2626">Delete workspace</h3><div class="mu" style="margin-bottom:0">Type <b>fernway</b> to confirm. This can't be undone.</div></div>
<div class="bar">You have unsaved changes<div><span>Discard</span><span style="background:#fff;color:#111;font-weight:600">Save changes</span></div></div></div>"""

T["parley"] = BASE + """<style>
body{background:#0f0f11;color:#ececf1;display:flex;font-size:15px}
.sb{width:250px;background:#0a0a0c;border-right:1px solid rgba(255,255,255,.06);padding:20px 14px}
.nb{border:1px solid rgba(255,255,255,.12);border-radius:10px;padding:10px 12px;margin-bottom:18px;font-weight:600}
.gr{font-size:12px;color:#777;margin:14px 8px 6px}.it{padding:8px 10px;border-radius:8px;color:#bbb;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}.it.on{background:#1c1c21;color:#fff}
.mn{flex:1;position:relative}.col{width:720px;margin:0 auto;padding-top:40px}
.u{margin-left:auto;width:max-content;max-width:480px;background:#232329;padding:12px 16px;border-radius:18px;margin-bottom:24px}
.a{display:flex;gap:14px}.av{flex:none;width:30px;height:30px;border-radius:9px;background:conic-gradient(#8b5cf6,#22d3ee,#f472b6,#8b5cf6)}
.tl{border:1px solid rgba(255,255,255,.1);border-radius:12px;padding:10px 14px;font-size:13px;color:#aaa;margin-bottom:12px}.tl div{margin:4px 0}.ok{color:#34d399}
pre{background:#0a0a0c;border:1px solid rgba(255,255,255,.1);border-radius:12px;padding:12px 14px;font:13px ui-monospace,Menlo,monospace;color:#b9f5ff;margin:10px 0;position:relative}
pre span{position:absolute;right:10px;top:8px;font-size:11px;color:#888}
.ci{display:inline-block;font-size:11px;padding:1px 7px;border-radius:99px;background:#26262d;color:#a78bfa;margin-left:3px}
.cp{position:absolute;left:50%;bottom:26px;width:720px;margin-left:-360px;background:#1a1a1f;border:1px solid rgba(255,255,255,.12);border-radius:20px;padding:14px 16px}
.cp .ch{display:inline-block;padding:5px 10px;border-radius:8px;background:#26262d;font-size:12px;margin-bottom:10px}
.cp .row{display:flex;justify-content:space-between;color:#777}.cp .go{width:34px;height:34px;border-radius:50%;background:#fff;color:#000;display:grid;place-items:center;font-weight:700}
</style>
<div class="sb"><div class="nb">＋ New chat</div><div class="gr">Today</div><div class="it on">Q3 churn analysis</div><div class="it">Rewrite onboarding email</div><div class="gr">Previous 7 days</div><div class="it">Pricing page copy ideas</div><div class="it">SQL for weekly actives</div><div class="it">Interview synthesis</div></div>
<div class="mn"><div class="col"><div class="u">Why did churn spike in August? Use the CRM export.</div>
<div class="a"><i class="av"></i><div style="flex:1"><div class="tl"><div class="ok">✓ Read crm_export_aug.csv</div><div class="ok">✓ Ran cohort analysis</div><div>◌ Checking support tickets…</div></div>
Churn rose from <b>3.1% → 4.6%</b>, driven almost entirely by accounts on the legacy plan after the price change <span class="ci">1</span> <span class="ci">2</span>
<pre><span>python · copy</span>df.groupby("plan")["churned"].mean()</pre></div></div></div>
<div class="cp"><span class="ch">📎 crm_export_aug.csv ×</span><div style="color:#ddd;margin-bottom:10px">Draft a win-back email for legacy-plan accounts</div><div class="row"><span>＋ &nbsp; Analyst mode ▾</span><span class="go">↑</span></div></div></div>"""

T["manual"] = BASE + """<style>
body{background:#fff;color:#1a1a1a;font-size:14px}
.top{height:56px;border-bottom:1px solid #eee;display:flex;align-items:center;padding:0 24px;gap:28px}.top b{font-size:17px}.top .s{margin-left:auto;width:260px;height:34px;border:1px solid #e5e5e5;border-radius:9px;display:flex;align-items:center;justify-content:space-between;padding:0 10px;color:#999}
.w{display:grid;grid-template-columns:230px 1fr 200px;height:744px}
.nv{border-right:1px solid #eee;padding:20px}.nv .g{font-size:12px;font-weight:700;color:#999;margin:16px 0 6px}.nv div{padding:5px 8px;border-radius:6px;color:#555}.nv .on{background:#eef4ff;color:#2563eb;font-weight:600}
.ct{padding:30px 50px}.bc{color:#999;font-size:13px}h1{font-size:36px;letter-spacing:-.03em;margin:8px 0 10px}
.co{border-left:4px solid #2563eb;background:#f5f8ff;border-radius:8px;padding:12px 16px;margin:16px 0;color:#1e3a8a}
.tb{display:flex;gap:4px;margin-top:16px}.tb span{padding:7px 12px;border-radius:8px 8px 0 0;font-size:13px;color:#888}.tb .on{background:#0f172a;color:#fff}
pre{background:#0f172a;color:#e2e8f0;border-radius:0 10px 10px 10px;padding:16px;font:13px/1.7 ui-monospace,Menlo,monospace}
.st{display:flex;gap:14px;margin-top:18px}.st i{flex:none;width:26px;height:26px;border-radius:50%;background:#2563eb;color:#fff;font-style:normal;display:grid;place-items:center;font-weight:700;font-size:13px}
.toc{padding:30px 16px;border-left:1px solid #eee;color:#777}.toc div{padding:4px 0}.toc .on{color:#2563eb;font-weight:600}
</style>
<div class="top"><b>▲ Relay Docs</b><span>Guides</span><span>API reference</span><span>Changelog</span><div class="s">Search docs <span>⌘K</span></div></div>
<div class="w"><div class="nv"><div class="g">GETTING STARTED</div><div class="on">Quickstart</div><div>Authentication</div><div>Core concepts</div><div class="g">GUIDES</div><div>Webhooks</div><div>Pagination</div><div>Errors</div></div>
<div class="ct"><div class="bc">Getting started / Quickstart</div><h1>Quickstart</h1><div style="color:#555">Make your first API call in under 5 minutes.</div>
<div class="co">ℹ You'll need an API key from Settings → API keys.</div>
<div class="st"><i>1</i><div><b>Install the SDK</b></div></div>
<div class="tb"><span class="on">cURL</span><span>JavaScript</span><span>Python</span></div>
<pre><span style="color:#7dd3fc">curl</span> https://api.relay.dev/v1/messages \\
  -H <span style="color:#86efac">"Authorization: Bearer $RELAY_KEY"</span> \\
  -d <span style="color:#86efac">'{"to":"+15550100","text":"Hello"}'</span></pre></div>
<div class="toc"><b style="color:#111">On this page</b><div class="on">Install the SDK</div><div>Authenticate</div><div>Send a message</div><div>Next steps</div></div></div>"""

T["lost"] = BASE + """<style>
body{background:#FBF7F1;color:#1f1d1a;display:grid;grid-template-columns:1.2fr 1fr;align-items:center;padding:0 90px;gap:40px}
h1{font-size:150px;letter-spacing:-.06em;line-height:.9;color:#E4572E}h2{font-size:40px;letter-spacing:-.03em;margin:10px 0}p{font-size:19px;color:#6b645a;max-width:460px}
.s{margin-top:24px;display:flex;border:1px solid #d8d0c3;border-radius:14px;background:#fff;height:52px;align-items:center;padding:0 16px;color:#999;width:440px}
.l{display:flex;gap:10px;margin-top:16px;flex-wrap:wrap}.l span{padding:8px 14px;border-radius:99px;background:#fff;border:1px solid #e6dfd3;font-size:15px}
.path{stroke-dasharray:10 12;animation:dash 3s linear infinite}@keyframes dash{to{stroke-dashoffset:-44}}
</style>
<div><h1>404</h1><h2>This page wandered off.</h2><p>The link may be old or mistyped. Try searching, or jump to a popular page.</p><div class="s">Search Fernway…</div>
<div class="l"><span>Pricing</span><span>Docs</span><span>Templates</span><span>Help center</span></div></div>
<svg viewBox="0 0 400 400" width="460"><rect x="30" y="50" width="340" height="300" rx="24" fill="#F2E3CB"/><path d="M30 150 L140 110 L260 160 L370 120" stroke="#E7D3B3" stroke-width="18" fill="none"/>
<path class="path" d="M70 300 C120 260 110 200 180 200 S260 250 300 180" stroke="#1f1d1a" stroke-width="5" fill="none" stroke-linecap="round"/><circle cx="70" cy="300" r="10" fill="#1F8A8A"/>
<circle cx="310" cy="150" r="42" fill="#E4572E"/><text x="310" y="168" font-size="52" font-weight="800" text-anchor="middle" fill="#fff" font-family="-apple-system,sans-serif">?</text></svg>"""

T["pocket"] = BASE + """<style>
body{background:#101014;display:flex;gap:40px;justify-content:center;align-items:center}
.ph{width:290px;height:620px;border-radius:46px;background:#000;padding:10px;box-shadow:0 40px 80px rgba(0,0,0,.5)}
.sc{height:100%;border-radius:38px;overflow:hidden;position:relative;padding:54px 22px 22px;font-size:14px}
.b{position:absolute;left:22px;right:22px;bottom:26px;height:52px;border-radius:16px;display:grid;place-items:center;font-weight:700;font-size:16px}
.ch{display:inline-block;padding:10px 14px;border-radius:99px;margin:0 6px 10px 0;border:1.5px solid #ddd;font-weight:600}.ch.on{background:#1b1b1f;color:#fff;border-color:#1b1b1f}
.dots{display:flex;gap:6px;justify-content:center;margin-top:18px}.dots i{width:7px;height:7px;border-radius:99px;background:#ccc}.dots i.on{width:22px;background:#FF7A45}
</style>
<div class="ph"><div class="sc" style="background:linear-gradient(180deg,#FFB38A,#FF7A45);color:#2a120a">
<svg viewBox="0 0 200 200" width="240" style="display:block;margin:40px auto 0"><circle cx="100" cy="100" r="80" fill="#FFE1CF"/><rect x="60" y="60" width="80" height="100" rx="18" fill="#fff"/><rect x="72" y="76" width="56" height="10" rx="5" fill="#FF7A45"/><rect x="72" y="94" width="40" height="8" rx="4" fill="#f2c6b0"/><rect x="72" y="110" width="48" height="8" rx="4" fill="#f2c6b0"/><circle cx="150" cy="60" r="16" fill="#1b1b1f"/><path d="M143 60l5 5 9-10" stroke="#fff" stroke-width="3" fill="none"/></svg>
<h2 style="font-size:30px;letter-spacing:-.03em;margin-top:30px">Meals planned<br>in 60 seconds.</h2><p style="margin-top:8px;opacity:.8">Tell us what you like. We'll do the rest.</p>
<div class="b" style="background:#1b1b1f;color:#fff">Get started</div></div></div>
<div class="ph"><div class="sc" style="background:#fff;color:#1b1b1f"><div style="font-size:12px;color:#999;font-weight:700;letter-spacing:.1em">STEP 2 OF 4</div><div style="height:5px;border-radius:3px;background:#eee;margin:8px 0 20px"><div style="width:50%;height:100%;border-radius:3px;background:#FF7A45"></div></div>
<h2 style="font-size:26px;letter-spacing:-.03em;margin-bottom:18px">What brings you here?</h2>
<span class="ch on">Eat healthier</span><span class="ch">Save money</span><span class="ch on">Cook faster</span><span class="ch">Less waste</span><span class="ch">Family meals</span><span class="ch">Try new food</span>
<div class="b" style="background:#FF7A45;color:#fff">Continue</div></div></div>
<div class="ph"><div class="sc" style="background:#FFF6F0;color:#1b1b1f"><h2 style="font-size:24px;letter-spacing:-.03em">Your first plan is ready</h2><p style="color:#777;margin:6px 0 16px">Based on "healthier" + "faster"</p>
<div style="background:#fff;border-radius:18px;padding:14px;box-shadow:0 10px 24px rgba(0,0,0,.06);margin-bottom:10px"><b>Mon · Lemon salmon bowl</b><div style="color:#999">20 min · 540 kcal</div></div>
<div style="background:#fff;border-radius:18px;padding:14px;box-shadow:0 0 0 3px #FF7A45;margin-bottom:10px;position:relative"><b>Tue · Miso veggie noodles</b><div style="color:#999">15 min · 480 kcal</div><div style="position:absolute;right:-8px;top:-34px;background:#1b1b1f;color:#fff;font-size:12px;padding:6px 10px;border-radius:10px">Tap to swap a meal</div></div>
<div class="dots"><i></i><i class="on"></i><i></i></div></div></div>"""
