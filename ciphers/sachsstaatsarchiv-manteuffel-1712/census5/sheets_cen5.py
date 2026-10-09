#!/usr/bin/env python3
"""MANT-CEN5 contact sheets (tile treatment of mant0608/sheets_d.py: top 16% cut, 600 px tiles, 4x3).
Usage: sheets_cen5.py TARGETS.tsv IMGDIR OUTDIR [--seed 6105]
Each sheet = 10 shuffled targets + 1 code-bearing control (0510/0511/0579/0580 from images/loc694-08-09) + clear control 0125.
Labels C<sheet>-<k>; key written to OUTDIR/sheet_key_cen5.tsv and not opened until every sheet is read."""
import csv,os,random,sys
from PIL import Image,ImageDraw,ImageFont
tg,imgdir,out=sys.argv[1:4]
seed=int(sys.argv[sys.argv.index('--seed')+1]) if '--seed' in sys.argv else 6105
here=os.path.dirname(os.path.abspath(__file__)); disk=os.path.join(here,'..','images','loc694-08-09')
rows=[r for r in csv.reader(open(tg),delimiter='\t')][1:]
targets=[(r[1],r[0]) for r in rows if r[2]=='target']
neg=[(r[1],r[0]) for r in rows if r[2]=='control-'][0]
pos=['0510','0579','0511','0580','0510','0579','0511']
def path(loc,fr):
    p=os.path.join(imgdir,loc.replace('/','-')+'_'+fr+'.jpg')
    return p if os.path.exists(p) else os.path.join(disk,'694-08_%s.jpg'%fr)
rng=random.Random(seed); rng.shuffle(targets)
n=(len(targets)+9)//10; os.makedirs(out,exist_ok=True); T=600
font=ImageFont.load_default(size=28)
key=open(os.path.join(out,'sheet_key_cen5.tsv'),'w'); key.write('sheet\tlabel\tloc\tframe\tkind\n')
for s in range(1,n+1):
    g=targets[(s-1)*10:s*10]
    items=[(l,f,'target') for l,f in g]+[('694/08',pos[(s-1)%len(pos)],'control+'),(neg[0],neg[1],'control-')]
    rng.shuffle(items)
    sheet=Image.new('L',(4*T,3*(T+34)),255); d=ImageDraw.Draw(sheet)
    for k,(loc,fr,kind) in enumerate(items):
        im=Image.open(path(loc,fr)).convert('L'); w,h=im.size
        im=im.crop((int(w*0.03),int(h*0.16),int(w*0.97),h)); im.thumbnail((T,T))
        x,y=(k%4)*T,(k//4)*(T+34); lab='C%d-%d'%(s,k+1)
        d.text((x+10,y+4),lab,fill=0,font=font); sheet.paste(im,(x,y+34))
        key.write('%d\t%s\t%s\t%s\t%s\n'%(s,lab,loc,fr,kind))
    sheet.save(os.path.join(out,'sheet%02d.jpg'%s),quality=82)
key.close()
