#!/usr/bin/env python3
# MONLUC-CURL (9 Oct 2026): value-blind sheet of the 17 f.86 K07 crops + the f.86 K38 on WIDER crops (180x160 native px, 1.5x,
# seed 1186, corner ticks only so no box hides a curl), for a binary "curl present?" question per tile.
# Usage: python3 -I f86_curl_sheet.py OUT_KEY.tsv OUT_SHEET.png  (run from the repo root; sheet goes to scratch, never committed)
import csv,random,sys
from PIL import Image,ImageOps,ImageDraw
T='ciphers/fr4735-monluc-lansac-poland-1573/'
src=Image.open(T+'images/src_ark_12148_btv1b9060724s_f172_1230_950_2580_520.jpg').convert('L')
P=200; _s=Image.new('L',(src.width+2*P,src.height+2*P),255); _s.paste(src,(P,P)); src=_s  # white pad: edge tiles get no black band
rows=[r for r in csv.reader(open(T+'blind_k07_sort.tsv'),delimiter='\t') if r and not r[0].startswith('#') and r[0]!='tile']
rows=[r for r in rows if r[1]=='c172']
items=[(r[2],r[3],r[4],int(r[5]),int(r[6])) for r in rows]
random.Random(1186).shuffle(items)
W,H=180,160; SC=1.5; w,h=int(W*SC),int(H*SC); C=4
sheet=Image.new('L',(C*(w+12)+12,((len(items)+C-1)//C)*(h+34)+12),255)
d=ImageDraw.Draw(sheet)
out=open(sys.argv[1],'w'); out.write('tile\tline\tpos\tcell\tx\ty\n')
for i,(l,p,c,x,y) in enumerate(items):
    cr=src.crop((x+P-W//2,y+P-H//2,x+P+W//2,y+P+H//2)).resize((w,h),Image.LANCZOS)
    cr=ImageOps.autocontrast(cr,cutoff=1)
    cx,cy=12+(i%C)*(w+12),12+(i//C)*(h+34)
    sheet.paste(cr,(cx,cy+24)); d.text((cx+4,cy+6),'tile '+str(i+1),fill=0)
    mx,my=cx+w//2,cy+24+h//2
    for sx in (-1,1):  # corner ticks marking the centre sign's box (about 64x72 native px), outside the strokes
        for sy in (-1,1):
            ax,ay=mx+sx*48,my+sy*54
            d.line((ax,ay,ax-sx*10,ay),fill=128,width=2); d.line((ax,ay,ax,ay-sy*10),fill=128,width=2)
    out.write(f'{i+1}\t{l}\t{p}\t{c}\t{x}\t{y}\n')
sheet.save(sys.argv[2])
print(len(items),sheet.size)
