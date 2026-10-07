# KHF-4, 7 Oct 2026: cut the held-out family-check tiles (f.143r test set, leaf-298 positive control, Mayenne f.61r
# negative control), normalise them (grey, autocontrast, 96 px), shuffle with a fixed seed and write blind ids.
# Usage: python3 make_tiles.py OUTDIR   (reads sources listed in SETS; writes OUTDIR/tNN.png and key_sealed.tsv rows' tile ids)
import sys, os, random, csv
from PIL import Image, ImageOps
H=os.path.dirname(os.path.abspath(__file__)); R=os.path.join(H,'..','..','..','..')
SETS={
 'f143r': (os.path.join(H,'..','img','c304_reg.jpg'), 1.0, 90),
 'leaf298': (os.path.join(R,'tools/keys/key60_atlas/src/f3986_c298_region.jpg'), 1.0, 90),
 'mayenne61': (os.path.join(H,'..','img','m61_reg.jpg'), 0.6, 90),
}
rows=list(csv.DictReader(open(os.path.join(H,'key_sealed.tsv')),delimiter='\t'))
out=sys.argv[1]; os.makedirs(out,exist_ok=True)
random.seed(20261007); order=list(range(len(rows))); random.shuffle(order)
for k,i in enumerate(order):
    r=rows[i]; src,sc,S=SETS[r['set']]; im=Image.open(src).convert('L')
    if sc!=1.0: im=im.resize((int(im.size[0]*sc),int(im.size[1]*sc)))
    x,y=int(r['x']),int(r['y']); t=im.crop((x-S//2,y-S//2,x+S//2,y+S//2))
    ImageOps.autocontrast(t,cutoff=1).resize((96,96)).save(os.path.join(out,f't{k+1:02d}.png'))
    r['tile']=f't{k+1:02d}'
with open(os.path.join(out,'tile_map.tsv'),'w') as f:
    f.write('tile\tset\tsrc_idx\n'); [f.write(f"{r['tile']}\t{r['set']}\t{r['idx']}\n") for r in rows]
print(len(rows),'tiles')
