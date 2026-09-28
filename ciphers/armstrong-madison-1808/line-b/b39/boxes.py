"""B39 step 1: cut unit boxes (B38's 30 px gap split) from (a) the seven pure-glyph crops and (b) the page-1 numeral-only
lines whose unit count equals the transcribed group count (L08, L14, L16: 10 each), labelling the numeral boxes with the
transcribed group value by order. Writes boxes.npz: 16x16 normalised images, source, label."""
import sys, json, numpy as np
from PIL import Image
sys.path.insert(0, "/home/user/cipher-lab/ciphers/armstrong-madison-1808/line-b/b38"); import gaps
ROOT = gaps.ROOT; THR = 30
def unit_boxes(path):
    im = np.asarray(Image.open(path).convert("L")) < 128
    runs, gs = gaps.runs_gaps(path); units = []; cur = [runs[0]]
    for r, g in zip(runs[1:], gs):
        if g > THR: units.append(cur); cur = [r]
        else: cur.append(r)
    units.append(cur); out = []
    for u in units:
        x0, x1 = u[0][0], u[-1][1]; sub = im[:, x0:x1]; rows = np.where(sub.sum(1) > 0)[0]
        if len(rows) == 0: continue
        sub = sub[rows[0]:rows[-1]+1]; h, w = sub.shape
        # v2 (control fix, see cluster_out_v1.txt): keep the aspect -- scale to height 16, width proportional, pad to 48
        nw = max(1, min(48, round(16 * w / h))); img = Image.fromarray((sub*255).astype(np.uint8)).resize((nw, 16), Image.BILINEAR)
        small = np.zeros((16, 48)); small[:, :nw] = np.asarray(img, float) / 255
        out.append((small, w, h))
    return out
X, src, lab, wh = [], [], [], []
for n in gaps.PURE:
    for small, w, h in unit_boxes(f"{ROOT}/images/shorthand/{n}.jpg"): X.append(small); src.append("glyph:" + n); lab.append(""); wh.append((w, h))
kA = gaps.items.__globals__  # noqa
tr = {l.split("\t")[0]: (l.rstrip("\n").split("\t")[1].split() if "\t" in l else []) for l in open(f"{ROOT}/tr/page1_passA.tsv")}
# v2: with period dots removed (b38/gaps.py v2) lines L14, L15, L16 give n+1 units for n groups, the first n units
# tracking the groups in order by width (L16: 66 91 115 60 139 137 54 28 129 144 px for 48 370 751 18 1540 1320 12 1
# 1170 1842); the trailing unit is a line-end mark. L08's unit widths do not track its groups in order and it is left out.
for L in ("L14", "L15", "L16"):
    b = unit_boxes(f"{ROOT}/images/crops_0030/f0030_{L}.jpg"); groups = [t for t in tr[L] if t.isdigit()]
    assert len(b) == len(groups) + 1, (L, len(b), len(groups))
    for (small, w, h), g in zip(b[:len(groups)], groups): X.append(small); src.append("numeral:" + L); lab.append(g); wh.append((w, h))
np.savez("boxes.npz", X=np.array(X), src=np.array(src), lab=np.array(lab), wh=np.array(wh))
print(f"{sum(s.startswith('glyph') for s in src)} glyph unit boxes, {sum(s.startswith('numeral') for s in src)} numeral group boxes; numeral labels:", [l for l in lab if l])
