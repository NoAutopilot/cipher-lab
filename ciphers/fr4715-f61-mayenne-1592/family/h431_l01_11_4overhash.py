#!/usr/bin/env python3
"""H431 (runner 16 session_01Vtwc6CEJD2BSnYdzzY4f8W, 29 Sept 2026), written before the call: H428b's hash reference was f.108r's looped hash, and
L01/11 matched none; its reader described a 4-topped hatched sign. Here the 4-over-hash in f.61's hand is on the panel: f.108v HASH4 tokens that
H162's gated blind read (controls 17/20) called 'four present' (scripts/f61hash4_forms_result.txt), tiles cut by f61hash4_forms.tile_from_crop.
 references (fixed order; greyscale; marker UNDER):
   R1 4-over-hash f.108v L03/6   R2 looped hash f.108r L05/19 (H428b's R1)   R3 4PI f.61 L11/9   R4 4STEM f.108r T1/2   R5 C43 L03/8   R6 PHI L01/5   R7 CROSS L07/10
   options: N none; O plain handwriting.
 items (shuffled, seed 431): L01/11 at W1 -45/+92, W2 -60/+55, W3 -70/+110; check L01/12 (-> R3); known: f.108v 4-over-hash L03/33, L05/34 (-> R1),
   f.108r looped hash L05/9 (-> R2), f.108r 4STEM T1/7 (-> R4), C43 L05/9 L08/2 (-> R5), PHI L05/15 (-> R6), CROSS L01/1 (-> R7) = 8.
 score -- GATE >= 7/8 known AND both 4-over-hash known -> R1. Pre-stated for L01/11: one answer at >= 2 of 3 windows; R1 -> 'the 4-over-hash
   (HASH4 d/q confirmed; V12's hold closed)'; R2 -> 'the looped hash (HASHLOOP, UNREAD in key v6+: one two-way token leaves the band)'; R3 -> '4PI';
   N -> 'still unmatched'. A transcription read for a verifier; no corrections-file, key or grade change.
 python3 h431_l01_11_4overhash.py tiles SCRATCH | score [--check]"""
import os, random, sys
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); T = os.path.abspath(f"{HERE}/.."); P = f"{HERE}/passes"
CHECK = "--check" in sys.argv; sys.argv = sys.argv[:1] + [a for a in sys.argv[1:] if a != "--check"]; sys.path.insert(0, HERE); sys.path.insert(0, f"{T}/scripts")
import h420_108r_qa2 as f8, h411_class_qa as q, h428_v12_holds as h8
REFS = [("4OH", "F108V", "L03", "6"), ("HASH4", "F108C", "L05", 19), ("4PI", "F61", "L11", "9"), ("4STEM", "F108", "L02", 2), ("C43", "F61", "L03", "8"),
        ("PHI", "F61", "L01", "5"), ("CROSS", "F61", "L07", "10")]
CL = [r[0] for r in REFS]
KNOWN = [("4OH", "F108V", "L03", "33"), ("4OH", "F108V", "L05", "34"), ("HASH4", "F108C", "L05", 9), ("4STEM", "F108", "L02", 7), ("C43", "F61", "L05", "9"),
         ("C43", "F61", "L08", "2"), ("PHI", "F61", "L05", "15"), ("CROSS", "F61", "L01", "1")]
def v108(line, pos, label):
    from PIL import Image, ImageDraw
    import f61hash4_forms as hf
    r = next(r for r in hf.rows(f"{hf.FAM}/passes/f108v3z_signsA.tsv") if r["line"] == line and r["pos"] == pos and r["sign"] == "HASH4")
    v = "3z" if r["line"] in ("L01", "L02") and r["segment"] == "s1" else "3y"
    t = hf.tile_from_crop(Image.open(f"{hf.FAM}/sheets/f108v{v}_{line}_{r['segment']}.jpg"), float(r["x_px"])).convert("L").convert("RGB")
    import numpy as np   # trim the uniform padding tile_from_crop adds past the sheet's edge (fixed before the call: the marker pointed at padding)
    a = np.asarray(t.convert("L"), float); keep = [i for i in range(a.shape[0]) if a[i].std() > 2.0]; t = t.crop((0, keep[0], t.width, keep[-1] + 1))
    s = min(165 / t.height, 360 / t.width); t = t.resize((int(t.width * s), int(t.height * s))); c = Image.new("RGB", (370, 190), "white"); x0 = 185 - t.width // 2; c.paste(t, (x0, 0))
    d = ImageDraw.Draw(c); d.polygon([(176, 186), (194, 186), (185, 170)], fill=(220, 0, 0)); d.text((6, 172), label, fill=(0, 0, 0)); return c
def tiles(scratch):
    from PIL import Image
    import h407_span_miss as h
    A, _, _ = f8.plan(); C = {}
    for r in q.rd(f"{T}/scripts/pass108C_classes.tsv"): C.setdefault(r["line"], []).append(r)
    G = q.geo(); im = Image.open(h.REG).convert("L").convert("RGB"); os.makedirs(f"{scratch}/h431", exist_ok=True)
    def mk(c, src, l, p, up, dn, lab):
        if src == "F108": assert A[l][p - 1]["sign"] == c; return f8.tile(A, l, p, 300, lab)
        if src == "F108C": assert C[l][p - 1]["sign"] == c; return f8.tile(C, l, p, 300, lab)
        if src == "F108V": return v108(l, p, lab)
        assert G[(l, p)][0] == c, (c, l, p); return h8.f61tile(im, G, l, p, up, dn, lab)
    f8.sheet([mk(*r, 45, 92, f"R{k}") for k, r in enumerate(REFS, 1)], f"{scratch}/h431/references.jpg", 2)
    its = [(w, "HASH4", "F61", "L01", "11", up, dn) for w, up, dn in (("W1", 45, 92), ("W2", 60, 55), ("W3", 70, 110))] + [("C", "4PI", "F61", "L01", "12", 45, 92)] + [("K", c, s, l, p, 45, 92) for c, s, l, p in KNOWN]
    random.Random(431).shuffle(its); key = ["item\tkind\tline\tpos\tref"]; ims = []
    for n, (kind, c, s, l, p, up, dn) in enumerate(its, 1):
        if kind.startswith("W") or kind == "C": ims.append(h8.f61tile(im, G, l, p, up, dn, f"I{n:02d}"))
        else: ims.append(mk(c, s, l, p, up, dn, f"I{n:02d}"))
        key.append(f"I{n:02d}\t{kind}\t{s}_{l}\t{p}\t{'R' + str(CL.index(c) + 1) if kind in ('K', 'C') else ''}")
    f8.sheet(ims, f"{scratch}/h431/items_01.jpg", 3)
    open(f"{HERE}/h431_items.tsv", "w").write("\n".join(key) + "\n"); print(len(its), "items")
def score():
    ans = {r["id"]: r["answer"].strip().upper() for r in q.rd(f"{P}/h431_reply.tsv")}; it = q.rd(f"{HERE}/h431_items.tsv")
    kn = [r for r in it if r["kind"] == "K"]; g = sum(ans.get(r["item"]) == r["ref"] for r in kn)
    oh = [ans.get(r["item"]) for r in kn if r["ref"] == "R1"]; c12 = [ans.get(r["item"]) for r in it if r["kind"] == "C"][0]
    out = [f"gate: {g}/8 known (>= 7); f.108v 4-over-hash known -> {oh} (both must be R1); check L01/12 (4PI) -> {c12}"]
    if g < 7 or oh != ["R1", "R1"]: out.append("CONTROL FAIL -- nothing scored")
    else:
        w = [ans.get(r["item"], "missing") for r in sorted((r for r in it if r["kind"].startswith("W")), key=lambda r: r["kind"])]
        top, n = Counter(w).most_common(1)[0]
        rdm = {"R1": "the 4-over-hash (HASH4 d/q confirmed; V12's hold closed)", "R2": "the looped hash (HASHLOOP, UNREAD in key v6+: one two-way token leaves the band)",
               "R3": "4PI", "N": "still unmatched"}
        out.append(f"f.61 L01/11 W1-W3: {w} -> " + (rdm.get(top, top) if n >= 2 else "unclear"))
    txt = "\n".join(out) + "\n"; p = f"{HERE}/h431_l01_11_4overhash_result.txt"
    if CHECK:
        ok = os.path.exists(p) and open(p).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(p, "w").write(txt); print(txt, end="")
if __name__ == "__main__":
    a = sys.argv[1:]
    tiles(a[1]) if a[0] == "tiles" else score()
