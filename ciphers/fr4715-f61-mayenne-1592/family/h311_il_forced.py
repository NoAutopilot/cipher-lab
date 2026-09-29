#!/usr/bin/env python3
"""H311 (runner 12 session_012eShPsWwW3quuzzUNV7nW5, 29 Sept 2026): H310's forced choice could not tell a doubled l from a clear 'Il' (both have two
tall strokes). This asks the question that decides L02's opening mark (read_call_U pass 1 LL / pass 2 'Il'): per tile, a fresh blind Opus reader
answers LEADIN (the LEFT tall stroke starts with a diagonal lead-in from the lower left, a capital I), UPRIGHT (the left stroke is an upright l-stroke
like the right one), NEITHER, or unclear. 13 tiles, ids Z01..Z13, seed 311: known LEADIN = f.61's clear 'Il' 2 (Il seroit L02 seg 3 x 890; Il a L04
seg 2 x 2065, as H302); known UPRIGHT = doubled l 5 (f.211r ville, elle, daumalle, Tellement at H309's positions; f.61 ella); NEITHER = PHI 2, C43 2;
targets = the L02 mark and LL (centroid-recentred; the runner has seen the L02 mark, never LL).
Gate, fixed before the call: >= 6 of the 7 LEADIN/UPRIGHT known answers correct AND 4/4 NEITHER, else CONTROL FAIL. Read-outs: the L02 mark 'reads as a
clear Il (pass 2)' iff LEADIN, 'reads as LL (pass 1)' iff UPRIGHT, else no read-out; LL's answer reported (UPRIGHT expected if LL is ll-shaped).
n = 1 each, flagged: for the verifier's recount only; no value, no count change.  python3 h311_il_forced.py tiles SCRATCH | score [--check]"""
import csv, os, random, sys
from math import comb
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); P = f"{HERE}/passes"; IM = f"{HERE}/../images"
# (kind, class, sheet file, band index 1-based, x)
ITEMS = [("LL", "LL", "f61sheetB_L05", 3, 1330), ("DISP", "L02-start", "f61sheetB_L02", 1, 425),
         ("LEADIN", "Il:Il seroit-L02", "f61sheetB_L02", 3, 890), ("LEADIN", "Il:Il a-L04", "f61sheetB_L04", 2, 2065),
         ("UPRIGHT", "ll:ville-211r", "f211r", 1790, 2995), ("UPRIGHT", "ll:elle-211r", "f211r", 1927, 2485), ("UPRIGHT", "ll:daumalle-211r", "f211r", 3730, 3430),
         ("UPRIGHT", "ll:Tellement-211r", "f211r", 3930, 1755), ("UPRIGHT", "ll:ella-f61", "f61sheetB_L07", 2, 1745),
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
    os.makedirs(f"{scratch}/h311", exist_ok=True)
    if "--place" in sys.argv:  # placement check of the TEXT tiles only (the runner may look at this sheet)
        its = [(k, crop(*k)) for k in ITEMS if k[0] in ("LEADIN", "UPRIGHT")]; sheet(its, f"{scratch}/h311/place_text.jpg", "P"); print(len(its), "text tiles"); return
    rng = random.Random(311); its = [(k, crop(*k)) for k in ITEMS]; rng.shuffle(its)
    sheet(its, f"{scratch}/h311/sheet_01.jpg", "Z")
    key = ["item\tkind\tclass\tsheet\tsegment\tx"] + [f"Z{n:02d}\t" + "\t".join(map(str, k)) for n, (k, _) in enumerate(its, 1)]
    open(f"{HERE}/h311_items.tsv", "w").write("\n".join(key) + "\n"); print(len(its), "tiles")
def rd(f): return [r for r in csv.DictReader((l for l in open(f) if not l.startswith("#")), delimiter="\t")]
def score():
    its = {r["item"]: r for r in rd(f"{HERE}/h311_items.tsv")}; a = {r["tile"].strip(): r["answer"].strip().upper() for r in rd(f"{P}/h311_forced.tsv")}
    want = {"LEADIN": "LEADIN", "UPRIGHT": "UPRIGHT", "CIPHER": "NEITHER"}; out = []
    for k in ("LEADIN", "UPRIGHT", "CIPHER"):
        ms = [m for m, r in its.items() if r["kind"] == k]
        out.append(f"{k} ({want[k]} expected): " + " ".join(f"{m}={a.get(m, '-')}" for m in ms) + f"; correct {sum(a.get(m) == want[k] for m in ms)}/{len(ms)}")
    kn = sum(a.get(m) == want[r["kind"]] for m, r in its.items() if r["kind"] in ("LEADIN", "UPRIGHT"))
    ne = sum(a.get(m) == "NEITHER" for m, r in its.items() if r["kind"] == "CIPHER")
    d = [a.get(m, "-") for m, r in its.items() if r["kind"] == "DISP"][0]; ll = [a.get(m, "-") for m, r in its.items() if r["kind"] == "LL"][0]
    if kn < 6 or ne < 4: out.append(f"gate: CONTROL FAIL (known {kn}/7, NEITHER {ne}/4); nothing read out")
    else:
        out.append(f"gate passes (known {kn}/7, NEITHER {ne}/4)")
        out.append("read-out: L02 mark = " + d + (" -- reads as a clear Il (pass 2)" if d == "LEADIN" else " -- reads as LL (pass 1)" if d == "UPRIGHT" else " -- no read-out") + f"; LL = {ll} (n = 1 each, flagged)")
    txt = "\n".join(out) + "\n"; res = f"{HERE}/h311_il_forced_result.txt"
    if "--check" in sys.argv:
        ok = os.path.exists(res) and open(res).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(res, "w").write(txt); print(txt, end="")
if __name__ == "__main__":
    tiles(sys.argv[2]) if sys.argv[1] == "tiles" else score()
