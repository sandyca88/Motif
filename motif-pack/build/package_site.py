"""Rebuild storefront + public motif-site folder (free files only) + motif-site.zip. Does NOT publish."""
import json,re,shutil,os,subprocess,glob
B=os.path.dirname(os.path.abspath(__file__));PK=os.path.dirname(B);OUT=os.path.dirname(PK);SITE=os.path.join(OUT,'motif-site')
subprocess.run(['python3',os.path.join(B,'build.py')],check=True)
shutil.rmtree(SITE,ignore_errors=True)  # may be blocked on synced folders; everything below overwrites in place
for d in ('motif-pack/dist','samples','thumbs'): os.makedirs(os.path.join(SITE,d),exist_ok=True)
shutil.copy(os.path.join(OUT,'motif-storefront.html'),os.path.join(SITE,'index.html'))
for n,d in [('obsidian','deck-obsidian'),('clearview','deck-clearview')]:
    shutil.copy(os.path.join(PK,'skills',d,'examples/sample-deck.html'),os.path.join(SITE,'samples',f'{n}-sample-deck.html'))
shutil.copy(os.path.join(PK,'dist/motif-free-bundle.zip'),os.path.join(SITE,'motif-pack/dist/'))
shutil.copytree(os.path.join(PK,'examples/softwork'),os.path.join(SITE,'samples/softwork'),dirs_exist_ok=True)
shutil.copytree(os.path.join(PK,'examples/lattice'),os.path.join(SITE,'samples/lattice'),dirs_exist_ok=True)
shutil.copy(os.path.join(PK,'skills/animated-mascot-logo/examples/mascot-concepts.html'),os.path.join(SITE,'samples/mascot-concepts.html'))
for f in ('motif-mark-32.png','motif-mark-180.png','motif-mark-192.png','motif-mark-512.png','motif-og.png'): shutil.copy(os.path.join(PK,'brand',f),os.path.join(SITE,f))
for f in glob.glob(os.path.join(B,'thumb-images','*.*')):
    if f.endswith(('.webp','.jpg','.png','.mp4')): shutil.copy(f,os.path.join(SITE,'thumbs'))
s=open(os.path.join(SITE,'index.html')).read()
data=json.loads(re.search(r'const DATA=(\[.*?\]);\nconst PICKS',s,re.S).group(1).replace('<\\/','</'))
for d in data:
    if d.get('zip') and d['free']: shutil.copy(os.path.join(OUT,d['zip']),os.path.join(SITE,d['zip']))
leak=[d['t'] for d in data if d['kind']=='prompt' and not d['free'] and len(d.get('prompt',''))>420]
assert not leak,leak
open(os.path.join(SITE,'_headers'),'w').write('/*\n  X-Content-Type-Options: nosniff\n  Referrer-Policy: strict-origin-when-cross-origin\n')
z=os.path.join(OUT,'motif-site.zip');tz='/tmp/motif-site-build.zip'
if os.path.exists(tz): os.remove(tz)
subprocess.run(f'cd "{SITE}" && zip -qr "{tz}" . -x "*.tmp" -x "*preview*.html" -x "zz-*"',shell=True,check=True)
shutil.copyfile(tz,z)
print('site ok:',len(data),'items,',sum(d['free'] for d in data),'free,',len(glob.glob(os.path.join(SITE,'thumbs','*'))),'custom thumbs')
