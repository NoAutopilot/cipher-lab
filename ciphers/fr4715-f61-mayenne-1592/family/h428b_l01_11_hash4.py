#!/usr/bin/env python3
"""H428b (runner 16 session_01Vtwc6CEJD2BSnYdzzY4f8W, 29 Sept 2026), written before the call: VERIFY-F61-V12's third hold, f.61 L01/11 (reader
code HASH4; V12's one read R15 4PI, against a panel with no HASH4 reference). An in-hand HASH4 reference now exists: f.108r L05 (f.61's hand),
where both independent passes C and D (scripts/pass108C/D_classes.tsv) read HASH4 at pos 9, 19 and 20, and on L07 at 5, 7, 13.
 references (fixed order; greyscale; marker UNDER):
   R1 HASH4 f.108r L05/19 (pass C x 2500 seg 2)   R2 4PI f.61 L11/9   R3 4STEM f.108r T1/2   R4 C43 L03/8   R5 PHI L01/5   R6 VBAR_A L03/6   R7 CROSS L07/10
   options: N none; O plain handwriting.
 items (shuffled, seed 4282): L01/11 at W1 -45/+92, W2 -60/+55, W3 -70/+110; check item L01/12 (reader code 4PI, the 4-over-Pi next to it; expected R2);
   known: f.108r HASH4 L05/9 and L07/5 (-> R1), f.108r 4STEM T1/7 (-> R3), C43 L05/9 L08/2 (-> R4), PHI L05/15 (-> R5), VBAR_A L05/3 (-> R6), CROSS L01/1 (-> R7) = 8.
 score -- GATE >= 7/8 known AND both f.108r HASH4 known -> R1. Pre-stated for L01/11: one answer at >= 2 of 3 windows; R1 -> 'HASH4 (reader code
   stands; V12's 4PI read not reproduced)'; R2 -> '4PI (V12's read reproduced; on L01 the 4PI is unread, so one two-way token leaves the band)'; else
   recorded / 'unclear'. L01/12 is reported beside it (if both L01/11 and L01/12 answer R2, say so: the two adjacent tiles may show one sign).
 A transcription read for a verifier; no corrections-file, key or grade change.  python3 h428b_l01_11_hash4.py tiles SCRATCH | score [--check]"""
import csv, os, random, sys
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); T = os.path.abspath(f"{HERE}/.."); P = f"{HERE}/passes"; IM = f"{T}/images"
CHECK = "--check" in sys.argv; sys.argv = sys.argv[:1] + [a for a in sys.argv[1:] if a != "--check"]; sys.path.insert(0, HERE)
import h420_108r_qa2 as f8, h411_class_qa as q, h428_v12_holds as h8
REFS = [("HASH4", "F108C", "L05", 19), ("4PI", "F61", "L11", "9"), ("4STEM", "F108", "L02", 2), ("C43", "F61", "L03", "8"), ("PHI", "F61", "L01", "5"),
        ("VBAR_A", "F61", "L03", "6"), ("CROSS", "F61", "L07", "10")]
CL = [r[0] for r in REFS]
KNOWN = [("HASH4", "F108C", "L05", 9), ("HASH4", "F108C", "L07", 5), ("4STEM", "F108", "L02", 7), ("C43", "F61", "L05", "9"), ("C43", "F61", "L08", "2"),
         ("PHI", "F61", "L05", "15"), ("VBAR_A", "F61", "L05", "3"), ("CROSS", "F61", "L01", "1")]
def tiles(scratch):
    from PIL import Image
    import h407_span_miss as h
    A, _, _ = f8.plan(); C = {}
    for r in q.rd(f"{T}/scripts/pass108C_classes.tsv"): C.setdefault(r["line"], []).append(r)
    G = q.geo(); im = Image.open(h.REG).convert("L").convert("RGB"); os.makedirs(f"{scratch}/h428b", exist_ok=True)
    def code(c, src, l, p): return A[l][p - 1]["sign"] if src == "F108" else C[l][p - 1]["sign"] if src == "F108C" else G[(l, p)][0]
    for r in REFS + KNOWN + [("HASH4", "F61", "L01", "11")]: assert code(*r) == r[0], (r, code(*r))
    def mk(c, src, l, p, up, dn, lab):
        if src == "F108": return f8.tile(A, l, p, 300, lab)
        if src == "F108C": return f8.tile(C, l, p, 300, lab)
        return h8.f61tile(im, G, l, p, up, dn, lab)
    f8.sheet([mk(*r, 45, 92, f"R{k}") for k, r in enumerate(REFS, 1)], f"{scratch}/h428b/references.jpg", 2)
    its = [(w, "", "F61", "L01", "11", up, dn) for w, up, dn in (("W1", 45, 92), ("W2", 60, 55), ("W3", 70, 110))] + [("C", "4PI", "F61", "L01", "12", 45, 92)] + [("K", c, s, l, p, 45, 92) for c, s, l, p in KNOWN]
    random.Random(4282).shuffle(its); key = ["item\tkind\tline\tpos\tref"]; ims = []
    for n, (kind, c, s, l, p, up, dn) in enumerate(its, 1):
        ims.append(mk(c, s, l, p, up, dn, f"I{n:02d}")); key.append(f"I{n:02d}\t{kind}\t{s}_{l}\t{p}\t{'R' + str(CL.index(c) + 1) if kind in ('K', 'C') else ''}")
    f8.sheet(ims, f"{scratch}/h428b/items_01.jpg", 3)
    open(f"{HERE}/h428b_items.tsv", "w").write("\n".join(key) + "\n"); print(len(its), "items")
def score():
    ans = {r["id"]: r["answer"].strip().upper() for r in q.rd(f"{P}/h428b_reply.tsv")}; it = q.rd(f"{HERE}/h428b_items.tsv")
    kn = [r for r in it if r["kind"] == "K"]; g = sum(ans.get(r["item"]) == r["ref"] for r in kn)
    hh = [ans.get(r["item"]) for r in kn if r["ref"] == "R1"]; c12 = [ans.get(r["item"]) for r in it if r["kind"] == "C"][0]
    out = [f"gate: {g}/8 known (>= 7); f.108r HASH4 known -> {hh} (both must be R1); check L01/12 (4PI) -> {c12}"]
    if g < 7 or hh != ["R1", "R1"]: out.append("CONTROL FAIL -- nothing scored")
    else:
        w = [ans.get(r["item"], "missing") for r in sorted((r for r in it if r["kind"].startswith("W")), key=lambda r: r["kind"])]
        top, n = Counter(w).most_common(1)[0]
        rdm = {"R1": "HASH4 (reader code stands; V12's 4PI read not reproduced)", "R2": "4PI (V12's read reproduced; L01's 4PI is unread, one two-way token leaves the band)"}
        ro = rdm.get(top, f"{top} ({CL[int(top[1:]) - 1] if top.startswith('R') else top})") if n >= 2 else "unclear"
        out.append(f"f.61 L01/11 W1-W3: {w} -> {ro}" + ("; NOTE L01/12 also R2: the adjacent tiles may show one sign" if top == "R2" and c12 == "R2" else ""))
    txt = "\n".join(out) + "\n"; p = f"{HERE}/h428b_l01_11_hash4_result.txt"
    if CHECK:
        ok = os.path.exists(p) and open(p).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(p, "w").write(txt); print(txt, end="")
if __name__ == "__main__":
    a = sys.argv[1:]
    tiles(a[1]) if a[0] == "tiles" else score()
