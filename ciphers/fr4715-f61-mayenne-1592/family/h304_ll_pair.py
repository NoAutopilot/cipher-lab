#!/usr/bin/env python3
"""H304 (runner 12 session_012eShPsWwW3quuzzUNV7nW5, 29 Sept 2026): is L02's opening mark (sheet B L02 seg 1 x 425; read_call_U pass 1 LL, pass 2 the
handwritten 'Il') the LL sign? H302 grouped it with f.61's LL (L05 16) by letterform, apart from the clear 'Il's -- descriptive, in no gate. Here the
capital-I control is explicit: 12 tiles, ids X01..X12, seed 304 -- LL 1 (sheet B L05 seg 3 x 1330) and the L02 mark 1 (both centroid-recentred; the
runner saw the L02 mark whole on sheet B L02, never the LL); clear capital I 3, centred on the I (Il of 'Il seroit' L02 seg 3, Il of 'Il a' L04 seg 2,
Impor[tances] L02 seg 2); clear single l 3 (les, les L02; le L04, as H302); PHI 2 and C43 2 (H298's tiles).
Gates, fixed before the call: GI = the group holding most clear I's, Gl = the group holding most single l's; gate = all 3 I's in GI, all 3 l's in Gl,
GI != Gl (else CONTROL FAIL, nothing scored). Read-outs: 'the L02 mark is the LL sign' iff the L02 mark and LL share one group that holds no clear I, no
single l and no cipher control; 'the L02 mark is a clear capital I (pass 2)' iff the L02 mark is in GI; else 'no read-out'. n = 2 on the LL side,
flagged: a lead for a verifier's recount of the null band's LL row, never a runner's recount, no value.
python3 h304_ll_pair.py tiles SCRATCH [--place] | score [--check]
Derived from h302_ll_text.py.
"""
import csv, os, random, sys
from math import comb
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); P = f"{HERE}/passes"; IM = f"{HERE}/../images"
# (kind, class, sheet file, band index 1-based, x)
ITEMS = [("LL", "LL", "f61sheetB_L05", 3, 1330), ("DISP", "L02-start", "f61sheetB_L02", 1, 425),
         ("TEXT_A", "I:Il seroit-L02", "f61sheetB_L02", 3, 810), ("TEXT_A", "I:Il a-L04", "f61sheetB_L04", 2, 2000), ("TEXT_A", "I:Impor-L02", "f61sheetB_L02", 2, 1835),
         ("TEXT_X", "l:les-L02s2", "f61sheetB_L02", 2, 1065), ("TEXT_X", "l:les-L02s4", "f61sheetB_L02", 4, 1860), ("TEXT_X", "l:le-L04", "f61sheetB_L04", 3, 2230),
         ("CIPHER", "PHI", "f61sheet_L11", 1, 660), ("CIPHER", "PHI", "f61sheet_L08", 1, 450),
         ("CIPHER", "C43", "f61sheet_L03", 2, 2320), ("CIPHER", "C43", "f61sheet_L08", 1, 770)]
def bands(im):
    W, H = im.size; rows = [y for y in range(H) if sum(im.getpixel((x, y)) < 40 for x in range(0, W, 20)) > (W // 20) * 0.9]
    out, y0 = [], 0
    for y in rows + [H]:
        if y - y0 > 40: out.append((y0, y))
        y0 = y + 1
    return out
def crop(kind, cls, sheet, seg, x):
    from PIL import Image
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
    os.makedirs(f"{scratch}/h304", exist_ok=True)
    if "--place" in sys.argv:  # placement check of the TEXT tiles only (the runner may look at this sheet)
        its = [(k, crop(*k)) for k in ITEMS if k[0].startswith("TEXT")]; sheet(its, f"{scratch}/h304/place_text.jpg", "P"); print(len(its), "text tiles"); return
    rng = random.Random(304); its = [(k, crop(*k)) for k in ITEMS]; rng.shuffle(its)
    sheet(its, f"{scratch}/h304/sheet_01.jpg", "X")
    key = ["item\tkind\tclass\tsheet\tsegment\tx"] + [f"X{n:02d}\t" + "\t".join(map(str, k)) for n, (k, _) in enumerate(its, 1)]
    open(f"{HERE}/h304_items.tsv", "w").write("\n".join(key) + "\n"); print(len(its), "tiles")
def rd(f): return [r for r in csv.DictReader((l for l in open(f) if not l.startswith("#")), delimiter="\t")]
def score():
    its = {r["item"]: r for r in rd(f"{HERE}/h304_items.tsv")}; g = {r["tile"].strip(): r["group"].strip() for r in rd(f"{P}/h304_sort.tsv")}
    of = lambda kind: [m for m, r in its.items() if r["kind"] == kind]
    ta, tx, ca, ci, dp = of("TEXT_A"), of("TEXT_X"), of("LL"), of("CIPHER"), of("DISP")
    groups = [x for x in dict.fromkeys(g.values()) if x.lower() != "unclear"]
    most = lambda ms: max(groups, key=lambda x: (sum(g.get(m) == x for m in ms), -groups.index(x)))
    GI, Gl = most(ta), most(tx); c = lambda ms, G: sum(g.get(m) == G for m in ms)
    out = ["by kind: " + "; ".join(f"{k}: " + " ".join(f"{x} {c_}" for x, c_ in sorted(Counter(g.get(m, '-') for m in ms).items())) for k, ms in (("clear I", ta), ("single l", tx), ("LL", ca), ("L02 mark", dp), ("PHI/C43", ci))),
           f"GI = {GI}: clear I {c(ta, GI)}/3; Gl = {Gl}: single l {c(tx, Gl)}/3"]
    if c(ta, GI) < 3 or c(tx, Gl) < 3 or GI == Gl: out.append("gate: CONTROL FAIL (clear I's or single l's not each in one group of their own); nothing scored")
    else:
        d, ll = g.get(dp[0], "-"), g.get(ca[0], "-"); out.append(f"gate passes; L02 mark in {d}, LL in {ll}")
        clean = d == ll and d.lower() != "unclear" and d not in (GI, Gl) and c(ci, d) == 0
        out.append("read-out: " + ("the L02 mark is the LL sign" if clean else "the L02 mark is a clear capital I (pass 2)" if d == GI else "no read-out") + " (n = 2, flagged)")
    txt = "\n".join(out) + "\n"; res = f"{HERE}/h304_ll_pair_result.txt"
    if "--check" in sys.argv:
        ok = os.path.exists(res) and open(res).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(res, "w").write(txt); print(txt, end="")
if __name__ == "__main__":
    tiles(sys.argv[2]) if sys.argv[1] == "tiles" else score()
