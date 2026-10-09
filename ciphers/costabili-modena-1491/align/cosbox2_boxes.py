# COS-BOX2, 9 Oct 2026: PREREG-COS-SPAN step 2 box cutter. Boxes = runs between breaks (clear word or line end) on the R1163 P2 and R1165 P5 (levelled -2.4 deg) cipher slips;
# x breaks are thumbnail (1400 px wide) coordinates read by eye from the iiif_lines debug overlays; writes crops to SCRATCH/box (never committed) and boxes.tsv.
# Usage: python3 cosbox2_boxes.py SCRATCH  (SCRATCH/img holds the DECODE pages and p5_level.png)
import sys
from PIL import Image, ImageDraw
S=sys.argv[1]
segs={'c63':{1:[25,220,425,1340],2:[55,125,255,1345],3:[55,254,570,1345],4:[55,515,1300],5:[25,292,690,840,1395],6:[25,575,1345],7:[25,1345],8:[25,135,620,1310],9:[25,265,1365]},
      'c65':{5:[125,605,1240,1300],6:[115,565,780,1005,1250,1310],7:[110,955,1085,1350],8:[105,1345],9:[105,1278,1345],10:[115,342,890,1310]}}
cfg={'c63':(S+'/img/IMG_R1163_I5840_P2.png',(540,1530),1720/1400,[121,209,291,389,483,582,674,777,876],58),
     'c65':(S+'/img/p5_level.png',(0,0),2080/1400,[32,113,195,294,379,485,581,677,772,878,983],56)}
out=open(S+'/boxes.tsv','w'); out.write('box\tpage\tx0\ty0\tx1\ty1\n')
for slip,(img,(ox,oy),f,cent,h) in cfg.items():
    im=Image.open(img).convert('RGB'); dbg=im.copy(); d=ImageDraw.Draw(dbg)
    for L,xs in segs[slip].items():
        cy=oy+cent[L-1]
        for k in range(len(xs)-1):
            x0=int(ox+xs[k]*f); x1=int(ox+xs[k+1]*f); y0=cy-h; y1=cy+h
            name=f'{slip}_L{L:02d}_b{k+1}'
            im.crop((x0,y0,x1,y1)).save(f'{S}/box/{name}.jpg',quality=92)
            out.write(f'{name}\t{img.split("/")[-1]}\t{x0}\t{y0}\t{x1}\t{y1}\n')
            d.rectangle((x0,y0,x1,y1),outline=(0,90,255),width=3)
    x0=int(ox); y0=oy; dbg=dbg.crop((ox,oy,ox+int(1400*f),oy+cent[-1]+60)); dbg.thumbnail((1400,1400)); dbg.save(f'{S}/{slip}_boxdbg.jpg')
