import sys
from PIL import Image
S=sys.argv[1]
P='images/04610_p1.jpg'
L=lambda l:'images/04610_%s.jpg'%l
crops={
 'h_head':(P,(172,205,251,245)),'h_ctl':(P,(352,205,390,245)),
 't80':(P,(308,205,350,245)),'t80_ctl':(P,(280,205,303,245)),
 't25':(L('p2_L22'),(500,0,545,37)),'t25_ctl':(L('p2_L22'),(450,0,492,37)),
 't35':(L('p2_L30'),(176,0,222,37)),'t35_ctl':(L('p2_L30'),(218,0,255,37)),
 't141':(P,(165,1345,215,1390)),'t141_ctl':(P,(444,1345,484,1390)),
 'tfut':(P,(388,175,437,215)),'tfut_ctl':(P,(437,175,482,215)),
}
import json
json.dump({k:[v[0],v[1]] for k,v in crops.items()},open(S+'/crops.json','w'),indent=0)
for k,(f,b) in crops.items():
    c=Image.open(f).crop(b).convert('L'); c=c.resize((c.width*5,c.height*5),Image.LANCZOS); c.save(f'{S}/l05/{k}.png')
# contact sheet
ims=[Image.open(f'{S}/l05/{k}.png') for k in crops]
W=sum(i.width for i in ims)+10*len(ims); H=max(i.height for i in ims)
sh=Image.new('L',(W,H),255); x=0
for i in ims: sh.paste(i,(x,0)); x+=i.width+10
sh.save(S+'/l05/sheet.png')
