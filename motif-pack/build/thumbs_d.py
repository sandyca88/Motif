# part D: deck thumbnails (title slide of each style) + avatar set
from thumbs_a import BASE
T = {}
CNT = '<div style="position:absolute;right:40px;bottom:30px;font:600 14px ui-monospace,Menlo,monospace;opacity:.55">01 / 12</div>'

T["d_marker"] = BASE + """<style>
body{background:#FBF7EE;background-image:radial-gradient(#d9d2c3 1.2px,transparent 1.2px);background-size:28px 28px;color:#1E1B18;font-family:'Comic Neue','Segoe Print','Chalkboard SE',cursive;padding:90px 100px;position:relative}
h1{font-family:'Permanent Marker','Marker Felt','Chalkboard SE',cursive;font-size:118px;line-height:1;letter-spacing:-.01em;position:relative}
.hl{position:relative;z-index:1}.hl::before{content:"";position:absolute;left:-12px;right:-12px;top:52%;height:48%;background:#FFE14D;z-index:-1;transform:rotate(-1.5deg);border-radius:6px 20px 8px 16px;opacity:.9}
p{font-size:34px;margin-top:28px;max-width:720px}
.by{position:absolute;left:100px;bottom:70px;font-size:24px}
svg.d{position:absolute}.st{fill:none;stroke:#1E1B18;stroke-width:4;stroke-linecap:round;stroke-linejoin:round}
.note{position:absolute;right:120px;top:360px;width:280px;padding:26px;background:#9BE7C4;transform:rotate(3deg);font-size:26px;box-shadow:4px 6px 0 rgba(0,0,0,.1)}
</style>
<h1>How we <span class="hl">actually</span><br>ship features</h1>
<p>A visual field guide to our product process, in 8 doodles.</p>
<svg class="d" style="right:110px;top:70px" width="220" height="200"><path class="st" d="M40 150 q10-90 90-100 q60-5 70 40" /><path class="st" d="M185 70 l18 22 l-26 6" /><circle class="st" cx="60" cy="40" r="22"/><path class="st" d="M48 36h2M68 36h2M50 50q10 8 20 0"/></svg>
<div class="note">Spoiler: it starts with a <b>question</b>, not a solution →</div>
<svg class="d" style="left:90px;top:330px" width="760" height="40"><path d="M5 25 q60-20 120 0 t120 0 t120 0 t120 0 t120 0 t120 0" fill="none" stroke="#2F6BFF" stroke-width="5" stroke-linecap="round"/></svg>
<div class="by">Maya · Product Design Guild · Oct 2026</div>""" + CNT

T["d_kraft"] = BASE + """<style>
body{background:#C9A77C;padding:50px;position:relative}
.pg{position:absolute;inset:50px 50px 50px 120px;background:#F3EEE3;background-image:linear-gradient(#DCE4EC 1px,transparent 1px),linear-gradient(90deg,#DCE4EC 1px,transparent 1px);background-size:32px 32px;box-shadow:6px 8px 0 rgba(0,0,0,.15);padding:70px 80px}
.tab{position:absolute;left:62px;width:70px;height:110px;border-radius:10px 0 0 10px;font:700 14px 'Courier New',monospace;writing-mode:vertical-rl;display:grid;place-items:center;color:#23201C}
.stamp{display:inline-block;border:4px solid #B4412E;color:#B4412E;font:800 22px 'Courier New',monospace;letter-spacing:.2em;padding:8px 18px;transform:rotate(-3deg);opacity:.85}
h1{font-family:Georgia,'Source Serif 4',serif;font-size:86px;line-height:1;color:#23201C;margin:28px 0 18px;font-weight:600;letter-spacing:-.02em}
.tw{font:20px 'Courier New',monospace;color:#23201C}
.pol{position:absolute;right:70px;top:250px;width:250px;background:#fff;padding:14px 14px 50px;transform:rotate(4deg);box-shadow:0 12px 24px rgba(0,0,0,.18)}
.pol div{height:210px;background:linear-gradient(135deg,#8aa6a3,#3e5c5a)}.pol span{position:absolute;bottom:14px;left:18px;font:24px 'Bradley Hand','Segoe Print',cursive}
.tape{position:absolute;width:120px;height:34px;background:rgba(255,236,170,.8);top:-14px;left:90px;transform:rotate(-6deg)}
.mn{position:absolute;right:170px;bottom:120px;font:28px 'Bradley Hand','Segoe Print',cursive;color:#B4412E;transform:rotate(-4deg)}
</style>
<div class="tab" style="top:120px;background:#E9D3A6">FIELD</div><div class="tab" style="top:240px;background:#D7C29A">NOTES</div>
<div class="pg"><span class="stamp">FIELD REPORT · 03</span><h1>What 9 nurses<br>taught us about<br>night shifts</h1><div class="tw">Vol. 2 · Oct 2026 · St. Mary's, Ward 4B</div>
<div class="pol"><div class="tape"></div><div></div><span>P4 · 02:14am</span></div><div class="mn">7 of 9 said the same thing ↑</div></div>""" + CNT

T["d_collage"] = BASE + """<style>
body{background:#FFF8EF;position:relative;font-family:'DM Sans',sans-serif}
.s{position:absolute;filter:drop-shadow(5px 7px 0 rgba(0,0,0,.12))}
.ban{position:absolute;left:90px;top:90px;background:#fff;padding:34px 44px;clip-path:polygon(0 4%,3% 0,20% 3%,40% 0,62% 4%,80% 0,100% 3%,98% 50%,100% 96%,78% 100%,55% 96%,30% 100%,8% 97%,0 100%,2% 50%);filter:drop-shadow(6px 8px 0 rgba(0,0,0,.1))}
h1{font-family:Fraunces,'Recoleta',Georgia,serif;font-size:80px;line-height:1;color:#222;font-weight:900;letter-spacing:-.02em}
h1 span{color:#F2613F}
p{font-size:26px;color:#444;margin-top:14px}
</style>
<div class="s" style="right:120px;top:60px;width:240px;height:240px;border-radius:50%;background:#F7B32B"></div>
<svg class="s" style="left:0;bottom:0" width="1280" height="360"><path d="M0 180 C200 80 380 120 560 170 S900 60 1280 140 V360 H0Z" fill="#5DAA68"/><path d="M0 260 C240 190 460 230 700 260 S1080 200 1280 240 V360 H0Z" fill="#1F8A8A"/></svg>
<div class="s" style="left:420px;bottom:120px"><svg width="600" height="260">
<g><circle cx="60" cy="60" r="34" fill="#8A5530"/><rect x="18" y="100" width="84" height="150" rx="40" fill="#F2613F"/></g>
<g><circle cx="190" cy="40" r="34" fill="#F4D2B5"/><rect x="148" y="80" width="84" height="170" rx="40" fill="#B8A1E3"/><rect x="150" y="10" width="80" height="30" rx="15" fill="#222"/></g>
<g><circle cx="320" cy="70" r="34" fill="#B97A4F"/><rect x="278" y="110" width="84" height="140" rx="40" fill="#F7B32B"/></g>
<g><circle cx="450" cy="50" r="34" fill="#5A3825"/><rect x="408" y="90" width="84" height="160" rx="40" fill="#fff"/><circle cx="450" cy="20" r="20" fill="#5A3825"/></g>
<g><circle cx="570" cy="80" r="30" fill="#E0AC7E"/><rect x="534" y="116" width="72" height="134" rx="36" fill="#1F8A8A"/></g></svg></div>
<div class="ban"><h1>Everyone gets<br>a <span>seat</span> here.</h1><p>Our community program, 2027</p></div>""" + CNT

T["d_grid"] = BASE + """<style>
body{background:#F4F4F0;color:#111;font-family:'Inter Tight','Helvetica Neue',Helvetica,Arial,sans-serif;position:relative;
background-image:linear-gradient(90deg,rgba(0,0,0,.06) 1px,transparent 1px);background-size:calc((1280px - 160px)/12) 100%;background-position:80px 0}
.top{position:absolute;left:80px;right:80px;top:50px;display:flex;justify-content:space-between;font:500 15px ui-monospace,Menlo,monospace}
h1{position:absolute;left:80px;top:170px;width:760px;font-size:118px;line-height:.92;letter-spacing:-.05em;font-weight:700}
.blk{position:absolute;right:80px;top:170px;width:340px;height:470px;background:#1F3FFF}
.blk b{position:absolute;left:28px;bottom:24px;font-size:170px;color:#fff;letter-spacing:-.06em;line-height:.8}
.bot{position:absolute;left:80px;right:80px;bottom:46px;display:flex;justify-content:space-between;border-top:2px solid #111;padding-top:14px;font:500 15px ui-monospace,Menlo,monospace}
</style>
<div class="top"><span>01 / STRATEGY</span><span>PLATFORM REVIEW · Q4 2026</span></div>
<h1>One platform. Three bets. Zero rewrites.</h1>
<div class="blk"><b>03</b></div>
<div class="bot"><span>Design Systems Team</span><span>Confidential</span><span>p. 01</span></div>"""

T["d_serif"] = BASE + """<style>
body{background:#F5EFE4;color:#1C1A17;font-family:Georgia,'Source Serif 4',serif;position:relative}
.mast{position:absolute;left:70px;right:70px;top:40px;display:flex;justify-content:space-between;align-items:baseline;border-bottom:3px double #1C1A17;padding-bottom:12px}
.mast b{font:italic 400 44px 'Playfair Display','Didot',Georgia,serif}.mast span{font:600 13px -apple-system,sans-serif;letter-spacing:.2em}
.img{position:absolute;left:70px;right:70px;top:130px;bottom:70px;background:linear-gradient(160deg,#d7b98a 0%,#a8773a 55%,#4B4A2E 100%)}
.img::after{content:"";position:absolute;inset:0;background:radial-gradient(circle at 70% 30%,rgba(255,240,210,.55),transparent 45%)}
.t{position:absolute;left:120px;bottom:120px;color:#fff;max-width:760px}
.k{font:600 14px -apple-system,sans-serif;letter-spacing:.24em;margin-bottom:14px}
h1{font:400 100px/0.95 'Playfair Display','Didot',Georgia,serif;letter-spacing:-.02em}h1 i{color:#FBE3B8}
.f{position:absolute;right:100px;bottom:40px;font:italic 16px Georgia,serif}
</style>
<div class="mast"><b>The Quarterly</b><span>ISSUE 04 · AUTUMN 2026</span></div>
<div class="img"></div><div class="t"><div class="k">THE BRAND STORY</div><h1>Made slowly,<br>on <i>purpose.</i></h1></div><div class="f">— 01 —</div>"""

T["d_frost"] = BASE + """<style>
body{background:#F4F7FF;position:relative;font-family:'Plus Jakarta Sans','SF Pro Display',-apple-system,sans-serif;color:#16213A}
.o{position:absolute;border-radius:50%;filter:blur(60px);animation:fl 12s ease-in-out infinite alternate}
.g{position:absolute;left:170px;right:170px;top:150px;bottom:150px;border-radius:40px;background:rgba(255,255,255,.45);backdrop-filter:blur(24px) saturate(160%);border:1px solid rgba(255,255,255,.8);box-shadow:inset 0 1px 0 #fff,0 30px 80px rgba(80,90,180,.18);text-align:center;padding-top:110px}
.pl{display:inline-block;padding:8px 16px;border-radius:99px;background:rgba(255,255,255,.7);font-size:15px;font-weight:600;color:#5B6CFF}
h1{font-size:84px;letter-spacing:-.04em;line-height:1;margin:24px 0 16px;font-weight:700}
h1 span{background:linear-gradient(90deg,#5B6CFF,#A17BFF);-webkit-background-clip:text;color:transparent}
p{font-size:24px;color:#5B6785}
.c{position:absolute;padding:14px 20px;border-radius:18px;background:rgba(255,255,255,.6);backdrop-filter:blur(14px);border:1px solid #fff;font-weight:600;font-size:16px;box-shadow:0 10px 30px rgba(80,90,180,.15)}
</style>
<div class="o" style="width:520px;height:520px;left:-80px;top:-80px;background:#BFD9FF"></div><div class="o" style="width:460px;height:460px;right:-60px;top:80px;background:#E6D5FF;animation-delay:-4s"></div><div class="o" style="width:420px;height:420px;left:420px;bottom:-160px;background:#FFE2F0;animation-delay:-7s"></div>
<div class="g"><span class="pl">Keynote · 2027 Vision</span><h1>Software that<br><span>feels like air.</span></h1><p>Introducing Lumen OS 3</p></div>
<div class="c" style="left:110px;bottom:190px">✦ 40% faster</div><div class="c" style="right:120px;top:120px">Private by default</div>""" + CNT

T["d_riso"] = BASE + """<style>
body{background:#FFF6E8;position:relative;overflow:hidden;font-family:'Anton','Bebas Neue','Impact',sans-serif}
.sh{position:absolute;mix-blend-mode:multiply}
h1{position:absolute;left:70px;top:60px;font-size:210px;line-height:.84;text-transform:uppercase;letter-spacing:-.01em;color:#0078BF;mix-blend-mode:multiply}
h1.b{color:#FF48B0;left:78px;top:66px}
.stk{position:absolute;right:120px;bottom:90px;width:230px;height:230px;border-radius:50%;background:#FFE800;display:grid;place-items:center;text-align:center;font:700 26px/1.1 'Space Grotesk',-apple-system,sans-serif;color:#1a1a1a;transform:rotate(-10deg);mix-blend-mode:multiply}
.ht{position:absolute;inset:0;background-image:radial-gradient(rgba(0,0,0,.18) 1.4px,transparent 1.6px);background-size:9px 9px;opacity:.35;pointer-events:none}
</style>
<div class="sh" style="right:260px;top:120px;width:360px;height:360px;border-radius:50%;background:#FF48B0"></div>
<div class="sh" style="right:80px;top:260px;width:340px;height:340px;background:#0078BF;transform:rotate(18deg)"></div>
<svg class="sh" style="left:560px;top:470px" width="200" height="200"><polygon points="100,0 124,70 200,76 140,122 162,200 100,154 38,200 60,122 0,76 76,70" fill="#FFE800"/></svg>
<h1 class="b">Gather<br>Round<br>Friday</h1><h1>Gather<br>Round<br>Friday</h1>
<div class="stk">OCT 18<br>7PM · THE<br>OLD MILL</div><div class="ht"></div>"""

T["d_board"] = BASE + """<style>
body{background:#fff;color:#0E1A2B;font-family:Inter,'Source Sans 3',-apple-system,sans-serif;padding:60px 80px;position:relative}
.tr{position:absolute;right:80px;top:40px;font-size:13px;color:#5E6B7D;display:flex;gap:6px}.tr span{padding:4px 10px;border:1px solid #D9DEE5;border-radius:4px}.tr .on{background:#0B2A5B;color:#fff;border-color:#0B2A5B}
h2{font-size:38px;line-height:1.2;font-weight:600;max-width:1000px;margin-top:30px;letter-spacing:-.01em}
.row{display:grid;grid-template-columns:1.5fr 1fr;gap:40px;margin-top:40px}
.ch{border-top:2px solid #0E1A2B;padding-top:16px}.bars{display:flex;align-items:end;gap:26px;height:330px;padding:0 10px;border-bottom:1px solid #D9DEE5}
.bars div{flex:1;text-align:center;font-size:15px;color:#5E6B7D}.bars i{display:block;background:#C5CEDB;margin-bottom:8px}.bars .hi i{background:#0FA3A3}.bars b{display:block;color:#0E1A2B;font-size:18px;margin-bottom:6px}
.co{display:grid;gap:18px}.co div{border-left:4px solid #0B2A5B;padding:4px 0 4px 18px;font-size:19px;line-height:1.4}.co div:first-child{border-color:#0FA3A3}
.src{position:absolute;left:80px;bottom:30px;font-size:13px;color:#5E6B7D}.pn{position:absolute;right:80px;bottom:30px;font-size:13px;color:#5E6B7D}
</style>
<div class="tr"><span>Situation</span><span class="on">Opportunity</span><span>Recommendation</span><span>Plan</span></div>
<h2>Mid-market accounts grow 2.4× faster than enterprise, so we should shift 30% of sales capacity there in 2027</h2>
<div class="row"><div class="ch"><b>Net revenue retention by segment, %</b><div class="bars">
<div><b>104</b><i style="height:150px"></i>Enterprise</div><div class="hi"><b>131</b><i style="height:260px"></i>Mid-market</div><div><b>97</b><i style="height:120px"></i>SMB</div><div><b>112</b><i style="height:185px"></i>Public sector</div></div></div>
<div class="co"><div>Mid-market has the highest expansion and lowest CAC payback (9 mo)</div><div>Enterprise deals take 2.1× longer to close</div><div>SMB churn offsets new bookings</div></div></div>
<div class="src">Source: CRM export FY26, n = 1,284 accounts</div><div class="pn">7</div>"""

AV = [("#F2613F","#F4D2B5","c"),("#6D4AFF","#8A5530","s"),("#1F8A8A","#E0AC7E","b"),("#F7B32B","#5A3825","a"),("#5DAA68","#F4D2B5","l"),("#FF48B0","#B97A4F","c"),("#0078BF","#E0AC7E","s"),("#B8A1E3","#8A5530","b"),("#E4572E","#F4D2B5","a"),("#0F7B5F","#5A3825","l"),("#D98E04","#B97A4F","c"),("#2B50FF","#E0AC7E","s")]
def av(i,bg,skin,hair):
    eyes = ['<circle cx="100" cy="118" r="7"/><circle cx="156" cy="118" r="7"/>','<path d="M92 120 q8-10 16 0M148 120 q8-10 16 0" fill="none" stroke="#1E1B18" stroke-width="5" stroke-linecap="round"/>','<circle cx="100" cy="118" r="14" fill="none" stroke="#1E1B18" stroke-width="4"/><circle cx="156" cy="118" r="14" fill="none" stroke="#1E1B18" stroke-width="4"/><path d="M114 118h28" stroke="#1E1B18" stroke-width="4"/><circle cx="100" cy="118" r="5"/><circle cx="156" cy="118" r="5"/>'][i%3]
    mouth = ['<path d="M108 150 q20 18 40 0" fill="none" stroke="#1E1B18" stroke-width="5" stroke-linecap="round"/>','<ellipse cx="128" cy="154" rx="10" ry="8"/>','<path d="M106 148 h44 q-4 20-22 20 q-18 0-22-20z" fill="#1E1B18"/>'][(i*2)%3]
    top = {"c":'<circle cx="84" cy="62" r="26"/><circle cx="118" cy="46" r="28"/><circle cx="154" cy="50" r="26"/><circle cx="180" cy="72" r="22"/>',
           "s":'<path d="M64 88 L84 30 L104 70 L128 22 L150 70 L172 30 L192 88Z"/>',
           "b":'<circle cx="128" cy="30" r="24"/><path d="M62 92 q66-70 132 0 v-10 q-66-60-132 0z"/>',
           "a":'<path d="M128 56 q-4-30 20-44" fill="none" stroke="#1E1B18" stroke-width="5"/><circle cx="150" cy="12" r="10" fill="#FFE14D"/>',
           "l":'<path d="M70 80 q58-80 116 0 q-58-30-116 0z"/><path d="M128 40 q30-40 60-26 q-26 30-60 26z" fill="#5DAA68"/>'}[hair]
    return f'<div class="t" style="background:{bg}"><svg viewBox="0 0 256 256"><g fill="#1E1B18">{top}</g><rect x="64" y="60" width="128" height="140" rx="60" fill="{skin}"/><circle cx="92" cy="96" r="10" fill="#fff" opacity=".35"/><g fill="#1E1B18">{eyes}{mouth}</g><circle cx="86" cy="146" r="9" fill="#F2613F" opacity=".35"/><circle cx="170" cy="146" r="9" fill="#F2613F" opacity=".35"/></svg><span>{i+1:02d}</span></div>'
T["avatar"] = BASE + """<style>body{background:#111114;padding:44px 56px;color:#fff}
h2{font-size:30px;letter-spacing:-.02em;margin-bottom:6px}.m{color:#8e8e96;font-size:15px;margin-bottom:20px}
.g{display:grid;grid-template-columns:repeat(6,1fr);gap:16px}.t{border-radius:22px;aspect-ratio:1;position:relative;display:grid;place-items:center;animation:up .7s both}
.t svg{width:86%}.t span{position:absolute;left:12px;top:10px;font:600 12px ui-monospace,Menlo,monospace;color:rgba(0,0,0,.45)}
.sm{display:flex;gap:14px;margin-top:22px;align-items:center;color:#8e8e96;font-size:14px}.sm i{width:32px;height:32px;border-radius:50%;overflow:hidden;display:block}
</style><h2>Bloblings: avatar family</h2><div class="m">12 original characters · 1 construction system · SVG · &lt; 3KB each</div><div class="g">""" + "".join(av(i,*a) for i,a in enumerate(AV)) + """</div>
<div class="sm">32px check →""" + "".join(f'<i style="background:{a[0]}"></i>' for a in AV[:8]) + "</div>"
