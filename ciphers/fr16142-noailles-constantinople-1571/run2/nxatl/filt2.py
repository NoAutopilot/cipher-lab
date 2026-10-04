"""Keep, per strip, the segmented line nearest the strip centre; drop overlap duplicates between _s1/_s2;
drop tiles with |dy|>0.9 median heights (neighbour-line/gloss intrusions) and specks (rh<0.5 and rw<0.5).
Rule fixed on c262 (in-sample; see REPORT.md)."""
import csv, json, sys, collections
from PIL import Image
out, pagemap, ov = sys.argv[1], json.load(open(sys.argv[2])), int(sys.argv[3])
rows=list(csv.DictReader(open(f'{out}/signs.tsv'),delimiter='\t'))
bypage=collections.defaultdict(list)
for r in rows: bypage[r['page']].append(r)
keep=[]
for pg,rs in bypage.items():
    W,H=Image.open(pagemap[pg]).size
    lines=collections.defaultdict(list)
    for r in rs: lines[r['line']].append(r)
    def cy(l): ys=sorted(int(r['y'])+int(r['h'])/2 for r in lines[l]); return ys[len(ys)//2]
    best=min(lines, key=lambda l: abs(cy(l)-H/2) - 0.001*len(lines[l]))
    leaf,L,seg=pg.rsplit('_',2); nxt=f'{leaf}_{L}_s{int(seg[1:])+1}'
    for r in lines[best]:
        cx=int(r['x'])+int(r['w'])/2
        if seg!='s1' and cx < ov/2: continue
        if cx > W-ov/2 and nxt in bypage: continue
        if abs(float(r['dy']))>0.9: continue
        if float(r['rh'])<0.5 and float(r['rw'])<0.5: continue
        keep.append(r)
json.dump([r['sid'] for r in keep],open(f'{out}/keep.json','w'))
