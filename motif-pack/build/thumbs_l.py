# part L: credited free picks (from the aura.build/skills directory). Coded previews, no third-party art.
from thumbs_a import BASE
T = {}

CSS = """<style>body{background:#0c0c0f;color:#f5f5f7;position:relative;overflow:hidden}
.g{position:absolute;inset:0;background:radial-gradient(900px 500px at 85% 20%,var(--a),transparent 60%),radial-gradient(700px 500px at 0% 100%,var(--b),transparent 60%)}
.top{position:absolute;left:64px;top:56px;display:flex;gap:12px;align-items:center;font:600 15px ui-monospace,Menlo,monospace;letter-spacing:.12em;color:#c9c9d1}
.top i{font-style:normal;padding:8px 14px;border-radius:99px;background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.14)}
.top i.f{background:#22c55e;color:#04140a;border:0;font-weight:800}
h1{position:absolute;left:64px;bottom:300px;font-size:92px;line-height:.96;letter-spacing:-.045em;font-weight:800;max-width:640px}
.by{position:absolute;left:64px;bottom:64px;font-size:22px;color:#a1a1aa}.by b{color:#fff}
.art{position:absolute;right:64px;top:150px;width:500px;height:500px}
.chips{position:absolute;left:64px;top:528px;display:flex;flex-wrap:wrap;gap:10px;max-width:640px}
.chips span{padding:9px 14px;border-radius:10px;background:rgba(255,255,255,.07);border:1px solid rgba(255,255,255,.1);font-size:16px;color:#d4d4d8}
@keyframes spin{to{transform:rotate(360deg)}}@keyframes bob{50%{transform:translateY(-16px)}}@keyframes pul{50%{opacity:.35}}
</style>"""

def card(a, b, title, by, chips, art, lic='MIT'):
    c = "".join(f"<span>{x}</span>" for x in chips)
    return BASE + CSS + f"""<div class="g" style="--a:{a};--b:{b}"></div><div class="top"><i class="f">FREE</i><i>{lic} · OPEN SOURCE</i></div>
<h1>{title}</h1><div class="chips">{c}</div><div class="by">by <b>{by}</b> · via GitHub</div><div class="art">{art}</div>"""

# art snippets (pure CSS, original)
GRID = '<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:16px;width:100%;height:100%">' + "".join(
    f'<div style="border-radius:22px;background:{c};box-shadow:inset 0 0 0 1px rgba(255,255,255,.12);animation:bob 4s ease-in-out {i*-.4}s infinite"></div>'
    for i, c in enumerate(["#8b5cf6", "#1f1f27", "#22d3ee", "#1f1f27", "#f472b6", "#1f1f27", "#facc15", "#1f1f27", "#34d399"])) + "</div>"
GLOBE = ('<div style="position:absolute;inset:40px;border-radius:50%;background:radial-gradient(circle at 35% 30%,#3b3b4a,#0c0c12 70%);box-shadow:0 0 120px rgba(99,102,241,.45)"></div>'
         + "".join(f'<div style="position:absolute;inset:{40+i*0}px;border-radius:50%;border:1px solid rgba(165,180,252,.35);transform:rotateY({i*30}deg) scaleX({abs(1-i*0.3):.2f});animation:spin {14+i*3}s linear infinite"></div>' for i in range(4))
         + "".join(f'<i style="position:absolute;left:{x}px;top:{y}px;width:8px;height:8px;border-radius:50%;background:#a5b4fc;animation:pul 2s {d}s infinite"></i>' for x, y, d in [(150, 160, 0), (300, 210, .5), (220, 320, 1), (340, 360, 1.5), (130, 280, .7)]))
CUBE = ('<div style="position:absolute;left:110px;top:110px;width:280px;height:280px;border-radius:30px;background:linear-gradient(135deg,#22d3ee,#6366f1 55%,#0f172a);transform:rotate(18deg) skew(-6deg);box-shadow:0 60px 120px rgba(34,211,238,.35);animation:bob 5s ease-in-out infinite"></div>'
        '<div style="position:absolute;left:40px;top:60px;width:420px;height:420px;border-radius:50%;border:1.5px dashed rgba(255,255,255,.18);animation:spin 30s linear infinite"></div>')
WAVE = "".join(f'<div style="position:absolute;left:{20+i*48}px;bottom:80px;width:26px;height:{80+((i*53)%260)}px;border-radius:13px;background:linear-gradient(#fb7185,#f59e0b);animation:bob {2+i%3}s ease-in-out {i*-.2}s infinite"></div>' for i in range(10))
RULES = '<div style="display:flex;flex-direction:column;gap:14px;padding-top:30px">' + "".join(
    f'<div style="display:flex;gap:14px;align-items:center;padding:18px 20px;border-radius:16px;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.1);font-size:20px"><b style="width:26px;height:26px;border-radius:8px;background:{c};display:grid;place-items:center;font-size:15px;color:#000">✓</b>{t}</div>'
    for c, t in [("#34d399", "Focus rings visible"), ("#34d399", "Hit targets ≥ 24px"), ("#facc15", "Honor reduced motion"), ("#34d399", "Optimistic UI"), ("#34d399", "Tabular numbers")]) + "</div>"
FUNNEL = "".join(f'<div style="margin:0 auto 16px;width:{460-i*90}px;height:74px;border-radius:18px;background:linear-gradient(90deg,#f97316,#ec4899);opacity:{1-i*.15:.2f};display:grid;place-items:center;font:700 20px -apple-system,sans-serif">{t}</div>'
                 for i, t in enumerate(["Visitors 12.4k", "Signups 2.1k", "Trials 640", "Paid 212", "Loyal 96"]))
TOKENS = '<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:14px">' + "".join(
    f'<div style="aspect-ratio:1;border-radius:18px;background:{c}"></div>' for c in ["#0ea5e9", "#38bdf8", "#7dd3fc", "#e0f2fe", "#111827", "#374151", "#9ca3af", "#f3f4f6"]) + "</div>" + \
    '<div style="margin-top:22px;font:800 64px -apple-system,sans-serif;letter-spacing:-.04em">Aa <span style="font-weight:300;opacity:.6">Aa</span></div><div style="display:flex;gap:10px;margin-top:16px">' + \
    "".join(f'<span style="padding:8px 12px;border-radius:8px;background:rgba(255,255,255,.08);font:600 15px ui-monospace,Menlo,monospace">{s}</span>' for s in ["sm:", "md:", "lg:", "xl:"]) + "</div>"
EYEDROP = ('<div style="position:absolute;inset:30px;border-radius:28px;background:#16161c;border:1px solid rgba(255,255,255,.12);overflow:hidden">'
           '<div style="height:44px;background:#1f1f27;display:flex;gap:8px;align-items:center;padding:0 16px"><i style="width:12px;height:12px;border-radius:50%;background:#f87171"></i><i style="width:12px;height:12px;border-radius:50%;background:#facc15"></i><i style="width:12px;height:12px;border-radius:50%;background:#4ade80"></i></div>'
           '<div style="margin:26px;height:120px;border-radius:14px;background:linear-gradient(90deg,#334155,#1e293b)"></div><div style="margin:0 26px;display:flex;gap:14px"><div style="flex:1;height:150px;border-radius:14px;background:#1e293b"></div><div style="flex:1;height:150px;border-radius:14px;background:#1e293b;outline:3px dashed #f472b6;outline-offset:4px"></div></div></div>'
           '<div style="position:absolute;right:20px;bottom:40px;padding:14px 18px;border-radius:14px;background:#f472b6;color:#200;font:700 18px -apple-system,sans-serif;box-shadow:0 20px 40px rgba(244,114,182,.4)">2 issues · fix contrast</div>')
SLIDERS = "".join(f'<div style="margin:0 0 34px"><div style="display:flex;justify-content:space-between;font:600 18px ui-monospace,Menlo,monospace;color:#a1a1aa;margin-bottom:12px"><span>{t}</span><span>{v}</span></div><div style="height:12px;border-radius:6px;background:rgba(255,255,255,.1)"><div style="width:{v*10}%;height:100%;border-radius:6px;background:linear-gradient(90deg,#a78bfa,#f472b6)"></div></div></div>'
                  for t, v in [("DESIGN_VARIANCE", 8), ("MOTION_INTENSITY", 6), ("VISUAL_DENSITY", 4)])
SPARK = ('<div style="position:absolute;left:150px;top:150px;width:200px;height:200px;background:conic-gradient(from 0deg,#fb923c,#f472b6,#a78bfa,#fb923c);clip-path:polygon(50% 0,61% 39%,100% 50%,61% 61%,50% 100%,39% 61%,0 50%,39% 39%);animation:spin 18s linear infinite"></div>'
         '<div style="position:absolute;inset:60px;border-radius:50%;border:1px solid rgba(255,255,255,.12)"></div>')

T["af_mengto"] = card("rgba(99,102,241,.45)", "rgba(236,72,153,.25)", "Aura Web Design Skills", "Meng To",
                      ["Landing page", "GSAP", "Vanta.js", "Progressive blur", "Pricing page", "Border gradients", "cobe globe", "Matter.js"], GLOBE)
T["af_ccui"] = card("rgba(139,92,246,.45)", "rgba(34,211,238,.2)", "UI Design System", "Daniel Ávila",
                    ["Components", "Tokens", "Spacing", "Accessibility"], GRID)
T["af_wsh"] = card("rgba(14,165,233,.45)", "rgba(99,102,241,.25)", "Tailwind v4 &amp; Responsive Design", "Seth Hobson",
                   ["Tailwind v4 tokens", "Interaction design", "Responsive layout"], TOKENS)
T["af_three"] = card("rgba(34,211,238,.4)", "rgba(99,102,241,.3)", "Three.js Skills", "CloudAI-X",
                     ["Scenes", "Materials", "Lighting", "Shaders", "Post-processing", "Animation"], CUBE)
T["af_anime"] = card("rgba(251,113,133,.4)", "rgba(245,158,11,.25)", "Anime.js v4 Skill", "BowTiedSwan",
                     ["Timelines", "Stagger", "SVG morph", "Scroll", "Draggable", "Springs"], WAVE)
T["af_vercel"] = card("rgba(255,255,255,.18)", "rgba(52,211,153,.18)", "Web Interface Guidelines", "Vercel Labs",
                      ["Interactions", "Forms", "Animation", "Layout", "Performance"], RULES)
T["af_corey"] = card("rgba(249,115,22,.4)", "rgba(236,72,153,.25)", "Marketing Skills", "Corey Haines",
                     ["Copywriting", "Marketing psychology", "Analytics tracking", "CRO"], FUNNEL)
T["af_kostja"] = card("rgba(250,204,21,.32)", "rgba(249,115,22,.22)", "Marketing Skills Pack", "kostja94",
                      ["SEO", "Content", "Landing pages", "Growth"], FUNNEL.replace("#f97316", "#facc15").replace("#ec4899", "#f97316"))
T["af_webrev"] = card("rgba(244,114,182,.38)", "rgba(99,102,241,.22)", "Web Design Reviewer", "GitHub · awesome-copilot",
                      ["Visual QA", "Layout issues", "Contrast", "Fix suggestions"], EYEDROP)
T["af_taste"] = card("rgba(167,139,250,.42)", "rgba(244,114,182,.22)", "Taste Skill", "Leonxlnx",
                     ["High-agency frontend", "Image art direction", "Variance dials"], SLIDERS)
T["af_frontend"] = card("rgba(251,146,60,.38)", "rgba(167,139,250,.22)", "Frontend Design", "Anthropic",
                        ["Bold aesthetic direction", "Typography", "Motion", "Non-generic UI"], SPARK, "APACHE-2.0")
