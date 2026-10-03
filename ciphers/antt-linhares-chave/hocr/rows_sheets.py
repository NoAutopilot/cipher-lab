import json, os, sys
from PIL import Image, ImageDraw, ImageFont
S=sys.argv[1]; leaf,col,nrows,tag=sys.argv[2],sys.argv[3],int(sys.argv[4]),sys.argv[5]
d=f'{S}/rows_{leaf}_{col}'; man=json.load(open(d+'/manifest.json'))['iiif_lines']
ents=sorted(man,key=lambda e:e['box'][1])[:nrows]
src=Image.open(os.path.join('images/book',ents[0]['source_file'])).convert('L')
try: font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',26)
except Exception: font=ImageFont.load_default()
U=2; PAD=5; out=[]
strips=[]
for i,e in enumerate(ents,1):
    x0,y0,x1,y1=e['box']
    st=src.crop((x0,y0-PAD,x1,y1+PAD)); st=st.resize((st.width*U,st.height*U),Image.LANCZOS)
    w=st.width+110+50; h=st.height+12
    im=Image.new('RGB',(w,h),'white'); dr=ImageDraw.Draw(im)
    dr.rectangle([0,0,80,h],fill=(225,225,225)); dr.text((8,h//2-14),'R%02d'%i,fill=(0,0,160),font=font)
    dr.rectangle([88,0,94,h],fill=(90,90,90))
    im.paste(st.convert('RGB'),(105,6))
    cy=6+(PAD+(y1-y0)//2)*U; xr=105+st.width+8
    dr.polygon([(xr,cy),(xr+30,cy-12),(xr+30,cy+12)],fill=(220,0,0))
    dr.line([(0,h-1),(w,h-1)],fill=(150,150,255),width=2)
    strips.append(im)
per=23
for s in range(0,len(strips),per):
    g=strips[s:s+per]; W=max(x.width for x in g); H=sum(x.height for x in g)
    sh=Image.new('RGB',(W,H),'white'); y=0
    for x in g: sh.paste(x,(0,y)); y+=x.height
    p=f'{S}/sheet_{tag}_{s//per+1}.png'; sh.save(p); print(p,sh.size,len(g))
