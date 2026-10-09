#!/usr/bin/env python3
# MONLUC-F86 (9 Oct 2026): value-blind sheet of the 17 f.86 K07 crops + the f.86 K38 (one scale, 2x, seed 886).
# Usage: python3 -I f86_sort_sheet.py OUT_KEY.tsv OUT_SHEET.png  (run from the repo root; sheet goes to scratch, never committed)
import csv,random,sys
from PIL import Image,ImageOps,ImageDraw
T='ciphers/fr4735-monluc-lansac-poland-1573/'
src=Image.open(T+'images/src_ark_12148_btv1b9060724s_f172_1230_950_2580_520.jpg').convert('L')
rows=[r for r in csv.reader(open(T+'blind_k07_sort.tsv'),delimiter='\t') if r and not r[0].startswith('#') and r[0]!='tile']
rows=[r for r in rows if r[1]=='c172']
items=[(r[2],r[3],r[4],int(r[5]),int(r[6])) for r in rows]
random.Random(886).shuffle(items)
W,H=96,108; SC=2
sheet=Image.new('L',(6*(W*SC+10)+10,((len(items)+5)//6)*(H*SC+40)+10),255)
d=ImageDraw.Draw(sheet)
out=open(sys.argv[1],'w'); out.write('tile\tline\tpos\tcell\tx\ty\n')
for i,(l,p,c,x,y) in enumerate(items):
    cr=src.crop((x-W//2,y-H//2,x+W//2,y+H//2)).resize((W*SC,H*SC),Image.LANCZOS)
    cr=ImageOps.autocontrast(cr,cutoff=1)
    cx,cy=10+(i%6)*(W*SC+10),10+(i//6)*(H*SC+40)
    sheet.paste(cr,(cx,cy+28)); d.text((cx+4,cy+4),str(i+1),fill=0)
    d.rectangle((cx+W*SC//2-30,cy+28+H*SC//2-34,cx+W*SC//2+30,cy+28+H*SC//2+34),outline=160)
    out.write(f'{i+1}\t{l}\t{p}\t{c}\t{x}\t{y}\n')
sheet=sheet.resize((sheet.width,sheet.height)); sheet.save(sys.argv[2])
print(len(items),sheet.size)
