from PIL import Image
import json, random, sys
K='/home/user/cipher-lab/ciphers/na-suriname-map-1781/images/inv86_0003_left_native.jpg'
k=Image.open(K).convert('RGB')
def reg(x,y,w,h): return k.crop((x,y,x+w,y+h))
refs={'R1':reg(85,1950,115,170),'R2':reg(95,1770,150,190),'R3':reg(85,1560,115,120)}
for n,t in refs.items(): t.resize((t.size[0]*2,t.size[1]*2)).save('tiles/%s.jpg'%n)
def line(f,a,b,pad=4):
    im=Image.open('img/'+f).convert('RGB'); h=im.size[1]; return im.crop((a-pad,int(h*0.28),b+pad,h))
B=json.load(open('boxes.json'))
q={}
for n,(cls,f,a,b,what) in B.items():
    q[n]=(cls, reg(85-12,1950+12,115,170).resize((144,212)) if f=='KEY' else line(f,a,b), what)
names=list(q); random.Random(20261008).shuffle(names)
key={}
for i,n in enumerate(names,1):
    cls,t,what=q[n]; t.resize((t.size[0]*2,t.size[1]*2)).save('tiles/Q%d.jpg'%i); key['Q%d'%i]={'id':n,'class':cls,'what':what}
json.dump(key,open('tiles/blind_key.json','w'),indent=1)
ims=[Image.open('tiles/Q%d.jpg'%i) for i in range(1,len(q)+1)]
W=sum(i.size[0]+15 for i in ims); H=max(i.size[1] for i in ims); s=Image.new('RGB',(W,H),'white'); x=0
for i in ims: s.paste(i,(x,0)); x+=i.size[0]+15
s.save('cand/qcheck.jpg'); print({k:v['id'] for k,v in key.items()})
