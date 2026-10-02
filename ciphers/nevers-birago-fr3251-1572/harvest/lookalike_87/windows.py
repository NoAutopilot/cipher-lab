# BIRAGO-SMALL (2 Oct 2026): context windows around each no.87 tile labelled T50/T98/T52/T46 (position estimated from pos/line length,
# +-3 signs; segments overlap, so a window can repeat a sign). Usage from harvest/: python3 lookalike_87/windows.py lookalike_87 T50 out.png
import csv,sys,glob
from PIL import Image, ImageDraw
S=sys.argv[1]; want=sys.argv[2].split(','); out=sys.argv[3]; extra=sys.argv[4:] # extra: fol:line:pos
tiles=list(csv.DictReader(open(S+'/tiles.tsv'),delimiter='\t'))
sel=[t for t in tiles if t['sign'] in want]
cnt={}
for fol in ['f178r','f178v','f179r']:
    for r in csv.DictReader(open(f'ciphertext_{fol}.tsv'),delimiter='\t'):
        cnt[r['line']]=max(cnt.get(r['line'],0),int(r['pos']))
panels=[]
for t in sel:
    fol=t['folio']; L=t['line'].split('_')[1]
    segs=[Image.open(f) for f in sorted(glob.glob(f'{fol}/{fol}_{L}_s*.jpg'))]
    W=sum(s.size[0] for s in segs); H=max(s.size[1] for s in segs)
    line=Image.new('RGB',(W,H),'white'); x=0
    for s in segs: line.paste(s,(x,0)); x+=s.size[0]
    n=cnt[t['line']]; p=int(t['pos']); cx=int((p-0.5)/n*W); half=int(W/n*3)
    win=line.crop((max(0,cx-half),0,min(W,cx+half),H))
    lab=Image.new('RGB',(win.size[0],win.size[1]+18),'white'); lab.paste(win,(0,18))
    ImageDraw.Draw(lab).text((2,2),f"{len(panels)+1}: {t['line']}.{p} ctx {t['ctx']}",fill='red')
    panels.append((lab,t))
cols=2; w=max(p[0].size[0] for p in panels); h=max(p[0].size[1] for p in panels)
m=Image.new('RGB',(cols*w+10,((len(panels)+1)//2)*(h+6)),'white')
for i,(p,t) in enumerate(panels): m.paste(p,((i%cols)*(w+10),(i//cols)*(h+6)))
m.save(out); print(m.size)
for i,(p,t) in enumerate(panels): print(i+1,t['line'],t['pos'],t['sign'],t['conf'],t['chunk'],t['status'],sep='\t')
