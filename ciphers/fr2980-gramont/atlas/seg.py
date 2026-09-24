import json,sys,numpy as np
from PIL import Image
S=sys.argv[1]
C=json.load(open('crops/crops.json')); SP=json.load(open('crops/splits.json'))
arr={k:np.array(Image.open(f'{S}/full/{k}_norm.jpg').convert('L')) for k in ('f29r','f30r','f30v')}
def runs_of(col,gapmin):
    runs=[];x=0;W=len(col)
    while x<W:
        if col[x]:
            s=x
            while x<W and col[x]: x+=1
            runs.append([s,x])
        else: x+=1
    m=[]
    for rn in runs:
        if m and rn[0]-m[-1][1]<gapmin: m[-1][1]=rn[1]
        else: m.append(rn)
    return m
def half(im,gapmin=5):
    H=im.shape[0]
    for thr,up,dn in ((190,.16,.16),(190,.2,.03),(160,.18,0),(140,.14,-.02)):
        bw=im<thr
        prof=bw.sum(1); c=int(np.argmax(np.convolve(prof,np.ones(15),'same')[int(H*.3):int(H*.8)]))+int(H*.3)
        core=bw[c-int(H*up):c+int(H*dn)]
        m=runs_of(core.sum(0)>0,gapmin)
        if max((e-s for s,e in m),default=0)<260: break
    res=[]
    for s,e in m:
        top=max(0,c-int(H*.45)); rows=np.where(bw[top:c+int(H*.4),s:e].any(1))[0]
        if len(rows)==0: continue
        ar=int(core[:,s:e].sum())
        if ar<15: continue
        res.append((s,top+rows[0],e,top+rows[-1],ar))
    return res
def seg(lid):
    a=arr[lid[:4]]; r=C[lid]; cut=SP[lid]; out=[]
    for h,(l,t,rr,b) in (('a',(r['a'][0],r['a'][1],cut,r['a'][3])),('b',(cut,r['b'][1],r['b'][2],r['b'][3]))):
        for s,y0,e,y1,ar in half(a[t:b,l:rr]): out.append((lid[:4],h,l+s,t+y0,l+e,t+y1,ar))
    return out
