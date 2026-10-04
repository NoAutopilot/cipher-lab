# Draw the overlap split (middle of the 150 px s1/s2 overlap) as a thin red line: s1 at x=1825, s2 at x=75.
import glob, sys
from PIL import Image, ImageDraw
d = sys.argv[1]
for f in glob.glob(d + '/c51?_L[0-9][0-9]_s[12].jpg'):
    if f.endswith('L00_s1.jpg'): continue
    im = Image.open(f).convert('RGB'); dr = ImageDraw.Draw(im)
    x = 1825 if f.endswith('_s1.jpg') else 75
    dr.line([(x, 0), (x, im.height)], fill=(255, 0, 0), width=3)
    im.save(f, quality=92)
