import sys,json; S=sys.argv[1]; exec(open(S+'/seg.py').read())
from PIL import Image, ImageDraw
res=json.load(open(S+'/f29_dp.json')); fx=json.load(open(S+'/fix.json')); by={}
for lid,o in res.items():
    for c,fo,x0,t,x1,b,d in o: by.setdefault(c,[]).append((d,fo,int(x0),int(t),int(x1),int(b),lid))
ex={}
for c in sorted(by):
    L=[]
    for i,e in enumerate(sorted(by[c])):
        k=f'{c}:{i}'
        if k in fx['drop']: continue
        d,fo,x0,t,x1,b,lid=e
        if k in fx['frac']: f0,f1=fx['frac'][k]; w=x1-x0; x0,x1=x0+int(w*f0),x0+int(w*f1)
        L.append((fo,x0,t,x1,b,lid))
        if len(L)==3: break
    if L: ex[c]=L
json.dump(ex,open(S+'/atlas_ex.json','w'))
codes=sorted(ex,key=str.lower); K=3; CW=140; RH=120; cols=3; n=len(codes); rows=(n+cols-1)//cols; w=150+K*CW
sh=Image.new('L',(w*cols,rows*RH),255); dr=ImageDraw.Draw(sh)
for q,c in enumerate(codes):
    X=(q//rows)*w; Y=(q%rows)*RH; dr.text((X+8,Y+40),c,fill=0,font_size=34)
    for p,(fo,x0,t,x1,b,lid) in enumerate(ex[c]):
        im=Image.fromarray(arr[fo][t:b+1,x0:x1]); im.thumbnail((CW-12,RH-10)); sh.paste(im,(X+150+p*CW,Y+5))
    dr.line([(X,Y+RH-1),(X+w,Y+RH-1)],fill=170); dr.line([(X+w-2,Y),(X+w-2,Y+RH)],fill=120)
sh.save(S+'/atlas.png'); print(n)
