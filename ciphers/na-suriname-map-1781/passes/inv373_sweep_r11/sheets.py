"""Contact sheets: 3x2 grid of 600 px thumbnails, tile 1 = positive control scan 0693 (images/inv373_0693_600px.jpg),
then 5 sampled scans in plan order, each tile labelled with its scan number. Usage: sheets.py THUMBDIR OUTDIR."""
import sys,os
from PIL import Image,ImageDraw
th,out=sys.argv[1],sys.argv[2]; os.makedirs(out,exist_ok=True)
ctrl=Image.open('../../images/inv373_0693_600px.jpg').convert('RGB')
labs=[l.split('\t')[1].split('_')[-1][:4] for l in open('plan.tsv').read().split('\n')[1:] if l]
labs=[n for n in labs if os.path.exists(f'{th}/s{n}.jpg')]
W,H=600,500
for k in range(0,len(labs),5):
    sh=Image.new('RGB',(3*W,2*(H+20)),'white'); d=ImageDraw.Draw(sh)
    tiles=[('CTRL 0693',ctrl)]+[(n,Image.open(f'{th}/s{n}.jpg').convert('RGB')) for n in labs[k:k+5]]
    for i,(name,im) in enumerate(tiles):
        im.thumbnail((W,H)); x,y=(i%3)*W,(i//3)*(H+20)
        sh.paste(im,(x,y+20)); d.text((x+5,y+3),name,fill='red')
    sh.save(f'{out}/sheet{k//5:02d}.jpg',quality=88)
print(len(labs),'tiles')
