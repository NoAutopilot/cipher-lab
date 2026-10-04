import csv
from PIL import Image
imgs={'1':'dec/IMG_R1166_I5853_P1.png','2':'dec/IMG_R1166_I5854_P2.png'}
cache={}; out=open('n8cos_boxes.tsv','w'); out.write('unit\tpage\tx0\ty0\tx1\ty1\n')
import os; os.makedirs('gcrops',exist_ok=True)
for r in csv.DictReader(open('boxes_view.tsv'),delimiter='\t'):
    s=1.06; ox,oy=int(r['ox']),int(r['oy'])
    x0,y0,x1,y1=[round(o+s*int(r[k])) for o,k in ((ox,'vx0'),(oy,'vy0'),(ox,'vx1'),(oy,'vy1'))]
    out.write(f"{r['unit']}\t{r['page']}\t{x0}\t{y0}\t{x1}\t{y1}\n")
    im=cache.setdefault(r['page'],Image.open(imgs[r['page']]).convert('RGB'))
    c=im.crop((x0,y0,x1,y1))
    w,h=c.size
    if w<500: c=c.resize((w*2,h*2))
    c.save(f"gcrops/{r['unit']}.png")
