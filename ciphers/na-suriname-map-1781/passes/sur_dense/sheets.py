import glob,os
from PIL import Image,ImageDraw
os.makedirs('sheets',exist_ok=True)
R='/home/user/cipher-lab/ciphers/na-suriname-map-1781/'
ctrl=R+'images/inv373_0693_600px.jpg'; plain='img/370_0043.jpg'
for inv in ['370','371','378','379','380']:
    items=[(os.path.basename(f)[:-4],f) for f in sorted(glob.glob(f'img/{inv}_*.jpg'))]
    for si in range(0,len(items),4):
        chunk=items[si:si+4]; chunk.insert(2,('CTRL373_0693 cipher',ctrl)); chunk.insert(5,('PLAIN 370_0043',plain))
        W=400; ims=[Image.open(p).convert('RGB') for _,p in chunk]
        ims=[i.resize((W,int(i.height*W/i.width))) for i in ims]
        H=max(i.height for i in ims)
        sh=Image.new('RGB',(W*3,(H+16)*2),'white'); d=ImageDraw.Draw(sh)
        for k,((n,_),im) in enumerate(zip(chunk,ims)):
            x=(k%3)*W; y=(k//3)*(H+16); sh.paste(im,(x,y+16)); d.text((x+4,y+2),n,fill='red')
        sh.save(f'sheets/{inv}_s{si//4+1}.jpg',quality=60)
