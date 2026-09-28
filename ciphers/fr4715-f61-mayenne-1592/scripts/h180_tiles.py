#!/usr/bin/env python3
"""H180 (runner 6, 28 Sept 2026; pre-registered here and in scripts/H180_PROMPT.md before the call): which bracket form are fr.3984
f.176r's brackets? Anchors: H22's blind bracket sort (scripts/read_call_BR.tsv) -- group A (hairline diagonal, f.108, f/s under
Tomokiyo's letters) and group B (plain squared C, all f.61 brackets, l/y), cut from images/{f61,f108}sheetB_*.jpg by (segment, x_px);
segments found as the sheet's horizontal separator rows. Targets: the first 12 f.176r columns where both H177b passes read a bracket
(EBR_A/EBR_B), rows L13-L19, cut at pass A's x_px from the native crops (argv[1]). All tiles 180 px high, auto-contrast, shuffled
(seed 180); key scripts/h180_key.tsv.  python3 h180_tiles.py CROPDIR"""
import csv, difflib, random, sys
import numpy as np
from PIL import Image, ImageDraw, ImageOps
H = "ciphers/fr4715-f61-mayenne-1592"
def rd(p): return [r for r in csv.DictReader((l for l in open(p) if not l.startswith("#")), delimiter="\t")]
def segments(im):
    a = np.asarray(im.convert("L")); dark = (a < 40).mean(axis=1) > 0.9; bounds = []; y = 0; start = 0
    while y < len(dark):
        if dark[y]:
            if y - start > 20: bounds.append((start, y))
            while y < len(dark) and dark[y]: y += 1
            start = y
        else: y += 1
    if len(dark) - start > 20: bounds.append((start, len(dark)))
    return bounds
def anchors():
    out = []
    for r in rd(f"{H}/scripts/read_call_BR.tsv"):
        if r["group"] not in ("A", "B") or "uncertain" in (r["note"] or "").lower(): continue
        im = Image.open(f"{H}/images/{r['sheet']}.jpg").convert("L"); segs = segments(im); s = int(r["segment"])
        if s > len(segs): continue
        y0, y1 = segs[s - 1]; x = float(r["x_px"])
        out.append(((r["sheet"], r["segment"], r["x_px"], "anchor_" + r["group"]), im.crop((int(x) - 110, y0, int(x) + 110, y1))))
    return out
def targets(cropdir, n=12):
    A = rd(f"{H}/family/passes/f176r_signsA_L13-L19.tsv"); B = rd(f"{H}/family/passes/f176r_signsB_L13-L19.tsv"); out = []
    for line in sorted(set(r["line"] for r in A)):
        a = [r for r in A if r["line"] == line and r["sign"] != "PLAIN"]; b = [r for r in B if r["line"] == line and r["sign"] != "PLAIN"]
        sm = difflib.SequenceMatcher(None, [r["sign"] for r in a], [r["sign"] for r in b], autojunk=False)
        for op, i1, i2, j1, j2 in sm.get_opcodes():
            if op == "equal":
                for ra in a[i1:i2]:
                    if ra["sign"].startswith("EBR"): out.append((line, ra["segment"], float(ra["x_px"])))
    res = []
    for line, seg, x in out[:n]:
        im = Image.open(f"{cropdir}/f176_{line}_{seg}.jpg").convert("L")
        res.append(((line, seg, x, "f176"), im.crop((int(x) - 55, 0, int(x) + 55, im.size[1]))))
    return res
def main():
    tiles = anchors() + targets(sys.argv[1]); random.Random(180).shuffle(tiles); W = 6; cell = (250, 220)
    sheet = Image.new("L", (W * cell[0], ((len(tiles) + W - 1) // W) * cell[1]), 255); d = ImageDraw.Draw(sheet)
    with open(f"{H}/scripts/h180_key.tsv", "w") as f:
        f.write("# H180 key (never shown to the reader)\ntile\tsource\tsegment\tx\tkind\n")
        for n, (k, im) in enumerate(tiles, 1):
            im = ImageOps.autocontrast(im.resize((int(im.size[0] * 180 / im.size[1]), 180)), cutoff=2); im.thumbnail((cell[0] - 10, 180))
            X, Y = ((n - 1) % W) * cell[0], ((n - 1) // W) * cell[1]; sheet.paste(im, (X + 5, Y + 30)); d.text((X + 8, Y + 6), f"tile {n}", fill=0)
            f.write("\t".join(map(str, (n,) + tuple(k))) + "\n")
    sheet.save(f"{H}/images/h180/tiles.jpg", quality=90); print(len(tiles), "tiles")
if __name__ == "__main__": main()
