# LIN-SIB (9 Oct 2026): blind-control contact sheets of DigitArq thumbnails; run from images/maco86_scan, e.g. python3 ../../scripts/linsib_montage.py OUT 30 202 doc02
# usage: montage.py OUTPREFIX PER_SHEET SEED dir1 [dir2...]  ; inserts control tiles blind
import sys,glob,os,random,json
from PIL import Image,ImageDraw
out,per,seed=sys.argv[1],int(sys.argv[2]),int(sys.argv[3]); dirs=sys.argv[4:]
CT=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','images','full_PT-TT-CLNH-0086-11_m000%d.jpg.jpg')
tiles=[]
for d in dirs:
    for f in sorted(glob.glob(os.path.join(d,'thumb_*.jpg'))):
        tiles.append((os.path.basename(d)+':'+os.path.basename(f).split('_m')[-1].split('.')[0],Image.open(f).convert('RGB')))
def thumb(p):
    im=Image.open(p).convert('RGB'); w,h=im.size; s=128/min(w,h); return im.resize((round(w*s),round(h*s)),Image.LANCZOS)
rnd=random.Random(seed)
ctrls=[('CTRL:11m0002',thumb(CT%2)),('CTRL:11m0003',thumb(CT%3))]
# one control per sheet, at random positions, cycling
nsheets=(len(tiles)+per-2)//(per-1)
sheets=[tiles[i*(per-1):(i+1)*(per-1)] for i in range(nsheets)]
key={}
cols=6; T=300
for si,sh in enumerate(sheets):
    sh=list(sh); c=ctrls[si%2]; sh.insert(rnd.randrange(len(sh)+1),c)
    rows=(len(sh)+cols-1)//cols
    M=Image.new('RGB',(cols*T,rows*(T+22)),'white'); dr=ImageDraw.Draw(M)
    for k,(lab,im) in enumerate(sh):
        code=f'S{si+1:02d}-{k+1:02d}'; key[code]=lab
        t=im.copy(); s=min((T-6)/t.width,(T-6)/t.height); t=t.resize((int(t.width*s),int(t.height*s)),Image.LANCZOS)
        x=(k%cols)*T; y=(k//cols)*(T+22)
        M.paste(t,(x+3,y+22)); dr.text((x+4,y+4),code,fill='black')
    M.save(f'{out}_{si+1:02d}.jpg',quality=88)
json.dump(key,open(out+'_key.json','w'),indent=0)
print(len(tiles),'tiles',len(sheets),'sheets')
