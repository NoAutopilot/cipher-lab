# GAPS117 (3 Oct 2026): anonymised key-4 sign sheet. Run in key4/ after: pdftoppm -r 300 -png ../../../sources/florence/keys/58-6.pdf k300
# Boxes are 150-dpi page coordinates read from a gridded render; ids shuffled with seed 117; values only in sheet_map.tsv.
import random, json
from PIL import Image, ImageDraw, ImageFont
im=Image.open('k300-1.png').convert('L'); S=2
# letter row cells: (value, xcenter, band)
bands={1:(238,277),2:(278,311),3:(312,348)}
L=[('a',198,1),('b',238,1),('c',276,1),('d',316,1),('e',358,1),('f',400,1),('g',440,1),('h',480,1),('i',520,1),('l',560,1),('m',603,1),('n',640,1),('o',683,1),('p',722,1),('q',758,1),('r',795,1),('s',835,1),('t',873,1),('u',915,1),('u',955,1),('z',1040,1),
   ('a',200,2),('e',360,2),('o',685,2),('u',918,2),('u',957,2),('a',200,3),('e',360,3),('o',688,3),('u',918,3),('u',955,3)]
cells=[]
for v,x,b in L:
    y0,y1=bands[b]; cells.append((v,(x-20,y0,x+20,y1),'letter'))
col1=['ba','be','ca','ce','ci','da','pa','pe','pi','fu','ge','gi','le','le','li','lo','lu','ma','na','ni','ne','pa','pe','pi','pe']
vals={}
import csv
for r in csv.reader(open('key4.tsv'),delimiter='\t'):
    if r and r[0].startswith('col'): vals[r[1]]=r[2]
c2r=[318,322,318,318,305,316,307,318,312,316,314,335,324,325,350,332,352,354,338,340,372,352,358,360,358]
c3r=[470,483,473,491,490,492,455,479,477,468,462,466,463,476,472,465,462,477,478,478,477,477,477,480,473]
c4r=[568,587,582,584,582,598,590,590,585,588,592,591,612,595,586,595,606,605,606,612,600,602,610,603,603]
c5r=[704,703,707,723,708,706,728,719,737,725,730,724,727,727,718,714,718,735,729,733,726,730,725,726,736]
c6r=[832,831,840,840,838,845]
starts={1:180,2:281,3:425,4:555,5:677,6:800}
rights={1:[232]*25,2:c2r,3:c3r,4:c4r,5:c5r,6:c6r}
for c in range(1,7):
    for r,xr in enumerate(rights[c]):
        yc=410+r*37.1
        cells.append((vals[f'c{c}r{r+1}'],(starts[c],yc-19,xr,yc+19),f'c{c}r{r+1}'))
random.seed(117); order=list(range(len(cells))); random.shuffle(order)
rows=[];crops=[]
for k,i in enumerate(order):
    v,(x0,y0,x1,y1),src=cells[i]; sid=f'K{k+1:03d}'
    cr=im.crop((int(x0*S),int(y0*S),int(x1*S),int(y1*S)))
    crops.append((sid,cr)); rows.append((sid,src,v,f'{x0},{y0},{x1},{y1}'))
# sheet: 10 per row
cw=max(c.size[0] for _,c in crops)+20; ch=max(c.size[1] for _,c in crops)+34
per=10; nrow=(len(crops)+per-1)//per
font=ImageFont.load_default()
for part,(a,b) in enumerate([(0,len(crops))]):
    sh=Image.new('L',(cw*per,ch*nrow),255); d=ImageDraw.Draw(sh)
    for k,(sid,cr) in enumerate(crops):
        X=(k%per)*cw; Y=(k//per)*ch
        sh.paste(cr,(X+10,Y+24)); d.text((X+4,Y+4),sid,fill=0,font=ImageFont.load_default(size=18)); d.rectangle([X,Y,X+cw-1,Y+ch-1],outline=160)
    sh.save('sheet_key4_anon.png'); print(sh.size, len(crops))
open('sheet_map.tsv','w').write('id\tsource_cell\tvalue\tbox150dpi\n'+''.join('\t'.join(r)+'\n' for r in rows))
