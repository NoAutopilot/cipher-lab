import sys,json,csv
import numpy as np
from PIL import Image, ImageDraw
page,man,keyf,letter,out=sys.argv[1:6]; GAP=int(sys.argv[6]) if len(sys.argv)>6 else 9
def walk(o):
    if isinstance(o,dict):
        if 'crop' in o and 'box' in o: yield o
        for v in o.values(): yield from walk(v)
    elif isinstance(o,list):
        for v in o: yield from walk(v)
E={e['crop']:e['box'] for e in walk(json.load(open(man)))}
pim=Image.open(page).convert('L'); im=np.array(pim)
key=list(csv.DictReader(open(keyf),delimiter='\t'))
lines=sorted({k['line'] for k in key})
seg={}; strips=[]
for ln in lines:
    x0,y0,x1,y1=[2*v for v in E[f'{letter}_{ln}.jpg']]
    yy0=max(0,y0-14); yy1=y1+14
    band=im[y0+6:y1-2]<150
    col=band.sum(0); on=col>=2
    m=[];a=None
    for x,v in enumerate(on):
        if v and a is None: a=x
        if not v and a is not None: m.append([a,x]); a=None
    mm=[]
    for a,b in m:
        if mm and a-mm[-1][1]<GAP: mm[-1][1]=b
        else: mm.append([a,b])
    mm=[(a,b) for a,b in mm if b-a>=14 and col[a:b].sum()>150]
    seg[ln]=[[int(a),int(b)] for a,b in mm]
    s=pim.crop((0,yy0,2481,yy1)).convert('RGB'); s2=Image.new('RGB',(2481,s.height+18),'white'); s2.paste(s,(0,18)); d=ImageDraw.Draw(s2)
    for i,(a,b) in enumerate(mm):
        d.line([(a,16),(b,16)],fill=(0,90,200),width=3); d.text(((a+b)//2-6,2),str(i+1),fill=(200,40,0))
    strips.append((ln,s2))
json.dump(seg,open(out+'_seg.json','w'))
k=0
for i in range(0,len(strips),4):
    ims=[]
    for ln,s in strips[i:i+4]:
        nz=[b for b in seg[ln]]; lo=max(0,nz[0][0]-20) if nz else 0; hi=min(2481,nz[-1][1]+20) if nz else 2481
        s=s.crop((lo,0,hi,s.height)); mid=(s.width+1)//2
        for half in (s.crop((0,0,mid+30,s.height)),s.crop((mid-30,0,s.width,s.height))):
            t=Image.new('RGB',(1300,half.height+14),'white'); t.paste(half,(0,14)); ImageDraw.Draw(t).text((2,1),ln,fill=(0,120,0)); ims.append(t)
    o=Image.new('RGB',(1300,sum(x.height for x in ims)),'white'); y=0
    for x in ims: o.paste(x,(0,y)); y+=x.height
    o.save(f'{out}_{k}.jpg',quality=82); k+=1
print(k)
