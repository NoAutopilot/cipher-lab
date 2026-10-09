import glob,os
from PIL import Image,ImageDraw
os.makedirs('sheets',exist_ok=True)
ctrl='../../images/inv373_0693_600px.jpg'
inv_list=sorted({os.path.basename(f).split('_')[0] for f in glob.glob('img/*.jpg')})
for inv in inv_list:
    fs=sorted(glob.glob(f'img/{inv}_*.jpg'))
    # positive control placed at random-ish slot 3, negative = first sampled scan of the next sheet placed anywhere? use sampled scan 8 reused as plain only if judged plain
    items=[(os.path.basename(f)[:-4],f) for f in fs]
    per=5
    for si in range(0,len(items),per):
        chunk=items[si:si+per]; chunk.insert(3,('CTRL373_0693',ctrl))
        W=600;ims=[Image.open(p).convert('RGB') for _,p in chunk]
        ims=[i.resize((W,int(i.height*W/i.width))) for i in ims]
        H=max(i.height for i in ims)
        sh=Image.new('RGB',(W*3,(H+16)*2),'white');d=ImageDraw.Draw(sh)
        for k,((n,_),im) in enumerate(zip(chunk,ims)):
            x=(k%3)*W;y=(k//3)*(H+16);sh.paste(im,(x,y+16));d.text((x+4,y+2),n,fill='red')
        sh.save(f'sheets/{inv}_s{si//per+1}.jpg',quality=82)
