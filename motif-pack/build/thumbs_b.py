# part B: prompts 07-12
from thumbs_a import BASE
T = {}

T["waitlist"] = BASE + """<style>
body{background:#060914;color:#fff;text-align:center;position:relative}
.m{position:absolute;inset:-20%;background:radial-gradient(40% 50% at 30% 30%,rgba(59,130,246,.55),transparent),radial-gradient(40% 50% at 70% 70%,rgba(236,72,153,.45),transparent);filter:blur(40px);animation:fl 10s ease-in-out infinite alternate}
.c{position:relative;padding-top:92px}
.pl{display:inline-block;padding:7px 16px;border:1px solid rgba(255,255,255,.2);border-radius:99px;font-size:14px;background:rgba(255,255,255,.06)}
h1{font-size:92px;letter-spacing:-.05em;line-height:1;margin:28px 0 20px}p{font-size:20px;color:rgba(255,255,255,.7)}
.f{margin:36px auto 0;width:540px;display:flex;padding:7px;border-radius:99px;background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.18);backdrop-filter:blur(10px)}
.f span{flex:1;text-align:left;padding:14px 20px;color:rgba(255,255,255,.45);font-size:16px}.f b{padding:14px 26px;border-radius:99px;background:#fff;color:#000}
.cd{display:flex;gap:18px;justify-content:center;margin-top:46px}.cd div{width:110px;padding:18px 0;border-radius:18px;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.12)}
.cd b{display:block;font-size:44px;font-variant-numeric:tabular-nums;letter-spacing:-.03em}.cd small{font-size:12px;letter-spacing:.14em;color:rgba(255,255,255,.55)}
.sp{margin-top:34px;font-size:15px;color:rgba(255,255,255,.7);display:flex;gap:12px;justify-content:center;align-items:center}
.sp i{width:30px;height:30px;border-radius:50%;border:2px solid #060914;margin-left:-10px;display:inline-block}
</style><div class="m"></div><div class="c"><span class="pl">Launching March 3</span><h1>Notes that write<br>themselves.</h1><p>The AI notebook for researchers. Join the early list.</p>
<div class="f"><span>you@work.com</span><b>Join the waitlist</b></div>
<div class="cd"><div><b>12</b><small>DAYS</small></div><div><b>08</b><small>HOURS</small></div><div><b>41</b><small>MIN</small></div><div><b>27</b><small>SEC</small></div></div>
<div class="sp"><span><i style="background:#fbbf24"></i><i style="background:#60a5fa"></i><i style="background:#f472b6"></i><i style="background:#34d399"></i></span>Join 2,400+ researchers already waiting</div></div>"""

T["vault"] = BASE + """<style>
body{background:#f7f7f4;color:#0f1115;font-family:'Avenir Next',Manrope,-apple-system,sans-serif}
nav{display:flex;justify-content:space-between;padding:28px 64px;font-size:15px}nav b{font-size:21px;color:#0f7b5f}
.w{display:grid;grid-template-columns:1.1fr 1fr;padding:50px 64px;align-items:center}
h1{font-size:86px;letter-spacing:-.045em;line-height:1}h1 span{color:#0f7b5f}
p{font-size:20px;color:#5d6068;margin:22px 0 32px;max-width:480px}
.st{display:flex;gap:12px}.st span{padding:14px 22px;border-radius:14px;background:#0f1115;color:#fff;font-size:15px;font-weight:600}
.rt{margin-top:22px;font-size:15px;color:#5d6068}
.ph{position:relative;width:300px;height:600px;margin:0 auto;border-radius:48px;background:#0f1115;padding:12px;box-shadow:0 50px 100px -30px rgba(15,123,95,.45);animation:bob 5s ease-in-out infinite}
.sc{height:100%;border-radius:38px;background:#fff;padding:26px 18px;overflow:hidden}
.bal{border-radius:22px;background:linear-gradient(135deg,#0f7b5f,#16a37e);color:#fff;padding:20px}.bal b{font-size:32px;display:block;margin-top:4px}
.tx{display:flex;justify-content:space-between;padding:12px 4px;border-bottom:1px solid #eee;font-size:14px}
.chip{position:absolute;background:#fff;padding:12px 16px;border-radius:16px;font-size:14px;font-weight:600;box-shadow:0 20px 40px rgba(0,0,0,.1);animation:bob 4s ease-in-out infinite}
</style><nav><b>● vault</b><span>Save · Spend · Invest · Security</span></nav>
<div class="w"><div><h1>Money that<br><span>grows quietly.</span></h1><p>Automatic savings, smart budgets and fee-free investing — in one calm app.</p><div class="st"><span> App Store</span><span>▶ Google Play</span></div><div class="rt">★★★★★ 4.9 from 12k reviews</div></div>
<div style="position:relative"><div class="ph"><div class="sc"><div style="font-size:13px;color:#888">Good morning, Dana</div>
<div class="bal" style="margin-top:12px"><small>Total balance</small><b>$12,480.20</b><small>▲ $240 this month</small></div>
<svg viewBox="0 0 100 100" style="width:150px;display:block;margin:20px auto"><circle cx="50" cy="50" r="38" fill="none" stroke="#eef3f1" stroke-width="12"/><circle cx="50" cy="50" r="38" fill="none" stroke="#0f7b5f" stroke-width="12" stroke-dasharray="160 240" stroke-linecap="round" transform="rotate(-90 50 50)"/><circle cx="50" cy="50" r="38" fill="none" stroke="#a7e3cc" stroke-width="12" stroke-dasharray="50 240" stroke-dashoffset="-165" stroke-linecap="round" transform="rotate(-90 50 50)"/></svg>
<div class="tx"><span>Coffee Lab</span><b>−$4.50</b></div><div class="tx"><span>Salary</span><b style="color:#0f7b5f">+$3,200</b></div><div class="tx"><span>Round-up saved</span><b style="color:#0f7b5f">+$0.50</b></div></div></div>
<div class="chip" style="left:10px;top:120px">+$240 saved this month</div><div class="chip" style="right:0;top:380px;animation-delay:-2s">Bill paid <span style="color:#0f7b5f">✓</span></div></div></div>"""

T["studio"] = BASE + """<style>
body{background:#0d0d0d;color:#f2f2f2;font-family:'Helvetica Neue',Arial,sans-serif}
.top{display:flex;justify-content:space-between;padding:26px 40px;font-size:14px;border-bottom:1px solid #2a2a2a;text-transform:uppercase;letter-spacing:.06em}
h1{font-size:236px;letter-spacing:-.06em;line-height:.85;padding:30px 30px 0;font-weight:800}
h1 span{display:inline-block;animation:up .8s both}
.row{display:flex;justify-content:space-between;padding:20px 40px;font-size:15px;text-transform:uppercase;letter-spacing:.06em;border-bottom:1px solid #2a2a2a}
.l{display:grid;grid-template-columns:60px 1fr 200px 80px;padding:18px 40px;border-bottom:1px solid #2a2a2a;align-items:center}
.l b{font-size:44px;letter-spacing:-.03em}.l.on b{color:#ff4d00}
.pv{position:absolute;right:250px;top:500px;width:220px;height:150px;border-radius:6px;background:linear-gradient(135deg,#ff4d00,#ffb199);transform:rotate(-4deg)}
</style><div class="top"><span>Northwall®</span><span>Work · Services · Studio · Contact</span><span>Oslo 14:32</span></div>
<h1><span>NORTH</span><span style="animation-delay:.1s;color:#ff4d00">WALL</span></h1>
<div class="row"><span>Brand & Digital — Oslo — Est. 2014</span><span>(Scroll)</span></div>
<div class="l mut"><span>01</span><b>Fjord Air</b><span>Rebrand</span><span>2026</span></div>
<div class="l on"><span>02</span><b>Kiln Coffee</b><span>Packaging, Web</span><span>2025</span></div>
<div class="l"><span>03</span><b>Aurel Bank</b><span>Product design</span><span>2025</span></div><div class="pv"></div>"""

T["drop"] = BASE + """<style>
body{background:#f1eef9;color:#16131f}
nav{display:flex;justify-content:space-between;padding:26px 60px;font-size:15px}nav b{font-size:20px}
.w{display:grid;grid-template-columns:1fr 1.2fr 1fr;padding:30px 60px;align-items:center;gap:30px}
h1{font-size:64px;letter-spacing:-.04em;line-height:1}.r{color:#6e6880;margin:14px 0}.pr{font-size:34px;font-weight:700}
.pd{position:relative;height:540px;display:grid;place-items:center}
.hp{position:relative;width:320px;height:360px;animation:bob 5s ease-in-out infinite}
.band{position:absolute;left:30px;right:30px;top:0;height:260px;border:34px solid #6d4aff;border-bottom:0;border-radius:160px 160px 0 0}
.cup{position:absolute;bottom:40px;width:110px;height:160px;border-radius:40px;background:linear-gradient(160deg,#8f73ff,#4b2fd6);box-shadow:inset -10px -10px 30px rgba(0,0,0,.25)}
.sh{position:absolute;bottom:40px;width:300px;height:30px;border-radius:50%;background:rgba(40,20,120,.18);filter:blur(10px)}
.sw{display:flex;gap:12px;margin:18px 0}.sw i{width:34px;height:34px;border-radius:50%;border:3px solid #fff;box-shadow:0 0 0 1px #ccc}
.sz{display:flex;gap:8px;margin-bottom:22px}.sz span{padding:10px 16px;border:1px solid #d3cde6;border-radius:10px}
.add{display:block;text-align:center;padding:16px;border-radius:99px;background:#16131f;color:#fff;font-weight:600}
.hs{position:absolute;width:18px;height:18px;border-radius:50%;background:#fff;box-shadow:0 0 0 6px rgba(255,255,255,.4)}
</style><nav><b>Hush</b><span>Shop · Tech · Reviews · Bag (1)</span></nav>
<div class="w"><div><h1>Hush One</h1><div class="r">Silence the noise. Keep the music.<br>★★★★★ 4.8 · 2,184 reviews</div><div class="pr">$249</div></div>
<div class="pd"><div class="sh"></div><div class="hp"><div class="band"></div><div class="cup" style="left:0"></div><div class="cup" style="right:0"></div></div><i class="hs" style="left:140px;top:180px"></i><i class="hs" style="right:120px;top:330px"></i></div>
<div><b>Color — Violet</b><div class="sw"><i style="background:#6d4aff;box-shadow:0 0 0 2px #16131f"></i><i style="background:#16131f"></i><i style="background:#e8e3d6"></i><i style="background:#9fd4c3"></i></div>
<b>Fit</b><div class="sz" style="margin-top:10px"><span>S</span><span style="border-color:#16131f">M</span><span>L</span></div><span class="add">Add to bag — $249</span><div class="r" style="font-size:14px">Free shipping · 30-day returns</div></div></div>"""

T["summit"] = BASE + """<style>
body{background:#07060c;color:#fff;position:relative}
.bg{position:absolute;inset:0;background:linear-gradient(120deg,#ff3d77 0%,#6b2cff 60%,#07060c 100%);opacity:.9}
.rg{position:absolute;right:-160px;top:-160px;width:900px;height:900px;border-radius:50%;border:1px solid rgba(255,255,255,.25);animation:spin 40s linear infinite}
.rg::before,.rg::after{content:"";position:absolute;inset:110px;border-radius:50%;border:1px dashed rgba(255,255,255,.3)}.rg::after{inset:230px;border-style:solid}
.c{position:relative;padding:44px 64px}.top{display:flex;justify-content:space-between;font-size:15px;font-weight:600}
h1{font-family:'Arial Narrow','Helvetica Neue',sans-serif;font-stretch:condensed;font-size:190px;line-height:.85;letter-spacing:-.03em;margin-top:60px;text-transform:uppercase;font-weight:800}
.i{display:flex;gap:40px;font-size:20px;margin:26px 0 30px}.b{display:flex;gap:12px}.b span{padding:16px 28px;border-radius:99px;font-weight:700}
.sp{position:absolute;right:64px;bottom:50px;display:flex;gap:14px}.sp div{text-align:center;font-size:13px}
.sp i{display:block;width:92px;height:92px;border-radius:50%;margin-bottom:8px;border:3px solid rgba(255,255,255,.8);background:linear-gradient(135deg,#ffd6e3,#8a63ff);filter:grayscale(.3)}
</style><div class="bg"></div><div class="rg"></div><div class="c"><div class="top"><span>◎ SUMMIT/27</span><span>Speakers · Schedule · Venue · Tickets</span></div>
<h1>Design<br>Summit 27</h1><div class="i"><span>▣ May 14–15, 2027</span><span>◉ Lisbon + Online</span><span>40+ speakers</span></div>
<div class="b"><span style="background:#fff;color:#000">Get tickets</span><span style="border:1px solid rgba(255,255,255,.5)">Add to calendar</span></div></div>
<div class="sp"><div><i></i>Ana Ruiz</div><div><i style="background:linear-gradient(135deg,#ffe0b2,#ff3d77)"></i>Kenji Ito</div><div><i style="background:linear-gradient(135deg,#c7f0ff,#6b2cff)"></i>Lea Vogt</div></div>"""

T["horizon"] = BASE + """<style>
body{background:#030308;color:#fff;text-align:center;position:relative}
.arc{position:absolute;left:50%;top:420px;width:1800px;height:900px;margin-left:-900px;border-radius:50%;background:radial-gradient(closest-side,rgba(99,102,241,.0) 70%,rgba(129,140,248,.9) 72%,rgba(56,189,248,.35) 76%,transparent 84%);filter:blur(4px)}
.gl{position:absolute;left:50%;top:380px;width:1100px;height:300px;margin-left:-550px;background:radial-gradient(ellipse at 50% 100%,rgba(99,102,241,.55),transparent 70%)}
.st i{position:absolute;width:2px;height:2px;background:#fff;border-radius:50%;animation:blink 3s infinite}
h2{position:relative;font-size:92px;letter-spacing:-.05em;padding-top:120px}p{position:relative;color:#9aa0c0;font-size:20px;margin:18px 0 32px}
.b{position:relative;display:flex;gap:12px;justify-content:center}.b span{padding:15px 28px;border-radius:99px;font-weight:600}
.ft{position:absolute;left:0;right:0;bottom:0;height:230px;background:#05050c;border-top:1px solid rgba(255,255,255,.07);display:grid;grid-template-columns:1.4fr 1fr 1fr 1fr;text-align:left;padding:34px 64px;font-size:14px;color:#8a8fae;gap:20px}
.ft b{color:#fff;display:block;margin-bottom:10px}.wm{position:absolute;left:0;right:0;bottom:-70px;font-size:250px;font-weight:800;letter-spacing:-.06em;color:rgba(255,255,255,.05);line-height:1}
</style><div class="gl"></div><div class="arc"></div>
<div class="st"><i style="left:120px;top:90px"></i><i style="left:340px;top:200px;animation-delay:-1s"></i><i style="left:980px;top:120px;animation-delay:-2s"></i><i style="left:1150px;top:260px"></i><i style="left:700px;top:60px;animation-delay:-1.5s"></i><i style="left:520px;top:300px"></i></div>
<h2>Ready when you are.</h2><p>Start building in minutes. No credit card required.</p><div class="b"><span style="background:#fff;color:#000">Get started</span><span style="border:1px solid rgba(255,255,255,.25)">Talk to sales</span></div>
<div class="ft"><div><b>Lumen</b>Infrastructure for curious teams.<br><br><span style="color:#34d399">●</span> All systems normal</div><div><b>Product</b>Features<br>Pricing<br>Changelog</div><div><b>Company</b>About<br>Careers<br>Blog</div><div><b>Legal</b>Privacy<br>Terms<br>Security</div><div class="wm">LUMEN</div></div>"""
