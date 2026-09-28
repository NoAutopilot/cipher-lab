"""H63: one sign or two at r16:21? Horizontal gaps between digit-sized ink components on line r16 of
images/f22r_canvas58.jpg (native), with H15's settings: band y 3019-3244 (h2crops crop_r16 box height), threshold < 100,
connected components of area >= 40 px and height >= 12 px; component x-spans merged when overlapping; every gap between
consecutive spans listed. H10/H15 measured intra-group gaps 9-24 px and between-group gaps 45-66 px at native size."""
import numpy as np
from PIL import Image
from collections import deque
im=np.array(Image.open('images/f22r_canvas58.jpg').convert('L'))
y0,y1=3019,3244
band=im[y0:y1]<100
H,W=band.shape; lab=np.zeros_like(band,dtype=np.int32); comps=[]; n=0
for y in range(H):
    for x in range(W):
        if band[y,x] and not lab[y,x]:
            n+=1; q=deque([(y,x)]); lab[y,x]=n; xs=[];ys=[]
            while q:
                cy,cx=q.popleft(); xs.append(cx); ys.append(cy)
                for dy in (-1,0,1):
                    for dx in (-1,0,1):
                        ny,nx=cy+dy,cx+dx
                        if 0<=ny<H and 0<=nx<W and band[ny,nx] and not lab[ny,nx]: lab[ny,nx]=n; q.append((ny,nx))
            if len(xs)>=40 and max(ys)-min(ys)+1>=12: comps.append((min(xs),max(xs),min(ys)+y0,max(ys)+y0,len(xs)))
comps.sort(); spans=[]
for c in comps:
    if spans and c[0]<=spans[-1][1]: spans[-1]=[spans[-1][0],max(spans[-1][1],c[1]),spans[-1][2]+1]
    else: spans.append([c[0],c[1],1])
print(f'{len(comps)} components, {len(spans)} x-spans on r16 (native px)')
for i,s in enumerate(spans):
    g=spans[i+1][0]-s[1]-1 if i+1<len(spans) else None
    print(f'span {i:2d} x {s[0]:4d}-{s[1]:4d} (w {s[1]-s[0]+1:3d}, comps {s[2]})  gap to next {g}')
