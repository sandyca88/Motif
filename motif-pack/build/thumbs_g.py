# part G: Obsidian deck + video skills
from thumbs_a import BASE
T = {}
T["d_obsidian"] = BASE + """<style>
body{background:#050507;color:#F5F5F7;position:relative;font-family:'Inter Tight','SF Pro Display',-apple-system,sans-serif;padding:90px 96px}
body::before{content:"";position:absolute;inset:0;background:radial-gradient(900px 460px at 50% -10%,rgba(124,92,255,.22),transparent)}
.gl{position:absolute;left:360px;top:220px;width:640px;height:360px;border-radius:50%;filter:blur(90px);opacity:.42;background:linear-gradient(90deg,#7C5CFF,#22D3EE)}
.k{position:relative;font:500 15px ui-monospace,Menlo,monospace;letter-spacing:.12em;color:#8E8E96}
h1{position:relative;font-size:104px;font-weight:650;letter-spacing:-.05em;line-height:.98;margin:26px 0 28px}
.g{background:linear-gradient(90deg,#7C5CFF,#22D3EE);-webkit-background-clip:text;color:transparent}
p{position:relative;font-size:24px;color:#8E8E96}
.strip{position:absolute;left:96px;right:96px;bottom:50px;display:grid;grid-template-columns:repeat(4,1fr);gap:14px}
.strip div{aspect-ratio:16/9;border-radius:12px;background:#0d0d11;border:1px solid rgba(255,255,255,.1);padding:12px;font-size:12px;color:#8E8E96;position:relative;overflow:hidden}
.strip b{display:block;color:#F5F5F7;font-size:26px;letter-spacing:-.03em;margin-top:6px}
.bar{position:absolute;bottom:12px;width:16px;border-radius:3px;background:#26262c}
</style><div class="gl"></div><div class="k">NORTHSTAR · SERIES A · OCTOBER 2026</div>
<h1>Scheduling that<br><span class="g">runs itself.</span></h1><p>Complete 10-slide sample deck included</p>
<div class="strip"><div>02 — MARKET<b class="g" style="font-size:44px">$41B</b></div>
<div>03 — SOLUTION<b>Fills every slot.</b></div>
<div>04 — TRACTION<i class="bar" style="left:14px;height:18px"></i><i class="bar" style="left:36px;height:26px"></i><i class="bar" style="left:58px;height:40px"></i><i class="bar" style="left:80px;height:56px;background:linear-gradient(#22D3EE,#7C5CFF)"></i></div>
<div>08 — THE ASK<b>Raising <span class="g">$12M</span></b></div></div>"""

T["vprompt"] = BASE + """<style>
body{background:#07070a;color:#eee;display:grid;grid-template-columns:1.15fr 1fr;gap:28px;padding:44px}
.fr{position:relative;border-radius:18px;overflow:hidden;background:linear-gradient(180deg,#2b1a0e,#5a3417 45%,#1a0f08);box-shadow:0 30px 60px rgba(0,0,0,.5)}
.fr::before{content:"";position:absolute;right:-60px;top:-60px;width:360px;height:360px;border-radius:50%;background:radial-gradient(circle,rgba(255,200,120,.75),transparent 65%)}
.mug{position:absolute;left:190px;bottom:120px;width:190px;height:170px;border-radius:14px 14px 46px 46px;background:linear-gradient(90deg,#141414,#2a2a2a 60%,#111)}
.mug::after{content:"";position:absolute;right:-50px;top:40px;width:60px;height:80px;border:16px solid #1c1c1c;border-left:0;border-radius:0 40px 40px 0}
.st{position:absolute;left:260px;bottom:300px;width:6px;height:150px;border-radius:3px;background:linear-gradient(transparent,rgba(255,255,255,.35));filter:blur(2px);animation:bob 3s ease-in-out infinite}
.tb{position:absolute;left:0;right:0;bottom:0;height:92px;background:#3b2414}
.hud{position:absolute;left:16px;top:14px;right:16px;display:flex;justify-content:space-between;font:600 13px ui-monospace,Menlo,monospace;color:rgba(255,255,255,.8)}
.rec{color:#ff5a5a}.cor i{position:absolute;width:26px;height:26px;border-color:rgba(255,255,255,.6);border-style:solid}
.p{background:#101014;border:1px solid rgba(255,255,255,.1);border-radius:18px;padding:22px;font-size:14px;line-height:1.55}
.lb{font:700 11px ui-monospace,Menlo,monospace;letter-spacing:.12em;color:#8e8e96;margin-bottom:10px}
.pt{display:grid;grid-template-columns:110px 1fr;gap:8px 12px;margin-top:6px}.pt b{color:#f59e0b;font:600 12px ui-monospace,Menlo,monospace}
.cfg{display:flex;gap:8px;margin-top:16px;flex-wrap:wrap}.cfg span{padding:6px 10px;border-radius:8px;background:#1b1b21;font:12px ui-monospace,Menlo,monospace;color:#bbb}
</style>
<div class="fr"><div class="tb"></div><div class="mug"></div><div class="st"></div><div class="st" style="left:300px;animation-delay:-1s;height:120px"></div>
<div class="hud"><span class="rec">● REC 00:06</span><span>100mm · f/2.8 · 16:9</span></div>
<div class="cor"><i style="left:14px;bottom:14px;border-width:0 0 2px 2px"></i><i style="right:14px;bottom:14px;border-width:0 2px 2px 0"></i></div></div>
<div class="p"><div class="lb">VIDEO-PROMPT-DIRECTOR · 8-PART SHOT</div>
<div class="pt"><b>SHOT</b><span>Macro close-up</span><b>SUBJECT</b><span>Matte-black ceramic mug on walnut</span><b>ACTION</b><span>Coffee poured from above, crema swirls</span><b>CAMERA</b><span>Slow push-in</span><b>LENS</b><span>100mm macro, shallow DoF</span><b>LIGHT</b><span>Golden side light, drifting steam</span><b>AUDIO</b><span>Café ambience, soft pour</span></div>
<div class="cfg"><span>16:9</span><span>6s</span><span>motion: low</span><span>no text</span><span>+2 variants</span></div></div>"""

T["storyboard"] = BASE + """<style>
body{background:#0c0c10;color:#eee;padding:40px 44px}
h2{font-size:30px;letter-spacing:-.02em}.m{color:#8e8e96;font-size:14px;margin:6px 0 20px}
.g{display:grid;grid-template-columns:repeat(6,1fr);gap:12px}
.f{border-radius:12px;overflow:hidden;background:#15151b;border:1px solid rgba(255,255,255,.08)}
.f .v{aspect-ratio:9/12;position:relative;display:grid;place-items:center;font-weight:800;text-align:center;padding:10px;font-size:20px;line-height:1.05}
.f .c{padding:9px 10px;font-size:11.5px;color:#aaa;line-height:1.4}.f .c b{color:#fff;font:600 11px ui-monospace,Menlo,monospace;display:block;margin-bottom:3px}
.tl{margin-top:18px;height:34px;border-radius:8px;background:#15151b;position:relative;overflow:hidden;display:flex}
.tl i{height:100%;border-right:2px solid #0c0c10;display:grid;place-items:center;font:600 11px ui-monospace,Menlo,monospace;color:#111}
.ph{position:absolute;top:0;bottom:0;left:38%;width:2px;background:#fff}
</style><h2>Launch storyboard · "Pocket" meal planner · 30s · 9:16</h2><div class="m">Hook → Problem → Reveal → Show → Proof → CTA · VO 2.5 words/sec · captions + 15s / 6s cut-downs</div>
<div class="g">
<div class="f"><div class="v" style="background:linear-gradient(160deg,#FF7A45,#ff4d7a)">Dinner,<br>solved.</div><div class="c"><b>0–2s HOOK</b>Kinetic text slam, whoosh</div></div>
<div class="f"><div class="v" style="background:#2a2230;color:#ddd;font-size:16px">😩 "What's for dinner?" ×7</div><div class="c"><b>2–7s PROBLEM</b>Fridge-open B-roll (AI prompt)</div></div>
<div class="f"><div class="v" style="background:#101014"><span style="width:70px;height:70px;border-radius:20px;background:#FF7A45;display:block"></span></div><div class="c"><b>7–12s REVEAL</b>Logo + "Meals planned in 60s"</div></div>
<div class="f"><div class="v" style="background:#fff;color:#111;font-size:15px">[UI] pick<br>tastes →</div><div class="c"><b>12–18s SHOW</b>Screen rec, zoom to chips</div></div>
<div class="f"><div class="v" style="background:#FFF6F0;color:#111;font-size:15px">[UI] weekly<br>plan ✓</div><div class="c"><b>18–24s SHOW</b>Swap a meal, pop SFX</div></div>
<div class="f"><div class="v" style="background:linear-gradient(160deg,#1b1b1f,#3a2a22)">4.9★<br><span style="font-size:14px;font-weight:600">Get it free →</span></div><div class="c"><b>24–30s PROOF + CTA</b>Rating, App Store badge, hold 2s</div></div></div>
<div class="tl"><i style="width:6.7%;background:#FF7A45">H</i><i style="width:16.7%;background:#f4b39a">PROBLEM</i><i style="width:16.7%;background:#a78bfa">REVEAL</i><i style="width:40%;background:#67e8f9">SHOW</i><i style="width:20%;background:#34d399">PROOF · CTA</i><span class="ph"></span></div>"""
