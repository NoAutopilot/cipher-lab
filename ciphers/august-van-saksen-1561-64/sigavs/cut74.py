import json, numpy as np, random, os
from PIL import Image, ImageDraw
S='/tmp/claude-0/-home-user-cipher-lab/e4271a40-9fe4-5996-802c-3c19bf5bea68/scratchpad/'
A=Image.open(S+'pdf/00074-002.jpg').convert('L')
spec={
 'X_74_L10i6_Tq':(745,815,1510,1630),
 'T1_74_L10i1_T':(395,465,1510,1630),
 'T2_74_L9i8_T':(960,1035,1390,1520),
 'S1_74_L10i4_7':(570,632,1510,1630),
 'S2_74_L9i7_7':(870,930,1390,1520),
 'J_74_L11_J':(1375,1460,1680,1790),
}
os.makedirs(S+'signs74',exist_ok=True)
sheet=Image.new('L',(len(spec)*120,200),255); d=ImageDraw.Draw(sheet); boxes={}
for i,(k,(x0,x1,y0,y1)) in enumerate(spec.items()):
    c=A.crop((x0,y0,x1,y1)); a=np.asarray(c)<130; rows=np.where(a.sum(1)>0)[0]
    if len(rows): c=c.crop((0,max(0,rows[0]-12),c.width,min(c.height,rows[-1]+12)))
    c.save(S+'signs74/'+k+'.png'); boxes[k]=[x0,y0,x1,y1]
    sheet.paste(c,(i*120,30)); d.text((i*120,5),k[:3],fill=0)
sheet.save(S+'v_signs74.png'); json.dump(boxes,open(S+'signs74/boxes.json','w'))
keys=sorted(spec)
for r,seed in ((1,303),(2,404)):
    dd=S+f'read74_{r}'; os.makedirs(dd,exist_ok=True)
    rnd=random.Random(seed); ks=keys[:]; rnd.shuffle(ks); ids=rnd.sample(range(10,99),len(ks)); m={}
    for k,j in zip(ks,ids):
        im=Image.open(S+'signs74/'+k+'.png'); a=np.array(im); a[:, :7]=np.maximum(a[:, :7],200); a[:, -7:]=np.maximum(a[:, -7:],200)
        im=Image.fromarray(a); im.resize((im.width*2,im.height*2),Image.LANCZOS).save(f'{dd}/t{j}.png'); m[f't{j}']=k
    json.dump(m,open(S+f'key_read74_{r}.json','w'),indent=1)
