"""LIN-COUNT (9 Oct 2026): cut a 1897 px Vieyra leaf into masked column images for tools/iiif_lines.py.
The leaf has no printed column rules and its gutters are narrow; the left text margin of columns 2 and 3 is the peak of the
histogram of x positions where ink resumes after a >=14 px blank, taken separately in the top and bottom halves (skew);
the cut line runs 16 px left of the line through the two margins, and the column image is the leaf with everything left
of its own cut and right of the next column's cut whitened (so a
skewed page never crops a margin and neighbouring line-ends do not bleed in).
Usage: python3 hires_columns.py LEAF.jpg COL OUT.png  -> writes the masked column image (full leaf size), prints the
margin fits (stderr) and a box x0,y0,w,h for iiif_lines --region."""
import sys, numpy as np
from PIL import Image
src=Image.open(sys.argv[1]).convert('L'); im=np.asarray(src).astype(float); H,W=im.shape
bg=np.median(im); ink=im<bg-60
y0,y1=int(H*0.06),int(H*0.96)
prof=np.convolve(ink[y0:y1].sum(0),np.ones(15)/15,'same')
def margins(ya,yb):
    """column 2/3 text margins in rows ya..yb: peaks of the histogram of ink-run starts after a >=14 px blank."""
    h=np.zeros(W)
    for y in range(ya,yb,2):
        idx=np.where(ink[y])[0]
        if len(idx)<2: continue
        h[idx[1:][np.diff(idx)>=14]]+=1
    h=np.convolve(h,np.ones(5),'same')
    return [lo+int(np.argmax(h[lo:hi])) for lo,hi in ((int(W*.25),int(W*.5)),(int(W*.55),int(W*.8)))]
mt,mb=margins(150,1000),margins(1100,2000)
gs=[]
for k in range(2):  # cut line = margin line through (575, top) and (1550, bottom), 16 px left of it
    b=(mb[k]-mt[k])/(1550-575); a=mt[k]-b*575-16; gs.append((a,b,mt[k],mb[k]))
for a,b,t,u in gs: print('cut x=%.1f%+.4f*y (margins top %d bottom %d)'%(a,b,t,u),file=sys.stderr)
c=int(sys.argv[2]); yy=np.arange(H)[:,None]; xx=np.arange(W)[None,:]
left=np.full((H,1),-1.0) if c==1 else gs[c-2][0]+gs[c-2][1]*yy
right=np.full((H,1),W+1.0) if c==3 else gs[c-1][0]+gs[c-1][1]*yy
mask=(xx>left)&(xx<right)
out=np.where(mask,im,255).astype(np.uint8); Image.fromarray(out).save(sys.argv[3])
x0=int(max(0,left.min())); x1=int(min(W,right.max()))
print(f'{x0},50,{x1-x0},{H-100}')
