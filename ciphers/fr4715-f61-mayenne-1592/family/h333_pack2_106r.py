#!/usr/bin/env python3
"""H333 (runner 13 session_01MSoJWwZxNPSjQd4hszNdvQ, 29 Sept 2026), script-only: ASKS 99's person desk pack (images/person_pack_106r/, H243) extended
to f.106r rows 7-12 (H332's cut, sheets/f106r_b_bands.json with H334's re-cut boxes). Arrows mark every HASH4 that both H332 sign passes wrote at the
same reconciled position (passes/recf106r_c2/ciphertext_draft.tsv, why 'agree' or 'agree-flagged'); x from pass A when its sign at that position is
the same, else pass B (H325's rule). Numbering continues ASKS 99's N01-N17 (N18..), so one answer file covers both packs. Shape (looped vs 4-head)
was not read for rows 7-12: key.tsv says 'unshaped'. Same drawing as H243 (row band from 60 px above to the box bottom, x1.5, blue arrow under
the sign, number below). No reading.   python3 h333_pack2_106r.py [--check]"""
import csv, json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); P = f"{HERE}/passes"; OUT = f"{HERE}/images/person_pack_106r"
rd = lambda f: [r for r in csv.DictReader((l for l in open(f) if not l.startswith("#")), delimiter="\t")]
bj = json.load(open(f"{HERE}/sheets/f106r_b_bands.json")); B = dict(bj["boxes"]); B.update(bj.get("recut_h334", {}))
A = {(r["line"], r["pos"]): r for r in rd(f"{P}/f106r_signsA_c2.tsv")}; Bp = {(r["line"], r["pos"]): r for r in rd(f"{P}/f106r_signsB_c2.tsv")}
marks = []
for r in rd(f"{P}/recf106r_c2/ciphertext_draft.tsv"):
    if r["sign"] != "HASH4" or not r["why"].startswith("agree"): continue
    src = A.get((r["line"], r["position"]))
    if not src or src["sign"] != "HASH4": src = Bp.get((r["line"], r["position"]))
    if not src or src["sign"] != "HASH4": continue
    b = B[f"f106r_{r['line']}_{src['segment']}.jpg"]; marks.append((r["line"], r["position"], b[0] + int(float(src["x_px"])) // 3, src["segment"], r["why"]))
marks.sort(key=lambda m: (m[0], m[2])); key = []; n = 17
for m in marks: n += 1; key.append(f"N{n:02d}\t{m[0]}\t{m[1]}\tunshaped ({m[4]})")
ktxt = "\n".join(key) + "\n"
if "--check" in sys.argv:
    k = open(f"{OUT}/key.tsv").read(); ok = k.endswith(ktxt); print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
from PIL import Image, ImageDraw, ImageFont
try: F = ImageFont.load_default(size=26)
except TypeError: F = ImageFont.load_default()
nat = Image.open(f"{HERE}/images/3983_f106r.jpg").convert("RGB"); n = 17
for line in sorted({m[0] for m in marks}):
    bx = [v for k, v in B.items() if k.startswith(f"f106r_{line}_")]; x0 = min(b[0] for b in bx); x1 = max(b[2] for b in bx); y0 = min(b[1] for b in bx) - 60; y1 = max(b[3] for b in bx)
    s = 1.5; im = nat.crop((x0, y0, x1, y1)); im = im.resize((int(im.width * s), int(im.height * s))); c = Image.new("RGB", (im.width, im.height + 40), "white"); c.paste(im, (0, 0)); d = ImageDraw.Draw(c)
    for m in (m for m in marks if m[0] == line):
        n += 1; b = B[f"f106r_{line}_{m[3]}.jpg"]; x = int((m[2] - x0) * s); ys = int((b[1] + 78 - y0) * s)
        d.line([(x, ys + 25), (x, im.height + 4)], fill=(0, 0, 220), width=2); d.polygon([(x - 9, ys + 40), (x + 9, ys + 40), (x, ys + 24)], fill=(0, 0, 220))
        d.text((x - 16, im.height + 8), f"N{n:02d}", fill=(0, 0, 220), font=F)
    c.save(f"{OUT}/f106r_{line}.jpg", quality=82)
k = open(f"{OUT}/key.tsv").read().split("\nN18\t")[0].rstrip("\n") + "\n"; open(f"{OUT}/key.tsv", "w").write(k + ktxt)
print(len(marks), "numbered signs, N18 to", f"N{n:02d}")
