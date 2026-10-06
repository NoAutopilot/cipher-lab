#!/usr/bin/env python3
"""R12D-GRA: list the z/zb and d/n6 split slots of n9gra4/recon.tsv (same opcodes as n9gra4/split_slots.py) with their
half-line crop and estimated x (token index / tokens in that half, pass A), and cut a per-slot window crop with a tick
mark over the estimated position. Writes n12gra/slots.tsv and images/fr3040_f18/slots/S<nn>.jpg."""
import difflib, sys
from pathlib import Path
from PIL import Image, ImageDraw
HERE = Path(__file__).resolve().parent; G = HERE.parent
ns = {}; exec(compile((G / "n9gra4/reconcile.py").read_text().split("A = load")[0], "rec", "exec"), ns)
A = ns["load"]([str(G / "n9gra4/passA.tsv")]); B = ns["load"]([str(G / "n9gra4/passB.tsv")])
WANT = {frozenset(("z", "zb")), frozenset(("d", "n6"))}
D = G / "images/fr3040_f18"; O = D / "slots"; O.mkdir(exist_ok=True)
rows = ["slot\tline\trecon_idx\tpassA\tpassB\thalf\tidx_in_half\tn_half\tx_est"]; k = 0
for ln in sorted({r[:-2] for r in A}):
    na = len(A[ln + "_a"]); a = A[ln + "_a"] + A[ln + "_b"]; b = B[ln + "_a"] + B[ln + "_b"]; pos = 0
    for op, a0, a1, b0, b1 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
        if op == "replace" and a1 - a0 == b1 - b0:
            for j, (x, y) in enumerate(zip(a[a0:a1], b[b0:b1])):
                if frozenset((x, y)) in WANT:
                    i = a0 + j; h = "a" if i < na else "b"; ih = i if h == "a" else i - na
                    nh = na if h == "a" else len(a) - na
                    im = Image.open(D / f"{ln}_{h}.jpg").convert("RGB"); w, H = im.size
                    xe = int((ih + 0.5) / nh * w); tw = w / nh
                    x0 = max(0, int(xe - 2.5 * tw)); x1 = min(w, int(xe + 2.5 * tw))
                    c = im.crop((x0, 0, x1, H)); c = c.resize((c.width * 2, H * 2))
                    dr = ImageDraw.Draw(c); xm = (xe - x0) * 2; dr.polygon([(xm - 8, 0), (xm + 8, 0), (xm, 14)], fill=(255, 0, 0))
                    k += 1; c.save(O / f"S{k:02d}.jpg", quality=90)
                    rows.append(f"S{k:02d}\t{ln}\t{pos + j}\t{x}\t{y}\t{h}\t{ih}\t{nh}\t{xe}")
        pos += max(a1 - a0, b1 - b0)
(HERE / "slots.tsv").write_text("\n".join(rows) + "\n"); print(k, "slots")
