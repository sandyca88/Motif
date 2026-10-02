# part M: prompts 56-64 (original genre templates) — coded previews
from thumbs_a import BASE
import math, random
T = {}
NAV = lambda logo, links, cta, col="#fff", st="": f'<nav style="position:absolute;left:0;right:0;top:0;display:flex;justify-content:space-between;align-items:center;padding:30px 56px;color:{col};font-size:14px;z-index:3;{st}"><b style="font-size:22px;letter-spacing:-.02em">{logo}</b><span style="display:flex;gap:28px;opacity:.8">{"".join(f"<i style=font-style:normal>{l}</i>" for l in links)}</span>{cta}</nav>'

# 56 Northbound
T["northbound"] = BASE + """<style>body{background:linear-gradient(180deg,#f2c9c0 0%,#cfd9e6 38%,#a9c6d3 60%,#0e2230 100%);position:relative;overflow:hidden;color:#fff}
.ice{position:absolute;left:0;right:0;bottom:0;height:300px;background:#0e2230}
.f{position:absolute;bottom:250px;height:40px;background:#eef3f6;border-radius:40% 50% 10% 10%;box-shadow:0 12px 0 rgba(0,0,0,.18)}
.ship{position:absolute;right:300px;bottom:285px;width:260px;height:44px;background:#18242c;clip-path:polygon(0 0,100% 0,92% 100%,6% 100%)}.ship::before{content:"";position:absolute;left:70px;top:-36px;width:110px;height:36px;background:#f4f6f7;clip-path:polygon(8% 0,100% 0,100% 100%,0 100%)}
.mtn{position:absolute;left:0;right:0;bottom:290px;height:150px;background:#dfe7ee;opacity:.7;clip-path:polygon(0 100%,10% 40%,22% 70%,35% 20%,50% 60%,64% 30%,78% 65%,90% 35%,100% 60%,100% 100%)}
h1{position:absolute;left:56px;top:190px;font:400 88px/0.98 'Iowan Old Style',Georgia,serif;letter-spacing:-.02em;color:#0e2230;max-width:620px}
.c{position:absolute;right:56px;top:110px;font:600 12px ui-monospace,Menlo,monospace;letter-spacing:.14em;color:#0e2230;opacity:.7}
.btn{position:absolute;left:56px;top:420px;padding:16px 26px;background:#E8642C;color:#fff;font-weight:700;border-radius:4px}
.strip{position:absolute;left:56px;right:56px;bottom:40px;display:flex;justify-content:space-between;font:600 13px ui-monospace,Menlo,monospace;letter-spacing:.12em;border-top:1px solid rgba(255,255,255,.25);padding-top:18px}
</style><div class="mtn"></div><div class="f" style="left:80px;width:220px"></div><div class="f" style="left:380px;width:120px"></div><div class="f" style="left:640px;width:180px"></div><div class="f" style="right:80px;width:140px"></div><div class="ship"></div><div class="ice"></div>""" + NAV("NORTHBOUND", ["Voyages", "Ships", "Journal"], '<i style="font-style:normal;padding:10px 16px;border:1px solid #0e2230">Plan a voyage</i>', "#0e2230") + """<div class="c">78°13′N 15°38′E</div><h1>Go where the map goes quiet.</h1><div class="btn">Plan a voyage →</div><div class="strip"><span>WATER −1.4°C</span><span>DAYLIGHT 21H</span><span>NEXT DEPARTURE 41 DAYS</span></div>"""

# 57 Prism Bench
rays = "".join(f'<div style="position:absolute;left:690px;top:400px;width:620px;height:3px;background:{c};transform-origin:0 50%;transform:rotate({a}deg);filter:blur(.4px);box-shadow:0 0 14px {c};opacity:.9"></div>' for a, c in zip(range(-14, 16, 4), ["#ff3b3b", "#ff8a1f", "#ffd21f", "#4cff6a", "#38E1FF", "#4f6bff", "#FF3DCB", "#b04dff"]))
T["prismbench"] = BASE + """<style>body{background:#07080A;background-image:radial-gradient(#1a1d24 1px,transparent 1px);background-size:16px 16px;color:#e9edf2;position:relative;overflow:hidden}
.beam{position:absolute;left:0;top:420px;width:640px;height:3px;background:#fff;box-shadow:0 0 18px #fff;transform:rotate(-4deg);transform-origin:100% 50%}
.pr{position:absolute;left:600px;top:300px;width:200px;height:200px;background:linear-gradient(135deg,rgba(255,255,255,.35),rgba(140,200,255,.08));clip-path:polygon(50% 0,100% 100%,0 100%);border:0;filter:drop-shadow(0 0 20px rgba(56,225,255,.4))}
h1{position:absolute;left:56px;top:150px;font-size:76px;font-weight:700;letter-spacing:-.045em;line-height:.98;max-width:560px}
.m{position:absolute;left:56px;top:330px;font:600 13px ui-monospace,Menlo,monospace;letter-spacing:.1em;color:#38E1FF}
.btn{position:absolute;left:56px;bottom:90px;padding:15px 22px;border:1px solid #38E1FF;color:#38E1FF;border-radius:8px;font-weight:600}
.card{position:absolute;right:56px;bottom:70px;width:280px;padding:18px;background:#101217;border:1px solid #1E222A;border-radius:12px;font:500 13px ui-monospace,Menlo,monospace;line-height:1.9;color:#9aa3ad}
</style><div class="beam"></div>""" + rays + """<div class="pr"></div>""" + NAV("Prism Bench", ["Components", "Configurator", "Lessons"], '<i style="font-style:normal;padding:10px 16px;background:#e9edf2;color:#07080A;border-radius:8px">Get a quote</i>') + """<h1>Bend light. Measure everything.</h1><div class="m">λ 532 nm · f/2.8 · ±0.01 mm</div><div class="btn">Configure a bench →</div><div class="card">ANGLE 41.8°<br>n(λ) 1.519<br>DISPERSION 0.0082</div>"""

# 58 Wobble Co.
T["wobble"] = BASE + """<style>body{background:#FFF7EC;color:#2B1B3A;position:relative;overflow:hidden}
h1{position:absolute;left:56px;top:170px;font-size:118px;font-weight:900;letter-spacing:-.05em;line-height:.9}
.blob{position:absolute;right:120px;top:140px;width:470px;height:420px;background:radial-gradient(circle at 35% 30%,#ffd1e6,#FF7AB6 45%,#d9488c);border-radius:58% 42% 55% 45%/48% 60% 40% 52%;box-shadow:inset -30px -40px 60px rgba(120,0,60,.25),0 40px 0 -10px rgba(43,27,58,.12);animation:j 3s ease-in-out infinite}
@keyframes j{50%{border-radius:45% 55% 42% 58%/58% 44% 56% 42%;transform:scale(1.03,.97)}}
.hl{position:absolute;right:400px;top:200px;width:90px;height:50px;border-radius:50%;background:rgba(255,255,255,.7);transform:rotate(-25deg);filter:blur(2px)}
.btn{position:absolute;left:56px;top:430px;padding:18px 28px;background:#B8F15A;border:3px solid #2B1B3A;box-shadow:6px 6px 0 #2B1B3A;border-radius:22px;font-weight:900;font-size:20px}
.st{position:absolute;right:90px;top:120px;padding:12px 18px;background:#8C6CFF;color:#fff;border:3px solid #2B1B3A;border-radius:40px;font-weight:900;transform:rotate(10deg)}
.tabs{position:absolute;left:56px;bottom:60px;display:flex;gap:12px}.tabs span{padding:12px 20px;border:3px solid #2B1B3A;border-radius:99px;font-weight:800;background:#fff}
.dot{position:absolute;border-radius:50%;border:3px solid #2B1B3A}
</style>""" + NAV("wobble co.", ["Shop", "Build-a-slime", "Safety"], '<i style="font-style:normal;padding:10px 16px;border:3px solid #2B1B3A;border-radius:99px;font-weight:800;background:#6FD3FF">Cart (2)</i>', "#2B1B3A", "font-weight:800") + """<h1>Squish<br>responsibly.</h1><div class="btn">Shop the drop →</div><div class="blob"></div><div class="hl"></div><div class="st">New: Galaxy Goo</div><i class="dot" style="right:640px;top:520px;width:40px;height:40px;background:#B8F15A"></i><i class="dot" style="right:80px;bottom:150px;width:56px;height:56px;background:#6FD3FF"></i><div class="tabs"><span style="background:#FF7AB6">Fluffy</span><span>Crunchy</span><span>Clear</span><span>Butter</span><span>Cloud</span></div>"""

# 59 Duotone Press
T["duotone"] = BASE + """<style>body{background:#F3EEE3;position:relative;overflow:hidden}
.g{position:absolute;inset:0;opacity:.18;background-image:radial-gradient(#000 .6px,transparent .7px);background-size:5px 5px}
h1{position:absolute;left:52px;top:150px;font:900 150px/.86 'Arial Narrow','Helvetica Neue',sans-serif;letter-spacing:-.03em;text-transform:uppercase;mix-blend-mode:multiply}
.b{color:#0078BF}.p{color:#FF48B0;transform:translate(5px,4px)}
.ht{position:absolute;right:70px;top:120px;width:380px;height:500px;border-radius:50% 50% 0 0;background-image:radial-gradient(#FF48B0 38%,transparent 40%);background-size:14px 14px;mix-blend-mode:multiply}
.ht2{position:absolute;right:150px;top:220px;width:300px;height:380px;border-radius:50%;background-image:radial-gradient(#0078BF 30%,transparent 33%);background-size:12px 12px;mix-blend-mode:multiply}
.badge{position:absolute;right:420px;top:520px;width:150px;height:150px;border-radius:50%;border:3px solid #0078BF;color:#0078BF;display:grid;place-items:center;text-align:center;font:800 15px/1.2 'Arial Narrow',sans-serif;text-transform:uppercase;transform:rotate(-12deg)}
.btn{position:absolute;left:56px;bottom:70px;padding:16px 26px;background:#0078BF;color:#F3EEE3;font-weight:800;text-transform:uppercase;letter-spacing:.06em}
</style><div class="g"></div><div class="ht"></div><div class="ht2"></div><h1 class="b">Two inks.<br>Infinite<br>trouble.</h1><h1 class="p">Two inks.<br>Infinite<br>trouble.</h1>""" + NAV("DUOTONE PRESS", ["Services", "Inks", "Shop"], '<i style="font-style:normal;padding:10px 16px;border:2px solid #0078BF">Get a quote</i>', "#0078BF", "font-weight:800") + """<div class="badge">Open studio<br>Thursdays</div><div class="btn">Get a quote →</div>"""

# 60 Fall Line
T["fallline"] = BASE + """<style>body{background:linear-gradient(180deg,#5ea2e8,#bcd9f5 60%,#f7f9fb);position:relative;overflow:hidden}
.pk{position:absolute;left:0;right:0;bottom:260px;height:280px;background:#fff;clip-path:polygon(0 100%,14% 30%,24% 60%,40% 0,55% 55%,68% 20%,82% 62%,100% 25%,100% 100%)}
.slope{position:absolute;left:-100px;right:-100px;bottom:-120px;height:520px;background:#F7F9FB;transform:rotate(-8deg)}
.sk{position:absolute;left:330px;top:340px;width:60px;height:110px;background:#FF2D2D;border-radius:30px 30px 12px 12px;transform:rotate(-35deg)}.sp{position:absolute;left:220px;top:420px;width:260px;height:120px;border-radius:50%;background:radial-gradient(#fff,rgba(255,255,255,0) 70%)}
h1{position:absolute;right:56px;top:140px;text-align:right;font:900 italic 92px/.9 -apple-system,'Helvetica Neue',sans-serif;letter-spacing:-.04em;color:#0B1220;text-transform:uppercase}
.cd{position:absolute;right:56px;top:360px;display:flex;gap:10px}.cd span{background:#0B1220;color:#FFD400;font:700 34px ui-monospace,Menlo,monospace;padding:12px 14px;border-radius:6px;text-align:center}.cd small{display:block;font-size:10px;color:#9aa;letter-spacing:.1em}
.bar{position:absolute;left:0;right:0;bottom:0;height:90px;background:#0B1220;display:flex;align-items:center;gap:40px;padding:0 56px;font:600 15px ui-monospace,Menlo,monospace;color:#fff}.bar b{color:#FFD400}
</style><div class="pk"></div><div class="slope"></div><div class="sp"></div><div class="sk"></div>""" + NAV("FALL LINE", ["Course", "Schedule", "Results"], '<i style="font-style:normal;padding:10px 16px;background:#FF2D2D;color:#fff;font-weight:800">Register</i>', "#0B1220", "font-weight:800;font-style:italic") + """<h1>The mountain<br>doesn't wait.</h1><div class="cd"><span>12<small>DAYS</small></span><span>08<small>HRS</small></span><span>41<small>MIN</small></span><span>09<small>SEC</small></span></div><div class="bar"><span>01 <b>BIB 07</b> 1:42.38</span><span>02 BIB 14 +0.21</span><span>03 BIB 22 +0.64</span><span style="margin-left:auto;color:#FF2D2D">● LIVE (SAMPLE)</span></div>"""

# 61 Static FM
bars = "".join(f'<i style="display:inline-block;width:12px;margin-right:6px;height:{20+int(abs(math.sin(i*0.7)*140)+ (i*37)%60)}px;background:#C6FF3D;vertical-align:bottom"></i>' for i in range(44))
T["staticfm"] = BASE + """<style>body{background:#0A0A0A;color:#EDEDE6;position:relative;overflow:hidden}
.sl{position:absolute;inset:0;background:repeating-linear-gradient(0deg,rgba(255,255,255,.035) 0 1px,transparent 1px 4px)}
h1{position:absolute;left:56px;top:140px;font-size:120px;font-weight:900;letter-spacing:-.05em;line-height:.88;text-transform:uppercase}
.on{position:absolute;left:56px;top:400px;display:flex;gap:14px;align-items:center;font:700 14px ui-monospace,Menlo,monospace;letter-spacing:.12em}.on b{background:#C6FF3D;color:#0A0A0A;padding:6px 10px}
.pl{position:absolute;left:56px;right:56px;bottom:56px;height:200px;border-top:1px solid #333;border-bottom:1px solid #333;display:flex;align-items:flex-end;gap:30px;padding:20px 0}
.pb{width:110px;height:110px;border-radius:50%;background:#C6FF3D;display:grid;place-items:center;flex:none;align-self:center}.pb::after{content:"";border-left:34px solid #0A0A0A;border-top:20px solid transparent;border-bottom:20px solid transparent;margin-left:10px}
.sch{position:absolute;right:56px;top:140px;width:360px;font:500 14px ui-monospace,Menlo,monospace}.sch div{display:flex;justify-content:space-between;padding:12px 0;border-bottom:1px solid #2a2a2a}.sch .n{color:#C6FF3D}
</style><div class="sl"></div>""" + NAV("STATIC FM", ["Schedule", "Residents", "Archive"], '<i style="font-style:normal;padding:10px 16px;border:1px solid #EDEDE6">Support</i>', "#EDEDE6", "font-weight:900") + """<h1>Tune out.<br>Tune in.</h1><div class="on"><b>● ON AIR</b><span>NIGHT SHIFT w/ DJ LUMEN · 22:00–00:00</span></div><div class="sch"><div><span>20:00</span><span>Low Tide</span></div><div class="n"><span>22:00</span><span>Night Shift ●</span></div><div><span>00:00</span><span>Afterhours</span></div><div><span>02:00</span><span>Drift Archive</span></div></div><div class="pl"><div class="pb"></div><div>""" + bars + """</div></div>"""

# 62 Halden
T["halden"] = BASE + """<style>body{background:#EFEBE4;color:#1C1B19;position:relative;overflow:hidden}
.ph{position:absolute;right:56px;top:100px;width:520px;height:640px;background:linear-gradient(180deg,#d9c79e 0%,#c9a96a 55%,#8a7140 100%)}
.fig{position:absolute;right:250px;top:250px;width:120px;height:440px}.fig .h{width:46px;height:56px;border-radius:50%;background:#5a4636;margin-left:37px}.fig .c{width:120px;height:330px;margin-top:8px;background:#6B6A4A;clip-path:polygon(30% 0,70% 0,100% 100%,0 100%)}
h1{position:absolute;left:56px;top:200px;font:300 128px/.92 'Didot','Bodoni 72',Georgia,serif;letter-spacing:-.03em}
.k{position:absolute;left:56px;top:150px;font:600 12px -apple-system,sans-serif;letter-spacing:.14em}
.lk{position:absolute;left:56px;top:520px;font:600 13px -apple-system,sans-serif;letter-spacing:.12em;border-bottom:1px solid #1C1B19;padding-bottom:4px}
.gr{position:absolute;left:56px;bottom:56px;display:flex;gap:16px}.gr div{width:150px;height:110px;background:#d8d0c2}
</style><div class="ph"></div><div class="fig"><div class="h"></div><div class="c"></div></div>""" + NAV("HALDEN", ["WOMEN", "MEN", "ATELIER"], '<i style="font-style:normal;font-size:12px;letter-spacing:.12em">BAG (0)</i>', "#1C1B19", "font-size:12px;letter-spacing:.12em") + """<div class="k">AW27</div><h1>The Long<br>Field</h1><div class="lk">SHOP THE COLLECTION</div><div class="gr"><div></div><div style="background:#c9c1b0"></div><div style="background:#bdb39c"></div></div>"""

# 63 Facet
sp = "".join(f'<i style="position:absolute;left:{x}px;top:{y}px;width:{s}px;height:{s}px;background:#fff;clip-path:polygon(50% 0,58% 42%,100% 50%,58% 58%,50% 100%,42% 58%,0 50%,42% 42%);animation:tw 2s {d}s infinite"></i>' for x, y, s, d in [(840, 250, 26, 0), (960, 330, 16, .5), (790, 380, 12, 1), (1010, 210, 20, 1.4), (900, 460, 14, .8)])
T["facet"] = BASE + """<style>body{background:radial-gradient(700px 500px at 75% 50%,#2a2228,#0B0A0C 70%);color:#F7F3EC;position:relative;overflow:hidden}
@keyframes tw{50%{opacity:.1;transform:scale(.5)}}
.ring{position:absolute;left:740px;top:330px;width:380px;height:380px;border-radius:50%;border:22px solid #D8B983;box-shadow:inset 0 0 30px rgba(0,0,0,.5),0 30px 60px rgba(0,0,0,.6);transform:rotateX(62deg)}
.st{position:absolute;left:860px;top:230px;width:140px;height:140px;background:conic-gradient(from 0deg,#fff,#cfe8ff,#fff,#e8e0ff,#fff,#d6f5ff,#fff);clip-path:polygon(50% 0,100% 38%,82% 100%,18% 100%,0 38%);filter:drop-shadow(0 0 30px rgba(255,255,255,.5))}
h1{position:absolute;left:56px;top:230px;font:400 96px/1 'Didot','Bodoni 72',Georgia,serif;letter-spacing:-.01em;background:linear-gradient(100deg,#F7F3EC 40%,#D8B983 50%,#F7F3EC 60%);-webkit-background-clip:text;color:transparent}
.btn{position:absolute;left:56px;top:470px;padding:16px 28px;border:1px solid #D8B983;color:#D8B983;letter-spacing:.14em;font-size:13px;font-weight:600}
.steps{position:absolute;left:56px;bottom:56px;display:flex;gap:30px;font:600 12px -apple-system,sans-serif;letter-spacing:.14em;color:#8d8580}.steps b{color:#D8B983}
</style><div class="ring"></div><div class="st"></div>""" + sp + NAV("FACET", ["RINGS", "DESIGN", "ATELIER"], '<i style="font-style:normal;font-size:12px;letter-spacing:.14em;color:#D8B983">BOOK A VIEWING</i>', "#F7F3EC", "font-size:12px;letter-spacing:.14em") + """<h1>Made to be<br>looked at.</h1><div class="btn">DESIGN YOUR RING</div><div class="steps"><b>01 STONE</b><span>02 CUT</span><span>03 METAL</span><span>04 BAND</span><span>05 ENGRAVING</span></div>"""

# 64 Lattice (particle sphere) — coded fallback; replaced by Gemini video thumbnail when present
random.seed(7)
dots = []
for i in range(260):
    th = random.random() * 2 * math.pi; ph = math.acos(2 * random.random() - 1)
    x = math.sin(ph) * math.cos(th); y = math.cos(ph); z = math.sin(ph) * math.sin(th)
    r = 1.6 + (z + 1) * 1.6
    dots.append(f'<i style="position:absolute;left:{920+x*230:.0f}px;top:{400+y*230:.0f}px;width:{r:.1f}px;height:{r:.1f}px;border-radius:50%;background:#5fe3ff;opacity:{.25+(z+1)*.35:.2f};box-shadow:0 0 {r*2:.0f}px #39c6ff"></i>')
T["lattice"] = BASE + """<style>body{background:#050608;color:#f2f4f7;position:relative;overflow:hidden}
.glow{position:absolute;left:690px;top:170px;width:460px;height:460px;border-radius:50%;background:radial-gradient(circle,rgba(40,170,210,.28),transparent 65%)}
.orb{position:absolute;left:600px;top:280px;width:640px;height:240px;border-radius:50%;border:1px solid rgba(95,227,255,.28);transform:rotate(-14deg)}
.orb2{position:absolute;left:660px;top:150px;width:520px;height:520px;border-radius:50%;border:1px solid rgba(95,227,255,.14);transform:rotateX(70deg) rotate(30deg)}
.k{position:absolute;left:64px;top:250px;font:600 13px -apple-system,sans-serif;letter-spacing:.18em;color:#39c6ff}.k::before{content:"";display:inline-block;width:7px;height:7px;border-radius:50%;background:#39c6ff;margin-right:10px;vertical-align:1px}
h1{position:absolute;left:64px;top:280px;font-size:84px;font-weight:500;letter-spacing:-.045em;line-height:1.02;background:linear-gradient(180deg,#fff,#9aa1ab);-webkit-background-clip:text;color:transparent}
p{position:absolute;left:64px;top:490px;width:470px;font-size:19px;line-height:1.55;color:#8b929c}
.b{position:absolute;left:64px;top:620px;display:flex;gap:14px}.b span{padding:15px 24px;border-radius:99px;border:1px solid #23272e;font-weight:600;font-size:15px}.b span:first-child{background:linear-gradient(90deg,#0d1116,#11313c);border-color:#1f4652}
</style><div class="glow"></div>""" + "".join(dots) + """<div class="orb"></div><div class="orb2"></div>""" + NAV("<i style='font-family:Snell Roundhand,cursive;font-weight:400'>Lattice</i>", ["PLATFORM", "FEATURES", "PRICING", "DOCS"], '<i style="font-style:normal;padding:11px 20px;border:1px solid #23272e;border-radius:99px;font-weight:600">Join the beta</i>', "#c9ced6", "font-size:13px;letter-spacing:.06em") + """<div class="k">SIGNAL PLATFORM</div><h1>See the shape<br>of your data.</h1><p>Lattice maps every event, agent and customer into one living graph, so your team can see patterns before they become problems.</p><div class="b"><span>Start exploring</span><span>Read the docs</span></div>"""
