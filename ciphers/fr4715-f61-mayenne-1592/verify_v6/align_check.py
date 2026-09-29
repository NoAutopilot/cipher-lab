#!/usr/bin/env python3
"""VERIFY-F61-V6 (29 Sept 2026), task 2: is H193's f.176r / fol. 177r alignment right, position by position, and was any period letter used
both to set and to test the bowl rule?
 (a) re-derive H193's pairs exactly as the runner did (h193_attr.data(), key v4 via h170_gate.load_key, f61crib.align);
 (b) re-align f.176r with every 4-family class (4TRI, C43, 4STEM, 4PI and any '?x|y' split involving one) REMOVED from the aligning key, so
     no 4-family value can steer the DP; for each of H193's 40 targets report the text index and letter under (a) and (b);
 (c) the H193 2x2 (runner's answers, passes/h193_attribute.tsv) under (a) and under (b);
 (d) text disjointness: the anchor clear (fol. 177v from V06) against the target clear (fol. 177r + 177v V01-V05), by line label, and whether
     the aligning key (key_period_v4.tsv) has any row from fr.3984 f.176.
  python3 align_check.py [--check]"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); F = os.path.abspath(f"{HERE}/../family"); sys.path.insert(0, F)
import h193_attr as H, h190_4fam as h190
from f61crib import align
g = H.g
FAM = ("4TRI", "C43", "4STEM", "4PI")
def fam(c): return c in FAM or (c.startswith("?") and any(x in FAM for x in c[1:].split("|")))
def pairs_idx(seq, org, text, key):
    _, pr = align(text, seq, key); return {org[j]: (i, text[i], seq[j]) for i, j in pr if org[j]}
def flank(seq, text, key, K=3):
    """key-free letter for each 4-family column: under the leave-out alignment, take the nearest paired non-family column on each side
    within K columns that MATCHED (letter in its key set); if both exist and text distance equals column distance (no indel between),
    the column's letter is read off the text by interpolation; else None."""
    _, pr = align(text, seq, key); m = {j: i for i, j in pr}; out = {}
    ok = lambda j: j in m and not fam(seq[j]) and text[m[j]] in key.get(seq[j], ())
    for j in range(len(seq)):
        if not fam(seq[j]): continue
        L = next((jj for jj in range(j - 1, max(-1, j - K - 1), -1) if ok(jj)), None); R = next((jj for jj in range(j + 1, min(len(seq), j + K + 1)) if ok(jj)), None)
        if L is not None and R is not None and m[R] - m[L] == R - L: out[j] = (m[L] + j - L, text[m[L] + j - L])
    return out
def main():
    import glob
    lines = {}
    for f in sorted(glob.glob(f"{H.b.P}/f177v_clearA_*.tsv")):
        for r in g.rd(f): lines.setdefault("V" + r["line"].lstrip("LV"), r["text"])
    sr, orr = H.cons_origin(H.rows_full("f176r_signsA_*.tsv"), H.rows_full("f176r_signsB_*.tsv"), [f"L{k:02d}" for k in range(1, 48)])
    tr = H.v.clear177r() + "".join(g.fold(lines[f"V{k:02d}"]) for k in range(1, 6)); tr = tr[:len(sr)]
    kfull = g.load_key(); kout = {c: v for c, v in kfull.items() if not fam(c)}
    A = pairs_idx(sr, orr, tr, kfull); B = pairs_idx(sr, orr, tr, kout)
    FL = {orr[j]: v for j, v in flank(sr, tr, kout).items() if orr[j]}
    items = list(g.rd(f"{F}/h193_items.tsv")); ans = {r["item"]: r["answer"].strip().lower() for r in g.rd(f"{F}/passes/h193_attribute.tsv")}
    out = ["item\tline\tseg\tx\tcode\tidx_full\tletter_full\tidx_leaveout\tletter_leaveout\tsame\tflank_idx\tflank_letter\trunner_bowl"]
    same = moved = unp = 0; c = {"full": {"yes": [0, 0], "no": [0, 0]}, "out": {"yes": [0, 0], "no": [0, 0]}, "flank": {"yes": [0, 0], "no": [0, 0]}}
    for r in items:
        if r["group"] != "T": continue
        o = (r["line"], r["segment"], int(r["x_px"])); a = A.get(o); bb = B.get(o); an = ans.get(r["item"], "")
        assert a and a[1] == r["letter"], (r, a)
        s = "yes" if bb and bb[0] == a[0] else ("unpaired" if not bb else "no")
        same += s == "yes"; moved += s == "no"; unp += s == "unpaired"
        out.append(f"{r['item']}\t{r['line']}\t{r['segment']}\t{r['x_px']}\t{a[2]}\t{a[0]}\t{a[1]}\t{bb[0] if bb else '-'}\t{bb[1] if bb else '-'}\t{s}\t{FL[o][0] if o in FL else '-'}\t{FL[o][1] if o in FL else '-'}\t{an}")
        for tag, p in (("full", a), ("out", bb), ("flank", FL.get(o))):
            if p and an in ("yes", "no") and p[1] in "cpan": c[tag][an][0 if p[1] in "cp" else 1] += 1
    out.append(f"# 40 H193 targets: same text position with 4-family cells removed from the aligning key {same}, moved {moved}, unpaired {unp}")
    for tag in ("full", "out", "flank"):
        y, n = c[tag]["yes"], c[tag]["no"]
        out.append(f"# H193 2x2 under {dict(full='key v4 (runner)', out='4-family left out', flank='flank-anchored letter (leave-out key, both flanks matched within 3, no indel)')[tag]}: bowl yes c/p {y[0]} a/n {y[1]}; bowl no c/p {n[0]} a/n {n[1]}; Fisher p {h190.fisher(y[0], y[1], n[0], n[1]):.2g}")
    # whole-leaf: every f.176r 4-family column, letters under both keys
    allf = [o for o in A if fam(A[o][2])]; agree = sum(1 for o in allf if o in B and B[o][0] == A[o][0])
    out.append(f"# all f.176r 4-family columns paired under key v4: {len(allf)}; same text position under the leave-out key: {agree}")
    # (d) disjointness
    vlines = H.v.clear("V06")[1]; tlines = [f"V{k:02d}" for k in range(1, 6)]
    out.append(f"# anchor clear lines (f.176v): {vlines[0]}..{vlines[-1]} ({len(vlines)}); target clear: fol. 177r + {tlines[0]}..{tlines[-1]}; overlap {sorted(set(vlines) & set(tlines)) or 'none'}")
    leaves = sorted({r['leaf'] for r in g.rd(f'{F}/key_period_v4.tsv')})
    out.append(f"# aligning key key_period_v4.tsv leaves: {', '.join(leaves)}; any f.176: {any('176' in l for l in leaves)}")
    txt = "\n".join(out) + "\n"; p = f"{HERE}/align_check_result.txt"
    if "--check" in sys.argv:
        ok = os.path.exists(p) and open(p).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(p, "w").write(txt); print(txt, end="")
if __name__ == "__main__": main()
