# part J: prompts 33-44
from thumbs_a import BASE
T = {}

T["blockhaus"] = BASE + """<style>body{background:#F5F1E8;color:#000;font-family:'Archivo Black','Arial Black',sans-serif;padding:26px 50px}
.nv{display:flex;justify-content:space-between;align-items:center;border:3px solid #000;padding:12px 18px;background:#fff;font:700 14px ui-monospace,Menlo,monospace}.bt{border:3px solid #000;box-shadow:5px 5px 0 #000;padding:10px 16px;background:#FFE14D;font:800 15px -apple-system,sans-serif}
.w{display:grid;grid-template-columns:1.1fr 1fr;gap:40px;margin-top:50px;align-items:center}h1{font-size:92px;line-height:.92;letter-spacing:-.02em}h1 span{background:#FF7AB6;padding:0 10px;border:3px solid #000}
p{font:600 19px -apple-system,sans-serif;margin:22px 0}.cl{position:relative;height:460px}.cd{position:absolute;border:3px solid #000;box-shadow:6px 6px 0 #000;background:#fff;padding:16px;font:700 15px -apple-system,sans-serif;width:300px}
.cd i{display:block;height:10px;background:#eee;margin:8px 0;border:2px solid #000}
</style><div class="nv"><span>▣ BLOCKHAUS</span><span>FEATURES · PRICING · DOCS</span><span class="bt">Start free</span></div>
<div class="w"><div><h1>Projects,<br>minus the <span>mess.</span></h1><p>Boards, docs and invoices in one loud little app.</p><span class="bt" style="display:inline-block">Try it free →</span></div>
<div class="cl"><div class="cd" style="left:20px;top:20px;transform:rotate(-4deg);background:#7CE0B5">✓ Ship landing page<i></i><i style="width:60%"></i></div><div class="cd" style="left:170px;top:170px;transform:rotate(3deg)">INVOICE #0042 · $2,400<i style="background:#3A5BFF"></i><i></i></div><div class="cd" style="left:60px;top:320px;transform:rotate(-2deg);background:#FFE14D">💬 "Looks great, ship it!"</div></div></div>"""

T["tiles"] = BASE + """<style>body{background:#0B0B0C;color:#f4f4f5;padding:34px 60px;font-family:Inter,-apple-system,sans-serif}
.g{display:grid;grid-template-columns:repeat(4,1fr);grid-template-rows:repeat(3,228px);gap:12px}.t{background:#151517;border:1px solid rgba(255,255,255,.07);border-radius:24px;padding:20px;position:relative;overflow:hidden;font-size:14px;color:#a1a1aa}
.t b{color:#fff}.av{width:70px;height:70px;border-radius:50%;background:linear-gradient(135deg,#a5b4fc,#6366F1);margin-bottom:16px}
.eq{display:flex;gap:4px;align-items:end;height:40px;position:absolute;right:20px;bottom:20px}.eq i{width:6px;background:#6366F1;border-radius:3px;animation:grow 1s ease-in-out infinite alternate}
</style><div class="g">
<div class="t" style="grid-column:span 2;grid-row:span 2"><div class="av"></div><b style="font-size:34px;letter-spacing:-.03em">Hi, I'm Ren.</b><div style="font-size:18px;margin-top:10px;line-height:1.5">Product designer making calm tools for busy teams. Based in Lisbon.</div><div style="margin-top:24px;display:inline-flex;gap:8px;align-items:center;padding:7px 12px;border-radius:99px;background:rgba(52,211,153,.12);color:#34d399">● Available for work</div></div>
<div class="t"><b style="font-size:18px">GitHub</b><br>@renmakes<br><span style="position:absolute;bottom:20px">2.1k followers</span></div>
<div class="t" style="background:linear-gradient(135deg,#1e1b4b,#151517)"><b style="font-size:18px">Lisbon</b><br>14:32 · sunny<div style="position:absolute;right:30px;bottom:30px;width:18px;height:18px;border-radius:50%;background:#6366F1;box-shadow:0 0 0 12px rgba(99,102,241,.25)"></div></div>
<div class="t" style="grid-column:span 2"><b style="font-size:18px">Featured · Orbit</b><br>Scheduling app used by 40k teams<div style="position:absolute;right:-20px;bottom:-30px;width:280px;height:160px;border-radius:14px;background:linear-gradient(135deg,#312e81,#6366F1)"></div></div>
<div class="t"><b style="font-size:18px">On repeat</b><br>Night Swim — Aurel<div class="eq"><i style="height:40%"></i><i style="height:80%;animation-delay:-.3s"></i><i style="height:60%;animation-delay:-.6s"></i><i style="height:90%;animation-delay:-.1s"></i></div></div>
<div class="t"><b style="font-size:18px">Writing</b><br><br>Design is subtraction<br>Calm software<br>Tools &gt; rules</div>
<div class="t"><b style="font-size:18px">LinkedIn</b><br>Ren Oliveira</div><div class="t" style="background:#6366F1;color:#fff"><b style="font-size:18px">Say hello →</b><br>ren@hey.design</div></div>"""

T["configure"] = BASE + """<style>body{background:#EEF0F3;color:#111;display:grid;grid-template-columns:1.5fr 1fr;font-family:-apple-system,Inter,sans-serif}
.st{position:relative;background:radial-gradient(circle at 50% 40%,#fff,#dfe3e8)}.sh{position:absolute;left:170px;bottom:170px;width:460px;height:40px;border-radius:50%;background:rgba(0,0,0,.15);filter:blur(10px)}
.sn{position:absolute;left:140px;top:250px;width:520px;height:220px;animation:bob 5s ease-in-out infinite}
.sn .up{position:absolute;left:40px;top:10px;width:420px;height:150px;background:#FF5A36;border-radius:140px 160px 30px 60px}.sn .so{position:absolute;left:0;bottom:0;width:520px;height:60px;background:#fff;border-radius:30px;box-shadow:inset 0 -12px 0 #d9dde2}
.sn .sw{position:absolute;left:210px;top:60px;width:200px;height:60px;border-radius:30px;background:#1F2937}.hs{position:absolute;width:20px;height:20px;border-radius:50%;background:#fff;box-shadow:0 0 0 6px rgba(255,255,255,.5),0 4px 10px rgba(0,0,0,.2)}
.pn{background:#fff;padding:36px;display:flex;flex-direction:column;gap:18px}.stp{display:flex;gap:6px;font-size:13px;font-weight:700;color:#999}.stp .on{color:#111}
.sw2{display:flex;gap:12px}.sw2 i{width:44px;height:44px;border-radius:50%;box-shadow:0 0 0 2px #fff,0 0 0 4px transparent}.sw2 .on{box-shadow:0 0 0 3px #fff,0 0 0 5px #111}
.mt{display:grid;grid-template-columns:repeat(3,1fr);gap:8px}.mt span{padding:12px;border:1.5px solid #e5e7eb;border-radius:12px;font-size:14px}.mt .on{border-color:#111}
.sm{margin-top:auto;border-top:1px solid #eee;padding-top:16px;display:flex;justify-content:space-between;align-items:center}.sm b{font-size:30px}.sm span{padding:14px 22px;border-radius:12px;background:#111;color:#fff;font-weight:700}
</style><div class="st"><div class="sh"></div><div class="sn"><div class="up"></div><div class="sw"></div><div class="so"></div></div><i class="hs" style="left:300px;top:280px"></i><i class="hs" style="left:560px;top:430px"></i></div>
<div class="pn"><div class="stp"><span class="on">1 Color</span>·<span>2 Material</span>·<span>3 Details</span>·<span>4 Size</span></div><b style="font-size:28px;letter-spacing:-.02em">Runner 02 · Custom</b><div><b>Color · Ember</b><div class="sw2" style="margin-top:10px"><i class="on" style="background:#FF5A36"></i><i style="background:#1F2937"></i><i style="background:#3B82F6"></i><i style="background:#A3E635"></i><i style="background:#F5F5F4"></i></div></div>
<div><b>Material</b><div class="mt" style="margin-top:10px"><span class="on">Knit</span><span>Leather +$20</span><span>Recycled</span></div></div><div><b>Monogram</b><div style="margin-top:8px;padding:12px;border:1.5px solid #e5e7eb;border-radius:12px;color:#999">"SC" on heel</div></div>
<div class="sm"><b>$149</b><span>Add to bag</span></div></div>"""

T["daybreak"] = BASE + """<style>body{background:#FFFCF7;color:#16151A;position:relative;font-family:-apple-system,Inter,sans-serif}
body::before{content:"";position:absolute;left:0;right:0;top:0;height:520px;background:linear-gradient(180deg,#FFD9C2,#E6DDFF 60%,transparent)}
.w{position:relative;display:grid;grid-template-columns:1.1fr 1fr;gap:40px;align-items:center;padding:110px 70px 0}h1{font-size:82px;letter-spacing:-.045em;line-height:.98}h1 em{font-family:Georgia,serif;font-weight:400;color:#FF6B3D}
p{font-size:20px;color:#55525c;margin:18px 0 26px}.f{display:flex;background:#fff;border-radius:99px;padding:6px;width:460px;box-shadow:0 10px 30px rgba(0,0,0,.08)}.f span{flex:1;padding:12px 18px;color:#aaa}.f b{padding:12px 20px;border-radius:99px;background:#16151A;color:#fff}
.ag{background:#fff;border-radius:22px;padding:24px;box-shadow:0 30px 60px -20px rgba(80,60,120,.3);border:1px solid #f0ebf5}.it{display:flex;gap:12px;align-items:center;padding:12px 0;border-top:1px solid #f4f0f7;font-size:16px}.it i{width:24px;height:24px;border-radius:50%;display:grid;place-items:center;font-size:12px;font-style:normal}
.ok{background:#dcfce7;color:#16a34a}.run{border:2.5px solid #FF6B3D;border-top-color:transparent;animation:spin 1s linear infinite}.it small{margin-left:auto;color:#aaa;font-size:13px}
</style><div class="w"><div><h1>Your inbox,<br>handled <em>by sunrise.</em></h1><p>Daybreak drafts replies, routes tickets and only asks you when it matters.</p><div class="f"><span>work email</span><b>Get early access</b></div></div>
<div class="ag"><b>Agent · Support inbox</b><div class="it"><i class="ok">✓</i>Read 24 new emails<small>6:02</small></div><div class="it"><i class="ok">✓</i>Drafted 18 replies<small>6:04</small></div><div class="it"><i class="ok">✓</i>Tagged 4 refund requests<small>6:05</small></div><div class="it"><i class="run"></i>Escalating 2 to you…<small>now</small></div></div></div>"""

T["formvoid"] = BASE + """<style>body{background:#EDEDEA;color:#0E0E0E;font-family:'Helvetica Neue',Arial,sans-serif;position:relative}
.cols{position:absolute;inset:0 50px;display:grid;grid-template-columns:repeat(12,1fr);pointer-events:none}.cols i{border-left:1px solid rgba(0,0,0,.07)}
.top{position:relative;display:flex;justify-content:space-between;padding:26px 50px;font-size:13px;letter-spacing:.14em}
.hero{position:relative;margin:0 50px;height:470px;background:linear-gradient(180deg,#bdbdb8,#6f6f6a)}
.hero::before{content:"";position:absolute;left:14%;bottom:0;width:44%;height:78%;background:#2c2c2a;clip-path:polygon(0 30%,60% 0,100% 20%,100% 100%,0 100%)}.hero::after{content:"";position:absolute;right:16%;bottom:0;width:22%;height:60%;background:#e6e6e2}
.cap{position:absolute;left:24px;bottom:20px;color:#fff;font-size:14px;letter-spacing:.1em}.pr{position:absolute;left:24px;right:24px;bottom:10px;height:2px;background:rgba(255,255,255,.3)}.pr i{display:block;width:35%;height:100%;background:#fff}
.ix{position:relative;margin:18px 50px 0}.ix div{display:grid;grid-template-columns:60px 1fr 200px 160px 60px;padding:12px 0;border-top:1px solid rgba(0,0,0,.15);font-size:15px}
</style><div class="cols">""" + "<i></i>"*12 + """</div><div class="top"><b>FORM &amp; VOID</b><span>PROJECTS · STUDIO · CONTACT</span></div>
<div class="hero"><span class="cap">HOUSE ON THE RIDGE · NORWAY · 2025</span><span class="pr"><i></i></span></div>
<div class="ix"><div><span>01</span><b>House on the Ridge</b><span>Residential</span><span>Norway</span><span>2025</span></div><div><span>02</span><b>Salt Library</b><span>Cultural</span><span>Portugal</span><span>2024</span></div></div>"""

T["roast"] = BASE + """<style>body{background:#F6EFE6;color:#2B1B12;display:grid;grid-template-columns:1.1fr 1fr;gap:30px;align-items:center;padding:0 70px;font-family:'Cooper Black','Recoleta',Georgia,serif;position:relative}
h1{font-size:92px;line-height:.92;letter-spacing:-.02em}p{font:20px -apple-system,sans-serif;margin:18px 0 26px;color:#5a4636}.b{display:flex;gap:12px;font:700 16px -apple-system,sans-serif}.b span{padding:15px 24px;border-radius:99px}
.bag{position:relative;margin:0 auto;width:320px;height:450px;background:#E2533A;border-radius:18px 18px 26px 26px;box-shadow:0 40px 70px -20px rgba(43,27,18,.5);transform:rotate(-4deg)}
.bag::before{content:"";position:absolute;left:0;right:0;top:0;height:60px;background:#c8432c;border-radius:18px 18px 0 0;clip-path:polygon(0 0,100% 0,100% 70%,90% 100%,80% 70%,70% 100%,60% 70%,50% 100%,40% 70%,30% 100%,20% 70%,10% 100%,0 70%)}
.lb{position:absolute;left:40px;right:40px;top:130px;background:#F6EFE6;border-radius:12px;padding:20px;text-align:center}.lb b{display:block;font-size:30px}.lb span{font:600 13px -apple-system,sans-serif;letter-spacing:.1em}
.stk{position:absolute;right:-40px;top:40px;width:130px;height:130px;border-radius:50%;background:#E6B422;display:grid;place-items:center;text-align:center;font:800 13px/1.2 -apple-system,sans-serif;transform:rotate(14deg)}
.dots{display:flex;gap:4px;justify-content:center;margin-top:8px}.dots i{width:10px;height:10px;border-radius:50%;background:#2B1B12}.dots i.o{background:#e1d3c3}
</style><div><h1>Coffee that<br>tastes like<br>Saturday.</h1><p>Small-batch roasts, delivered the week they're roasted.</p><div class="b"><span style="background:#2B1B12;color:#F6EFE6">Shop coffee</span><span style="border:2px solid #2B1B12">Take the quiz ☕</span></div></div>
<div style="position:relative"><div class="bag"><div class="lb"><span>ETHIOPIA · GUJI</span><b>Sunday Best</b><span style="letter-spacing:0">peach · jasmine · honey</span><div class="dots"><i></i><i></i><i class="o"></i><i class="o"></i><i class="o"></i></div></div><div class="stk">ROASTED<br>MONDAY,<br>AT YOUR DOOR<br>WEDNESDAY</div></div></div>"""

T["encore"] = BASE + """<style>body{background:#0D0B14;color:#F5F3FF;display:grid;grid-template-columns:1fr 1fr;gap:30px;padding:40px 56px;font-family:-apple-system,Inter,sans-serif}
.ev{border-radius:24px;overflow:hidden;background:linear-gradient(160deg,#FF3D7F,#7C5CFF 70%,#1b1030);position:relative;padding:28px}.ev h2{font:900 72px/.9 'Arial Narrow','Helvetica Neue',sans-serif;text-transform:uppercase;letter-spacing:-.02em;margin-top:180px}
.ev .d{position:absolute;left:28px;top:28px;background:#fff;color:#0D0B14;border-radius:14px;padding:10px 14px;text-align:center;font-weight:800}.ev p{opacity:.9;margin-top:10px}
.mp{background:#15121f;border:1px solid rgba(255,255,255,.08);border-radius:24px;padding:24px}.stg{margin:0 auto 18px;width:70%;padding:10px;text-align:center;border-radius:10px;background:#2a2340;font-size:13px;letter-spacing:.2em}
.rw{display:flex;gap:6px;justify-content:center;margin:6px 0}.rw i{width:22px;height:22px;border-radius:6px;background:#3a3350}.rw i.a{background:#7C5CFF}.rw i.s{background:#FF3D7F;box-shadow:0 0 0 3px rgba(255,61,127,.35)}.rw i.x{background:#221d33;opacity:.5}
.tm{display:flex;justify-content:space-between;margin-top:18px;padding:14px;border-radius:14px;background:rgba(255,61,127,.12);color:#ff9dbd;font-weight:700}
.sm{display:flex;justify-content:space-between;margin-top:12px;font-size:15px;color:#b8b0d6}.go{margin-top:16px;padding:16px;border-radius:14px;background:#FF3D7F;text-align:center;font-weight:800}
</style><div class="ev"><div class="d">OCT<br><span style="font-size:26px">18</span></div><h2>Neon<br>Harbor<br>Live</h2><p>Pier 9 Arena · Doors 7pm · 18+</p></div>
<div class="mp"><div class="stg">STAGE</div>""" + "".join('<div class="rw">'+"".join(f'<i class="{c}"></i>' for c in row)+'</div>' for row in ["aaxaaaaxaa","aaaassaaaa","xaaaaaaaax","aaaxaaaaaa","aaaaaxaaaa","aaxaaaaaaa"]) + """<div class="tm"><span>Seats held for you</span><span>08:42</span></div><div class="sm"><span>2 × Section B, Row 2</span><b style="color:#fff">$184.00 incl. fees</b></div><div class="go">Continue to payment</div></div>"""

T["counsel"] = BASE + """<style>body{background:#F8F5EF;color:#0F1E33;display:grid;grid-template-columns:1.2fr 1fr;font-family:-apple-system,Inter,sans-serif}
.l{padding:40px 70px}.l nav{display:flex;justify-content:space-between;font-size:14px;margin-bottom:100px}.l nav b{font:600 22px Georgia,serif;letter-spacing:.04em}
h1{font:400 78px/1 Georgia,'Source Serif 4',serif;letter-spacing:-.02em}p{font-size:20px;color:#4a5566;margin:20px 0 28px;max-width:520px}
.b{display:flex;gap:12px}.b span{padding:15px 24px;border-radius:4px;font-weight:600}.tr{display:flex;gap:36px;margin-top:40px;font-size:14px;color:#4a5566;border-top:1px solid #d9d2c4;padding-top:20px}.tr b{display:block;font:400 30px Georgia,serif;color:#0F1E33}
.r{background:#0F1E33;color:#F8F5EF;padding:60px 50px;display:flex;flex-direction:column;justify-content:flex-end;position:relative;overflow:hidden}
.r::before{content:"";position:absolute;right:-120px;top:-120px;width:420px;height:420px;border-radius:50%;border:1px solid rgba(176,141,87,.4);box-shadow:0 0 0 60px rgba(176,141,87,.06),0 0 0 120px rgba(176,141,87,.04)}
.pa div{padding:16px 0;border-top:1px solid rgba(248,245,239,.15);display:flex;justify-content:space-between;font-size:18px}.pa span{color:#B08D57}
</style><div class="l"><nav><b>Ashby &amp; Rowe</b><span>Services · People · Insights · Contact</span></nav><h1>Clear advice for<br>growing businesses.</h1><p>Corporate, employment and IP law for founders and scale-ups, explained in plain English.</p>
<div class="b"><span style="background:#0F1E33;color:#fff">Book a consultation</span><span style="border:1px solid #0F1E33">Our services</span></div><div class="tr"><div><b>32</b>years</div><div><b>1,400+</b>clients</div><div><b>4.9★</b>client rating</div></div></div>
<div class="r"><div style="color:#B08D57;font-size:13px;letter-spacing:.2em;margin-bottom:14px">PRACTICE AREAS</div><div class="pa"><div>Corporate &amp; fundraising<span>→</span></div><div>Employment<span>→</span></div><div>Intellectual property<span>→</span></div><div>Commercial contracts<span>→</span></div></div></div>"""

T["tides"] = BASE + """<style>body{background:#EDE3D1;color:#1D1B18;position:relative;font-family:-apple-system,sans-serif}
.h{position:absolute;inset:0 0 150px;background:linear-gradient(180deg,#f3c9a1 0%,#D98A5B 38%,#2F5D62 62%,#1f4246 100%);overflow:hidden}
.h::before{content:"";position:absolute;left:50%;top:190px;width:180px;height:180px;margin-left:-90px;border-radius:50%;background:#ffe0b8;opacity:.9;box-shadow:0 0 100px #ffcf99}
.h::after{content:"";position:absolute;left:0;right:0;bottom:0;height:260px;background:repeating-linear-gradient(180deg,rgba(255,255,255,.08) 0 3px,transparent 3px 18px)}
.t{position:absolute;left:0;right:0;top:70px;text-align:center;color:#fff}.t small{letter-spacing:.4em;font-size:13px}.t h1{font:400 96px Georgia,'Cormorant Garamond',serif;letter-spacing:.02em;margin-top:10px}
.bk{position:absolute;left:120px;right:120px;bottom:110px;display:grid;grid-template-columns:repeat(3,1fr) auto;background:#fff;border-radius:6px;padding:18px 18px 18px 30px;align-items:center;box-shadow:0 20px 50px rgba(0,0,0,.2)}.bk div b{display:block;font-size:12px;letter-spacing:.14em;color:#2F5D62}.bk div span{font:20px Georgia,serif}.bk i{font-style:normal;padding:16px 26px;background:#2F5D62;color:#fff;letter-spacing:.1em;font-size:13px;font-weight:700}
.bot{position:absolute;left:120px;right:120px;bottom:30px;display:flex;justify-content:space-between;font-size:14px;color:#5b5346}
</style><div class="h"></div><div class="t"><small>A HOTEL BY THE SEA · CORNWALL</small><h1>Tides House</h1></div>
<div class="bk"><div><b>CHECK IN</b><span>Fri, 17 Oct</span></div><div><b>CHECK OUT</b><span>Mon, 20 Oct</span></div><div><b>GUESTS</b><span>2 adults</span></div><i>CHECK AVAILABILITY</i></div><div class="bot"><span>Best rate guaranteed when you book direct</span><span>Rooms · Dining · Spa · Offers</span></div>"""

T["onair"] = BASE + """<style>body{background:#121015;color:#F6F1EA;display:grid;grid-template-columns:420px 1fr;gap:50px;align-items:center;padding:0 70px;font-family:Nunito,-apple-system,sans-serif;position:relative}
.cv{width:420px;height:420px;border-radius:24px;background:radial-gradient(circle at 50% 38%,#F59E0B 0 18%,#b45309 19% 22%,transparent 23%),linear-gradient(160deg,#3b1d4a,#121015);position:relative;box-shadow:0 40px 80px rgba(0,0,0,.6)}
.cv b{position:absolute;left:30px;bottom:30px;font-size:44px;font-weight:900;line-height:.95;letter-spacing:-.02em}.oa{position:absolute;right:24px;top:24px;padding:6px 12px;border-radius:8px;background:#F59E0B;color:#121015;font-weight:900;font-size:13px}
.k{color:#F59E0B;font-weight:800;font-size:14px;letter-spacing:.14em}h2{font-size:52px;letter-spacing:-.03em;line-height:1;margin:10px 0 20px}
.pl{background:#1c1920;border:1px solid rgba(255,255,255,.08);border-radius:20px;padding:20px}.row{display:flex;align-items:center;gap:14px}.row i{width:52px;height:52px;border-radius:50%;background:#F59E0B;color:#121015;display:grid;place-items:center;font-style:normal;font-size:20px}
.pb{position:relative;height:6px;border-radius:3px;background:#2e2a33;margin:18px 0 8px}.pb i{position:absolute;left:0;top:0;bottom:0;width:38%;border-radius:3px;background:#F59E0B}.pb b{position:absolute;top:-3px;width:2px;height:12px;background:#6b6470}
.ctl{display:flex;justify-content:space-between;font-size:13px;color:#a39bb0}.eps{margin-top:16px;font-size:15px;color:#cfc6d9}.eps div{padding:10px 0;border-top:1px solid rgba(255,255,255,.07);display:flex;justify-content:space-between}
</style><div class="cv"><span class="oa">● ON AIR</span><b>Late<br>Signal</b></div>
<div><div class="k">EPISODE 87 · 54 MIN</div><h2>What makes a product feel calm?</h2><div class="pl"><div class="row"><i>▶</i><div><b>with guest Priya Rao</b><div style="font-size:13px;color:#a39bb0">Chapter 3 · Designing for silence</div></div><span style="margin-left:auto;font-weight:800">1.5×</span></div>
<div class="pb"><i></i><b style="left:15%"></b><b style="left:38%"></b><b style="left:62%"></b><b style="left:81%"></b></div><div class="ctl"><span>20:31</span><span>−15s · +15s</span><span>−33:40</span></div></div>
<div class="eps"><div><span>86 · The myth of the power user</span><span>48 min</span></div><div><span>85 · Notes from 100 onboarding flows</span><span>51 min</span></div></div></div>"""

T["nest"] = BASE + """<style>body{background:#F3EEE7;color:#2A2522;display:grid;grid-template-columns:1fr 1.1fr;gap:50px;align-items:center;padding:0 80px;font-family:Georgia,'Cormorant Garamond',serif}
.ar{height:600px;border-radius:260px 260px 16px 16px;background:linear-gradient(180deg,#d9c7b3,#B7775A 70%,#8a5a44);position:relative;overflow:hidden}
.ar::before{content:"";position:absolute;left:18%;right:18%;bottom:0;height:34%;background:#6E7250;border-radius:40px 40px 0 0}.ar::after{content:"";position:absolute;right:14%;top:26%;width:80px;height:200px;border-radius:40px;background:#efe6da;opacity:.8}
.k{font:600 13px -apple-system,sans-serif;letter-spacing:.24em;color:#B7775A}h1{font-size:92px;line-height:.95;letter-spacing:-.02em;margin:18px 0}h1 i{color:#6E7250}
p{font:19px -apple-system,sans-serif;color:#6b615a;max-width:480px}.b{margin-top:28px;display:inline-block;padding:15px 28px;border-radius:99px;background:#2A2522;color:#F3EEE7;font:600 16px -apple-system,sans-serif}
.mb{display:flex;gap:10px;margin-top:34px}.mb div{width:74px;height:74px;border-radius:12px}.mb span{display:block;font:12px -apple-system,sans-serif;color:#6b615a;margin-top:6px;text-align:center}
</style><div class="ar"></div><div><div class="k">INTERIOR DESIGN STUDIO · AUSTIN</div><h1>Homes that feel<br>like <i>you.</i></h1><p>Warm, minimal interiors for real life, from single rooms to full renovations.</p><span class="b">Start a project</span>
<div class="mb"><div><div style="background:#B7775A"></div><span>Clay</span></div><div><div style="background:#6E7250"></div><span>Olive</span></div><div><div style="background:#e4d8c8"></div><span>Linen</span></div><div><div style="background:#8a6b52"></div><span>Walnut</span></div></div></div>"""

T["signal"] = BASE + """<style>body{background:#070B17;color:#E6ECFF;position:relative;font-family:'Inter Tight','Helvetica Neue',-apple-system,sans-serif;overflow:hidden}
.c{position:relative;padding:60px 70px}.k{font:600 14px ui-monospace,Menlo,monospace;color:#22D3EE;letter-spacing:.12em}h1{font-size:96px;letter-spacing:-.05em;line-height:.95;margin:18px 0}p{color:#8a95b8;font-size:20px}
svg{position:absolute;left:0;right:0;bottom:60px;width:100%;height:360px}.ctr{position:absolute;right:80px;top:80px;text-align:right}.ctr b{display:block;font:700 64px ui-monospace,Menlo,monospace;color:#A3E635}.ctr span{color:#8a95b8;font-size:14px}
.chip{position:absolute;padding:10px 14px;border-radius:12px;background:rgba(34,211,238,.1);border:1px solid rgba(34,211,238,.3);font:13px ui-monospace,Menlo,monospace;color:#bff4ff}
</style><div class="c"><div class="k">● LIVE</div><h1>See every signal<br>as it happens.</h1><p>Real-time product analytics without the lag.</p></div>
<div class="ctr"><b>12,480</b><span>events / sec</span></div>
<svg viewBox="0 0 1280 360" preserveAspectRatio="none"><defs><linearGradient id="lg" x1="0" x2="1"><stop offset="0" stop-color="#8B5CF6"/><stop offset="1" stop-color="#22D3EE"/></linearGradient><linearGradient id="fg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#22D3EE" stop-opacity=".25"/><stop offset="1" stop-color="#22D3EE" stop-opacity="0"/></linearGradient></defs>
<path d="M0 260 C120 240 180 280 260 230 S420 150 520 190 S700 260 800 170 S980 90 1080 130 S1200 60 1280 70 V360 H0Z" fill="url(#fg)"/>
<path d="M0 260 C120 240 180 280 260 230 S420 150 520 190 S700 260 800 170 S980 90 1080 130 S1200 60 1280 70" fill="none" stroke="url(#lg)" stroke-width="4"/><circle cx="1270" cy="72" r="9" fill="#22D3EE"><animate attributeName="r" values="7;12;7" dur="1.5s" repeatCount="indefinite"/></circle></svg>
<span class="chip" style="left:520px;top:430px">signup · Berlin · 2s ago</span><span class="chip" style="left:860px;top:360px">purchase · $49 · now</span>"""
