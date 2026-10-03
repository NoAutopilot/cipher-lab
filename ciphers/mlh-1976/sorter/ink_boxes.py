import numpy as np, sys
from PIL import Image
from scipy import ndimage
im=np.array(Image.open('ciphers/mlh-1976/images/MLH-Cryptogram.jpg').convert('L')).astype(float)
bg=ndimage.median_filter(im,size=31)
ink=(bg-im)>35
lab,n=ndimage.label(ink,structure=np.ones((3,3)))
objs=ndimage.find_objects(lab)
bands=[(3,106),(106,208),(208,295)]
want=[11,17,5]
out={}
for bi,(a,b) in enumerate(bands):
    comps=[]
    for i,s in enumerate(objs):
        y0,y1=s[0].start,s[0].stop; x0,x1=s[1].start,s[1].stop
        area=(lab[s]==i+1).sum()
        if a<=(y0+y1)/2<b and area>=6: comps.append([x0,y0,x1,y1,area])
    comps.sort()
    for g in range(0,60):
        grp=[]
        for c in comps:
            if grp and c[0]-grp[-1][2]<=g:
                G=grp[-1];G[0]=min(G[0],c[0]);G[1]=min(G[1],c[1]);G[2]=max(G[2],c[2]);G[3]=max(G[3],c[3]);G[4]+=c[4]
            else: grp.append(list(c))
        if len(grp)<=want[bi]: break
    print('L0%d g=%d n=%d (want %d)'%(bi+1,g,len(grp),want[bi]))
    for G in grp: print('   x%d-%d y%d-%d area%d'%(G[0],G[2],G[1],G[3],G[4]))
print('--- raw comps')
for (a,b,x0r,x1r) in [(106,208,100,300),(3,106,340,480)]:
    for i,s in enumerate(objs):
        y0,y1=s[0].start,s[0].stop; x0,x1=s[1].start,s[1].stop
        if a<=(y0+y1)/2<b and x0r<=x0<x1r:
            m=(lab[s]==i+1); print('  x%d-%d y%d-%d area%d fill%.2f'%(x0,x1,y0,y1,m.sum(),m.mean()))
    print()
