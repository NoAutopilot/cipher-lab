#!/usr/bin/env python3
"""F19 glyph test (PREREG-F19.md): f vs long-s by NCC against the hand's own exemplars.
Usage: python3 f19_glyph.py [--sheet OUT.png]   (reads ../../images/clear/*.jpg and exemplars.tsv beside this file)
For each box: greyscale, autocontrast, binarise (Otsu), take the connected ink component of greatest height whose
x-centre lies in the box, crop it to its bounding box, resize to 16x48, zero-mean unit-norm. Class mean = mean vector.
Control: leave-one-out nearest-class-mean accuracy vs a 1000-draw label-shuffled null. Writes result.tsv."""
import sys, os, random
import numpy as np
from PIL import Image, ImageOps

def label(ink):
    lab=np.zeros(ink.shape,int); n=0; objs=[]
    for y,x in zip(*np.nonzero(ink)):
        if lab[y,x]: continue
        n+=1; st=[(y,x)]; lab[y,x]=n; ys=[];xs=[]
        while st:
            a,b=st.pop(); ys.append(a); xs.append(b)
            for da in (-1,0,1):
                for db in (-1,0,1):
                    c,d=a+da,b+db
                    if 0<=c<ink.shape[0] and 0<=d<ink.shape[1] and ink[c,d] and not lab[c,d]:
                        lab[c,d]=n; st.append((c,d))
        objs.append((slice(min(ys),max(ys)+1),slice(min(xs),max(xs)+1)))
    return lab,n,objs
H=os.path.dirname(os.path.abspath(__file__)); IMG=os.path.join(H,'..','..','images','clear')
rows=[l.rstrip('\n').split('\t') for l in open(os.path.join(H,'exemplars.tsv'))][1:]
def glyph(crop,y0,y1,x0,x1):
    im=np.asarray(ImageOps.autocontrast(Image.open(os.path.join(IMG,crop+'.jpg')).convert('L')),float)
    band=im[y0:y1,max(0,x0-40):x1+40]; off=max(0,x0-40)
    hist=np.histogram(band,256,(0,256))[0]; tot=band.size; best=(0,0); sb=0; wb=0; mt=(hist*np.arange(256)).sum()
    for t in range(256):
        wb+=hist[t]
        if wb==0 or wb==tot: continue
        sb+=t*hist[t]; m0=sb/wb; m1=(mt-sb)/(tot-wb); v=wb*(tot-wb)*(m0-m1)**2
        if v>best[0]: best=(v,t)
    ink=band<best[1]; lab,n,objs=label(ink); cand=[]
    for i,sl in enumerate(objs):
        xc=(sl[1].start+sl[1].stop)/2+off
        if x0<=xc<=x1: cand.append((sl[0].stop-sl[0].start,i,sl))
    if not cand: return None,None
    h,i,sl=max(cand); g=(lab[sl]==i+1).astype(float)
    v=np.asarray(Image.fromarray((g*255).astype(np.uint8)).resize((16,48),Image.BILINEAR),float).ravel()
    v-=v.mean(); v/=np.linalg.norm(v)+1e-9; return v,(h,sl[1].stop-sl[1].start)
V={}; info={}
for r in rows:
    v,s=glyph(r[2],*map(int,r[3:7])); V[r[0]]=v; info[r[0]]=s
ex=[r for r in rows if r[1] in 'fs' and V[r[0]] is not None]
def loo(labels):
    right=0; margins=[]
    for k,r in enumerate(ex):
        means={c:np.mean([V[q[0]] for j,q in enumerate(ex) if j!=k and labels[j]==c],0) for c in 'fs'}
        nf=V[r[0]]@means['f']/np.linalg.norm(means['f']); ns=V[r[0]]@means['s']/np.linalg.norm(means['s'])
        right+=(('f' if nf>ns else 's')==labels[k])
    return right/len(ex)
lab=[r[1] for r in ex]; acc=loo(lab); random.seed(1162); null=[]
for _ in range(1000):
    L=lab[:]; random.shuffle(L); null.append(loo(L))
p95=float(np.percentile(null,95))
means={c:np.mean([V[r[0]] for r in ex if r[1]==c],0) for c in 'fs'}
def margin(v): return v@means['f']/np.linalg.norm(means['f'])-v@means['s']/np.linalg.norm(means['s'])
tm=margin(V['T']) if V.get('T') is not None else float('nan')
mnull=[]
for _ in range(1000):
    L=lab[:]; random.shuffle(L); m={c:np.mean([V[r[0]] for r,l in zip(ex,L) if l==c],0) for c in 'fs'}
    mnull.append(V['T']@m['f']/np.linalg.norm(m['f'])-V['T']@m['s']/np.linalg.norm(m['s']))
lo,hi=np.percentile(mnull,[2.5,97.5])
nf=sum(1 for r in ex if r[1]=='f'); ns=len(ex)-nf
gate= acc>=0.8 and nf>=4 and ns>=4 and acc>p95
out=[('n_f',nf),('n_s',ns),('loo_acc',round(acc,3)),('null_p95',round(p95,3)),('control','PASS' if gate else 'FAIL'),
     ('target_margin_f_minus_s',round(float(tm),4)),('shuffle_margin_2.5',round(lo,4)),('shuffle_margin_97.5',round(hi,4))]
for r in rows: out.append(('size_'+r[0],info[r[0]]))
with open(os.path.join(H,'result.tsv'),'w') as f:
    for k,v in out: f.write('%s\t%s\n'%(k,v))
for k,v in out: print(k,v,sep='\t')
if '--sheet' in sys.argv:
    tiles=[(r[0],V[r[0]]) for r in rows if V[r[0]] is not None]; W=Image.new('L',(len(tiles)*40,110),255)
    for i,(k,v) in enumerate(tiles):
        t=((v-v.min())/(v.max()-v.min()+1e-9)*255).reshape(48,16).astype(np.uint8)
        W.paste(Image.fromarray(255-t).resize((32,96)),(i*40+4,10))
    W.save(sys.argv[sys.argv.index('--sheet')+1])
