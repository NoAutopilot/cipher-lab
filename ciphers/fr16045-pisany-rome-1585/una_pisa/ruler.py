"""UNA-PISA locating aid (not evidence): a line strip with a tick per sign at the linearly predicted x across the ink
extent, labelled with the sign's position and transcription label, targets in a box. The worker reads it by eye and
records the x centre of each target and control token in una_pisa/tokens_pos.tsv. usage: ruler.py PAGE LINE OUT.png"""
import sys, numpy as np
from PIL import Image, ImageDraw
sys.path.insert(0, 'ciphers/fr16045-pisany-rome-1585/una_pisa')
from strips import strip, tokens
TGT = {'T45', 'T47', 'T57'}
def ruler(page, line, out):
    s = strip(page, line); a = np.array(s) < 140; col = a.sum(0)
    xs = np.where(col > 2)[0]; x0, x1 = xs.min(), xs.max()
    toks = tokens(page, line); n = len(toks)
    W, H = s.size; im = Image.new('RGB', (W, H + 60), 'white'); im.paste(s.convert('RGB'), (0, 0)); d = ImageDraw.Draw(im)
    for k, (pos, sg) in enumerate(toks):
        x = int(x0 + (k + 0.5) * (x1 - x0) / n)
        hot = sg in TGT
        d.line([(x, H), (x, H + 12)], fill='black', width=3 if hot else 1)
        d.text((x - 12, H + (14 if k % 2 == 0 else 34)), f'{pos}{"*" if hot else ""}', fill='black')
    for gx in range(0, W, 100):
        d.line([(gx, 0), (gx, 6)], fill='black'); d.text((gx + 2, 6), str(gx), fill='black')
    im.save(out)
if __name__ == '__main__':
    ruler(sys.argv[1], sys.argv[2], sys.argv[3])
