"""Rebuild the Motif site and run every pre-release check.
usage: python3 check_site.py <path-to-Motif-folder> [--no-build]
Checks: build runs · JS syntax · DATA parses · no Pro prompt leak · Drive link not public ·
thumbnails/videos referenced exist · banned claims · counts · featured keys exist · zip has no preview files.
Exit code 1 if anything fails. Visual checks (screenshots in both themes) are still required.
"""
import json, os, re, subprocess, sys, zipfile
root = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 and not sys.argv[1].startswith('--') else '.')
PK = os.path.join(root, 'motif-pack'); SITE = os.path.join(root, 'motif-site'); ok = True
def bad(msg):
    global ok; ok = False; print('  ✗', msg)
def good(msg): print('  ✓', msg)
if '--no-build' not in sys.argv:
    r = subprocess.run(['python3', os.path.join(PK, 'build', 'package_site.py')], capture_output=True, text=True)
    (good if r.returncode == 0 else bad)('build: ' + (r.stdout.strip().splitlines() or [''])[-1] if r.returncode == 0 else 'build failed: ' + r.stderr[-400:])
html = open(os.path.join(SITE, 'index.html'), encoding='utf-8').read()
scripts = re.findall(r'<script>(.*?)</script>', html, re.S); app = max(scripts, key=len)
tmp = '/tmp/motif_app_check.js'; open(tmp, 'w').write(app)
r = subprocess.run(['node', '--check', tmp], capture_output=True, text=True)
(good if r.returncode == 0 else bad)('JavaScript syntax' if r.returncode == 0 else 'JS syntax error: ' + r.stderr[:300])
D = json.JSONDecoder().raw_decode(app[app.index('[{"k"'):])[0]; good(f'{len(D)} items parsed')
leak = [d['k'] for d in D if d['kind'] == 'prompt' and not d['free'] and len(d.get('prompt', '')) > 420]
(bad(f'Pro prompt leak: {leak}') if leak else good('no Pro prompt text leaked'))
(bad('Drive link found in public site!') if 'drive.google.com/file' in html else good('Drive link not in public site'))
miss = [d.get(f) for d in D for f in ('img', 'vid') if d.get(f) and not os.path.exists(os.path.join(SITE, d[f]))]
(bad(f'missing media: {miss}') if miss else good('all thumbnail images/videos exist'))
keys = {d['k'] for d in D}; dup = len(D) - len(keys); (bad(f'{dup} duplicate keys') if dup else good('item keys unique'))
names = [d['t'].lower() for d in D if not d.get('ext')]; dn = {n for n in names if names.count(n) > 1}
(bad(f'duplicate titles: {dn}') if dn else good('titles unique'))
for pat in ('tested in lovable', 'weekly drops', 'subscribers get', 'monthly free drop'):
    if pat.lower() in html.lower(): bad(f'banned/outdated claim present: "{pat}"')
for var in ('HERO3', 'TOPFREE', 'OSSFIRST'):
    m = re.search(var + r"=\[([^\]]*)\]", app)
    if m:
        ks = re.findall(r"'([^']+)'", m.group(1)); miss = [k for k in ks if k not in keys]
        (bad(f'{var} unknown keys {miss}') if miss else good(f'{var} = {ks}'))
own = lambda k: sum(1 for d in D if d['kind'] == k and not d.get('ext'))
print(f'  · counts: {own("prompt")} prompts, {own("skill")} skills, {own("deck")} decks, {sum(1 for d in D if d.get("ext"))} link-outs, {sum(1 for d in D if d["free"])} free')
z = os.path.join(root, 'motif-site.zip')
if os.path.exists(z):
    n = zipfile.ZipFile(z).namelist(); junk = [x for x in n if re.search(r'(zz-|preview|\.tmp$)', x)]
    (bad(f'preview/junk files in zip: {junk[:5]}') if junk else good(f'motif-site.zip clean ({len(n)} files)'))
    pro = [x for x in n if 'motif-pro-bundle' in x or '/assets/' in x]; (bad(f'Pro files in public zip: {pro[:3]}') if pro else good('no Pro files in public zip'))
print('\nRESULT:', 'PASS' if ok else 'FAIL', '(still screenshot home, prompts, item, pricing, guide in dark + light)')
sys.exit(0 if ok else 1)
