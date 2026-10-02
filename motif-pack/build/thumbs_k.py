# part K: prompts 45-47 (fallback coded previews; replaced by real images when available)
from thumbs_a import BASE
T = {}
T["ronin"] = BASE + """<style>body{background:#0b0606;color:#f3ead9;position:relative;overflow:hidden;font-family:'Arial Narrow','Helvetica Neue',sans-serif}
.sky{position:absolute;inset:0;background:linear-gradient(180deg,#2a0d0d,#0b0606 70%)}.sun{position:absolute;right:230px;top:120px;width:380px;height:380px;border-radius:50%;background:radial-gradient(circle,#e0412f,#9b1d17 70%);box-shadow:0 0 120px rgba(224,65,47,.5)}
.mtn{position:absolute;left:0;right:0;bottom:0;height:360px;background:#130909;clip-path:polygon(0 60%,15% 30%,28% 55%,42% 20%,58% 50%,72% 25%,86% 48%,100% 30%,100% 100%,0 100%)}
h1{position:absolute;left:60px;top:230px;font-size:230px;font-weight:900;letter-spacing:-.02em;color:#f3ead9;text-shadow:0 10px 40px rgba(0,0,0,.6)}
.hero{position:absolute;left:760px;top:170px;width:170px;height:520px}.hero .hd{width:60px;height:70px;border-radius:30px 30px 24px 24px;background:#e8dcc6;margin-left:55px}.hero .hr{position:absolute;left:30px;top:-10px;width:120px;height:60px;border-radius:50%;background:#f1f1f1}
.hero .bd{width:170px;height:330px;margin-top:6px;background:linear-gradient(180deg,#1a1a1a,#3a0f0f);clip-path:polygon(30% 0,70% 0,100% 100%,0 100%)}.hero .sc{position:absolute;left:150px;top:40px;width:10px;height:420px;background:#c9c2b2;transform:rotate(18deg)}
.p{position:absolute;width:14px;height:10px;border-radius:60% 0;background:#f4a6b8;opacity:.8;animation:bob 4s ease-in-out infinite}
.ui{position:absolute;left:60px;bottom:60px;display:flex;gap:14px;font:700 15px -apple-system,sans-serif}.ui span{padding:14px 22px;border-radius:4px}
</style><div class="sky"></div><div class="sun"></div><div class="mtn"></div><h1>RONIN DAWN</h1><div class="hero"><div class="hr"></div><div class="hd"></div><div class="bd"></div><div class="sc"></div></div>""" + "".join(f'<i class="p" style="left:{x}px;top:{y}px;animation-delay:-{d}s"></i>' for x,y,d in [(120,80,1),(300,160,2),(520,60,0),(900,100,3),(1100,260,1),(1180,520,2),(640,600,0),(220,560,3)]) + """<div class="ui"><span style="background:#e0412f;color:#fff">Wishlist now</span><span style="border:1px solid rgba(243,234,217,.5)">▶ Watch trailer</span><span style="opacity:.7;padding-top:16px">Coming Spring 2027 · PC · Console</span></div>"""
T["nova"] = BASE + """<style>body{background:#F2735A;color:#fff;position:relative;overflow:hidden;font-family:'Inter Tight','Helvetica Neue',-apple-system,sans-serif}
nav{display:flex;justify-content:space-between;align-items:center;padding:28px 56px;font-size:14px}nav b{font-size:26px;letter-spacing:-.03em}nav span{display:flex;gap:30px;opacity:.9}nav i{font-style:normal;padding:10px 16px;border:1.5px solid #fff}
.k{position:absolute;left:56px;top:190px;font:600 12px ui-monospace,Menlo,monospace;letter-spacing:.18em;opacity:.85}h1{position:absolute;left:56px;top:220px;font-size:104px;letter-spacing:-.055em;line-height:.95;font-weight:700}
p{position:absolute;left:56px;top:460px;width:460px;font-size:18px;opacity:.92}.cta{position:absolute;left:56px;top:540px;display:flex;gap:18px;align-items:center}.cta span{padding:16px 24px;background:#fff;color:#1b1b1b;font-weight:700}.cta b{width:44px;height:44px;border-radius:50%;border:1.5px solid #fff;display:grid;place-items:center;font-size:14px}
.obj{position:absolute;right:170px;top:170px;width:360px;height:320px;border-radius:90px;background:linear-gradient(145deg,#fff,#dcdfe2);box-shadow:inset -20px -26px 40px rgba(0,0,0,.12),0 50px 80px rgba(120,30,10,.35);transform:rotate(-12deg);animation:bob 6s ease-in-out infinite}
.obj::before{content:"";position:absolute;left:70px;top:60px;width:210px;height:190px;border-radius:50%;background:radial-gradient(circle at 40% 35%,#3fb3a7,#0F5E5A 55%,#062a28);box-shadow:inset 0 0 0 16px #0b3f3c}
.base{position:absolute;right:160px;top:520px;width:380px;height:70px;border-radius:40px;background:linear-gradient(180deg,#ff9b6a,#e2582e);box-shadow:0 30px 50px rgba(120,30,10,.35)}
.chip{position:absolute;padding:10px 14px;background:#fff;color:#333;border-radius:8px;font-size:13px;box-shadow:0 10px 24px rgba(0,0,0,.12)}
.sp{position:absolute;border-radius:50%;background:radial-gradient(circle at 30% 30%,#fff3b0,#c9a227)}.ft{position:absolute;left:56px;right:56px;bottom:26px;border-top:1px solid rgba(255,255,255,.35);padding-top:12px;display:flex;justify-content:space-between;font:12px ui-monospace,Menlo,monospace;opacity:.85}
</style><nav><b>● nova</b><span>Platform · How it works · Pricing</span><i>Try Nova ↗</i></nav><div class="k">A CALMER WAY TO GET THINGS DONE</div><h1>Fewer tabs.<br>More focus.</h1><p>Nova turns scattered tasks into one calm daily plan, so you can think, create and finish.</p>
<div class="cta"><span>Plan my day ↗</span><b>▶</b><small>See Nova in action</small></div><div class="base"></div><div class="obj"></div>
<span class="chip" style="right:470px;top:170px">✓ Inbox sorted</span><span class="chip" style="right:110px;top:470px">● 3 tasks planned</span><i class="sp" style="right:560px;top:430px;width:50px;height:50px"></i><i class="sp" style="right:90px;top:250px;width:30px;height:30px;background:#fff"></i>
<div class="ft"><span>01 / MEET NOVA</span><span>SCROLL TO EXPLORE ↓</span></div>"""
T["tidewater"] = BASE + """<style>body{background:#FBFBF8;color:#111;font-family:'Helvetica Neue',Arial,sans-serif;position:relative}
nav{display:flex;justify-content:space-between;align-items:center;padding:20px 40px;font-size:11px;letter-spacing:.14em}nav b{font-size:18px;letter-spacing:0}nav i{font-style:normal;padding:10px 16px;border-radius:99px;background:#0E2A47;color:#fff}
.lb{position:absolute;font:10px ui-monospace,Menlo,monospace;letter-spacing:.14em;color:#555;line-height:1.6}
.sk{position:absolute;left:40px;right:40px;top:80px;height:420px}
.sk svg{width:100%;height:100%}
h1{position:absolute;left:40px;top:560px;font-size:70px;letter-spacing:-.05em;line-height:.95;font-weight:500;color:#0E2A47}
.mid{position:absolute;left:560px;top:570px;width:320px;font-size:14px;color:#444;border-left:1px solid #ddd;padding-left:20px}.mid b{display:block;color:#111;margin-bottom:6px}
.pl{position:absolute;right:60px;top:590px;width:56px;height:56px;border-radius:50%;background:#0E2A47;color:#fff;display:grid;place-items:center}
.ct{position:absolute;left:40px;bottom:26px;font:11px ui-monospace,Menlo,monospace;display:flex;gap:10px;align-items:center}.ct i{display:block;width:80px;height:2px;background:#ddd}.ct i::after{content:"";display:block;width:25%;height:100%;background:#0E2A47}
</style><nav><b>≋ TIDEWATER</b><span style="display:flex;gap:26px">EXPERIENCE · PROJECTS · DESIGN · PROCESS · ABOUT</span><i>REQUEST A QUOTE →</i></nav>
<div class="lb" style="left:40px;top:90px">DESIGNED ·<br>BUILT ·<br>WARRANTED</div><div class="lb" style="right:40px;top:90px;text-align:right">CALM ·<br>DURABLE ·<br>YOURS</div>
<div class="sk"><svg viewBox="0 0 1200 420" fill="none" stroke="#1a1a1a" stroke-width="1.4">
<path d="M170 330 L1030 330 L1120 400 L80 400 Z" fill="#f1f3f4"/>""" + "".join(f'<path d="M{110+i*36} 400 L{190+i*32} 330" stroke-opacity=".35"/>' for i in range(28)) + """
<path d="M220 340 L980 340 L1050 392 L150 392 Z" fill="#dfe8ec"/>""" + "".join(f'<path d="M{170+i*60} 380 q20 -6 40 0" stroke="#5b7c8c" stroke-opacity=".7"/>' for i in range(14)) + """
<rect x="470" y="150" width="260" height="10" fill="#1a1a1a"/><path d="M480 160 V330 M720 160 V330 M540 160 V330 M660 160 V330"/>""" + "".join(f'<path d="M{480+i*12} 150 V160"/>' for i in range(22)) + """
<g stroke-opacity=".8"><circle cx="160" cy="170" r="90"/><circle cx="120" cy="200" r="60"/><circle cx="210" cy="210" r="55"/><path d="M165 260 V330"/></g>
<g stroke-opacity=".8"><circle cx="1060" cy="160" r="85"/><circle cx="1010" cy="210" r="55"/><circle cx="1110" cy="205" r="50"/><path d="M1060 250 V330"/></g>
<path d="M860 200 q60 -40 120 0" /><path d="M920 200 V330"/><path d="M820 320 L900 300 L980 320" /><path d="M300 320 L380 300 L440 320"/>""" + "".join(f'<path d="M{60+i*8} {230+(i%5)*6} l6 -14" stroke-opacity=".5"/>' for i in range(30)) + """</svg></div>
<h1>Your backyard,<br>reimagined.</h1><div class="mid"><b>Pools and outdoor spaces, designed around you.</b>Thoughtful design, lasting materials and a simpler way to build the space you'll love.<br><br><span style="font:11px ui-monospace,Menlo,monospace;letter-spacing:.14em;color:#0E2A47">EXPLORE OUR WORK →</span></div><div class="pl">▶</div>
<div class="ct"><span>01 / 04</span><i></i></div>"""

T["meridian"] = BASE + """<style>body{background:#FBFBF8;display:grid;place-items:center;font:600 40px Georgia,serif;color:#13254A}</style>Meridian"""
T["jade"] = BASE + """<style>body{background:#1b2a24;display:grid;place-items:center;font:700 60px Georgia,serif;color:#F4EBDD}</style>Jade Pavilion"""
T["aero"] = BASE + """<style>body{background:#DCEBFA;display:grid;place-items:center;font:700 60px -apple-system,sans-serif;color:#0E1726}</style>AERO"""
T["ember1"] = BASE + """<style>body{background:#E36A4C;display:grid;place-items:center;font:700 60px -apple-system,sans-serif;color:#fff}</style>Ember One"""
T["lumenfold"] = BASE + """<style>body{background:#F5F5F7;display:grid;place-items:center;font:600 70px -apple-system,sans-serif;color:#1D1D1F}</style>Lumen Fold"""
T["lumora"] = BASE + """<style>body{background:linear-gradient(#f6e6dc,#e9dff0);display:grid;place-items:center;font:300 70px -apple-system,sans-serif;color:#1B1530}</style>Lumora"""
T["softwork"] = BASE + """<style>body{background:#F5E0CF;display:grid;place-items:center;font:900 70px -apple-system,sans-serif;color:#2A1A14}</style>softwork"""
T["concord"] = BASE + """<style>body{background:#f4f4f4;display:grid;place-items:center;font:300 70px -apple-system,sans-serif;color:#111}</style>Built together."""
T["aipipe"] = BASE + """<style>body{background:#0b0b10;display:grid;place-items:center;font:700 60px -apple-system,sans-serif;color:#fff}</style>AI Art Pipeline"""
T["uupm"] = BASE + """<style>body{background:#111827;display:grid;place-items:center;font:700 60px -apple-system,sans-serif;color:#fff}</style>UI UX Pro Max"""
T["mascotkit"] = BASE + """<style>
body{background:#0b0b0c;color:#f5f5f7;font-family:-apple-system,Inter,sans-serif;padding:46px 56px}
.k{font:600 14px ui-monospace,Menlo,monospace;letter-spacing:.14em;color:#a78bfa}h1{font-size:54px;letter-spacing:-.04em;margin:8px 0 34px}
.row{display:grid;grid-template-columns:1fr 1.5fr;gap:26px}.st{height:440px;border-radius:26px;background:radial-gradient(circle at 50% 30%,rgba(139,92,246,.22),transparent 60%),#141416;border:1px solid rgba(255,255,255,.08);display:grid;place-items:center;position:relative}
.m{--s:150px;position:relative;width:var(--s);height:var(--s);border-radius:31%;background:conic-gradient(from 210deg,#8b5cf6,#22d3ee,#f472b6,#8b5cf6);box-shadow:inset 0 -10px 22px rgba(0,0,0,.25),inset 0 8px 16px rgba(255,255,255,.35),0 18px 44px rgba(139,92,246,.4)}
.m i{position:absolute;top:36%;width:18%;height:24%;border-radius:50%;background:#fff}.m i::after{content:"";position:absolute;left:30%;top:28%;width:52%;height:48%;border-radius:50%;background:#0b0b10;box-shadow:inset 3px 3px 0 -1px #fff}
.m i:first-child{left:27%}.m i:last-child{left:55%}
.mo{animation:mo 6s cubic-bezier(.65,0,.35,1) infinite}@keyframes mo{0%,20%{border-radius:31%}33%,53%{border-radius:50%}66%,86%{border-radius:50% 50% 28% 28%/60% 60% 40% 40%}}
.f{display:flex;gap:22px;align-items:flex-end}.f .m{--s:92px;animation:hop 2.4s ease-in-out infinite}
.f .a{background:radial-gradient(circle at 35% 30%,#7df0ff,#06b6d4);border-radius:50%}.f .b{animation-delay:-.6s}.f .c{background:radial-gradient(circle at 35% 30%,#ff9fd0,#ec4899);border-radius:50% 50% 30% 30%/62% 62% 38% 38%;animation-delay:-1.2s}.f .d{background:radial-gradient(circle at 35% 30%,#86efac,#10b981);border-radius:99px;width:130px;animation-delay:-1.8s}
@keyframes hop{0%,60%,100%{transform:none}70%{transform:translateY(-16px) scale(1.04,.96)}80%{transform:scale(1.06,.94)}}
.lab{position:absolute;bottom:18px;font:600 13px ui-monospace,Menlo,monospace;color:#8e8e96;letter-spacing:.1em}
.ty{position:absolute;top:22px;right:22px;display:flex;gap:5px;padding:10px 12px;border-radius:14px;background:#1d1d22}.ty b{width:8px;height:8px;border-radius:50%;background:#a1a1aa;animation:dt 1.2s infinite}.ty b:nth-child(2){animation-delay:.15s}.ty b:nth-child(3){animation-delay:.3s}@keyframes dt{30%{transform:translateY(-5px);background:#fff}}
</style><div class="k">ANIMATED MASCOT LOGO KIT</div><h1>Give your logo a personality.</h1>
<div class="row"><div class="st"><div class="m mo"><i></i><i></i></div><span class="lab">B · MORPH</span></div>
<div class="st"><div class="ty"><b></b><b></b><b></b></div><div class="f"><div class="m a"><i></i><i></i></div><div class="m b"><i></i><i></i></div><div class="m c"><i></i><i></i></div><div class="m d"><i></i><i></i></div></div><span class="lab">C · FAMILY</span></div></div>"""
