import sys, json
from PIL import Image, ImageDraw
D='/home/user/cipher-lab/ciphers/sforza-italien1584-1447/duke/images/'
spec=json.load(open(sys.argv[1]))
tiles=[]
for k,(f,x0,x1) in spec.items():
    im=Image.open(D+f+'.jpg').convert('L'); h=im.size[1]
    t=im.crop((x0,0,x1,h)); t=t.resize((t.size[0]*3,h*3)); tiles.append((k,t))
W=sum(t.size[0]+20 for _,t in tiles); H=max(t.size[1] for _,t in tiles)+30
sheet=Image.new('L',(W,H),255); d=ImageDraw.Draw(sheet); x=0
for k,t in tiles:
    sheet.paste(t,(x,30)); d.text((x+2,5),k,fill=0); x+=t.size[0]+20
sheet.save(sys.argv[2])
