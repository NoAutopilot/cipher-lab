import glob,os
from PIL import Image,ImageDraw
os.makedirs('sheets',exist_ok=True)
ctrl='/home/user/cipher-lab/ciphers/na-suriname-map-1781/images/sur_gov/../inv373_0693_600px.jpg'
if not os.path.exists(ctrl): ctrl='/home/user/cipher-lab/ciphers/na-suriname-map-1781/images/inv373_0693_600px.jpg'
for inv in ['266','267','268','269','270']:
    fs=sorted(glob.glob(f'img/{inv}_*.jpg')); items=[(os.path.basename(f)[:-4],f) for f in fs]
    for si in range(0,len(items),5):
        chunk=items[si:si+5]; chunk.insert(3,('CTRL373_0693',ctrl))
        W=400; ims=[Image.open(p).convert('RGB') for _,p in chunk]
        ims=[i.resize((W,int(i.height*W/i.width))) for i in ims]
        H=max(i.height for i in ims)
        sh=Image.new('RGB',(W*3,(H+16)*2),'white'); d=ImageDraw.Draw(sh)
        for k,((n,_),im) in enumerate(zip(chunk,ims)):
            x=(k%3)*W; y=(k//3)*(H+16); sh.paste(im,(x,y+16)); d.text((x+4,y+2),n,fill='red')
        sh.save(f'sheets/{inv}_s{si//5+1}.jpg',quality=85)
