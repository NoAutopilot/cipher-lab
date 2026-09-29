#!/usr/bin/env python3
"""H421 (runner 15 session_01BDhspZ38TdrrXYSvLPTpjc, 29 Sept 2026), written before the call: is f.61's unassigned sign L02/2 (H414: none of 15 f.61
references) the sign f.108r's period overlay reads 'l' (T2 signs 3, 27) or 'm' (T2 sign 37), which matched none of nine f.108r references (H420)?
References (f.108r tiles, H418 format, marker UNDER): R1 T2/3 (l), R2 T2/37 (m), R3-R7 the H420 references for PHI, C43, VBAR_A, EBR, INF.
Items: f.61 L02/2 at W1 -45/+92, W2 -60/+55, W3 -70/+110 (H414's eye position), f.108r T2/27 (the second 'l'; must name R1), and known cross-leaf
items = f.61 PHI L01/5 L05/15, C43 L05/9 L08/2, VBAR_A L05/3 L11/6, EBR L07/5 L11/3, INF L05/10 L08/4 (f.61 tiles in H410's geometry). All f.61
tiles converted to greyscale (the f.108r sheets are greyscale). Shuffled (seed 421), I01..I14. Prompt: H418's.
score -- GATE >= 7/8 known AND (CHANGED before the call after the placement look: INF dropped from references and known items -- f.108r draws
   it as a crossed double loop, f.61 as an open lemniscate on a bar; references R3-R6 = PHI, C43, VBAR_A, EBR); T2/27 -> R1. Pre-stated: L02/2 R1 at >= 2 of 3 -> 'the f.108r l-sign (overlay l)'; R2 at >= 2 -> 'the f.108r m-sign
(overlay m)'; else 'unassigned'. A proposal for the verifier; no key, grade or class change.  python3 h421_l02_crossleaf.py tiles SCRATCH | score [--check]"""
import os, random, sys
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); P = f"{HERE}/passes"; CHECK = "--check" in sys.argv; sys.argv = sys.argv[:1] + [a for a in sys.argv[1:] if a != "--check"]
sys.path.insert(0, HERE)
import h420_108r_qa2 as f8, h411_class_qa as q, h414_other_two as o
REFS = [("l", "L03", 3), ("m", "L03", 37)]
KNOWN = [("PHI", "L01", "5"), ("PHI", "L05", "15"), ("C43", "L05", "9"), ("C43", "L08", "2"), ("VBAR_A", "L05", "3"), ("VBAR_A", "L11", "6"),
         ("EBR", "L07", "5"), ("EBR", "L11", "3")]   # INF dropped before the call: f.108r draws it crossed, f.61 open (placement look)
CL = ["l", "m", "PHI", "C43", "VBAR_A", "EBR"]
def tiles(scratch):
    from PIL import Image
    import h407_span_miss as h
    A, refs8, _ = f8.plan(); r8 = {c: (row, pos) for c, row, pos in refs8}
    refs = REFS + [(c, *r8[c]) for c in ("PHI", "C43", "VBAR_A", "EBR")]
    os.makedirs(f"{scratch}/h421", exist_ok=True)
    f8.sheet([f8.tile(A, row, pos, 300, f"R{k}") for k, (c, row, pos) in enumerate(refs, 1)], f"{scratch}/h421/references.jpg", 2)
    G = q.geo(); G.update(o.EYE); im = Image.open(h.REG).convert("L").convert("RGB")
    its = [(w, "L02", "2", up, dn, "") for w, up, dn in (("W1", 45, 92), ("W2", 60, 55), ("W3", 70, 110))] + [("C", "L03", 27, 0, 0, "R1")] + [("K", l, p, 45, 92, "R" + str(CL.index(c) + 1)) for c, l, p in KNOWN]
    random.Random(421).shuffle(its); key = ["item\tkind\tline\tpos\tref"]; ims = []
    for n, (kind, l, p, up, dn, ref) in enumerate(its, 1):
        if kind == "C": ims.append(f8.tile(A, l, p, 300, f"I{n:02d}"))
        else:
            c = h.strip(im, G[(l, p)][1], G[(l, p)][2], up, dn, f"I{n:02d}")
            from PIL import ImageDraw   # H418's format puts the marker UNDER the sign; redraw the f.61 tile's marker below its strip
            d = ImageDraw.Draw(c); d.rectangle((0, 0, 369, 20), fill="white"); d.text((320, 4), f"I{n:02d}", fill=(0, 0, 0)); d.polygon([(176, 186), (194, 186), (185, 170)], fill=(220, 0, 0))
            ims.append(c)
        key.append(f"I{n:02d}\t{kind}\t{l}\t{p}\t{ref}")
    f8.sheet(ims, f"{scratch}/h421/items_01.jpg", 4)
    open(f"{HERE}/h421_items.tsv", "w").write("\n".join(key) + "\n"); print(len(its), "items")
def score():
    ans = {r["id"]: r["answer"].strip().upper() for r in q.rd(f"{P}/h421_reply.tsv")}; it = q.rd(f"{HERE}/h421_items.tsv")
    g = sum(ans.get(r["item"]) == r["ref"] for r in it if r["kind"] == "K"); c = [ans.get(r["item"]) for r in it if r["kind"] == "C"][0]
    out = [f"gate: {g}/8 known cross-leaf (>= 7); f.108r T2/27 -> {c} (must be R1)"]
    if g < 7 or c != "R1": out.append("CONTROL FAIL -- nothing scored")
    else:
        w = [ans.get(r["item"], "missing") for r in sorted((r for r in it if r["kind"].startswith("W")), key=lambda r: r["kind"])]
        top, n = Counter(w).most_common(1)[0]
        ro = "the f.108r l-sign (overlay l)" if top == "R1" and n >= 2 else "the f.108r m-sign (overlay m)" if top == "R2" and n >= 2 else "unassigned"
        out.append(f"f.61 L02/2 W1-W3: {w} -> {ro}")
    txt = "\n".join(out) + "\n"; p = f"{HERE}/h421_l02_crossleaf_result.txt"
    if CHECK:
        ok = os.path.exists(p) and open(p).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(p, "w").write(txt); print(txt, end="")
if __name__ == "__main__":
    a = sys.argv[1:]
    tiles(a[1]) if a[0] == "tiles" else score()
