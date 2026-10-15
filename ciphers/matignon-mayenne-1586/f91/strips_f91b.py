# MAT-F91B 15 Oct 2026: line strips for blocks C, F of f.91v/92r from c98_max.jpg (fetch: see regen_f91.sh). Usage: python3 -I strips_f91b.py SCRATCHDIR (expects SCRATCHDIR/img/c98_max.jpg, writes SCRATCHDIR/strips/). Strips are cy+-75 px, which proved too tall (neighbour lines; pass agreement 45%): use cy+-50 and half-line segments next time.
import sys, numpy as np
from PIL import Image

def find_peaks(p,distance):
    idx=sorted(range(len(p)),key=lambda i:-p[i]); keep=[]
    for i in idx:
        if p[i]<=0: break
        if all(abs(i-k)>=distance for k in keep): keep.append(i)
    return keep,None
S=sys.argv[1]; im=Image.open(S+'/img/c98_max.jpg').convert('L')
regs={'C':(1480,1050,3100,1380,13),'F1':(5250,2685,2860,840,9),'F2':(5250,3800,2860,240,2)}
out=[]
for b,(x,y,w,h,n) in regs.items():
    a=255-np.asarray(im.crop((x,y,x+w,y+h)),dtype=float)
    prof=np.convolve((a>90).sum(1),np.ones(31)/31,'same')
    pk,_=find_peaks(prof,distance=80)
    pk=sorted(sorted(pk,key=lambda p:-prof[p])[:n])
    for i,p in enumerate(pk,1):
        cy=y+p; c=im.crop((x-20,cy-75,x+w,cy+75)); c=c.resize((2400,int(150*2400/(w+20))))
        nm=f'{b}{i}'; c.save(f'{S}/strips/{nm}.jpg',quality=88); out.append((nm,cy))
print(out)
