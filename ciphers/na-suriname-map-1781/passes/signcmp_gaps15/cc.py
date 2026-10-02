import sys,json
import numpy as np
from PIL import Image, ImageDraw
from scipy import ndimage
L='images/2039_legend_native.jpg'; B='images/2061_battery_legend_native.jpg'
regs={'mg':(L,1540,715,1700,830),'mm61':(B,180,20,360,120),'mm61b':(B,180,230,330,300)}
out={}
sheets=[]
for name,(f,x0,y0,x1,y1) in regs.items():
    g=np.asarray(Image.open(f).convert('L').crop((x0,y0,x1,y1))).astype(float)
    thr=g.mean()-2.2*g.std() if g.std()>0 else 100
    thr=min(thr, np.percentile(g,50)-45)
    m=g<thr
    m=ndimage.binary_dilation(m,iterations=2)
    lab,n=ndimage.label(m)
    objs=ndimage.find_objects(lab)
    comps=[]
    for i,sl in enumerate(objs):
        ys,xs=sl
        if (ys.stop-ys.start)*(xs.stop-xs.start)<120: continue
        comps.append((xs.start+x0,ys.start+y0,xs.stop+x0,ys.stop+y0))
    # merge comps overlapping heavily in x (dots/diaeresis above)
    comps.sort()
    merged=[]
    for c in comps:
        if merged:
            p=merged[-1]; ov=min(p[2],c[2])-max(p[0],c[0])
            if ov>0.6*min(p[2]-p[0],c[2]-c[0]):
                merged[-1]=(min(p[0],c[0]),min(p[1],c[1]),max(p[2],c[2]),max(p[3],c[3])); continue
        merged.append(c)
    out[name]=[f,merged]
    im=Image.open(f).convert('RGB').crop((x0,y0,x1,y1)); s=2; im=im.resize((im.size[0]*s,im.size[1]*s)); d=ImageDraw.Draw(im)
    for i,(a,b,c,e) in enumerate(merged):
        d.rectangle([(a-x0)*s,(b-y0)*s,(c-x0)*s,(e-y0)*s],outline=(255,0,0)); d.text(((a-x0)*s+1,(b-y0)*s+1),str(i),fill=(0,0,255))
    d.text((2,2),name,fill=(0,128,0))
    sheets.append(im)
json.dump(out,open(sys.argv[1]+'/cc.json','w'))
W=max(i.size[0] for i in sheets); H=sum(i.size[1]+4 for i in sheets)
o=Image.new('RGB',(W,H),'white'); y=0
for i in sheets: o.paste(i,(0,y)); y+=i.size[1]+4
o.save(sys.argv[1]+'/cc.jpg',quality=85); print(o.size)
