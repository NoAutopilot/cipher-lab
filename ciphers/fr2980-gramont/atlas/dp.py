import sys,json; S=sys.argv[1]; exec(open(S+'/seg.py').read())
import numpy as np
from PIL import Image
def feat(fo,x0,t,x1,b):
    a=arr[fo][t:b+1,x0:x1]; a=255-a.astype(float)
    im=Image.fromarray(a.astype(np.uint8)); h,w=a.shape; s=max(h,w)
    c=Image.new('L',(s,s),0); c.paste(im,((s-w)//2,(s-h)//2)); v=np.array(c.resize((24,24))).astype(float).ravel()
    v-=v.mean(); n=np.linalg.norm(v); return v/n if n else v
tok={}
for l in open('ciphertext.txt'):
    if l.startswith('#') or not l.strip(): continue
    h,b=l.split('|'); fo,ln=h.split(); tok[f'{fo}_{ln}']=[t.rstrip('?') for t in b.split() if t!='.']
SEG={lid:seg(lid) for lid in tok}
init=json.load(open(S+'/f29_align.json'))['f29r_L03']
tmpl={}
for c,fo,h,x0,t,x1,b,ar in init: tmpl.setdefault(c,[]).append(feat(fo,x0,t,x1,b))
def dist(c,f):
    if c not in tmpl: return 0.55
    return min(1-float(v@f) for v in tmpl[c])
def box(G):
    return (G[0][0],min(g[3] for g in G) if 0 else G[0][2],min(g[3] for g in G),G[-1][4],max(g[5] for g in G))
for it in range(5):
    res={}
    for lid,T in tok.items():
        G=SEG[lid]; n,m=len(T),len(G); INF=1e9
        F={}
        def gf(j,k):
            if (j,k) not in F:
                g=G[j:j+k]; bx=(g[0][0],g[0][2],min(x[3] for x in g),g[-1][4],max(x[5] for x in g))
                F[(j,k)]=(bx,feat(*bx))
            return F[(j,k)]
        D=np.full((n+1,m+1),INF); D[0,0]=0; B={}
        for i in range(n+1):
            for j in range(m+1):
                d0=D[i,j]
                if d0>=INF: continue
                def up(ii,jj,c,bk):
                    if d0+c<D[ii,jj]: D[ii,jj]=d0+c; B[(ii,jj)]=bk
                if j<m: up(i,j+1,0.35 if G[j][6]<60 else 1.0,(i,j,'skip'))
                if i<n: up(i+1,j,1.2,(i,j,'miss'))
                if i<n and j<m:
                    for k in (1,2):
                        if j+k<=m and (k==1 or G[j][1]==G[j+k-1][1]): 
                            bx,f=gf(j,k); up(i+1,j+k,dist(T[i],f)+0.25*(k-1),(i,j,k))
                    if i+1<n: bx,f=gf(j,1); up(i+2,j+1,0.9,(i,j,'two'))
        i,j=n,m; out=[]
        while (i,j)!=(0,0):
            pi,pj,k=B[(i,j)]
            if isinstance(k,int):
                bx,f=gf(pj,k); out.append((T[pi],)+bx+(round(dist(T[pi],f),3),))
            i,j=pi,pj
        res[lid]=out[::-1]
    # update templates with confident matches
    tmpl2={}
    for lid,o in res.items():
        for c,fo,x0,t,x1,b,d in o:
            if d<0.45 or (c not in tmpl and c not in tmpl2): tmpl2.setdefault(c,[]).append(feat(fo,x0,t,x1,b))
    for c,v in tmpl2.items(): tmpl[c]=(tmpl.get(c,[])+v)[:8]
    print(it,sum(len(o) for o in res.values()),sum(len(v) for v in tok.values()),len(tmpl))
json.dump(res,open(S+'/f29_dp.json','w'),default=float)
