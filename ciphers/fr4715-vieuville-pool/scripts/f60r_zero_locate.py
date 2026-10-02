import sys, csv, glob, json, random
sys.path.insert(0,'ciphers/fr4715-vieuville-pool/scripts')
import numpy as np
from PIL import Image
from scipy import ndimage
import cut_f60r_bands as cb, f60r_blocks as fb
SP=sys.argv[1]
W='ciphers/fr4715-vieuville-pool/witness'
codes=fb.key_codes()
im=Image.open(cb.SRC); Wd=im.size[0]
lines=list(range(6,15)); tracks=cb.track_lines(im, lines, 0)
rows={}
for p in 'AB':
  for f in sorted(glob.glob(f'{W}/f60r_blocks_pass{p}_b*.tsv')):
    for r in csv.DictReader(open(f),delimiter='\t'):
      if int(r['crop'].strip()[-1])<=3: rows[(p,r['crop'].strip())]=r['text']
  for r in csv.DictReader(open(f'{W}/f60r_blocks_pass{p}_t.tsv'),delimiter='\t'): rows[(p,r['crop'].strip())]=r['text']
def blobs(b):
  ink=b<120; lab,k=ndimage.label(ink); objs=ndimage.find_objects(lab); bl=[]
  for i,s in enumerate(objs):
    h=s[0].stop-s[0].start; area=(lab[s]==i+1).sum()
    if area<25 or h<8: continue
    holes=ndimage.label(~ink[s] & ndimage.binary_fill_holes(lab[s]==i+1))[1]
    bl.append([s[1].start,s[1].stop,s[0].start,s[0].stop,holes])
  bl.sort(); m=[]
  for b2 in bl:
    if m and b2[0] < m[-1][1]-3:
      m[-1]=[min(m[-1][0],b2[0]),max(m[-1][1],b2[1]),min(m[-1][2],b2[2]),max(m[-1][3],b2[3]),m[-1][4]+b2[4]]
    else: m.append(b2)
  return m
def align(bl,n_units,wu):
  INF=1e18; nb=len(bl)
  D=np.full((nb+1,n_units+1),INF); B={}
  D[0,0]=0
  for i in range(nb+1):
    for j in range(n_units+1):
      if D[i,j]>=INF: continue
      if i<nb:
        w=bl[i][1]-bl[i][0]
        if D[i,j]+w*1.5 < D[i+1,j]: D[i+1,j]=D[i,j]+w*1.5; B[(i+1,j)]=(i,j,0)   # noise blob
        for k in range(1,5):
          if j+k<=n_units:
            c=D[i,j]+abs(w-k*wu)+ (2 if k>1 else 0)
            if c<D[i+1,j+k]: D[i+1,j+k]=c; B[(i+1,j+k)]=(i,j,k)
      if j<n_units and D[i,j]+wu*1.5<D[i,j+1]: D[i,j+1]=D[i,j]+wu*1.5; B[(i,j+1)]=(i,j,-1)  # unit with no blob
  path=[]; i,j=nb,n_units
  while (i,j)!=(0,0):
    pi,pj,k=B[(i,j)]; path.append((pi,pj,k)); i,j=pi,pj
  return path[::-1]
cands=[]
for n in lines:
  x0,s=0,1
  while x0<Wd:
    x1=min(Wd,x0+600)
    ta=rows.get(('A',f'f60r_L{n:02d}_s{s}')); tb=rows.get(('B',f'f60r_L{n:02d}_s{s}'))
    if ta and tb:
      ua=[a for a,_ in fb.parse(ta)]; ub=[a for a,_ in fb.parse(tb)]
      if not any(u.startswith('w:') for u in ua):
        units=ua
        import difflib
        sm=difflib.SequenceMatcher(None,[u.lstrip('.=') for u in ua],[u.lstrip('.=') for u in ub],autojunk=False)
        agreeB=set()
        for blk in sm.get_matching_blocks():
          for q in range(blk.size): agreeB.add(blk.a+q)
        toks=fb.segment_units(units,codes)
        # unit -> class for zeros
        cls=[None]*len(units); ui=0
        for t in toks:
          width=len(t.replace('8<','8').lstrip('.')) if t not in ('♀','▽') else 1
          if t.startswith('w:') or t=='?': width=1
          if '8<' in t: cls[ui]='P'
          elif width==2 and t.lstrip('.')[1]=='0' and units[ui+1].lstrip('.=')=='0' and not t.startswith('.'): cls[ui+1]='F'
          ui+=width
        band=np.array(cb.straight(im,tracks[n],x0,x1,(30,28)).convert('L')).astype(float)
        bl=blobs(band)
        wu=sum(b[1]-b[0] for b in bl)/len(units)
        path=align(bl,len(units),wu)
        for bi,uj,k in path:
          if k==1 and cls[uj] and uj in agreeB and 3<=uj<len(units)-3:
            best=None
            for bj in (bi-1,bi,bi+1):
              if 0<=bj<len(bl):
                q=bl[bj]; w=q[1]-q[0]; h=q[3]-q[2]
                if h<=24 and 0.55<=w/h<=1.8 and q[2]>=14:
                  sc=abs(bj-bi)*2+abs(w/h-1)
                  if best is None or sc<best[0]: best=(sc,q)
            if best is None: continue
            b=best[1]
            cands.append(dict(line=n,seg=s,unit=uj,cls=cls[uj],x=x0+b[0],x1=x0+b[1],y0=b[2],y1=b[3],holes=b[4],ctx=''.join(u.lstrip('.=') for u in units[max(0,uj-3):uj+4])))
    if x1>=Wd: break
    x0=x1-60; s+=1
print(len(cands), sum(c['cls']=='P' for c in cands), sum(c['cls']=='F' for c in cands))
print('with hole:', sum(c['holes']>=1 for c in cands if c['cls']=='P'), sum(c['holes']>=1 for c in cands if c['cls']=='F'))
json.dump(cands,open(f'{SP}/cands.json','w'))
