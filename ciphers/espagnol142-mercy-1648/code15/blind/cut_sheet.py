import random, json
from PIL import Image, ImageDraw
im=Image.open('images/f22v_canvas59.jpg').convert('L')
v04=[(960,1062),(1114,1196),(1233,1339),(1385,1445),(1504,1573),(1631,1707),(1763,1806),(1874,1953),(2019,2088),(2116,2172),(2238,2318),(2379,2422),(2463,2552),(2611,2682),(2724,2769),(2833,2937),(2987,3077),(3132,3180),(3224,3299)]
items=[('v04',p,v04[p-1],(850,1020)) for p in range(6,20)]
items+=[('v05',14,(2577,2678),(1015,1135)),('v05',15,(2724,2798),(1015,1135)),('v05',17,(2992,3097),(1015,1135)),('v05',9,(1984,2080),(1015,1135)),('v03',7,(1791,1849),(670,790)),('v03',8,(1887,1955),(670,790))]
random.seed(20261002); random.shuffle(items)
labs=['K','B','R','F','W','M','T','H','P','D','X','G','N','Q','A','L','V','E','S','J']
key=[];crops=[]
import os; os.makedirs(S+'/blind',exist_ok=True)
for lab,(ln,p,(x0,x1),(y0,y1)) in zip(labs,items):
    c=im.crop((x0-22,y0,min(x1+22,3546) if not (ln=='v04' and p==19) else 3330,y1))
    c=c.resize((c.width*3,c.height*3),Image.LANCZOS)
    f=f'{S}/blind/item_{lab}.png'; c.save(f); crops.append((lab,c))
    key.append(dict(label=lab,line=ln,pos=p,box=[x0-22,y0,x1+22,y1]))
json.dump(key,open(S+'/blind_key.json','w'),indent=1)
# sheet: 4 per row
W=max(c.width for _,c in crops)+20; H=max(c.height for _,c in crops)+60
sh=Image.new('L',(W*4,H*5),255); d=ImageDraw.Draw(sh)
for i,(lab,c) in enumerate(crops):
    x=(i%4)*W; y=(i//4)*H; d.text((x+8,y+5),lab,fill=0); sh.paste(c,(x+10,y+40))
sh.save(S+'/blind/sheet.png'); print(sh.size)
