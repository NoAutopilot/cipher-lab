#!/usr/bin/env python3
"""Symbol legend sheet for the transcription passes: exemplar tiles cut from the page images at the boxes
in legend_boxes.txt (label page x0 y0 x1 y1; r = c63 f.28r, v = c64 f.28v), same tone curve as crop.py.
Labels are arbitrary transcription codes, not values. Written 23 Sept 2026. Writes crops/legend.jpg."""
from PIL import Image, ImageDraw, ImageFont
import sys
import os; HERE=os.path.dirname(os.path.abspath(__file__)); base=os.path.join(HERE,'img')+'/'
LO,HI,G=90,240,1.4
t=[int(round(255*min(1,max(0,(v-LO)/(HI-LO)))**G)) for v in range(256)]
pages={'r':Image.open(base+'c63_full.jpg').convert('L').point(t),'v':Image.open(base+'c64_full.jpg').convert('L').point(t)}
ex=[l.split() for l in open(os.path.join(HERE,'legend_boxes.txt')) if l.strip() and not l.startswith('#')]
tiles=[]
for lab,p,x0,y0,x1,y1 in ex:
    c=pages[p].crop((int(x0),int(y0),int(x1),int(y1)))
    s=180/max(c.height,1); c=c.resize((max(1,int(c.width*s)),180))
    tiles.append((lab,c))
cols=6; W=260; H=240
rows=(len(tiles)+cols-1)//cols
sheet=Image.new('L',(cols*W,rows*H),255); d=ImageDraw.Draw(sheet)
try: f=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',34)
except: f=ImageFont.load_default()
for i,(lab,c) in enumerate(tiles):
    x=(i%cols)*W; y=(i//cols)*H
    c=c.crop((0,0,min(c.width,W-10),180)); sheet.paste(c,(x+5,y))
    d.text((x+10,y+190),lab,fill=0,font=f)
    d.rectangle([x,y,x+W-1,y+H-1],outline=128)
sheet.save(os.path.join(HERE,'crops','legend.jpg'),quality=85); print(sheet.size)
