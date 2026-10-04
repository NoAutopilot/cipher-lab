import random,glob,os,json
from PIL import Image,ImageDraw,ImageFont
S='/tmp/claude-0/-home-user-cipher-lab/486a3e53-9e9e-53d2-b166-4722a3e8b2d8/scratchpad'
L='/home/user/cipher-lab/ciphers/naf14913-rousseau-venice-1743/images/lowres/s300'
ctrl={'POS-A':(f'{S}/ctrl/c424.jpg',424),'POS-B':(f'{L}/v545_266r_300.jpg',545),'POS-C':(f'{S}/ctrl/c517.jpg',517),'NEG':(f'{S}/ctrl/c425.jpg',425)}
sweep=list(range(595,801))
rng=random.Random(290)
TW,TH=300,440;COLS,ROWS=6,3;LAB=28
font=ImageFont.load_default(size=22)
os.makedirs(S+'/sheets',exist_ok=True)
mask=[];per=14
for si in range(0,len(sweep),per):
    sid=si//per+1;items=[('SWEEP',n,f'{S}/s300/c{n:03d}.jpg') for n in sweep[si:si+per]]+[(k,v[1],v[0]) for k,v in ctrl.items()]
    rng.shuffle(items)
    sh=Image.new('RGB',(COLS*TW,ROWS*(TH+LAB)),'white');d=ImageDraw.Draw(sh)
    for i,(kind,n,f) in enumerate(items):
        tid=f'S{sid:02d}-T{i+1:02d}';x=(i%COLS)*TW;y=(i//COLS)*(TH+LAB)
        im=Image.open(f).convert('RGB');im.thumbnail((TW-6,TH));sh.paste(im,(x+3,y+LAB))
        d.text((x+5,y+2),tid,fill='red',font=font)
        mask.append((tid,kind,n))
    sh.save(f'{S}/sheets/sheet{sid:02d}.jpg',quality=85)
open(S+'/mask.json','w').write(json.dumps(mask))
print(len(sweep),'tiles',sid,'sheets')
