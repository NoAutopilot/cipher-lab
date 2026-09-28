"""B41: label-free superscript-tick detector. On the full frame (binarised at 128), connected components; for each
manuscript line (box from images/crops_<frame>/manifest.json, [x0,y0,x1,y1]) the band above the line's ink is
[top - ABOVE, top + INTO] where top = first row of the line's own main ink band (row ink >= 8 px inside the box). A
tick candidate = a component whose bbox lies inside that band, height <= 30, width <= 50, area 15..600 px, that does not
touch a large component (descenders of the line above are part of a big component and so excluded by size). Candidates
are placed over the line's B38 units (dots removed) by x. Known answer (ciphertext_ms.txt, ARM-S1): page 1 ticks on L07
"38" (second 38, group 7 of 11 in reading order incl. the two marks) and L08 "1640", "1276" (groups 6, 7 of 10); no other
page-1 line carries one. Then pages 2-3 (frame 0031, crops_0031L/R), where B35 pass A read eight A-marks on page2 L10,
page2 L13 and page3 L01 and pass B read none. Run: python3 ticks.py"""
import json, sys, numpy as np
from PIL import Image; from scipy import ndimage
sys.path.insert(0, "/home/user/cipher-lab/ciphers/armstrong-madison-1808/line-b/b38"); import gaps
ROOT = gaps.ROOT; ABOVE, INTO = 45, 12
def units_of(crop):
    runs, gs = gaps.runs_gaps(crop); U = [[runs[0]]]
    for r, g in zip(runs[1:], gs):
        if g > 30: U.append([r])
        else: U[-1].append(r)
    return [(u[0][0], u[-1][1]) for u in U]
def scan(frame, cropdir, prefix):
    Image.MAX_IMAGE_PIXELS = None
    im = np.asarray(Image.open(f"{ROOT}/images/{frame}.jpg").convert("L")) < 128
    lab, n = ndimage.label(im); objs = ndimage.find_objects(lab); areas = ndimage.sum(im, lab, range(1, n + 1))
    man = json.load(open(f"{ROOT}/images/{cropdir}/manifest.json"))["iiif_lines"]; out = {}
    for e in man:
        x0, y0, x1, y1 = e["box"]; name = e["crop"]
        sub = im[y0:y1, x0:x1]; prof = sub.sum(1); rows = np.where(prof >= 8)[0]
        if len(rows) == 0: continue
        top = y0 + rows[0]; band = (top - ABOVE, top + INTO)
        units = [(x0 + a, x0 + b) for a, b in units_of(f"{ROOT}/images/{cropdir}/{name}")]
        cands = []
        for i, sl in enumerate(objs):
            if sl is None: continue
            (r0, r1), (c0, c1) = (sl[0].start, sl[0].stop), (sl[1].start, sl[1].stop)
            if r0 >= band[0] and r1 <= band[1] and r1 - r0 <= 30 and c1 - c0 <= 50 and 15 <= areas[i] <= 600 and x0 <= c0 and c1 <= x1:
                cx = (c0 + c1) // 2; over = [k for k, (a, b) in enumerate(units) if a - 5 <= cx <= b + 5]
                cands.append((int(cx - x0), int(areas[i]), over[0] + 1 if over else None))
        out[name] = (len(units), cands)
    return out
if __name__ == "__main__":
    for frame, cropdir in (("M34-014-0030", "crops_0030"), ("M34-014-0031", "crops_0031L"), ("M34-014-0031", "crops_0031R")):
        print(f"== {frame} / {cropdir}: line: units | tick candidates as (x in crop, area, over unit)")
        for name, (nu, c) in scan(frame, cropdir, cropdir).items(): print(f"  {name}: {nu:2d} | {c}")
