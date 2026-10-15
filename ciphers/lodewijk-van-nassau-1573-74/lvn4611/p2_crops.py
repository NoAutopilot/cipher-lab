"""LVN-4611P2 (15 Oct 2026): tight and context crops for the WVO 4611 p2 per-token read, cut from the deskewed physical line crops
(PREREG-LVN-4611.md addendum LVN-4611P2). blobmap rows: line position K<nn> run-spec, where run-spec is i or i+j (ink runs numbered by
p2_blobs.py, merged first to last) and an optional 'dx' shift as i:+20. Tight = the runs extended to 6 px short of the neighbouring runs (at most 45 px), 3x; context = +/- 130 px, 2x, blue wedge.
usage: python3 p2_crops.py LINES_DIR SEG_JSON BLOBMAP OUTDIR   (images to OUTDIR in scratch, never into git)"""
import sys, json, os
from PIL import Image, ImageDraw
d, segf, bm, out = sys.argv[1:5]
seg = json.load(open(segf)); os.makedirs(out, exist_ok=True); sheet = []
for l in open(bm):
    if not l.strip(): continue
    ln, pos, K, spec = l.split()[:4]
    ids = [int(x) - 1 for x in spec.split('+')]; S = seg[K]
    # extend to the neighbouring runs (a thin '1' stroke is often below the run filter), at most 45 px each side
    pe = S[ids[0] - 1][1] if ids[0] > 0 else S[ids[0]][0] - 45; ns = S[ids[-1] + 1][0] if ids[-1] + 1 < len(S) else S[ids[-1]][1] + 45
    a = max(pe + 6, S[ids[0]][0] - 45); b = min(ns - 6, S[ids[-1]][1] + 45)
    a = min(a, S[ids[0]][0] - 4); b = max(b, S[ids[-1]][1] + 4)
    im = Image.open(os.path.join(d, 'p2_L%s.jpg' % K[1:])).convert('L')
    a = max(0, a); b = min(im.width, b)
    t = im.crop((a, 0, b, im.height)); t = t.resize((t.width * 3, t.height * 3), Image.LANCZOS)
    c0 = max(0, a - 130); c = im.crop((c0, 0, min(im.width, b + 130), im.height)).convert('RGB'); c = c.resize((c.width * 2, c.height * 2), Image.LANCZOS)
    cc = Image.new('RGB', (c.width, c.height + 24), 'white'); cc.paste(c, (0, 24)); dr = ImageDraw.Draw(cc)
    L = (a - c0) * 2; R = (b - c0) * 2; dr.polygon([(L, 2), (R, 2), ((L + R) // 2, 20)], fill=(0, 90, 200))
    t.save(f'{out}/tok_{ln}_{pos}_tight.jpg', quality=92); cc.save(f'{out}/tok_{ln}_{pos}_ctx.jpg', quality=92); sheet.append((ln, pos, t))
W = 280; cols = 5; ims = [(ln, pos, t.resize((min(W, t.width * 120 // t.height), 120))) for ln, pos, t in sheet]
rows = (len(ims) + cols - 1) // cols; o = Image.new('RGB', (cols * W, rows * 140), 'white'); dr = ImageDraw.Draw(o)
for k, (ln, pos, t) in enumerate(ims):
    x = (k % cols) * W; y = (k // cols) * 140; dr.text((x + 2, y), f'{ln[3:]}/{pos}', fill=(0, 120, 0)); o.paste(t, (x, y + 14))
o.save(out + '/sheet.jpg', quality=80); print(len(sheet), o.size)
