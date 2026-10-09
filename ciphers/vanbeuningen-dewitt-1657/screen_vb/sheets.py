import sys,os,glob,random,json
from PIL import Image,ImageDraw
src,ctl,out,tag=sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4]
random.seed(int(sys.argv[5]) if len(sys.argv)>5 else 7)
tg=sorted(glob.glob(src+'/*.jpg')); cs={'C1':ctl+'/ctl_0210.jpg','C2':ctl+'/ctl_0211.jpg','K1':ctl+'/ctl_0206.jpg','K2':ctl+'/ctl_0207.jpg'}
os.makedirs(out,exist_ok=True); key={}
for si in range(0,len(tg),8):
    items=[('T',f) for f in tg[si:si+8]]+[(k,v) for k,v in cs.items()]
    random.shuffle(items); n=si//8+1
    W,H,cols=400,330,4; rows=(len(items)+cols-1)//cols
    sh=Image.new('RGB',(W*cols,H*rows),'white'); d=ImageDraw.Draw(sh)
    for i,(k,f) in enumerate(items):
        im=Image.open(f).convert('RGB'); im.thumbnail((W-6,H-24))
        x,y=(i%cols)*W,(i//cols)*H; sh.paste(im,(x+3,y+20))
        lab=f'{tag}{n:02d}-{i+1:02d}'; d.rectangle([x,y,x+90,y+16],fill='black'); d.text((x+3,y+3),lab,fill='white')
        key[lab]={'kind':k,'file':os.path.basename(f)}
    sh.save(f'{out}/sheet_{tag}{n:02d}.jpg',quality=85)
json.dump(key,open(f'{out}/KEY_{tag}.json','w'),indent=0)
print(len(tg),'targets', (len(tg)+7)//8,'sheets')
