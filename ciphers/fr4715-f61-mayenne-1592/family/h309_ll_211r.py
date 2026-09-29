#!/usr/bin/env python3
"""H309 (runner 12 session_012eShPsWwW3quuzzUNV7nW5, 29 Sept 2026): H302's LL letterform sort with an ll-only control drawn from a clear page of
Mayenne's chancery, fr.3983 f.211r (Mayenne to de Diou, 1 Apr 1593; native fetched once, Gallica btv1b9059406b f362, scratch only, sha1 80c6c389
= MANIFEST; H308), because f.61 holds one clear doubled l only (H305). 16 tiles, ids Y01..Y16, seed 309:
  LL 1 (f.61 L05 16, sheet B L05 seg 3 x 1330) and the L02 opening mark 1 (DISP, descriptive only), both centroid-recentred, never seen by the runner
  (the L02 mark was seen whole on sheet B L02 in H302);
  doubled l 5 -- f.211r: ville (x 2995, y 1790), elle (2485, 1927), daumalle (3430, 3730), Tellement (1755, 3930); f.61: ella (sheet B L07 seg 2 x 1745);
  single l 5 -- f.211r: la (2715, 1815), le (2345, 3920); f.61: les, les (L02), le (L04) as H302;
  PHI 2 and C43 2 (H298's tiles).
  f.211r text tiles are native crops x +-100, y -120/+60 (letter size near f.61's sheet tiles), placed by the runner's eye on ruler strips of f.211r (text only).
Gates, fixed before the call: G = the group holding most doubled l's; gate 1 = all 5 doubled l's in G, f.211r's and f.61's together (else CONTROL FAIL;
if the doubled l's split by leaf, that is noted: the sort tracked the hand or leaf, not the letter); gate 2 = no single l in G (else NON-TEST).
Read-outs: 'LL has the clear ll letterform' iff LL in G and no cipher control in G; 'LL is a distinct glyph' iff LL outside G; else 'no read-out'.
DISP reported as in G / with LL / with a single l, descriptive. n = 1 on the LL side, flagged; a lead for the verifier's null-band wording, no value;
a merge cannot tell a clear 'll' left in a run from a null drawn as ll (H256's interpretation).
python3 h309_ll_211r.py tiles SCRATCH [--place] | score [--check]   (tiles needs SCRATCH/f211r_native.jpg)
Derived from h302_ll_text.py.
"""
import csv, os, random, sys
from math import comb
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); P = f"{HERE}/passes"; IM = f"{HERE}/../images"
# (kind, class, sheet file, band index 1-based, x)
ITEMS = [("LL", "LL", "f61sheetB_L05", 3, 1330), ("DISP", "L02-start", "f61sheetB_L02", 1, 425),
         ("TEXT_A", "ll:ville-211r", "f211r", 1790, 2995), ("TEXT_A", "ll:elle-211r", "f211r", 1927, 2485), ("TEXT_A", "ll:daumalle-211r", "f211r", 3730, 3430),
         ("TEXT_A", "ll:Tellement-211r", "f211r", 3930, 1755), ("TEXT_A", "ll:ella-f61", "f61sheetB_L07", 2, 1745),
         ("TEXT_X", "l:la-211r", "f211r", 1815, 2715), ("TEXT_X", "l:le-211r", "f211r", 3920, 2345),
         ("TEXT_X", "l:les-L02s2", "f61sheetB_L02", 2, 1065), ("TEXT_X", "l:les-L02s4", "f61sheetB_L02", 4, 1860), ("TEXT_X", "l:le-L04", "f61sheetB_L04", 3, 2230),
         ("CIPHER", "PHI", "f61sheet_L11", 1, 660), ("CIPHER", "PHI", "f61sheet_L08", 1, 450),
         ("CIPHER", "C43", "f61sheet_L03", 2, 2320), ("CIPHER", "C43", "f61sheet_L08", 1, 770)]
SCR = [None]
def bands(im):
    W, H = im.size; rows = [y for y in range(H) if sum(im.getpixel((x, y)) < 40 for x in range(0, W, 20)) > (W // 20) * 0.9]
    out, y0 = [], 0
    for y in rows + [H]:
        if y - y0 > 40: out.append((y0, y))
        y0 = y + 1
    return out
def crop(kind, cls, sheet, seg, x):
    from PIL import Image
    if sheet == "f211r":  # seg holds the native y here
        return Image.open(f"{SCR[0]}/f211r_native.jpg").convert("L").crop((x - 100, seg - 120, x + 100, seg + 60))
    im = Image.open(f"{IM}/{sheet}.jpg").convert("L"); a, b = bands(im)[seg - 1]
    if kind in ("LL", "DISP", "CIPHER"):  # re-centre on the ink centroid of the +-80 px window (no look)
        w = im.crop((x - 80, a + 10, x + 80, b - 6)); px = w.load(); sx = n = 0
        for yy in range(w.size[1]):
            for xx in range(w.size[0]):
                if px[xx, yy] < 110: sx += xx; n += 1
        if n: x = x - 80 + sx // n
    return im.crop((max(0, x - 150), a + 10, x + 150, b - 6))
def sheet(its, path, prefix):
    from PIL import Image, ImageDraw, ImageOps
    W, cw, ch = 5, 300, 240
    sh = Image.new("L", (W * cw, ((len(its) + W - 1) // W) * ch), 255); d = ImageDraw.Draw(sh)
    for n, (k, im) in enumerate(its, 1):
        im = ImageOps.autocontrast(im.resize((int(im.size[0] * 180 / im.size[1]), 180)), cutoff=2); im.thumbnail((cw - 10, 180))
        X, Y = ((n - 1) % W) * cw, ((n - 1) // W) * ch; sh.paste(im, (X + 5, Y + 28)); mx = X + 5 + im.size[0] // 2
        d.polygon([(mx - 8, Y + 8), (mx + 8, Y + 8), (mx, Y + 24)], fill=0); d.polygon([(mx - 8, Y + 228), (mx + 8, Y + 228), (mx, Y + 212)], fill=0)
        d.text((X + 8, Y + 4), f"{prefix}{n:02d}", fill=0)
    sh.convert("RGB").save(path, quality=90)
def tiles(scratch):
    SCR[0] = scratch
    os.makedirs(f"{scratch}/h309", exist_ok=True)
    if "--place" in sys.argv:  # placement check of the TEXT tiles only (the runner may look at this sheet)
        its = [(k, crop(*k)) for k in ITEMS if k[0].startswith("TEXT")]; sheet(its, f"{scratch}/h309/place_text.jpg", "P"); print(len(its), "text tiles"); return
    rng = random.Random(309); its = [(k, crop(*k)) for k in ITEMS]; rng.shuffle(its)
    sheet(its, f"{scratch}/h309/sheet_01.jpg", "Y")
    key = ["item\tkind\tclass\tsheet\tsegment\tx"] + [f"Y{n:02d}\t" + "\t".join(map(str, k)) for n, (k, _) in enumerate(its, 1)]
    open(f"{HERE}/h309_items.tsv", "w").write("\n".join(key) + "\n"); print(len(its), "tiles")
def rd(f): return [r for r in csv.DictReader((l for l in open(f) if not l.startswith("#")), delimiter="\t")]
def score():
    its = {r["item"]: r for r in rd(f"{HERE}/h309_items.tsv")}; g = {r["tile"].strip(): r["group"].strip() for r in rd(f"{P}/h309_sort.tsv")}
    of = lambda kind: [m for m, r in its.items() if r["kind"] == kind]
    ta, tx, ca, ci, dp = of("TEXT_A"), of("TEXT_X"), of("LL"), of("CIPHER"), of("DISP")
    groups = [x for x in dict.fromkeys(g.values()) if x.lower() != "unclear"]
    G = max(groups, key=lambda x: (sum(g.get(m) == x for m in ta), -groups.index(x)))
    n = lambda ms: sum(g.get(m) == G for m in ms); size = sum(v == G for v in g.values())
    out = ["by kind: " + "; ".join(f"{k}: " + " ".join(f"{x} {c}" for x, c in sorted(Counter(g.get(m, '-') for m in ms).items())) for k, ms in (("doubled l", ta), ("single l", tx), ("LL", ca), ("PHI/C43", ci), ("DISPUTED L02 start", dp))),
           f"G = {G} (size {size} of {len(its)}): doubled l {n(ta)}/{len(ta)}, single l {n(tx)}/{len(tx)}, LL {n(ca)}/{len(ca)}, cipher controls {n(ci)}/{len(ci)}"]
    if n(ta) < len(ta): out.append("gate 1: CONTROL FAIL (the doubled l's are not all in one group); nothing scored" + ("; the doubled l's split by leaf (f.211r vs f.61)" if len({g.get(m) for m in ta if '211r' in its[m]['class']}) == 1 and g.get([m for m in ta if 'f61' in its[m]['class']][0]) not in {g.get(m) for m in ta if '211r' in its[m]['class']} else ""))
    elif n(tx) >= 1: out.append("gate 2: NON-TEST (a single l sorts with the doubled l's: the sort tracked the tall ascender, not the doubling); nothing scored")
    else:
        k = n(ca); out.append(f"gates 1 and 2 pass; LL tile in G: {k}/1 (n = 1, flagged); cipher controls in G: {n(ci)}/4")
        out.append("read-out: " + ("LL has the clear ll letterform" if k == 1 and n(ci) == 0 else "LL is a distinct glyph" if k == 0 else "no read-out"))
    d = g.get(dp[0], "-"); ll = g.get(ca[0], "-"); sl = {g.get(m) for m in tx}
    out.append("DISPUTED (descriptive, no gate): group " + d + ("; in G" if d == G else "") + ("; with LL" if d == ll else "") + ("; with a single l" if d in sl else ""))
    txt = "\n".join(out) + "\n"; res = f"{HERE}/h309_ll_text_result.txt"
    if "--check" in sys.argv:
        ok = os.path.exists(res) and open(res).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(res, "w").write(txt); print(txt, end="")
if __name__ == "__main__":
    tiles(sys.argv[2]) if sys.argv[1] == "tiles" else score()
