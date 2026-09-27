"""Number connected ink components for manuscript transcription review.

Numbers are image component locators, not assigned cipher identities.
Do not assume a connected component equals a cryptographic token.
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from scipy import ndimage
import numpy as np
import json
import sys

D=Path(__file__).resolve().parent
BASE=D.parent/'images'
OUT=D/'audit_images'
OUT.mkdir(exist_ok=True)
font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',16)

def annotate(path):
    im=Image.open(path).convert('RGB')
    arr=np.asarray(im.convert('L'))
    ink=arr<100
    labeled,n=ndimage.label(ink)
    boxes=[]
    for label,sl in enumerate(ndimage.find_objects(labeled),1):
        if sl is None:continue
        y,x=sl;area=(labeled[sl]==label).sum()
        if area<22 or x.stop-x.start<7 or y.stop-y.start<7:continue
        if x.start<4 or x.stop>im.width-4:continue
        boxes.append([x.start,y.start,x.stop,y.stop,int(area)])
    boxes.sort()
    # Join multi-stroke marks whose horizontal spans overlap substantially.
    merged=[]
    for b in boxes:
        if merged:
            a=merged[-1];overlap=min(a[2],b[2])-max(a[0],b[0])
            if overlap>0.6*min(a[2]-a[0],b[2]-b[0]):
                merged[-1]=[min(a[0],b[0]),min(a[1],b[1]),max(a[2],b[2]),max(a[3],b[3]),a[4]+b[4]]
                continue
        merged.append(b)
    canvas=Image.new('RGB',(im.width,im.height+48),'white');canvas.paste(im,(0,0));draw=ImageDraw.Draw(canvas)
    for i,b in enumerate(merged,1):
        draw.rectangle(b[:4],outline='#be2538',width=1)
        draw.text((b[0],im.height+(i%2)*21),str(i),fill='#003a98',font=font)
    dst=OUT/(path.stem+'.png');canvas.save(dst)
    (OUT/(path.stem+'.json')).write_text(json.dumps({'source':str(path.relative_to(D.parent)),
       'size':im.size,'boxes':dict((str(i),b) for i,b in enumerate(merged,1))},indent=2)+'\n')
    print(dst, len(merged))

for name in sys.argv[1:]:
    hits=list(BASE.glob('crops_*'+'/'+name+'.jpg'))
    assert len(hits)==1,(name,hits)
    annotate(hits[0])
