import sys,json,random
sys.path.insert(0,'ciphers/fr4715-vieuville-pool/scripts')
from PIL import Image, ImageDraw
import cut_f60r_bands as cb
SP=sys.argv[1]
c=json.load(open(f'{SP}/cands.json'))
acc=[1,2,3,4,6,7,12,15,17,23,24,30,31,32,34,36,38,39,43,44,45,47,49,51,52,53,55,56,59,61,66,67,68,70,71]
rng=random.Random(20261002)
P=[i for i in acc if c[i]['cls']=='P']; F=[i for i in acc if c[i]['cls']=='F']
F=sorted(rng.sample(F,18)); sel=P+F; rng.shuffle(sel)
im=Image.open(cb.SRC); tr=cb.track_lines(im,list(range(6,15)),0)
S=5; tw,th=180,200
sheet=Image.new('RGB',(6*tw,5*(th+24)),'white'); d=ImageDraw.Draw(sheet)
truth=[]
for k,i in enumerate(sel):
  z=c[i]; pad=6
  a=max(0,z['x']-pad); b=min(im.size[0],z['x1']+pad)
  band=cb.straight(im,tr[z['line']],a,b,(30,28))
  g=band.crop((0,max(0,z['y0']-pad),b-a,min(58,z['y1']+pad)))
  sc=min((tw-10)/g.width,(th-10)/g.height,S)
  g=g.resize((int(g.width*sc),int(g.height*sc)),Image.LANCZOS)
  x=(k%6)*tw; y=(k//6)*(th+24)
  sheet.paste(g,(x+(tw-g.width)//2,y+24+(th-g.height)//2))
  d.text((x+4,y+4),f'Z{k+1:02d}',fill=(200,0,0)); d.rectangle([x,y,x+tw-1,y+th+23],outline=(180,180,180))
  truth.append(dict(tile=f'Z{k+1:02d}',cls=z['cls'],line=f"L{z['line']:02d}",seg=z['seg'],unit=z['unit'],x_region=z['x'],ctx=z['ctx']))
sheet.save(f'{SP}/zero_sheet.png'); json.dump(truth,open(f'{SP}/truth.json','w'),indent=0)
print(len(sel),sum(t['cls']=='P' for t in truth))
