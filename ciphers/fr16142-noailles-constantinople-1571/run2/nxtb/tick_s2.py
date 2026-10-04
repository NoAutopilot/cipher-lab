"""Mark the end of the 100 px overlap on every _s2 crop with corner ticks at x=100 (top and bottom), as NX-RECUT did."""
import glob
from PIL import Image, ImageDraw
for f in sorted(glob.glob('crops/*_s2.jpg')):
    im = Image.open(f).convert('L'); d = ImageDraw.Draw(im); h = im.height
    d.rectangle([98, 0, 102, 14], fill=0); d.rectangle([98, h - 15, 102, h - 1], fill=0)
    im.save(f, quality=90)
