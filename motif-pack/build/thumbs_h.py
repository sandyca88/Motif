# part H: Clearview, Toybox Bots, Chroma Launch
from thumbs_a import BASE
T = {}
T["d_clearview"] = BASE + """<style>
body{background:#FBFBFD;color:#1D1D1F;text-align:center;font-family:-apple-system,BlinkMacSystemFont,'SF Pro Display',Inter,sans-serif;padding-top:90px;position:relative}
.eb{font-size:22px;font-weight:600;color:#0A66FF}h1{font-size:112px;font-weight:600;letter-spacing:-.045em;margin:10px 0 16px}p{font-size:26px;color:#6E6E73}
.b{display:inline-block;width:170px;height:230px;border-radius:85px 85px 55px 55px;background:linear-gradient(160deg,#fff,#e7e8ee);box-shadow:0 34px 60px -16px rgba(0,0,0,.25),inset -12px -16px 26px rgba(0,0,0,.06);margin:50px 22px 0;animation:bob 6s ease-in-out infinite}
.f{position:absolute;left:60px;right:60px;bottom:30px;display:flex;justify-content:space-between;color:#a1a1a6;font-size:15px}
</style><div class="eb">Introducing</div><h1>Lumen Buds.</h1><p>Sound that fits your day. Silence when you need it.</p>
<div><span class="b"></span><span class="b" style="margin-top:90px;animation-delay:-3s"></span></div><div class="f"><span>Clearview · 8-slide sample included</span><span>01 / 08</span></div>"""

def bot(c, head, eye, prop, i):
    heads = {"cap":"border-radius:60px","cube":"border-radius:22px","dome":"border-radius:70px 70px 22px 22px","gum":"border-radius:50% 50% 40% 40%"}
    eyes = {"visor":'<i style="position:absolute;left:18px;right:18px;top:38px;height:26px;border-radius:14px;background:#12162B;box-shadow:inset 0 0 0 3px rgba(255,255,255,.15)"><b style="position:absolute;left:14px;top:7px;width:12px;height:12px;border-radius:50%;background:#7CF7FF"></b><b style="position:absolute;right:14px;top:7px;width:12px;height:12px;border-radius:50%;background:#7CF7FF"></b></i>',
            "dots":'<i style="position:absolute;left:30px;top:40px;width:16px;height:20px;border-radius:50%;background:#12162B"></i><i style="position:absolute;right:30px;top:40px;width:16px;height:20px;border-radius:50%;background:#12162B"></i>',
            "lens":'<i style="position:absolute;left:50%;top:30px;width:40px;height:40px;margin-left:-20px;border-radius:50%;background:#12162B;box-shadow:inset 0 0 0 6px #fff"><b style="position:absolute;left:12px;top:10px;width:10px;height:10px;border-radius:50%;background:#fff"></b></i>'}
    props = {"ant":'<i style="position:absolute;left:50%;top:-30px;width:4px;height:26px;margin-left:-2px;background:#12162B"></i><i style="position:absolute;left:50%;top:-40px;width:16px;height:16px;margin-left:-8px;border-radius:50%;background:#FFC53D"></i>',
             "prop":'<i style="position:absolute;left:50%;top:-22px;width:70px;height:10px;margin-left:-35px;border-radius:6px;background:#12162B"></i><i style="position:absolute;left:50%;top:-14px;width:6px;height:12px;margin-left:-3px;background:#12162B"></i>',
             "phones":'<i style="position:absolute;left:-10px;top:30px;width:16px;height:40px;border-radius:8px;background:#12162B"></i><i style="position:absolute;right:-10px;top:30px;width:16px;height:40px;border-radius:8px;background:#12162B"></i>',
             "leaf":'<i style="position:absolute;left:54%;top:-26px;width:30px;height:20px;border-radius:0 20px 0 20px;background:#2ED3A0"></i>'}
    clay = "box-shadow:inset -10px -14px 24px rgba(0,0,0,.22),inset 8px 10px 18px rgba(255,255,255,.35)"
    return f'''<div class="t" style="background:{c}22"><span class="n">{i:02d}</span><div class="bot" style="animation-delay:{-i*0.4}s">
<div style="position:relative;width:120px;height:100px;background:{c};{heads[head]};{clay}">{eyes[eye]}{props[prop]}<i style="position:absolute;left:44px;bottom:16px;width:32px;height:8px;border-radius:0 0 10px 10px;background:#12162B"></i></div>
<div style="width:86px;height:56px;margin:6px auto 0;border-radius:24px;background:{c};{clay}"></div></div></div>'''
C = [("#FF4D8D","cap","visor","ant"),("#8B5CF6","cube","dots","prop"),("#2ED3A0","dome","lens","phones"),("#3BA7FF","gum","dots","leaf"),
     ("#FFC53D","cube","visor","phones"),("#FF7A2F","dome","dots","ant"),("#3BA7FF","cap","lens","prop"),("#FF4D8D","gum","visor","leaf")]
T["d_toybox"] = BASE + """<style>
body{background:#12162B;background-image:linear-gradient(rgba(255,255,255,.04) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.04) 1px,transparent 1px);background-size:64px 64px;color:#fff;padding:40px 56px;font-family:Nunito,'Baloo 2','Arial Rounded MT Bold',-apple-system,sans-serif}
h1{font-size:62px;font-weight:900;letter-spacing:-.02em}h1 span{color:#FFC53D}.m{color:#aab0d6;font-size:20px;margin:4px 0 22px;font-weight:600}
.g{display:grid;grid-template-columns:repeat(4,1fr);gap:16px}.t{border-radius:24px;height:272px;display:grid;place-items:center;position:relative;border:1px solid rgba(255,255,255,.08)}
.n{position:absolute;left:14px;top:10px;font:700 13px ui-monospace,Menlo,monospace;color:rgba(255,255,255,.5)}.bot{animation:bob 3s ease-in-out infinite}
</style><h1>Meet the <span>Toybox</span> crew</h1><div class="m">8 original bots · poses: wave, point, think, celebrate</div><div class="g">""" + "".join(bot(*c, i+1) for i, c in enumerate(C)) + "</div>"

T["d_chroma"] = BASE + """<style>
body{background:#0B0620;color:#fff;position:relative;overflow:hidden;font-family:'Inter Tight','Helvetica Neue',-apple-system,sans-serif}
.b{position:absolute;border-radius:50%;filter:blur(80px);animation:fl 10s ease-in-out infinite alternate}
.gr{position:absolute;inset:0;opacity:.07;background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='120' height='120'><filter id='n'><feTurbulence baseFrequency='.9'/></filter><rect width='100%' height='100%' filter='url(%23n)'/></svg>")}
.c{position:relative;padding:70px 80px}.st{display:inline-block;padding:8px 16px;border-radius:99px;background:rgba(255,255,255,.14);border:1px solid rgba(255,255,255,.3);font-weight:700;font-size:16px;letter-spacing:.08em}
h1{font-size:220px;font-weight:800;letter-spacing:-.06em;line-height:.85;margin-top:40px}
.p{position:absolute;right:120px;bottom:90px;width:300px;height:300px;border-radius:50%;background:radial-gradient(circle at 35% 30%,#fff,#e9e3ff 25%,#6C2BFF 70%,#2a0f6b);box-shadow:0 40px 80px rgba(0,0,0,.5),0 0 120px rgba(255,79,94,.5)}
.ch{position:absolute;padding:14px 20px;border-radius:16px;background:rgba(255,255,255,.14);border:1px solid rgba(255,255,255,.3);backdrop-filter:blur(16px);font-weight:700;font-size:20px}
</style><div class="b" style="width:700px;height:600px;left:-150px;top:-150px;background:#6C2BFF"></div><div class="b" style="width:600px;height:520px;right:-100px;top:100px;background:#FF4F5E;animation-delay:-3s"></div><div class="b" style="width:520px;height:420px;left:380px;bottom:-200px;background:#FF9F1C;animation-delay:-6s"></div><div class="b" style="width:360px;height:300px;right:300px;bottom:-60px;background:#00D1C1;opacity:.7"></div><div class="gr"></div>
<div class="c"><span class="st">NEW · v2.0</span><h1>Faster.<br>Louder.</h1></div><div class="p"></div>
<div class="ch" style="right:420px;bottom:330px">2× speed</div><div class="ch" style="right:80px;bottom:420px">AI built in</div><div class="ch" style="right:430px;bottom:120px">Ships Friday</div>"""
