#!/usr/bin/env python3
"""H302 (runner 12 session_012eShPsWwW3quuzzUNV7nW5, 29 Sept 2026): H256/H298's letterform sort on f.61's one LL sign (L05 16; sheet B L05 segment 3
x 1330 from H299's scripts/f61_positions_L05B.tsv, re-centred on its ink centroid by script, never seen by the runner) against the clear ll-type letters
of f.61's own words -- 'ella' (sheet B L07 seg 2), 'Il' of 'Il seroit' (sheet B L02 seg 3), 'Il' of 'Il a' (sheet B L04 seg 2); text tiles placed by
the runner on a placement sheet of the TEXT tiles only -- with three clear SINGLE l's as the hand check (les L02 seg 2, les L02 seg 4, le L04 seg 3: the
test is whether the sort separates a doubled ascender from a single one) and PHI 2 / C43 2 (H298's tiles) as cipher controls. One DISPUTED tile, scored
apart and never in a gate: L02's opening mark (sheet B L02 seg 1, centroid-recentred), which read_call_U pass 1 coded LL and pass 2 read as the
handwritten 'Il' (NOTES 'Unmarked lines', H40s). 12 tiles, ids W01..W12, seed 302.
Gates and read-outs, fixed before the call: G = the group holding most text ll-type tiles; gate 1 = all 3 text ll-type in G (else CONTROL FAIL);
gate 2 = no single l in G (else NON-TEST: the sort tracked 'tall ascender', not the doubling). Read-outs: 'LL has the clear ll/Il letterform' iff the
LL tile is in G and no cipher control is; 'LL is a distinct glyph' iff the LL tile is outside G; else 'no read-out'. DISPUTED: reported as 'in G' /
'with LL' / 'with the single l's' / other, descriptive only (which of pass 1 / pass 2 the letterform agrees with). n = 1 on the LL side, flagged: a
lead for the verifier's null-band wording, never a value; a merge cannot tell a clear 'll' left in the run from a null drawn as ll (H256's
interpretation). python3 h302_ll_text.py tiles SCRATCH [--place] | score [--check]
Derived from h298_ch_text.py.
"""
import csv, os, random, sys
from math import comb
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); P = f"{HERE}/passes"; IM = f"{HERE}/../images"
# (kind, class, sheet file, band index 1-based, x)
ITEMS = [("LL", "LL", "f61sheetB_L05", 3, 1330), ("DISP", "ll-or-Il:L02-start", "f61sheetB_L02", 1, 425),
         ("TEXT_A", "ll:ella-L07", "f61sheetB_L07", 2, 1745), ("TEXT_A", "Il:Il seroit-L02", "f61sheetB_L02", 3, 890), ("TEXT_A", "Il:Il a-L04", "f61sheetB_L04", 2, 2065),
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
    os.makedirs(f"{scratch}/h302", exist_ok=True)
    if "--place" in sys.argv:  # placement check of the TEXT tiles only (the runner may look at this sheet)
        its = [(k, crop(*k)) for k in ITEMS if k[0].startswith("TEXT")]; sheet(its, f"{scratch}/h302/place_text.jpg", "P"); print(len(its), "text tiles"); return
    rng = random.Random(302); its = [(k, crop(*k)) for k in ITEMS]; rng.shuffle(its)
    sheet(its, f"{scratch}/h302/sheet_01.jpg", "W")
    key = ["item\tkind\tclass\tsheet\tsegment\tx"] + [f"W{n:02d}\t" + "\t".join(map(str, k)) for n, (k, _) in enumerate(its, 1)]
    open(f"{HERE}/h302_items.tsv", "w").write("\n".join(key) + "\n"); print(len(its), "tiles")
def rd(f): return [r for r in csv.DictReader((l for l in open(f) if not l.startswith("#")), delimiter="\t")]
def score():
    its = {r["item"]: r for r in rd(f"{HERE}/h302_items.tsv")}; g = {r["tile"].strip(): r["group"].strip() for r in rd(f"{P}/h302_sort.tsv")}
    of = lambda kind: [m for m, r in its.items() if r["kind"] == kind]
    ta, tx, ca, ci, dp = of("TEXT_A"), of("TEXT_X"), of("LL"), of("CIPHER"), of("DISP")
    groups = [x for x in dict.fromkeys(g.values()) if x.lower() != "unclear"]
    G = max(groups, key=lambda x: (sum(g.get(m) == x for m in ta), -groups.index(x)))
    n = lambda ms: sum(g.get(m) == G for m in ms); size = sum(v == G for v in g.values())
    out = ["by kind: " + "; ".join(f"{k}: " + " ".join(f"{x} {c}" for x, c in sorted(Counter(g.get(m, '-') for m in ms).items())) for k, ms in (("text ll/Il", ta), ("text single l", tx), ("LL", ca), ("PHI/C43", ci), ("DISPUTED L02 start", dp))),
           f"G = {G} (size {size} of {len(its)}): text ll/Il {n(ta)}/{len(ta)}, text single l {n(tx)}/{len(tx)}, LL {n(ca)}/{len(ca)}, cipher controls {n(ci)}/{len(ci)}"]
    if n(ta) < len(ta): out.append("gate 1: CONTROL FAIL (the text ll/Il tiles are not all in one group); nothing scored")
    elif n(tx) >= 1: out.append("gate 2: NON-TEST (a single l sorts with the text ll/Il: the sort tracked the tall ascender, not the doubling); nothing scored")
    else:
        k = n(ca); out.append(f"gates 1 and 2 pass; LL tile in G: {k}/1 (n = 1, flagged); cipher controls in G: {n(ci)}/4")
        out.append("read-out: " + ("LL has the clear ll/Il letterform" if k == 1 and n(ci) == 0 else "LL is a distinct glyph" if k == 0 else "no read-out"))
    d = g.get(dp[0], "-"); ll = g.get(ca[0], "-"); sl = {g.get(m) for m in tx}
    out.append("DISPUTED (descriptive, no gate): group " + d + ("; in G" if d == G else "") + ("; with LL" if d == ll else "") + ("; with a single l" if d in sl else ""))
    txt = "\n".join(out) + "\n"; res = f"{HERE}/h302_ll_text_result.txt"
    if "--check" in sys.argv:
        ok = os.path.exists(res) and open(res).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(res, "w").write(txt); print(txt, end="")
if __name__ == "__main__":
    tiles(sys.argv[2]) if sys.argv[1] == "tiles" else score()
