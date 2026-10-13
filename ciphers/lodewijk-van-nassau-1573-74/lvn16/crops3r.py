import sys
from PIL import Image, ImageDraw
SP=sys.argv[1]
rows=[l.split('\t') for l in open(SP+'/scr/tok.tsv').read().split('\n') if l]
sheet=[]
for ln,pos,cx,hw in rows:
    i=int(ln[-2:])-4; im=Image.open(f'{SP}/lvn/crops/04616_p1_L{i:02d}.jpg').convert('L')
    cx=int(cx);hw=int(hw)
    t=im.crop((max(0,cx-hw),0,min(im.width,cx+hw),im.height)); t=t.resize((t.width*3,t.height*3),Image.LANCZOS)
    c=im.crop((max(0,cx-hw-130),0,min(im.width,cx+hw+130),im.height)).convert('RGB')
    c=c.resize((c.width*2,c.height*2),Image.LANCZOS)
    cc=Image.new('RGB',(c.width,c.height+24),'white'); cc.paste(c,(0,24)); d=ImageDraw.Draw(cc)
    L=(cx-hw-max(0,cx-hw-130))*2; R=L+2*hw*2
    d.polygon([(L,2),(R,2),((L+R)//2,20)],fill=(0,90,200))
    sheet.append((ln,pos,t,cc))
    t.save(f'{SP}/lvn/tok_{ln}_{pos}_tight.jpg',quality=92); cc.save(f'{SP}/lvn/tok_{ln}_{pos}_ctx.jpg',quality=92)
# contact sheet of context crops for my eye check
W=900; H=sum(min(W,c.width)*0+ (c.height*W//c.width if c.width>W else c.height)+16 for *_,c in sheet)
out=Image.new('RGB',(W,H),'white'); d=ImageDraw.Draw(out); y=0
for ln,pos,t,c in sheet:
    if c.width>W: c=c.resize((W,c.height*W//c.width))
    d.text((2,y+2),f'{ln}/{pos}',fill=(200,0,0)); out.paste(c,(0,y+14)); y+=c.height+16
out.save(SP+'/lvn/sheet.jpg',quality=80); print(out.size)
