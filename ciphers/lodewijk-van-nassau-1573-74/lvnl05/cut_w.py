# LVN-L05W: wider re-cut of LVN-L05's six crop pairs (same PREREG 7e90dde79). Each crop holds the token plus a neighbour each side
# (word crops with their neighbours); 5x Lanczos, grey; scratch only, no image in git. Usage: python3 lvnl05/cut_w.py SCRATCHDIR
import sys, json
from PIL import Image
S=sys.argv[1]
P='images/04610_p1.jpg'
L=lambda l:'images/04610_%s.jpg'%l
# crop: (file, box, tokens expected left->right as committed or '?', index of the scored token(s))
crops={
 'h_head':(P,(160,203,275,247)),   # head 81?,125? | 2      -> scored tokens 1-2
 'h_ctl':(P,(300,203,400,247)),    # 80 | 28 | a            -> scored token 2 (28)
 't80':(P,(272,203,372,247)),      # 8 | 80 | 28            -> scored token 2
 't80_ctl':(P,(250,203,335,247)),  # 2 | 8 | 80             -> scored token 2 (8)
 't25':(L('p2_L22'),(445,0,585,42)),     # 82 | 25 | 101   -> scored token 2
 't25_ctl':(L('p2_L22'),(405,0,535,42)), # 77 | 82 | 25    -> scored token 2 (82)
 't35':(L('p2_L30'),(140,0,255,45)),     # 61 | 35 | 31    -> scored token 2
 't35_ctl':(L('p2_L30'),(185,0,300,45)), # 35 | 31 | par.. -> scored token 2 (31)
 't141':(P,(155,1343,262,1395)),   # 141 | 123              -> scored token 1
 't141_ctl':(P,(395,1343,490,1395)), # de | 21 | 8.        -> scored token 2 (21)
 'tfut':(P,(345,172,485,214)),     # auoir | fut/este | tout -> scored token 2
 'tfut_ctl':(P,(380,172,515,214)), # fut/este | tout | 7   -> scored token 2 (tout)
}
json.dump({k:[v[0],v[1]] for k,v in crops.items()},open(S+'/crops_w.json','w'),indent=0)
import os; os.makedirs(S+'/w',exist_ok=True)
for k,(f,b) in crops.items():
    c=Image.open(f).crop(b).convert('L'); c=c.resize((c.width*5,c.height*5),Image.LANCZOS); c.save(f'{S}/w/{k}.png')
