#!/usr/bin/env python3
"""Per-line montages of 4x per-box crops for the blind passes (campaign H15).

For each p.[1] line: every box of glyphs/signs.tsv (minus the excluded plain-text boxes below), cut with
tools/glyph_atlas.py crop --out glyphs --sid ... at 4x, laid out in reading order six to a row with the box's
strip number under it, to glyphs/montage/p1_L0N.png. A pass reads a sign at 4x instead of on a 1400-px strip.
Excluded (settled by the runner's eye on the v2 strips, 28 Sept 2026 00:0x UTC): line 1 boxes 1-11 (the plain
"al R.do frate mio" and the line above's descenders); line 8 boxes 18, 22, 24, 25, 27, 28, 30, 32, 33, 34, 35 (the plain
"La morte" line below, on a lower baseline). Needs Pillow.
  python3 glyphs/montage.py            -> glyphs/crops4x/*.png, glyphs/montage/p1_L01.png ... p1_L08.png
"""
import csv, os, subprocess, sys
from PIL import Image, ImageDraw, ImageFont
HERE=os.path.dirname(os.path.abspath(__file__)); REPO=os.path.abspath(os.path.join(HERE,'..','..','..'))
EXCL={'1':set(range(1,12)),'8':{18,22,24,25,27,28,30,32,33,34,35}}
rows=[r for r in csv.DictReader(open(os.path.join(HERE,'signs.tsv')),delimiter='\t') if r['page']=='p1']
dest=os.path.join(HERE,'crops4x'); os.makedirs(dest,exist_ok=True); os.makedirs(os.path.join(HERE,'montage'),exist_ok=True)
keep=[r for r in rows if int(r['pos']) not in EXCL.get(r['line'],set())]
sids=[r['sid'] for r in keep if not os.path.exists(os.path.join(dest,r['sid']+'.png'))]
for i in range(0,len(sids),40):
    cmd=[sys.executable,os.path.join(REPO,'tools','glyph_atlas.py'),'crop','--out',HERE,'--dest',dest,'--scale','4','--margin','10']
    for s in sids[i:i+40]: cmd+=['--sid',s]
    subprocess.run(cmd,check=True,capture_output=True)
try: font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',36)
except Exception: font=ImageFont.load_default()
CW,CH,PER=320,400,6
for ln in sorted(set(r['line'] for r in keep),key=int):
    L=sorted([r for r in keep if r['line']==ln],key=lambda r:int(r['pos']))
    nrow=(len(L)+PER-1)//PER; im=Image.new('RGB',(CW*PER,CH*nrow),'white'); d=ImageDraw.Draw(im)
    for i,r in enumerate(L):
        p=os.path.join(dest,r['sid']+'.png')
        if not os.path.exists(p): continue
        g=Image.open(p).convert('RGB'); g.thumbnail((CW-20,CH-70))
        x=(i%PER)*CW; y=(i//PER)*CH
        im.paste(g,(x+(CW-g.width)//2,y+10)); d.rectangle([x+2,y+2,x+CW-3,y+CH-3],outline=(180,180,180))
        d.text((x+CW//2-20,y+CH-55),r['pos'],fill=(200,0,0),font=font)
    out=os.path.join(HERE,'montage',f'p1_L{int(ln):02d}.png'); im.save(out); print(out,len(L),'boxes',im.size)
