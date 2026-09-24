import sys,json; S=sys.argv[1]; exec(open(S+'/seg.py').read())
exec(open(S+'/dp.py').read().split('tok={}')[0].split("from PIL import Image\n",1)[1])  # feat()
from PIL import Image, ImageDraw
res=json.load(open(S+'/f29_dp.json'))
T={}
for lid,o in res.items():
    for c,fo,x0,t,x1,b,d in o:
        if d<0.5: T.setdefault(c,[]).append(feat(fo,int(x0),int(t),int(x1),int(b)))
out={}; odd=[]
for lid in C:
    if lid.startswith('f29'): continue
    row=[]
    for g in seg(lid):
        fo,h,x0,t,x1,b,ar=g; f=feat(fo,x0,t,x1,b)
        sc=sorted(((1-max(float(v@f) for v in vs),c) for c,vs in T.items()))
        row.append([int(x0),int(t),int(x1),int(b),int(ar),sc[0][1],round(sc[0][0],3),sc[1][1]])
        if sc[0][0]>0.42 and ar>60: odd.append((lid,len(row)-1,f))
    out[lid]=row
json.dump(out,open(S+'/f30_cls.json','w'))
print(sum(len(v) for v in out.values()),'segments', len(odd),'odd')
# greedy cluster the odd ones
cl=[]
for o in odd:
    for c in cl:
        if float(c[0][2]@o[2])>0.6: c.append(o); break
    else: cl.append([o])
cl.sort(key=len,reverse=True)
json.dump([[(o[0],o[1]) for o in c] for c in cl],open(S+'/odd_cl.json','w'))
print([len(c) for c in cl][:40])
sh=Image.new('L',(1400,100*min(len(cl),40)),255); dr=ImageDraw.Draw(sh)
for r,c in enumerate(cl[:40]):
    dr.text((5,r*100+35),f'c{r} n={len(c)}',fill=0,font_size=24)
    for q,(lid,i,f) in enumerate(c[:10]):
        x0,t,x1,b=out[lid][i][:4]; im=Image.fromarray(arr[lid[:4]][t:b+1,x0:x1]); im.thumbnail((110,95)); sh.paste(im,(150+q*120,r*100))
sh.save(S+'/odd.png')
