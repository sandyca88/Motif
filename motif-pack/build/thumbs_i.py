# part I: prompts 21-32
from thumbs_a import BASE
T = {}
NAV = lambda logo, links, cta, col="#fff", ctabg="#fff", ctacol="#000": f'<nav style="position:relative;z-index:2;display:flex;justify-content:space-between;align-items:center;padding:26px 56px;color:{col};font-size:14px"><b style="font-size:19px">{logo}</b><span style="display:flex;gap:26px;opacity:.75">{links}</span><span style="padding:9px 16px;border-radius:99px;background:{ctabg};color:{ctacol};font-weight:600">{cta}</span></nav>'

T["halo"] = BASE + """<style>body{background:#050608;color:#fff;text-align:center;position:relative;font-family:-apple-system,'SF Pro Display',Inter,sans-serif}
h1{font-size:108px;letter-spacing:-.05em;font-weight:600;margin-top:36px}p{color:#8b93a1;font-size:20px;margin-top:10px}
.gl{position:absolute;left:50%;top:420px;width:760px;height:190px;margin-left:-380px;animation:bob 6s ease-in-out infinite}
.lens{position:absolute;top:30px;width:300px;height:140px;border-radius:70px;background:radial-gradient(circle at 30% 30%,rgba(125,211,252,.55),rgba(20,30,45,.95) 60%);box-shadow:inset 0 0 0 10px #1c2230,0 30px 60px rgba(0,0,0,.7)}
.br{position:absolute;left:300px;top:70px;width:160px;height:14px;background:#1c2230;border-radius:7px}
.fl{position:absolute;left:50%;top:640px;width:700px;height:60px;margin-left:-350px;background:radial-gradient(ellipse,rgba(125,211,252,.25),transparent 70%);filter:blur(8px)}
.sp{position:absolute;bottom:40px;left:0;right:0;display:flex;justify-content:center;gap:60px;font-size:13px;color:#8b93a1}.sp b{display:block;color:#fff;font-size:24px;font-variant-numeric:tabular-nums}
</style>""" + NAV("◉ halo","Overview · Tech specs · Compare","Pre-order") + """<h1>See more. Carry less.</h1><p>Halo One · 38g · all-day battery · from $499</p>
<div class="gl"><div class="lens" style="left:0"></div><div class="br"></div><div class="lens" style="right:0"></div></div><div class="fl"></div>
<div class="sp"><span><b>38 g</b>weight</span><span><b>52°</b>field of view</span><span><b>11 h</b>battery</span></div>"""

T["maison"] = BASE + """<style>body{background:#F4F1EC;color:#111;font-family:'Helvetica Neue',Arial,sans-serif}
.hd{display:grid;grid-template-columns:1fr auto 1fr;align-items:center;padding:24px 50px;font-size:12px;letter-spacing:.2em}.hd b{font:400 34px 'Didot','Bodoni 72',Georgia,serif;letter-spacing:.08em}
.g{display:grid;grid-template-columns:1.25fr 1fr;gap:18px;padding:0 50px}
.im{position:relative;background:linear-gradient(160deg,#d8cfc2,#8d7f70);height:640px}.im span{position:absolute;left:30px;bottom:30px;color:#fff;font:italic 44px Georgia,serif}
.r{display:grid;grid-template-rows:1fr auto;gap:18px}.r .a{background:linear-gradient(160deg,#c9c3b8,#5b534b)}.r .ps{display:grid;grid-template-columns:1fr 1fr;gap:14px}
.p div{height:210px;background:linear-gradient(160deg,#e8e2d8,#b8ab9b)}.p small{display:block;font-size:12px;letter-spacing:.14em;margin-top:8px}
</style><div class="hd"><span>MENU</span><b>MAISON VERRE</b><span style="text-align:right">SEARCH · ACCOUNT · BAG (0)</span></div>
<div class="g"><div class="im"><span>Autumn in linen</span></div><div class="r"><div class="a"></div><div class="ps"><div class="p"><div></div><small>WOOL COAT · $690</small></div><div class="p"><div style="background:linear-gradient(160deg,#ddd5ca,#7f7466)"></div><small>SILK SHIRT · $320</small></div></div></div></div>"""

T["ember"] = BASE + """<style>body{background:#1A1410;color:#F3E9DC;position:relative;font-family:Georgia,serif}
.bg{position:absolute;inset:0;background:radial-gradient(circle at 70% 40%,rgba(224,112,58,.55),transparent 45%),radial-gradient(circle at 75% 45%,#6b3a1e,transparent 55%)}
.plate{position:absolute;right:120px;top:170px;width:440px;height:440px;border-radius:50%;background:radial-gradient(circle,#f3e9dc 0 44%,#e8dccb 45% 60%,#2a1d15 61%);box-shadow:0 40px 80px rgba(0,0,0,.6)}
.plate i{position:absolute;border-radius:50%}
.c{position:relative;padding:40px 70px}.pill{display:inline-flex;gap:8px;align-items:center;padding:7px 14px;border:1px solid rgba(243,233,220,.3);border-radius:99px;font:14px -apple-system,sans-serif}
h1{font-size:104px;line-height:.95;margin:30px 0 18px;letter-spacing:-.02em}h1 em{color:#E0703A}p{font:20px -apple-system,sans-serif;opacity:.75}
.b{display:flex;gap:12px;margin-top:30px;font:600 16px -apple-system,sans-serif}.b span{padding:14px 24px;border-radius:99px}
</style><div class="bg"></div><div class="plate"><i style="left:150px;top:140px;width:90px;height:60px;background:#b5562a"></i><i style="left:210px;top:190px;width:70px;height:70px;background:#6f8f4e"></i><i style="left:160px;top:220px;width:60px;height:50px;background:#e0b46a"></i></div>
<div class="c"><b style="font-size:24px;letter-spacing:.06em">EMBER &amp; OAK</b><div style="margin-top:80px"><span class="pill"><span style="width:8px;height:8px;border-radius:50%;background:#7bd88f"></span>Open today · 5–11pm</span></div>
<h1>Wood-fired.<br>Local. <em>Late.</em></h1><p>Seasonal plates cooked over oak in the heart of Portland.</p>
<div class="b"><span style="background:#E0703A;color:#1A1410">Book a table</span><span style="border:1px solid rgba(243,233,220,.4)">View menu</span></div></div>"""

T["stride"] = BASE + """<style>body{background:#0C0F0A;color:#fff;display:grid;grid-template-columns:1.1fr 1fr;align-items:center;padding:0 70px;font-family:Nunito,'Arial Rounded MT Bold',-apple-system,sans-serif}
h1{font-size:92px;font-weight:900;letter-spacing:-.04em;line-height:.95}h1 span{color:#C7F53B}p{color:#9aa38f;font-size:20px;margin:18px 0 26px}
.bd{display:flex;gap:10px}.bd span{padding:12px 18px;border-radius:12px;background:#fff;color:#000;font-weight:800;font-size:14px}
.ph{position:relative;height:640px}.p{position:absolute;width:270px;height:560px;border-radius:44px;background:#000;padding:10px;box-shadow:0 40px 80px rgba(0,0,0,.6)}
.s{height:100%;border-radius:36px;background:#141911;padding:40px 20px;text-align:center}
.ring{width:190px;height:190px;margin:30px auto;border-radius:50%;background:conic-gradient(#C7F53B 0 72%,#263020 0);display:grid;place-items:center}.ring div{width:150px;height:150px;border-radius:50%;background:conic-gradient(#FF7A6B 0 58%,#2d2320 0);display:grid;place-items:center}.ring b{width:110px;height:110px;border-radius:50%;background:#141911;display:grid;place-items:center;font-size:26px}
</style><div><h1>Move a little.<br><span>Every day.</span></h1><p>Coach-built plans for real schedules: 10 to 45 minutes, no gym needed.</p><div class="bd"><span> App Store</span><span>▶ Google Play</span></div><p style="font-size:15px;margin-top:18px">★★★★★ 4.8 · 60k ratings</p></div>
<div class="ph"><div class="p" style="left:40px;top:40px"><div class="s"><b style="font-size:18px">Today</b><div class="ring"><div><b>72%</b></div></div><div style="color:#9aa38f">Move · Mindful</div></div></div>
<div class="p" style="left:250px;top:0;transform:rotate(4deg)"><div class="s" style="background:linear-gradient(180deg,#2b3a14,#141911)"><b style="font-size:16px;color:#C7F53B">NOW PLAYING</b><div style="font-size:30px;font-weight:900;margin:150px 0 8px">Core Burn</div><div style="color:#9aa38f">12:40 left · Coach Mia</div><div style="height:6px;border-radius:3px;background:#263020;margin-top:26px"><div style="width:40%;height:100%;border-radius:3px;background:#C7F53B"></div></div></div></div></div>"""

T["wander"] = BASE + """<style>body{background:#FBFAF7;color:#1D2320;font-family:-apple-system,Inter,sans-serif}
.h{position:relative;margin:20px;height:470px;border-radius:28px;overflow:hidden;background:linear-gradient(180deg,#8ec5d6,#f2d7b6 60%,#d49a6a)}
.h::after{content:"";position:absolute;left:0;right:0;bottom:0;height:200px;background:linear-gradient(180deg,transparent,#0F766E 90%);opacity:.6}
.h h1{position:absolute;left:50px;top:110px;font-size:78px;color:#fff;letter-spacing:-.04em;z-index:2}
.sb{position:absolute;left:50px;right:50px;bottom:36px;z-index:3;display:grid;grid-template-columns:1.4fr 1fr 1fr auto;background:#fff;border-radius:99px;padding:8px 8px 8px 28px;align-items:center;box-shadow:0 20px 50px rgba(0,0,0,.2);font-size:14px}
.sb div b{display:block;font-size:12px}.sb div span{color:#888}.sb i{font-style:normal;padding:16px 26px;border-radius:99px;background:#0F766E;color:#fff;font-weight:700}
.row{display:grid;grid-template-columns:repeat(4,1fr);gap:18px;padding:6px 20px}.cd div{height:170px;border-radius:18px}.cd b{display:block;margin-top:10px}.cd span{color:#6b716e;font-size:14px}
</style><div class="h"><h1>Stay somewhere<br>that stays with you.</h1><div class="sb"><div><b>Where</b><span>Search destinations</span></div><div><b>Dates</b><span>Oct 12 – 16</span></div><div><b>Guests</b><span>2 adults</span></div><i>Search</i></div></div>
<div class="row"><div class="cd"><div style="background:linear-gradient(135deg,#a3c9a8,#3d6b52)"></div><b>Lofoten cabins</b><span>from $180/night · ★ 4.9</span></div><div class="cd"><div style="background:linear-gradient(135deg,#f3c9a1,#c46a3c)"></div><b>Marrakech riads</b><span>from $95/night · ★ 4.8</span></div><div class="cd"><div style="background:linear-gradient(135deg,#9ec9e6,#2c6e91)"></div><b>Amalfi villas</b><span>from $260/night · ★ 4.9</span></div><div class="cd"><div style="background:linear-gradient(135deg,#d8d0e8,#6f5f9a)"></div><b>Kyoto machiya</b><span>from $150/night · ★ 5.0</span></div></div>"""

T["stage"] = BASE + """<style>body{background:#0b0710;color:#fff;display:grid;grid-template-columns:560px 1fr;gap:50px;align-items:center;padding:0 70px;position:relative;overflow:hidden;font-family:'Helvetica Neue',Arial,sans-serif}
body::before{content:"";position:absolute;inset:0;background:radial-gradient(circle at 20% 50%,rgba(255,64,129,.35),transparent 50%),radial-gradient(circle at 80% 30%,rgba(90,70,255,.35),transparent 50%)}
.cv{position:relative;width:560px;height:560px;background:conic-gradient(from 200deg,#ff4081,#5a46ff,#1b0f2e,#ff4081);box-shadow:0 40px 90px rgba(0,0,0,.6)}.cv::after{content:"";position:absolute;inset:36%;border-radius:50%;background:#0b0710;box-shadow:0 0 0 30px rgba(255,255,255,.08)}
.t{position:relative}.t small{letter-spacing:.3em;font-size:13px;opacity:.7}h1{font-size:170px;font-weight:900;letter-spacing:-.06em;line-height:.82;margin:14px 0 24px}
.pl{display:flex;align-items:center;gap:16px;background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.15);border-radius:18px;padding:14px 18px;width:460px}
.pl i{width:44px;height:44px;border-radius:50%;background:#fff;color:#000;display:grid;place-items:center;font-style:normal}.wv{flex:1;display:flex;gap:3px;align-items:center;height:36px}.wv b{flex:1;background:rgba(255,255,255,.5);border-radius:2px}
.tr{margin-top:22px;font-size:15px;opacity:.85}.tr div{display:flex;justify-content:space-between;width:460px;padding:10px 0;border-top:1px solid rgba(255,255,255,.12)}
</style><div class="cv"></div><div class="t"><small>NEW ALBUM · OUT NOW</small><h1>NIGHT<br>SWIM</h1><div class="pl"><i>▶</i><div class="wv">""" + "".join(f'<b style="height:{h}%"></b>' for h in [30,60,45,80,55,90,40,70,35,65,85,50,30,75,45,60,40,80,55,35]) + """</div><span style="font-size:13px">0:30</span></div>
<div class="tr"><div><span>OCT 14 · Berlin</span><b>Tickets</b></div><div><span>OCT 17 · Paris</span><b style="opacity:.5">Sold out</b></div></div></div>"""

T["care"] = BASE + """<style>body{background:#F7FAFA;color:#13232B;display:grid;grid-template-columns:1.15fr 1fr;gap:40px;align-items:center;padding:0 70px;font-family:-apple-system,Inter,sans-serif}
.bd{display:inline-flex;gap:8px;align-items:center;padding:8px 14px;border-radius:99px;background:#dff3ef;color:#1C7C8C;font-weight:700;font-size:14px}
h1{font-size:76px;letter-spacing:-.04em;line-height:1;margin:22px 0 16px}p{font-size:20px;color:#4d5f66;line-height:1.6}
.b{display:flex;gap:12px;margin-top:26px}.b span{padding:16px 26px;border-radius:14px;font-weight:700;font-size:17px}
.tr{display:flex;gap:30px;margin-top:30px;font-size:14px;color:#4d5f66}.tr b{display:block;color:#13232B;font-size:24px}
.bk{background:#fff;border-radius:24px;padding:26px;box-shadow:0 30px 60px -20px rgba(19,35,43,.25)}.bk h3{font-size:20px}
.dy{display:grid;grid-template-columns:repeat(5,1fr);gap:8px;margin:16px 0}.dy span{text-align:center;padding:10px 0;border-radius:12px;background:#F1F6F6;font-size:13px}.dy .on{background:#1C7C8C;color:#fff}
.sl{display:grid;grid-template-columns:repeat(3,1fr);gap:8px}.sl span{text-align:center;padding:12px 0;border:1.5px solid #cfe3e1;border-radius:12px;font-weight:600;font-size:14px}.sl .on{border-color:#1C7C8C;background:#e6f4f2}
</style><div><span class="bd">● Accepting new patients</span><h1>Care that fits<br>your schedule.</h1><p>Family dentistry in Oakland. Same-week appointments, evenings and Saturdays.</p>
<div class="b"><span style="background:#1C7C8C;color:#fff">Book an appointment</span><span style="border:1.5px solid #1C7C8C;color:#1C7C8C">Call (510) 555-0134</span></div>
<div class="tr"><div><b>4.9 ★</b>1,200 reviews</div><div><b>18 yrs</b>in the community</div><div><b>Most</b>insurance accepted</div></div></div>
<div class="bk"><h3>Book a cleaning</h3><div style="color:#4d5f66;font-size:14px;margin-top:4px">Dr. Patel or any available</div><div class="dy"><span>Mon<br>14</span><span class="on">Tue<br>15</span><span>Wed<br>16</span><span>Thu<br>17</span><span>Fri<br>18</span></div>
<div class="sl"><span>8:30</span><span class="on">10:00</span><span>11:30</span><span>2:00</span><span>4:30</span><span>6:00</span></div><div style="margin-top:16px;padding:14px;border-radius:12px;background:#1C7C8C;color:#fff;text-align:center;font-weight:700">Continue</div></div>"""

T["haven"] = BASE + """<style>body{background:#fff;color:#111827;font-family:-apple-system,Inter,sans-serif}
.h{position:relative;margin:18px;height:400px;border-radius:24px;overflow:hidden;background:linear-gradient(180deg,#cfd8dc,#8ea1a8 50%,#5b6b62)}
.hs{position:absolute;left:50%;bottom:0;width:560px;margin-left:-280px;height:250px;background:#efe9e0;clip-path:polygon(0 40%,50% 0,100% 40%,100% 100%,0 100%)}
.hs::after{content:"";position:absolute;left:220px;bottom:0;width:120px;height:130px;background:#B45309;opacity:.85}
.h h1{position:absolute;left:44px;top:40px;font-size:58px;color:#fff;letter-spacing:-.03em;text-shadow:0 2px 20px rgba(0,0,0,.3)}
.sr{position:absolute;left:44px;top:140px;display:flex;background:#fff;border-radius:16px;padding:6px;gap:6px;font-size:14px;box-shadow:0 14px 30px rgba(0,0,0,.15)}.sr span{padding:10px 16px;border-radius:10px}.sr .on{background:#111827;color:#fff}
.g{display:grid;grid-template-columns:repeat(3,1fr);gap:18px;padding:8px 18px}.c{border:1px solid #eee;border-radius:18px;overflow:hidden}.c div{height:160px}.c .i{padding:14px 16px;font-size:14px;color:#6b7280}.c .i b{display:block;color:#111827;font-size:22px}
.st{position:absolute;margin:10px;padding:4px 10px;border-radius:99px;background:#fff;font-size:12px;font-weight:700}
</style><div class="h"><div class="hs"></div><h1>Find the one.</h1><div class="sr"><span class="on">Buy</span><span>Rent</span><span>Sold</span><span style="color:#888;width:260px">Neighborhood, city or ZIP</span><span style="background:#B45309;color:#fff;font-weight:700">Search</span></div></div>
<div class="g"><div class="c"><span class="st">New</span><div style="background:linear-gradient(135deg,#d6cbb8,#8a7a61)"></div><div class="i"><b>$845,000</b>3 bd · 2 ba · 1,840 sqft<br>214 Alder St, Portland</div></div>
<div class="c"><span class="st">Open house Sat</span><div style="background:linear-gradient(135deg,#c9d6cf,#5f7d6d)"></div><div class="i"><b>$1,120,000</b>4 bd · 3 ba · 2,610 sqft<br>9 Birch Ln, Lake Oswego</div></div>
<div class="c"><div style="background:linear-gradient(135deg,#e2d4c8,#a2765a)"></div><div class="i"><b>$615,000</b>2 bd · 2 ba · 1,190 sqft<br>77 Pearl Ave #5, Portland</div></div></div>"""

T["learn"] = BASE + """<style>body{background:#FFFDF8;color:#1B1B1F;display:grid;grid-template-columns:1.2fr 1fr;gap:40px;align-items:center;padding:0 70px;font-family:-apple-system,Inter,sans-serif}
.k{font-weight:700;color:#4F46E5;font-size:15px}h1{font:600 76px/1 Georgia,'Source Serif 4',serif;letter-spacing:-.02em;margin:16px 0}h1 mark{background:linear-gradient(transparent 55%,#FFE14D 55%);color:inherit}
p{font-size:20px;color:#55555e}.seat{margin:24px 0 8px;font-size:14px;color:#55555e}.bar{height:10px;border-radius:5px;background:#eee;width:420px}.bar i{display:block;width:78%;height:100%;border-radius:5px;background:#4F46E5}
.b{display:flex;gap:12px;margin-top:22px}.b span{padding:15px 24px;border-radius:12px;font-weight:700}
.cu{background:#fff;border:1px solid #eee;border-radius:22px;padding:24px;box-shadow:0 30px 60px -30px rgba(0,0,0,.25)}.m{display:flex;justify-content:space-between;padding:14px 0;border-top:1px solid #f0f0f0;font-size:15px}.m span{color:#888}
.fr{font-size:11px;font-weight:800;padding:3px 7px;border-radius:6px;background:#e9e7ff;color:#4F46E5;margin-left:6px}
</style><div><div class="k">LIVE COHORT · STARTS NOV 3</div><h1>Ship your first <mark>AI product</mark> in 6 weeks.</h1><p>A hands-on course for designers and PMs. Weekly live sessions, real projects, mentor feedback.</p>
<div class="seat">31 of 40 seats taken</div><div class="bar"><i></i></div><div class="b"><span style="background:#4F46E5;color:#fff">Enroll: $490</span><span style="border:1.5px solid #ddd">Watch free lesson</span></div></div>
<div class="cu"><b style="font-size:19px">Curriculum</b><div class="m"><b>01 · Finding the problem</b><span>4 lessons<span class="fr">FREE</span></span></div><div class="m"><b>02 · Prompting &amp; prototyping</b><span>6 lessons</span></div><div class="m"><b>03 · Designing for trust</b><span>5 lessons</span></div><div class="m"><b>04 · Evaluating quality</b><span>4 lessons</span></div><div class="m"><b>05 · Shipping &amp; demo day</b><span>3 lessons</span></div></div>"""

T["kindred"] = BASE + """<style>body{background:#FFFBF5;color:#1F2A2E;display:grid;grid-template-columns:1.1fr 1fr;gap:40px;align-items:center;padding:0 70px;font-family:Nunito,-apple-system,sans-serif}
h1{font-size:72px;font-weight:900;letter-spacing:-.03em;line-height:1}h1 span{color:#E4572E}p{font-size:20px;color:#55615f;margin:18px 0}
.gp{font-size:15px;color:#55615f}.gb{height:14px;border-radius:7px;background:#f1e7da;margin:8px 0 24px;width:460px}.gb i{display:block;width:64%;height:100%;border-radius:7px;background:linear-gradient(90deg,#E4572E,#f59e6b)}
.dn{background:#fff;border-radius:24px;padding:26px;box-shadow:0 30px 60px -24px rgba(0,0,0,.2)}.tg{display:flex;background:#f6efe6;border-radius:12px;padding:4px;margin:14px 0}.tg span{flex:1;text-align:center;padding:10px;border-radius:9px;font-weight:700}.tg .on{background:#fff;box-shadow:0 2px 6px rgba(0,0,0,.08)}
.am{display:grid;grid-template-columns:repeat(4,1fr);gap:8px}.am span{text-align:center;padding:14px 0;border:2px solid #efe4d6;border-radius:12px;font-weight:800;font-size:18px}.am .on{border-color:#E4572E;background:#fff1ec;color:#E4572E}
.im{margin-top:14px;padding:12px;border-radius:12px;background:#eef6ea;color:#3d6b3a;font-weight:700;font-size:15px}
</style><div><h1>Clean water for<br><span>40,000 people</span><br>this year.</h1><p>Every well we build is maintained by the community it serves.</p><div class="gp"><b style="color:#1F2A2E">$256,400</b> raised of $400,000 goal</div><div class="gb"><i></i></div>
<div style="display:flex;gap:40px"><div><b style="font-size:30px">312</b><div class="gp">wells built</div></div><div><b style="font-size:30px">92%</b><div class="gp">to programs</div></div></div></div>
<div class="dn"><b style="font-size:20px">Make a difference</b><div class="tg"><span>One-time</span><span class="on">Monthly</span></div><div class="am"><span>$25</span><span class="on">$50</span><span>$100</span><span>Other</span></div><div class="im">$50/month = clean water for 5 people</div><div style="margin-top:16px;padding:16px;border-radius:14px;background:#E4572E;color:#fff;text-align:center;font-weight:800">Donate $50 monthly</div></div>"""

T["shipped"] = BASE + """<style>body{zoom:1.3;background:#0B0B0E;color:#EDEDF0;display:grid;grid-template-columns:230px 1fr;gap:40px;padding:50px 60px;font-family:-apple-system,Inter,sans-serif}
.r{font-size:14px;color:#8a8a94}.r b{display:block;color:#fff;font-size:22px;margin-bottom:18px}.ch{display:inline-block;margin:0 6px 8px 0;padding:6px 11px;border-radius:99px;border:1px solid rgba(255,255,255,.12)}.ch.on{background:#7C5CFF;border-color:#7C5CFF;color:#fff}
.e{display:grid;grid-template-columns:130px 1fr;gap:20px;padding:24px 0;border-top:1px solid rgba(255,255,255,.08)}.d{font:13px ui-monospace,Menlo,monospace;color:#8a8a94}.v{display:inline-block;margin-top:6px;padding:3px 8px;border-radius:6px;background:rgba(124,92,255,.15);color:#b3a3ff;font:600 12px ui-monospace,Menlo,monospace}
.e h3{font-size:22px;letter-spacing:-.02em}.e p{color:#a1a1aa;margin:6px 0 10px}.tg span{font-size:12px;padding:3px 8px;border-radius:6px;margin-right:6px}
.shot{height:120px;border-radius:12px;background:linear-gradient(135deg,#1c1830,#101018);border:1px solid rgba(255,255,255,.08);margin-top:10px}
</style><div class="r"><b>Changelog</b><span class="ch on">All</span><span class="ch">New</span><span class="ch">Improved</span><span class="ch">Fixed</span><span class="ch">API</span><div style="margin-top:20px;line-height:2">October 2026<br>September 2026<br>August 2026</div></div>
<div><div class="e"><div><div class="d">OCT 2, 2026</div><span class="v">v4.2</span></div><div><h3>Workflows now run on a schedule</h3><p>Trigger any workflow hourly, daily or with cron syntax.</p><div class="tg"><span style="background:rgba(52,211,153,.15);color:#34d399">New</span><span style="background:rgba(96,165,250,.15);color:#93c5fd">API</span></div><div class="shot"></div></div></div>
<div class="e"><div><div class="d">SEP 24, 2026</div><span class="v">v4.1.3</span></div><div><h3>Faster search across large workspaces</h3><p>Results now appear up to 3× faster for teams with 10k+ docs.</p><div class="tg"><span style="background:rgba(251,191,36,.15);color:#fbbf24">Improved</span></div></div></div></div>"""

T["dispatch"] = BASE + """<style>body{background:#FAF7F2;color:#171717;display:grid;grid-template-columns:1.1fr 1fr;gap:50px;align-items:center;padding:0 80px;font-family:Georgia,'Source Serif 4',serif}
.av{width:64px;height:64px;border-radius:50%;background:linear-gradient(135deg,#f5b087,#D9480F)}h1{font-size:88px;line-height:.95;letter-spacing:-.03em;margin:22px 0 14px}p{font:20px -apple-system,sans-serif;color:#57534e}
.f{display:flex;margin-top:26px;border:1.5px solid #171717;border-radius:14px;padding:6px;width:480px;font:16px -apple-system,sans-serif}.f span{flex:1;padding:12px;color:#a8a29e}.f b{padding:12px 20px;border-radius:10px;background:#D9480F;color:#fff}
.sp{font:14px -apple-system,sans-serif;color:#78716c;margin-top:12px}
.is div{padding:18px 0;border-top:1px solid #e7e0d6}.is small{font:600 12px ui-monospace,Menlo,monospace;color:#D9480F}.is b{display:block;font-size:24px;margin:4px 0}.is span{font:14px -apple-system,sans-serif;color:#78716c}
</style><div><div class="av"></div><h1>The Friday<br>Sketch</h1><p>One idea a week to design better products. Five-minute read.</p><div class="f"><span>you@email.com</span><b>Subscribe</b></div><div class="sp">Join 12,400 designers · No spam, unsubscribe anytime</div></div>
<div class="is"><div><small>ISSUE #142 · OCT 3</small><b>The empty state is the pitch</b><span>4 min read</span></div><div><small>ISSUE #141 · SEP 26</small><b>Why your onboarding has 3 too many steps</b><span>5 min read</span></div><div><small>ISSUE #140 · SEP 19</small><b>Designing for AI that's sometimes wrong</b><span>6 min read</span></div></div>"""
