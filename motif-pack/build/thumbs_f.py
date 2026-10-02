# part F: thumbnails for batch-3 skills
from thumbs_a import BASE
from thumbs_c import DOC
T = {}

T["dsys"] = BASE + DOC + """<style>body{zoom:1.22}
.g{display:grid;grid-template-columns:1.1fr 1fr;gap:20px}
.rp{display:flex;border-radius:10px;overflow:hidden;margin:8px 0 14px}.rp i{flex:1;height:48px}
.ty div{display:flex;align-items:baseline;gap:14px;margin:6px 0}.ty small{width:60px;font:12px ui-monospace,Menlo,monospace;color:#8b8b9a}
.bt{display:inline-flex;padding:10px 16px;border-radius:10px;font-weight:600;font-size:14px;margin:0 8px 8px 0}
.inp{border:1px solid rgba(255,255,255,.15);border-radius:10px;padding:10px 12px;font-size:14px;margin:8px 0 4px;color:#ddd}
.tk{font:12px ui-monospace,Menlo,monospace;color:#8b8b9a}
</style><div class="agent"><i></i>design-system-starter · brand #6D4AFF + Manrope</div>
<div class="g"><div class="card"><b>Color · primary 50–950</b><div class="rp">""" + "".join(f'<i style="background:{c}"></i>' for c in ["#F4F1FF","#E9E3FF","#D4C7FF","#B7A1FF","#9474FF","#6D4AFF","#5A33F0","#4A25CC","#3C20A3","#2F1C7D","#1C1152"]) + """</div>
<b>Neutral</b><div class="rp">""" + "".join(f'<i style="background:{c}"></i>' for c in ["#FAFAFA","#F4F4F5","#E4E4E7","#D4D4D8","#A1A1AA","#71717A","#52525B","#3F3F46","#27272A","#18181B","#09090B"]) + """</div>
<div class="tk">--primary · --text · --border · --focus-ring · AA ✓ 14/14</div>
<div class="ty" style="margin-top:16px"><div><small>5xl</small><span style="font-size:44px;font-weight:700;letter-spacing:-.03em">Display</span></div><div><small>2xl</small><span style="font-size:26px;font-weight:600">Heading</span></div><div><small>base</small><span style="font-size:16px">Body text for reading</span></div></div></div>
<div class="card"><b>Button · all states</b><div style="margin-top:12px"><span class="bt" style="background:#6D4AFF">Default</span><span class="bt" style="background:#5A33F0">Hover</span><span class="bt" style="background:#6D4AFF;box-shadow:0 0 0 3px #0b0b10,0 0 0 5px #B7A1FF">Focus</span><span class="bt" style="background:#3F3F46;color:#71717A">Disabled</span><span class="bt" style="border:1px solid rgba(255,255,255,.2)">Secondary</span><span class="bt" style="background:#DC2626">Delete</span></div>
<b style="display:block;margin-top:14px">Input</b><div class="inp">dana@fernway.com</div><div class="inp" style="border-color:#DC2626">fernway.c</div><div style="color:#F87171;font-size:13px">Enter a full email address, e.g. name@company.com</div>
<div class="tk" style="margin-top:14px">tokens.css · tailwind.config.js · tokens.json · styleguide.html</div></div></div>"""

T["casestudy"] = BASE + """<style>
body{background:#F6F3EE;color:#141414;padding:60px 80px}
.k{font:600 13px -apple-system,sans-serif;letter-spacing:.18em;color:#E4572E}
h1{font:400 64px/1.02 'Iowan Old Style','Palatino Linotype',Georgia,serif;letter-spacing:-.02em;margin:14px 0 22px;max-width:900px}
.row{display:flex;gap:40px;border-top:1px solid #d9d2c6;border-bottom:1px solid #d9d2c6;padding:14px 0;font-size:15px}.row b{display:block;font-size:12px;letter-spacing:.12em;color:#8a8175;margin-bottom:4px}
.g{display:grid;grid-template-columns:1fr 1fr;gap:30px;margin-top:26px}
.tl{background:#fff;border-radius:16px;padding:22px;font-size:17px;line-height:1.5}.tl li{margin:6px 0 6px 18px}
.m{display:flex;gap:16px}.m div{flex:1;background:#141414;color:#fff;border-radius:16px;padding:18px}.m b{font:400 54px Georgia,serif;display:block;color:#FFB199}
.cap{font:italic 15px Georgia,serif;color:#6b645a;margin-top:10px}
</style><div class="k">CASE STUDY · BRIGHTPAY</div><h1>Redesigning onboarding to lift activation 32%</h1>
<div class="row"><div><b>ROLE</b>Lead Product Designer</div><div><b>TEAM</b>PM, 3 eng, researcher</div><div><b>TIMELINE</b>10 weeks</div><div><b>PLATFORM</b>iOS · Web</div></div>
<div class="g"><div class="tl"><b>TL;DR</b><ul><li>60% of new users never connected a bank.</li><li>I moved value before setup and cut 9 steps to 4.</li><li>Activation rose 32%; support tickets fell by a third.</li></ul></div>
<div><div class="m"><div><b>+32%</b>activation</div><div><b>9→4</b>steps</div></div><div class="cap">"Moving plan selection before sign-up halved drop-off at step 2."</div></div></div>"""

T["form"] = BASE + DOC + """<style>
.g{display:grid;grid-template-columns:1fr 1fr;gap:22px}.lb{font-size:12px;font-weight:700;letter-spacing:.12em;margin-bottom:12px}
.f{background:#fff;color:#111;border-radius:16px;padding:22px}.fl{margin-bottom:12px}.fl span{display:block;font-size:13px;font-weight:600;margin-bottom:5px}.fl i{display:block;height:38px;border:1px solid #d4d4d8;border-radius:9px}
.bad .fl i{border-radius:3px;background:#f4f4f5}.bad .ph{font-size:13px;color:#aaa;padding:10px}
.two{display:grid;grid-template-columns:1fr 1fr;gap:10px}.b{height:44px;border-radius:10px;background:#111;color:#fff;display:grid;place-items:center;font-weight:700}
.big{font-size:40px;font-weight:700;letter-spacing:-.03em}
</style><div class="agent"><i></i>form-ux-optimizer · checkout.html</div>
<div class="g"><div><div class="lb" style="color:#f87171">BEFORE · 14 FIELDS</div><div class="f bad">""" + "".join('<div class="fl"><i class="ph">'+p+'</i></div>' for p in ["First name*","Last name*","Email*","Confirm email*","Phone*","Company*","Address line 1*","City*","State*","ZIP*"]) + """<div class="b" style="background:#999">Submit</div></div></div>
<div><div class="lb" style="color:#34d399">AFTER · 8 FIELDS</div><div class="f"><div class="fl"><span>Email</span><i></i></div><div class="fl"><span>Full name</span><i></i></div><div class="fl"><span>Address</span><i></i></div><div class="two"><div class="fl"><span>ZIP code</span><i></i></div><div class="fl"><span>City <small style="color:#888;font-weight:400">auto-filled</small></span><i style="background:#f4f4f5"></i></div></div><div class="two"><div class="fl"><span>Card number</span><i></i></div><div class="fl"><span>MM / YY · CVC</span><i></i></div></div><div class="b">Pay $49.00</div></div>
<div style="display:flex;gap:26px;margin-top:16px"><div><div class="big">−43%</div><div class="mut">fields</div></div><div><div class="big">14</div><div class="mut">autocomplete tokens added</div></div></div></div></div>"""

T["a11y"] = BASE + DOC + """<style>body{zoom:1.32}
.g{display:grid;grid-template-columns:300px 1fr;gap:20px}.n{font-size:64px;font-weight:700;letter-spacing:-.04em}
.row{display:grid;grid-template-columns:150px 1fr 70px 90px;gap:10px;padding:11px 0;border-top:1px solid rgba(255,255,255,.07);font-size:14px;align-items:center}
.mono{font:12px ui-monospace,Menlo,monospace;color:#8b8b9a}.sv{font-size:11px;font-weight:700;padding:3px 8px;border-radius:6px;width:max-content}
.cr{background:rgba(248,113,113,.15);color:#f87171}.se{background:rgba(251,191,36,.15);color:#fbbf24}.mo{background:rgba(139,92,246,.15);color:#a78bfa}
.sw{display:flex;gap:8px;align-items:center;margin-top:14px;font-size:14px}.sw i{width:26px;height:26px;border-radius:6px;display:block}
</style><div class="agent"><i></i>a11y-fixer · src/components · WCAG 2.2 AA</div>
<div class="g"><div class="card"><div class="mut">Issues fixed</div><div class="n" style="color:#34d399">23<span style="font-size:24px;color:#8b8b9a"> / 26</span></div><div class="mut">3 need your input (alt text, captions)</div>
<div class="sw"><i style="background:#8B9BFF"></i>3.2:1 → <i style="background:#4F46E5"></i>6.4:1 ✓</div></div>
<div class="card" style="padding:8px 22px"><div class="row mono" style="border:0"><span>FILE:LINE</span><span>FIX</span><span>WCAG</span><span>SEVERITY</span></div>
<div class="row"><span class="mono">Modal.tsx:42</span><span>Trap focus, Esc closes, return focus to trigger</span><span class="mono">2.4.3</span><span class="sv cr">Critical</span></div>
<div class="row"><span class="mono">Nav.tsx:18</span><span>div onClick → &lt;button&gt; with aria-expanded</span><span class="mono">4.1.2</span><span class="sv cr">Critical</span></div>
<div class="row"><span class="mono">Form.tsx:77</span><span>Linked error text via aria-describedby</span><span class="mono">3.3.1</span><span class="sv se">Serious</span></div>
<div class="row"><span class="mono">Button.css:9</span><span>Added :focus-visible ring (3:1)</span><span class="mono">2.4.7</span><span class="sv se">Serious</span></div>
<div class="row"><span class="mono">Hero.tsx:31</span><span>prefers-reduced-motion stops loop</span><span class="mono">2.3.3</span><span class="sv mo">Moderate</span></div></div></div>"""

T["usability"] = BASE + DOC + """<style>body{zoom:1.3}
.g{display:grid;grid-template-columns:1fr 1fr;gap:20px}
.cl{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin-top:12px}.st{border-radius:8px;padding:10px;font-size:12.5px;color:#1a1a1a;line-height:1.35}
.th{font-size:13px;font-weight:700;margin:14px 0 4px;color:#fff}
.tk{display:grid;grid-template-columns:1fr 70px 60px;padding:9px 0;border-top:1px solid rgba(255,255,255,.07);font-size:14px}.bar{height:6px;border-radius:3px;background:rgba(255,255,255,.08);margin-top:6px}.bar i{display:block;height:100%;border-radius:3px}
</style><div class="agent"><i></i>usability-test-kit · 6 sessions · checkout prototype v3</div>
<div class="g"><div class="card"><b>Affinity synthesis</b>
<div class="th">"Shipping cost appears too late" · 5/6</div><div class="cl"><div class="st" style="background:#FFE14D">P2: "Wait, why is it $12 more now?"</div><div class="st" style="background:#FFE14D">P4 went back to cart twice</div><div class="st" style="background:#FFE14D">P5: "I'd leave here."</div></div>
<div class="th">"Promo field is a distraction" · 4/6</div><div class="cl"><div class="st" style="background:#9BE7C4">P1 left to search for a code</div><div class="st" style="background:#9BE7C4">P3: "Am I overpaying?"</div><div class="st" style="background:#9BE7C4">P6 hesitated 40s</div></div></div>
<div class="card"><b>Task results</b>
<div class="tk mut" style="border:0;font-size:12px"><span>TASK</span><span>SUCCESS</span><span>SEQ</span></div>
<div class="tk"><span>Find a size-10 sneaker<div class="bar"><i style="width:100%;background:#34d399"></i></div></span><span>6/6</span><span>6.5</span></div>
<div class="tk"><span>Apply store credit<div class="bar"><i style="width:50%;background:#fbbf24"></i></div></span><span>3/6</span><span>3.8</span></div>
<div class="tk"><span>Check out as guest<div class="bar"><i style="width:67%;background:#fbbf24"></i></div></span><span>4/6</span><span>4.6</span></div>
<div style="margin-top:16px;padding:12px;border-radius:10px;background:rgba(248,113,113,.1);color:#fca5a5;font-size:14px"><b>Critical:</b> show shipping cost on the product page · Owner: Checkout team · Effort: S</div></div></div>"""

T["aiux"] = BASE + DOC + """<style>body{zoom:1.3}
.g{display:grid;grid-template-columns:1fr 1fr;gap:20px}
.stp div{display:flex;gap:10px;align-items:center;padding:8px 0;font-size:15px}.stp i{width:20px;height:20px;border-radius:50%;display:grid;place-items:center;font-size:11px;font-style:normal}
.ok{background:rgba(52,211,153,.2);color:#34d399}.run{border:2px solid #22d3ee;border-top-color:transparent;animation:spin 1s linear infinite}.wait{border:2px solid #444}
.ap{background:#fff;color:#111;border-radius:16px;padding:20px}.ap h4{font-size:18px}.df{font:13px/1.7 ui-monospace,Menlo,monospace;background:#f6f6f7;border-radius:10px;padding:10px 12px;margin:12px 0}
.df .a{color:#15803d}.df .r{color:#b91c1c;text-decoration:line-through}.bt{display:flex;gap:8px}.bt span{padding:10px 14px;border-radius:10px;font-weight:600;font-size:14px}
.mx{display:grid;grid-template-columns:repeat(4,1fr);gap:6px;margin-top:12px;font-size:12px;text-align:center}.mx div{padding:10px 4px;border-radius:8px}
</style><div class="agent"><i></i>ai-product-ux · "Inbox agent" for support teams</div>
<div class="g"><div><div class="card"><b>Agent progress (visible, stoppable)</b><div class="stp" style="margin-top:8px"><div><i class="ok">✓</i>Read 38 new tickets</div><div><i class="ok">✓</i>Grouped into 5 topics</div><div><i class="run"></i>Drafting replies for "refund delays"…</div><div><i class="wait"></i>Waiting for your approval</div></div><div style="margin-top:10px;display:inline-block;padding:8px 14px;border:1px solid rgba(255,255,255,.2);border-radius:99px;font-size:13px">■ Stop</div></div>
<div class="card" style="margin-top:16px"><b>Autonomy × risk</b><div class="mx"><div style="background:rgba(52,211,153,.15)">Suggest</div><div style="background:rgba(52,211,153,.15)">Draft</div><div style="background:rgba(251,191,36,.18)">Act + approve</div><div style="background:rgba(248,113,113,.18)">Autonomous</div></div></div></div>
<div class="ap"><h4>Send 12 replies to "refund delays"?</h4><div style="color:#666;font-size:14px;margin-top:4px">Preview before sending · 2 sources cited</div>
<div class="df"><span class="r">We are looking into it.</span><br><span class="a">Your refund was issued on Oct 2 and should</span><br><span class="a">arrive in 3–5 business days. [1]</span></div>
<div class="bt"><span style="background:#111;color:#fff">Send 12 replies</span><span style="border:1px solid #ddd">Review each</span><span style="color:#666">Undo available for 30s</span></div></div></div>"""
