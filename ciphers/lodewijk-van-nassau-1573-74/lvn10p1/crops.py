"""LVN-3R per-token crops for WVO 4610 p1 at 300 dpi (same shape as lvn16/crops3r.py).
usage: python3 crops.py PAGE_PNG MANIFEST_JSON TOK_TSV OUTDIR
Line box = images/manifest.json 150-dpi box x2, padded 14 px up/down; tight crop 3x, context crop 2x with a blue wedge.
Images go to OUTDIR (scratch), never into git."""
import sys,json
from PIL import Image, ImageDraw
page,man,tok,out=sys.argv[1:5]
def walk(o):
    if isinstance(o,dict):
        if 'crop' in o and 'box' in o: yield o
        for v in o.values(): yield from walk(v)
    elif isinstance(o,list):
        for v in o: yield from walk(v)
E={e['crop']:e['box'] for e in walk(json.load(open(man)))}
im=Image.open(page).convert('L')
sheet=[]
for l in open(tok):
    if not l.strip(): continue
    ln,pos,cx,hw=l.split('\t'); cx=int(cx); hw=int(hw)
    x0,y0,x1,y1=[2*v for v in E['04610_%s.jpg'%ln]]
    dy=15 if ln=="p1_L19" else 0
    y0=max(0,y0-14+dy); y1=y1+14+dy
    t=im.crop((cx-hw,y0,cx+hw,y1)); t=t.resize((t.width*3,t.height*3),Image.LANCZOS)
    a=max(0,cx-hw-130); c=im.crop((a,y0,cx+hw+130,y1)).convert('RGB'); c=c.resize((c.width*2,c.height*2),Image.LANCZOS)
    cc=Image.new('RGB',(c.width,c.height+24),'white'); cc.paste(c,(0,24)); d=ImageDraw.Draw(cc)
    L=(cx-hw-a)*2; R=L+4*hw; d.polygon([(L,2),(R,2),((L+R)//2,20)],fill=(0,90,200))
    t.save(f'{out}/tok_{ln}_{pos}_tight.jpg',quality=92); cc.save(f'{out}/tok_{ln}_{pos}_ctx.jpg',quality=92)
    sheet.append((ln,pos,cc))
W=760; ims=[c.resize((W,c.height*W//c.width)) if c.width>W else c for *_,c in sheet]
o=Image.new('RGB',(W*2,sum(i.height+14 for i in ims[::2])+20),'white'); d=ImageDraw.Draw(o)
y=[0,0]
for k,((ln,pos,_),i) in enumerate(zip(sheet,ims)):
    col=k%2; d.text((col*W+2,y[col]),f'{ln}/{pos}',fill=(0,120,0)); o.paste(i,(col*W,y[col]+12)); y[col]+=i.height+14
o.save(out+'/sheet.jpg',quality=85); print(o.size)
