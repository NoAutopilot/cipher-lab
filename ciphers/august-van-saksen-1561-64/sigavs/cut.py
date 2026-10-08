import json, numpy as np
from PIL import Image, ImageDraw
S='/tmp/claude-0/-home-user-cipher-lab/e4271a40-9fe4-5996-802c-3c19bf5bea68/scratchpad/'
A=Image.open(S+'pdf/00126-003.jpg').convert('L'); B=Image.open(S+'pdf/00098-001.jpg').convert('L')
spec={
 'T_126_L1p20_Qf':(A,2005,2080,350,500),
 'P1_126_L5p6_Pf':(A,935,990,1132,1345),
 'P2_126_L8p6_Pf':(A,985,1035,1767,1950),
 'D1_126_L3p4_Dp':(A,885,975,698,922),
 'D2_126_L7p1_Dp':(A,590,655,1550,1767),
 'G_126_L5p9_Qg':(A,1160,1235,1132,1345),
 'N_126_L5p7_9':(A,990,1060,1132,1345),
 'FQ_f66_L5i15_Qf':(B,1795,1870,1280,1470),
 'FP1_f66_L3i2_Pf':(B,648,700,880,1080),
 'FP2_f66_L2i13_Pf':(B,1625,1675,700,890),
 'FD_f66_L2i26_Dp':(B,2825,2900,700,890),
}
out={}
sheet=Image.new('L',(len(spec)*130,300),255); d=ImageDraw.Draw(sheet)
for i,(k,(im,x0,x1,y0,y1)) in enumerate(spec.items()):
    c=im.crop((x0-10,y0,x1+10,y1)); a=np.asarray(c)<130
    rows=np.where(a.sum(1)>0)[0]
    if len(rows): c=c.crop((0,max(0,rows[0]-12),c.width,min(c.height,rows[-1]+12)))
    c.save(S+'signs/'+k+'.png'); out[k]=[x0-10,y0,x1+10,y1]
    sheet.paste(c.resize((c.width,min(c.height,260))) if c.height>260 else c,(i*130,30)); d.text((i*130,5),k[:3],fill=0)
sheet.save(S+'v_signs.png'); json.dump(out,open(S+'signs/boxes.json','w'),indent=1)
