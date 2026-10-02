"""Rebuild per-skill zips + Pro and Free bundles. Run from anywhere: python3 build/bundle.py"""
import os, re, shutil, zipfile
PK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SK, DIST, TMP = os.path.join(PK, 'skills'), os.path.join(PK, 'dist'), '/tmp/motif-bundles'
FREE = ['microcopy-writer', 'deck-marker-margin', 'ux-heuristic-audit', 'deck-obsidian', 'deck-clearview',
        'deck-kraft-journal', 'video-prompt-director', 'case-study-writer']
LIC = os.path.join(PK, 'LICENSE.txt')

def zipdir(src, out, arc):
    with zipfile.ZipFile(out, 'w', zipfile.ZIP_DEFLATED) as z:
        for r, _, fs in os.walk(src):
            for f in sorted(fs):
                if f.startswith('.'): continue
                p = os.path.join(r, f); z.write(p, os.path.join(arc, os.path.relpath(p, src)))

skills = sorted(d for d in os.listdir(SK) if os.path.isfile(os.path.join(SK, d, 'SKILL.md')))
for s in skills:
    shutil.copy(LIC, os.path.join(SK, s, 'LICENSE.txt'))
    zipdir(os.path.join(SK, s), os.path.join(DIST, s + '.zip'), s)

shutil.rmtree(TMP, ignore_errors=True)
pro = os.path.join(TMP, 'motif-pro'); os.makedirs(pro)
shutil.copytree(SK, os.path.join(pro, 'skills'))
shutil.copytree(os.path.join(PK, 'assets'), os.path.join(pro, 'assets'))
shutil.copytree(os.path.join(PK, 'examples'), os.path.join(pro, 'examples'))
for f in ('prompts/motif-website-prompts.md', 'LICENSE.txt', 'THUMBNAIL-IMAGE-PROMPTS.md', 'START-HERE.md'):
    shutil.copy(os.path.join(PK, f), pro)
os.makedirs(os.path.join(pro, 'claude-app-zips'))
for s in skills: shutil.copy(os.path.join(DIST, s + '.zip'), os.path.join(pro, 'claude-app-zips'))
zipdir(pro, os.path.join(DIST, 'motif-pro-bundle.zip'), 'motif-pro')

free = os.path.join(TMP, 'motif-free'); os.makedirs(os.path.join(free, 'skills'))
for s in FREE: shutil.copytree(os.path.join(SK, s), os.path.join(free, 'skills', s))
md = open(os.path.join(PK, 'prompts/motif-website-prompts.md')).read()
blocks = re.findall(r"(## \d\d · .+?  `FREE`\n\n```\n.*?```)", md, re.S)
open(os.path.join(free, 'motif-free-prompts.md'), 'w').write('# Motif free website prompts\n\n' + '\n\n---\n\n'.join(blocks) + '\n')
shutil.copy(LIC, free)
shutil.copy(os.path.join(PK, 'START-HERE.md'), free)
os.makedirs(os.path.join(free, 'claude-app-zips'))
for s in FREE: shutil.copy(os.path.join(DIST, s + '.zip'), os.path.join(free, 'claude-app-zips'))
zipdir(free, os.path.join(DIST, 'motif-free-bundle.zip'), 'motif-free')
shutil.copy(os.path.join(PK, 'prompts/motif-website-prompts.md'), DIST)
print(f'{len(skills)} skills, {len(blocks)} free prompts, pro {os.path.getsize(os.path.join(DIST,"motif-pro-bundle.zip"))//1024//1024} MB')
