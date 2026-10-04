import random,glob,os,json
from PIL import Image,ImageDraw,ImageFont
S='/tmp/claude-0/-home-user-cipher-lab/dd6c29d6-6496-5bf8-b6e2-45c43428b1a8/scratchpad'
L='/home/user/cipher-lab/ciphers/naf14913-rousseau-venice-1743/images/lowres/s300'
ctrl={'POS-A':f'{S}/s300/c424.jpg','POS-B':f'{L}/v545_266r_300.jpg','POS-C':f'{L}/v517_252r_300.jpg','NEG':f'{S}/s300/c425.jpg'}
sweep=sorted([int(os.path.basename(f)[1:4]) for f in glob.glob(S+'/s300/c*.jpg')],reverse=True)
sweep=[n for n in sweep if n<=423]
rng=random.Random(210)
TW,TH=300,440;COLS,ROWS=6,3;LAB=28
font=ImageFont.load_default(size=22)
os.makedirs(S+'/sheets',exist_ok=True)
mask=[];per=COLS*ROWS-4
for si in range(0,len(sweep),per):
    sid=si//per+1;items=[('SWEEP',n,f'{S}/s300/c{n:03d}.jpg') for n in sweep[si:si+per]]+[(k,None,v) for k,v in ctrl.items()]
    rng.shuffle(items)
    sh=Image.new('RGB',(COLS*TW,ROWS*(TH+LAB)),'white');d=ImageDraw.Draw(sh)
    for i,(kind,n,f) in enumerate(items):
        tid=f'S{sid:02d}-T{i+1:02d}';x=(i%COLS)*TW;y=(i//COLS)*(TH+LAB)
        im=Image.open(f).convert('RGB');im.thumbnail((TW-6,TH));sh.paste(im,(x+3,y+LAB))
        d.text((x+5,y+2),tid,fill='red',font=font)
        mask.append((tid,kind,n if n else {'POS-A':424,'POS-B':545,'POS-C':517,'NEG':425}[kind]))
    sh.save(f'{S}/sheets/sheet{sid:02d}.jpg',quality=85)
open(S+'/mask.json','w').write(json.dumps(mask))
print(len(sweep),'sweep tiles,',sid,'sheets',sh.size)
