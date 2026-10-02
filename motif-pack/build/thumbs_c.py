# part C: skill end-result thumbnails
from thumbs_a import BASE
T = {}
DOC = """<style>body{background:#0b0b10;color:#ececf1;padding:40px 56px}.card{background:#12121a;border:1px solid rgba(255,255,255,.08);border-radius:18px;padding:24px}
.mut{color:#8b8b9a}.tag{font-size:12px;font-weight:700;padding:3px 9px;border-radius:6px}.agent{display:flex;gap:10px;align-items:center;font-size:14px;color:#8b8b9a;margin-bottom:18px}
.agent i{width:24px;height:24px;border-radius:7px;background:conic-gradient(#8b5cf6,#22d3ee,#f472b6,#8b5cf6)}</style>"""

T["audit"] = BASE + DOC + """<style>body{zoom:1.18}
.g{display:grid;grid-template-columns:360px 1fr;gap:22px}
.sc{font-size:110px;font-weight:700;letter-spacing:-.05em;line-height:1}.sc small{font-size:34px;color:#8b8b9a}
.gr{display:inline-block;margin-top:8px;font-size:15px;padding:5px 12px;border-radius:99px;background:rgba(52,211,153,.14);color:#34d399}
.ln{display:grid;grid-template-columns:140px 1fr 30px;gap:10px;align-items:center;margin:11px 0;font-size:14px}
.ln i{height:8px;border-radius:4px;background:rgba(255,255,255,.07);position:relative}.ln i b{position:absolute;inset:0;border-radius:4px;background:linear-gradient(90deg,#8b5cf6,#22d3ee);animation:grow 1s both;transform-origin:left}
.f{padding:16px 0;border-bottom:1px solid rgba(255,255,255,.07)}.f h4{font-size:17px;margin:6px 0 4px}
code{display:block;margin-top:10px;font-family:ui-monospace,Menlo,monospace;font-size:13px;background:#0b0b10;border:1px solid rgba(255,255,255,.08);border-radius:8px;padding:10px 12px;color:#b9f5ff}
</style><div class="agent"><i></i>ux-heuristic-audit · checkout.html</div>
<div class="g"><div class="card"><div class="mut">Overall score</div><div class="sc">31<small>/40</small></div><span class="gr">Grade B</span>
<div style="margin-top:22px"><div class="ln"><span>Clarity</span><i><b style="width:90%"></b></i><span>5</span></div><div class="ln"><span>Hierarchy</span><i><b style="width:70%"></b></i><span>4</span></div><div class="ln"><span>Action & flow</span><i><b style="width:60%"></b></i><span>3</span></div><div class="ln"><span>States</span><i><b style="width:50%"></b></i><span>3</span></div><div class="ln"><span>Consistency</span><i><b style="width:85%"></b></i><span>4</span></div><div class="ln"><span>Accessibility</span><i><b style="width:45%"></b></i><span>3</span></div></div></div>
<div class="card"><b style="font-size:19px">Findings</b>
<div class="f"><span class="tag" style="background:rgba(248,113,113,.15);color:#f87171">P0</span><h4>CTA text fails contrast (3.1:1)</h4><div class="mut">Where: .btn-pay · Target ≥ 4.5:1</div><code>.btn-pay { background:#5b21b6; color:#fff; } /* 8.6:1 */</code></div>
<div class="f"><span class="tag" style="background:rgba(251,191,36,.15);color:#fbbf24">P1</span><h4>Two equal-weight CTAs split attention</h4><div class="mut">Where: hero + nav "Sign up" · Make nav ghost style</div></div>
<div class="f" style="border:0"><span class="tag" style="background:rgba(139,92,246,.15);color:#a78bfa">P2</span><h4>Spacing off 8px scale in form group</h4><div class="mut">Where: .field + .field (13px → 16px)</div></div></div></div>"""

T["micro"] = BASE + DOC + """<style>body{zoom:1.38}
table{width:100%;border-collapse:collapse;font-size:16px}th{text-align:left;font-size:12px;letter-spacing:.1em;color:#8b8b9a;padding:12px 16px;font-weight:600}
td{padding:18px 16px;border-top:1px solid rgba(255,255,255,.07);vertical-align:top}.old{color:#8b8b9a;text-decoration:line-through;text-decoration-color:rgba(248,113,113,.6)}
.new{color:#fff;font-weight:500}.new span{display:inline-block;padding:8px 16px;border-radius:99px;background:#fff;color:#000;font-weight:600;font-size:14px}
.v{display:flex;gap:10px;margin-bottom:20px}.v span{padding:8px 14px;border-radius:99px;border:1px solid rgba(255,255,255,.12);font-size:14px}
</style><div class="agent"><i></i>microcopy-writer · settings + billing screens</div>
<h2 style="font-size:36px;letter-spacing:-.03em;margin-bottom:14px">Voice: confident, plain, warm</h2>
<div class="v"><span>Confident, not cocky</span><span>Plain, not dumbed-down</span><span>Warm, not cute</span></div>
<div class="card" style="padding:8px"><table><tr><th>LOCATION</th><th>CURRENT</th><th>SUGGESTED</th></tr>
<tr><td class="mut">Primary button</td><td class="old">Submit</td><td class="new"><span>Save changes</span></td></tr>
<tr><td class="mut">Card error</td><td class="old">Error: invalid input</td><td class="new">Your card number looks short. Check the last 4 digits.</td></tr>
<tr><td class="mut">Empty state</td><td class="old">No data</td><td class="new">No invoices yet. They'll appear here after your first payment.</td></tr>
<tr><td class="mut">Delete dialog</td><td class="old">Are you sure? OK / Cancel</td><td class="new">Delete "Q3 Report"? This can't be undone. <b style="color:#f87171">Delete report</b></td></tr></table></div>"""

T["taste"] = BASE + """<style>
body{display:grid;grid-template-columns:1fr 1fr;background:#000}
.s{position:relative;overflow:hidden;padding:40px}.lb{position:absolute;top:22px;left:22px;font-size:13px;font-weight:700;padding:6px 12px;border-radius:99px;z-index:2}
.a{background:#eef0f6;font-family:Arial,sans-serif;color:#222}.a .hero{margin-top:70px;text-align:center;padding:40px;border-radius:16px;background:linear-gradient(90deg,#6366f1,#3b82f6);color:#fff}
.a h1{font-size:40px}.a p{font-size:16px;margin:10px 0 20px}.a .btn{display:inline-block;padding:12px 22px;border-radius:12px;background:#fff;color:#4f46e5;font-weight:700;box-shadow:0 10px 20px rgba(0,0,0,.2)}
.a .cards{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin-top:22px}.a .cards div{background:#fff;border-radius:16px;padding:20px;box-shadow:0 10px 25px rgba(0,0,0,.12);text-align:center;font-size:14px}
.b{background:#0a0a0b;color:#f2f2f2;border-left:2px solid #fff}
.b::before{content:"";position:absolute;inset:0;background:radial-gradient(circle at 80% 0,rgba(198,255,61,.12),transparent 50%)}
.b .eb{margin-top:80px;font-family:ui-monospace,Menlo,monospace;font-size:13px;color:#c6ff3d}
.b h1{position:relative;font-size:60px;letter-spacing:-.045em;line-height:1;margin:18px 0}.b h1 em{font-family:'Iowan Old Style',Georgia,serif;font-weight:400}
.b p{color:#8f8f99;font-size:17px;max-width:420px}.b .row{display:flex;gap:10px;margin-top:26px}.b .row span{padding:13px 22px;border-radius:99px;font-weight:600;font-size:15px}
.b .bn{display:grid;grid-template-columns:2fr 1fr;gap:12px;margin-top:40px}.b .bn div{border:1px solid rgba(255,255,255,.09);border-radius:14px;height:150px;padding:16px;font-size:13px;color:#8f8f99}
</style>
<div class="s a"><span class="lb" style="background:#f87171;color:#fff">BEFORE — default AI</span><div class="hero"><h1>🚀 Welcome to AppName</h1><p>The best solution for all your needs</p><span class="btn">Get Started Now!</span></div>
<div class="cards"><div>⚡<br><b>Fast</b><br>Lorem ipsum dolor</div><div>🔒<br><b>Secure</b><br>Lorem ipsum dolor</div><div>💡<br><b>Smart</b><br>Lorem ipsum dolor</div></div></div>
<div class="s b"><span class="lb" style="background:#c6ff3d;color:#000">AFTER — taste-layer</span><div class="eb">Direction: Precision · Signature: serif accent</div>
<h1>Ship reviews in<br><em>half</em> the time.</h1><p>Async code review with AI summaries your team actually reads.</p>
<div class="row"><span style="background:#fff;color:#000">Start free</span><span style="border:1px solid rgba(255,255,255,.18)">See how it works</span></div>
<div class="bn"><div>PR summary · 3 files · risk: low</div><div>−48% review time</div></div></div>"""

T["motionhero"] = BASE + """<style>
body{background:#05050a;color:#fff;position:relative}
.r{position:absolute;left:430px;top:400px;border-radius:50%;border:1px solid rgba(34,211,238,.5);margin:-150px 0 0 -150px;animation:pulse 4s ease-out infinite}
.core{position:absolute;left:430px;top:400px;width:90px;height:90px;margin:-45px;border-radius:26px;background:conic-gradient(#22d3ee,#8b5cf6,#f472b6,#22d3ee);animation:spin 6s linear infinite;box-shadow:0 0 90px rgba(34,211,238,.6)}
.c{position:absolute;left:80px;top:90px;width:700px}
h1{font-size:78px;letter-spacing:-.045em;line-height:1}h1 span{background:linear-gradient(90deg,#22d3ee,#a78bfa);-webkit-background-clip:text;color:transparent}
.panel{position:absolute;right:50px;top:60px;width:350px;background:rgba(18,18,26,.85);border:1px solid rgba(255,255,255,.1);border-radius:20px;padding:24px;backdrop-filter:blur(10px)}
.panel h4{font-family:ui-monospace,Menlo,monospace;font-size:13px;color:#22d3ee;margin-bottom:18px}
.k{margin-bottom:18px;font-size:14px}.k div{display:flex;justify-content:space-between;color:#a0a0b0;margin-bottom:8px}.k div b{color:#fff;font-family:ui-monospace,Menlo,monospace;font-weight:400}
.k i{display:block;height:4px;border-radius:2px;background:rgba(255,255,255,.1);position:relative}.k i::after{content:"";position:absolute;left:0;top:0;bottom:0;width:var(--w);border-radius:2px;background:linear-gradient(90deg,#22d3ee,#8b5cf6)}
.k i::before{content:"";position:absolute;left:var(--w);top:50%;width:14px;height:14px;margin:-7px;border-radius:50%;background:#fff}
.sw{display:flex;gap:8px}.sw span{width:28px;height:28px;border-radius:8px}
.cn{position:absolute;left:80px;bottom:60px;font-family:ui-monospace,Menlo,monospace;font-size:14px;color:#8b8b9a}
</style><div class="r" style="width:300px;height:300px"></div><div class="r" style="width:300px;height:300px;animation-delay:-1.3s"></div><div class="r" style="width:300px;height:300px;animation-delay:-2.6s"></div><div class="core"></div>
<div class="c"><h1>Infra that<br><span>moves with you.</span></h1></div>
<div class="panel"><h4>// tuning knobs</h4><div class="k"><div>--ring-speed<b>4s</b></div><i style="--w:40%"></i></div><div class="k"><div>--glow-intensity<b>0.6</b></div><i style="--w:60%"></i></div><div class="k"><div>--blur<b>6px</b></div><i style="--w:30%"></i></div><div class="k"><div>--stagger<b>80ms</b></div><i style="--w:50%"></i></div>
<div class="k"><div>--palette</div><div class="sw"><span style="background:#22d3ee"></span><span style="background:#8b5cf6"></span><span style="background:#f472b6"></span></div></div></div>
<div class="cn">concept: Orbit + Word rotator · reduced-motion ✓ · hero JS 6.2KB</div>"""

T["dash"] = BASE + DOC + """<style>
.g{display:grid;grid-template-columns:380px 1fr;gap:22px;height:640px}
.q{padding:13px 0;border-bottom:1px solid rgba(255,255,255,.07);font-size:15px;display:flex;gap:12px}.q b{color:#22d3ee;font-family:ui-monospace,Menlo,monospace}
.wf{display:grid;grid-template-columns:repeat(4,1fr);grid-template-rows:90px 220px 1fr;gap:12px;height:100%}
.wf div{border:1px dashed rgba(255,255,255,.2);border-radius:12px;padding:12px;font-size:12px;color:#8b8b9a;font-family:ui-monospace,Menlo,monospace;position:relative}
.wf .k{border-style:solid;background:#15151f}.wf .k b{display:block;font-family:-apple-system,sans-serif;font-size:24px;color:#fff;margin-top:6px}
</style><div class="agent"><i></i>dashboard-architect · Dashboard brief → layout</div>
<div class="g"><div class="card"><b style="font-size:20px">Dashboard brief</b><div class="mut" style="margin:8px 0 14px">Audience: Head of Sales · Cadence: daily</div>
<div class="q"><b>Q1</b>Are we on track for the monthly target?</div><div class="q"><b>Q2</b>Which reps or regions are slipping?</div><div class="q"><b>Q3</b>Which deals need action today?</div>
<div style="margin-top:20px;font-size:14px" class="mut">Q1 → KPI tile + target line<br>Q2 → sorted horizontal bar<br>Q3 → alert table by urgency</div></div>
<div class="wf"><div class="k">KPI · Bookings<b>$1.24M</b></div><div class="k">KPI · Target<b>82%</b></div><div class="k">KPI · Win rate<b>27%</b></div><div class="k">KPI · Cycle<b>31d</b></div>
<div style="grid-column:span 3">line chart · bookings vs target (8/12)<svg viewBox="0 0 400 120" style="position:absolute;left:12px;right:12px;bottom:10px;width:calc(100% - 24px);height:150px"><path d="M0 100 C60 90 100 70 160 72 S260 40 320 30 S380 20 400 14" stroke="#22d3ee" stroke-width="3" fill="none"/><line x1="0" y1="30" x2="400" y2="30" stroke="#f472b6" stroke-dasharray="6 6"/></svg></div>
<div>bar · by region (4/12)</div><div style="grid-column:span 4">table · deals needing action — sorted by urgency · states: loading / empty / error</div></div></div>"""

T["onboard"] = BASE + DOC + """<style>body{zoom:1.45;padding-top:50px}
.g{display:grid;grid-template-columns:1fr 420px;gap:26px}
.fl{display:flex;align-items:center;gap:0;margin:30px 0}.n{padding:14px 18px;border-radius:14px;background:#15151f;border:1px solid rgba(255,255,255,.1);font-size:14px;white-space:nowrap}
.n.a{border-color:#34d399;background:rgba(52,211,153,.1)}.ln{width:34px;height:2px;background:linear-gradient(90deg,#8b5cf6,#22d3ee)}
.m{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}.m div{background:#12121a;border:1px solid rgba(255,255,255,.08);border-radius:14px;padding:18px}.m b{font-size:30px;display:block}
.ck{background:#fff;color:#111;border-radius:20px;padding:26px;box-shadow:0 40px 80px -20px rgba(139,92,246,.5)}
.pb{height:8px;border-radius:4px;background:#eee;margin:12px 0 18px;overflow:hidden}.pb i{display:block;height:100%;width:40%;background:linear-gradient(90deg,#8b5cf6,#22d3ee)}
.it{display:flex;gap:12px;align-items:center;padding:13px 0;border-top:1px solid #f0f0f0;font-size:15px}
.it i{width:22px;height:22px;border-radius:50%;border:2px solid #ccc;display:grid;place-items:center;font-size:12px;font-style:normal}.it.d i{background:#34d399;border-color:#34d399;color:#fff}.it.d span{text-decoration:line-through;color:#999}
</style><div class="agent"><i></i>onboarding-flow-designer · analytics SaaS</div>
<div class="g"><div><h2 style="font-size:40px;letter-spacing:-.03em">Sign-up → aha in <span style="color:#34d399">4 steps</span></h2><div class="mut" style="margin-top:8px">Aha: sees first report with their own data · Activation: 1 source + 1 report in 24h</div>
<div class="fl"><span class="n">SSO sign-up</span><span class="ln"></span><span class="n">2-question survey</span><span class="ln"></span><span class="n">Connect source</span><span class="ln"></span><span class="n a">First report ✓</span></div>
<div class="m"><div><span class="mut">Steps cut</span><b>9 → 4</b></div><div><span class="mut">Time to aha</span><b>~6 min</b></div><div><span class="mut">Emails</span><b>3</b></div></div></div>
<div class="ck"><b style="font-size:19px">Get set up</b><div style="color:#777;font-size:14px">2 of 5 done</div><div class="pb"><i></i></div>
<div class="it d"><i>✓</i><span>Create your account</span></div><div class="it d"><i>✓</i><span>Tell us your goal</span></div><div class="it"><i></i><b>Connect Google Ads</b></div><div class="it"><i></i>See your first report</div><div class="it"><i></i>Invite a teammate</div></div></div>"""
