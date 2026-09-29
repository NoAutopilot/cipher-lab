#!/usr/bin/env python3
"""H298 (runner 10 session_0148wt8Aokh6aZEdJsXzYiZX, 29 Sept 2026): H256's letterform sort on f.61's one CH sign (L05 2; sheet B x 2140 from H297/H299,
re-centred on its ink centroid by script, never seen) against the clear h letters of f.61's own words -- only three are on the sheets (choses on
sheet B L05 and L01, mehi on the L07 span sheet; text tiles placed by the runner on a ruler sheet of the TEXT tiles only) -- with three clear non-h
ascender letters (l of les, C of Come, l of le; L04) as the hand check and PHI 2 / C43 2 as cipher controls: 11 tiles, ids V01..V11, seed 298.
Gates and read-outs, fixed before the call, adapted to n: gate 1 = all 3 text h's in one group G; gate 2 = no non-h letter in G (else NON-TEST: the sort
tracked ascenders or hand); read-out 'CH has the clear h's letterform' iff the CH tile is in G and no cipher control is; 'CH is a distinct glyph' iff
the CH tile is outside G; n = 1 on the CH side, flagged: a lead for the verifier's null-band wording, never a value.
Derived from h256_ca_text.py (its docstring follows).
H256 (runner 10 session_0148wt8Aokh6aZEdJsXzYiZX, 29 Sept 2026): is f.61's CA ('a'-shaped; Tomokiyo's nulls, H44; 10 of f.61's 25 unread) the
clear letter a (a transcription artefact) or a cipher sign of its own? H63 judged by hand cues (weight, baseline, spacing: cipher 5 / text 1 of 6);
this sorts by LETTERFORM alone in H235's format. Written before the call.
 tiles SCRATCH: 20 tiles -- f.61 CA 5 (H253's positions, scripts/f61_positions.tsv: L01 s2 1030, L03 s1 2330, L03 s3 800, L05 s1 1750, L05 s1 2010);
   clear-text a 6 (H63's control rows on the sheetB sheets: L01 auons/parle/amplement, L07 Cependant/ella, L08 affere; x checked by the runner on a
   placement sheet of the TEXT tiles only); clear-text non-a letters 3 (L01 sheetB: 'toutes' o, 'choses' o, 'et' e; placed by the runner's eye) as a
   HAND check; cipher controls PHI 3 and C43 3 (H253 positions). Sheet crops x +-150 by segment band, grey, autocontrast, height 180, triangles above
   and below the centre, ids T01..T20 shuffled (seed 256), one sheet <scratch>/h298/sheet_01.jpg; key h298_items.tsv. The runner does not look at
   the sheet or at the CA/PHI/C43 tiles (one CA, L01's, was seen in passing on sheetB_L01 while placing the text letters -- disclosed in PROMPTS.md).
 One blind Opus call: free sort of the centre marks into 2-5 groups by letterform (ignoring ink, size, hand and any connecting strokes to neighbours).
 score, pre-stated: G = the group holding most of the 6 text a's. Gates: (1) G holds >= 5 of 6 text a's, else CONTROL FAIL (the reader could not group
   the clear a's; nothing scored); (2) HAND CHECK: if >= 2 of the 3 text non-a letters fall in G, the sort tracked hand/ink, not letterform: NON-TEST.
   Read-outs when both gates pass (the row's own rule first): "CA is the clear letter a by letterform" iff >= 4 of 5 CA in G and <= 1 of the 6 cipher
   controls in G; "CA is a distinct glyph" iff <= 1 of 5 CA in G; else "no read-out". Interpretation fixed now: a merge is consistent with both a text
   letter and an a-shaped cipher sign (a null drawn as an a), so only the separation is decisive; hypergeometric p of the CA count in G reported.
 A read-out is for the verifier; no key edit, no reading.  python3 h298_ca_text.py tiles SCRATCH | score [--check]"""
import csv, os, random, sys
from math import comb
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); P = f"{HERE}/passes"; IM = f"{HERE}/../images"
# (kind, class, sheet file, band index 1-based, x)
ITEMS = [("CA", "CH", "f61sheetB_L05", 1, 2140),
         ("TEXT_A", "h:choses-L05", "f61sheetB_L05", 1, 485), ("TEXT_A", "h:choses-L01", "f61sheetB_L01", 3, 1000), ("TEXT_A", "h:mehi-L07", "f61sheet_L07", 1, 2340),
         ("TEXT_X", "l:les", "f61sheetB_L04", 4, 1750), ("TEXT_X", "C:Come", "f61sheetB_L04", 3, 1440), ("TEXT_X", "l:le", "f61sheetB_L04", 3, 2230),
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
    if kind in ("CA", "CIPHER"):  # re-centre on the ink centroid of the +-80 px window (no look)
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
    os.makedirs(f"{scratch}/h298", exist_ok=True)
    if "--place" in sys.argv:  # placement check of the TEXT tiles only (the runner may look at this sheet)
        its = [(k, crop(*k)) for k in ITEMS if k[0].startswith("TEXT")]; sheet(its, f"{scratch}/h298/place_text.jpg", "P"); print(len(its), "text tiles"); return
    rng = random.Random(298); its = [(k, crop(*k)) for k in ITEMS]; rng.shuffle(its)
    sheet(its, f"{scratch}/h298/sheet_01.jpg", "V")
    key = ["item\tkind\tclass\tsheet\tsegment\tx"] + [f"V{n:02d}\t" + "\t".join(map(str, k)) for n, (k, _) in enumerate(its, 1)]
    open(f"{HERE}/h298_items.tsv", "w").write("\n".join(key) + "\n"); print(len(its), "tiles")
def rd(f): return [r for r in csv.DictReader((l for l in open(f) if not l.startswith("#")), delimiter="\t")]
def score():
    its = {r["item"]: r for r in rd(f"{HERE}/h298_items.tsv")}; g = {r["tile"].strip(): r["group"].strip() for r in rd(f"{P}/h298_sort.tsv")}
    of = lambda kind: [m for m, r in its.items() if r["kind"] == kind]
    ta, tx, ca, ci = of("TEXT_A"), of("TEXT_X"), of("CA"), of("CIPHER")
    groups = [x for x in dict.fromkeys(g.values()) if x.lower() != "unclear"]
    G = max(groups, key=lambda x: (sum(g.get(m) == x for m in ta), -groups.index(x)))
    n = lambda ms: sum(g.get(m) == G for m in ms); size = sum(v == G for v in g.values())
    out = ["by kind: " + "; ".join(f"{k}: " + " ".join(f"{x} {c}" for x, c in sorted(Counter(g.get(m, '-') for m in ms).items())) for k, ms in (("text h", ta), ("text non-h", tx), ("CH", ca), ("PHI/C43", ci))),
           f"G = {G} (size {size} of {len(its)}): text h {n(ta)}/{len(ta)}, text non-h {n(tx)}/{len(tx)}, CH {n(ca)}/{len(ca)}, cipher controls {n(ci)}/{len(ci)}"]
    if n(ta) < len(ta): out.append("gate 1: CONTROL FAIL (the text h's are not all in one group); nothing scored")
    elif n(tx) >= 1: out.append("gate 2: NON-TEST (a non-h ascender letter sorts with the text h's: the sort tracked ascenders or hand); nothing scored")
    else:
        k = n(ca); out.append(f"gates 1 and 2 pass; CH tile in G: {k}/1 (n = 1, flagged); cipher controls in G: {n(ci)}/4")
        out.append("read-out: " + ("CH has the clear h's letterform" if k == 1 and n(ci) == 0 else "CH is a distinct glyph" if k == 0 else "no read-out"))
    txt = "\n".join(out) + "\n"; res = f"{HERE}/h298_ca_text_result.txt"
    if "--check" in sys.argv:
        ok = os.path.exists(res) and open(res).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(res, "w").write(txt); print(txt, end="")
if __name__ == "__main__":
    tiles(sys.argv[2]) if sys.argv[1] == "tiles" else score()
