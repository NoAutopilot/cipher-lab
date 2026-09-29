#!/usr/bin/env python3
"""H428 (runner 16 session_01Vtwc6CEJD2BSnYdzzY4f8W, 29 Sept 2026), written before the call: VERIFY-F61-V12 held two out-of-span reads for one
more read each -- f.61 L11/8 (reader code 4STEM; V12's one read R14 CROSS, 'uncertain, could be a lone 4') and the mark that opens L02 before the PHI
(not in pass A; V12's C4 read it as the LL sign at 3 of 3). The L02 mark's centre is V12's own eye placement (verify_v12/v12_positions.tsv, L02 0,
x 144 y 215 on the native region image; disclosed, the runner did not place it); L11/8 is H410's geometry.
 references (fixed order; all tiles greyscale, marker UNDER the sign as the f.108r sheets draw it):
   R1 4STEM f.108r T1/2 (f.61's hand, overlay letter a)   R2 CROSS L07/10   R3 4PI L11/9   R4 C43 L03/8   R5 LL L05/16   R6 PHI L01/5   R7 VBAR_A L03/6
   options: N = none of the references; O = plain handwriting (a letter of the clear text), not a cipher sign.
 items (shuffled, seed 428): L11/8 and the L02 mark at W1 -45/+92, W2 -60/+55, W3 -70/+110; known items f.108r 4STEM T1/7 and T2/33 (-> R1),
   C43 L05/9 L08/2 (-> R4), PHI L05/15 L08/6 (-> R6), CROSS L01/1 (-> R2), VBAR_A L05/3 L11/6 (-> R7) = 9.
 score -- GATE >= 8/9 known AND both f.108r 4STEM -> R1 (else the in-hand 4STEM reference is not being seen and L11/8's answer means nothing).
   Pre-stated per target: one answer at >= 2 of 3 windows is the answer, else 'unclear'.
   L11/8: R1 -> '4STEM (the reader code stands; V12's CROSS read not reproduced)'; R2 -> 'CROSS (V12's read reproduced; a null class)'; other -> recorded.
   L02 mark: R5 -> 'LL (V12's C4 reproduced: a null, cipher count 100)'; O -> 'plain handwriting (not a cipher sign)'; other -> recorded.
 A transcription read for a verifier; no corrections-file, key or grade change.
 python3 h428_v12_holds.py tiles SCRATCH | score [--check]"""
import os, random, sys
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); P = f"{HERE}/passes"; CHECK = "--check" in sys.argv; sys.argv = sys.argv[:1] + [a for a in sys.argv[1:] if a != "--check"]
sys.path.insert(0, HERE)
import h420_108r_qa2 as f8, h411_class_qa as q
REFS = [("4STEM", "F108", "L02", 2), ("CROSS", "F61", "L07", "10"), ("4PI", "F61", "L11", "9"), ("C43", "F61", "L03", "8"), ("LL", "F61", "L05", "16"),
        ("PHI", "F61", "L01", "5"), ("VBAR_A", "F61", "L03", "6")]
CL = [r[0] for r in REFS]
KNOWN = [("4STEM", "F108", "L02", 7), ("4STEM", "F108", "L03", 33), ("C43", "F61", "L05", "9"), ("C43", "F61", "L08", "2"), ("PHI", "F61", "L05", "15"),
         ("PHI", "F61", "L08", "6"), ("CROSS", "F61", "L01", "1"), ("VBAR_A", "F61", "L05", "3"), ("VBAR_A", "F61", "L11", "6")]
EYE = {("L02", "0"): ("LL?", 144, 215)}   # VERIFY-F61-V12's placement
TARGETS = [("L11", "8"), ("L02", "0")]
def f61tile(im, G, l, p, up, dn, label):
    import h407_span_miss as h
    from PIL import ImageDraw
    c = h.strip(im, G[(l, p)][1], G[(l, p)][2], up, dn, label)
    d = ImageDraw.Draw(c); d.rectangle((0, 0, 369, 20), fill="white"); d.text((320, 4), label, fill=(0, 0, 0)); d.polygon([(176, 186), (194, 186), (185, 170)], fill=(220, 0, 0))
    return c
def tiles(scratch):
    from PIL import Image
    import h407_span_miss as h
    A, _, _ = f8.plan(); G = q.geo(); G.update(EYE); im = Image.open(h.REG).convert("L").convert("RGB"); os.makedirs(f"{scratch}/h428", exist_ok=True)
    for c, src, l, p in REFS + KNOWN:
        code = A[l][p - 1]["sign"] if src == "F108" else G[(l, p)][0]
        assert code == c, (c, src, l, p, code)
    mk = lambda c, src, l, p, up, dn, lab: f8.tile(A, l, p, 300, lab) if src == "F108" else f61tile(im, G, l, p, up, dn, lab)
    f8.sheet([mk(*r, 45, 92, f"R{k}") for k, r in enumerate(REFS, 1)], f"{scratch}/h428/references.jpg", 2)
    its = [(w, "", "F61", l, p, up, dn) for l, p in TARGETS for w, up, dn in (("W1", 45, 92), ("W2", 60, 55), ("W3", 70, 110))] + [("K", c, s, l, p, 45, 92) for c, s, l, p in KNOWN]
    random.Random(428).shuffle(its); key = ["item\tkind\tline\tpos\tref"]; ims = []
    for n, (kind, c, s, l, p, up, dn) in enumerate(its, 1):
        ims.append(mk(c, s, l, p, up, dn, f"I{n:02d}")); key.append(f"I{n:02d}\t{kind}\t{s}_{l}\t{p}\t{'R' + str(CL.index(c) + 1) if kind == 'K' else ''}")
    f8.sheet(ims, f"{scratch}/h428/items_01.jpg", 4)
    open(f"{HERE}/h428_items.tsv", "w").write("\n".join(key) + "\n"); print(len(its), "items")
def score():
    ans = {r["id"]: r["answer"].strip().upper() for r in q.rd(f"{P}/h428_reply.tsv")}; it = q.rd(f"{HERE}/h428_items.tsv")
    kn = [r for r in it if r["kind"] == "K"]; g = sum(ans.get(r["item"]) == r["ref"] for r in kn)
    st = [ans.get(r["item"]) for r in kn if r["line"].startswith("F108")]
    out = [f"gate: {g}/9 known (>= 8); f.108r 4STEM known -> {st} (both must be R1)"]
    if g < 8 or st != ["R1", "R1"]: out.append("CONTROL FAIL -- nothing scored")
    else:
        for l, p, rd in (("L11", "8", {"R1": "4STEM (the reader code stands; V12's CROSS read not reproduced)", "R2": "CROSS (V12's read reproduced; a null class)"}),
                         ("L02", "0", {"R5": "LL (V12's C4 reproduced: a null, cipher count 100)", "O": "plain handwriting (not a cipher sign)"})):
            w = [ans.get(r["item"], "missing") for r in sorted((r for r in it if r["kind"].startswith("W") and r["line"] == f"F61_{l}" and r["pos"] == p), key=lambda r: r["kind"])]
            top, n = Counter(w).most_common(1)[0]
            ro = (rd.get(top, f"{top} ({CL[int(top[1:]) - 1] if top.startswith('R') else top})") if n >= 2 else "unclear")
            out.append(f"f.61 {l}/{p} W1-W3: {w} -> {ro}")
    txt = "\n".join(out) + "\n"; p = f"{HERE}/h428_v12_holds_result.txt"
    if CHECK:
        ok = os.path.exists(p) and open(p).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(p, "w").write(txt); print(txt, end="")
if __name__ == "__main__":
    a = sys.argv[1:]
    tiles(a[1]) if a[0] == "tiles" else score()
