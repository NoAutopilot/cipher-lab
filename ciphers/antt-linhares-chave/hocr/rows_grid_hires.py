"""LIN-COUNT (9 Oct 2026): rows_grid.py at 1897 px. argv: 'c1 c2 ...' (iiif_lines --dry-run centres), region height.
Fits a straight-line grid (start pitch 42.6 px) to the detected centres, then snaps each grid centre to the nearest
detected centre within 12 px (detected peaks are kept where they agree, the grid fills the misses). Prints the centres."""
import sys, numpy as np
c=np.array(list(map(int,sys.argv[1].split())),float); H=int(sys.argv[2])
p=42.6; c0=c[0]
for it in range(6):
    k=np.round((c-c0)/p); A=np.vstack([np.ones_like(k),k]).T
    keep=np.abs(c-(A@np.linalg.lstsq(A,c,rcond=None)[0]))<12
    a,b=np.linalg.lstsq(A[keep],c[keep],rcond=None)[0]; c0=a; p=b
g=[a+b*j for j in range(int(np.ceil((10-a)/b)),int(np.floor((H-10-a)/b))+1)]
out=[]
for y in g:
    d=np.abs(c-y); out.append(int(c[d.argmin()]) if d.min()<=12 else int(round(y)))
print(','.join(map(str,out))); print('pitch %.2f phase %.1f n %d inliers %d/%d'%(b,a,len(out),keep.sum(),len(c)),file=sys.stderr)
