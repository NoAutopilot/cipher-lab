"""LIN-COUNT (9 Oct 2026): stack one column's iiif_lines row crops (images/rows_hires/r_<k>/) into numbered sheets.
argv: key (e.g. 0236_c1), max rows, out dir. Each strip = the row crop at native 1897 px scale with a grey tab 'Rnn';
24 strips per sheet. No other change to the pixels."""
import json, os, sys
from PIL import Image, ImageDraw, ImageFont
k,n,out=sys.argv[1],int(sys.argv[2]),sys.argv[3]
d=f'images/rows_hires/r_{k}'; man=json.load(open(d+'/manifest.json'))['iiif_lines']
ents=sorted(man,key=lambda e:e['box'][1])[:n]
font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',22)
strips=[]
for i,e in enumerate(ents,1):
    st=Image.open(os.path.join(d,e['crop'])).convert('RGB')
    im=Image.new('RGB',(st.width+86,st.height+4),'white'); dr=ImageDraw.Draw(im)
    dr.rectangle([0,0,70,im.height],fill=(220,220,220)); dr.text((6,im.height//2-12),'R%02d'%i,fill=(0,0,120),font=font)
    im.paste(st,(80,2)); dr.line([(0,im.height-1),(im.width,im.height-1)],fill=(120,120,255),width=2); strips.append(im)
os.makedirs(out,exist_ok=True)
for s in range(0,len(strips),24):
    g=strips[s:s+24]; W=max(x.width for x in g); sh=Image.new('RGB',(W,sum(x.height for x in g)),'white'); y=0
    for x in g: sh.paste(x,(0,y)); y+=x.height
    p=f'{out}/sheet_{k}_{s//24+1}.jpg'; sh.save(p,quality=85); print(p,sh.size,len(g))
