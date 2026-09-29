#!/usr/bin/env python3
"""H257 (runner 10 session_0148wt8Aokh6aZEdJsXzYiZX, 29 Sept 2026): join H253's positional read of f.61 L07 and L08 (h253_reply2.tsv; 10 and 13 signs
against read_call_A's 11 and 14) to read_call_A's order. Method, fixed before running: map every positional item's free-text description to a shape
FAMILY by keyword (loops-on-stem: PHI/DBL/SBS/LOOPSTEM1; 4-family: 4TRI/4STEM/4PI/HASH4; VBAR; INF; C43; C6; CROSS; ZHOOK; BETA; EBR; LOOPBAR; CA), map
read_call_A's positions to the same families through the decode's class column, and align the two family sequences with difflib.SequenceMatcher. An
A position left unmatched is joined to a WORD item read as the bare letter 'a' lying between its matched neighbours only if A's class there is CA
(the a-shaped sign a reader without the atlas would take for the word 'a'); such rows carry src=word_a. Writes f61_positions_L07L08.tsv (H253's
columns plus src) and f61_positions_all.tsv (H253's four lines verbatim plus these), and f61positions_join2_result.txt.  [--check]"""
import csv, difflib, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); F = os.path.abspath(f"{HERE}/../family")
FAM = {"PHI": "LOOPS", "DBL": "LOOPS", "SBS": "LOOPS", "LOOPSTEM1": "LOOPS", "4TRI": "FOUR", "4STEM": "FOUR", "4PI": "FOUR", "HASH4": "FOUR",
       "VBAR_A": "VBAR", "VBAR_B": "VBAR", "EBR_A": "EBR", "EBR_B": "EBR", "ISH": "EBR"}
KEYS = [("z-hook", "ZHOOK"), ("beta", "BETA"), ("uptick", "EBR"), ("bracket", "EBR"), ("43", "C43"), ("3/yogh", "C43"), ("3-shaped tail", "C43"),
        ("double horizontal stroke at base", "LOOPBAR"), ("-oo-", "INF"), ("v under", "VBAR"), ("nabla", "VBAR"), ("4", "FOUR"), ("plus", "CROSS"),
        ("cross", "CROSS"), ("6", "C6"), ("loop", "LOOPS"), ("phi", "LOOPS")]
# keyword table corrected once after a first run (29 Sept 2026, logged in NOTES H257): 'crossbar' had matched CROSS, and '4 with 3/yogh-shaped tail'
# (read_call_A's 43-shape) had fallen to FOUR; the 4-family keys now precede CROSS and the 3-tail wording maps to C43.
def fam_of_desc(d):
    d = d.lower()
    for k, f in KEYS:
        if k in d: return f
    return "?"
def main():
    rows = [l.rstrip("\n").split("\t") for l in open(f"{HERE}/h253_reply2.tsv") if l[0] == "L"]
    dec = {(r["line"], int(r["pos"])): r["class"] for r in csv.DictReader(open(f"{F}/f61_decode_period_v4_frac0.1_sbs.tsv"), delimiter="\t")}
    A = {}
    for r in csv.DictReader(open(f"{HERE}/read_call_A.tsv"), delimiter="\t"): A.setdefault(r["line"], []).append(int(r["pos"]))
    out = ["line\tpos\tclass\tsegment\tx\tprev\tnext\tsrc"]; rep = []
    for L in ("L07", "L08"):
        items = [r for r in rows if r[0][:3] == L and not (r[3] == "sign" and ("dot" in r[4] or "punctuation" in r[4]))]
        signs = [k for k, r in enumerate(items) if r[3] == "sign"]
        a_cls = [dec[(L, p)] for p in A[L]]; a_fam = [FAM.get(c, c) for c in a_cls]; s_fam = [fam_of_desc(items[k][4]) for k in signs]
        sm = difflib.SequenceMatcher(a=a_fam, b=s_fam, autojunk=False); match = {}
        for i, j, n in sm.get_matching_blocks():
            for t in range(n): match[i + t] = signs[j + t]
        joined = []
        for i, p in enumerate(A[L]):
            if i in match: joined.append((p, match[i], "sign")); continue
            lo = match.get(i - 1, -1); hi = match.get(i + 1, len(items))
            cand = [k for k in range(lo + 1, hi) if items[k][3] == "word" and items[k][4].strip().lower() == "a"]
            if a_cls[i] == "CA" and len(cand) == 1: joined.append((p, cand[0], "word_a"))
            else: joined.append((p, None, "unmatched"))
        n_ok = sum(1 for _, k, _ in joined if k is not None); n_wa = sum(1 for _, _, s in joined if s == "word_a")
        rep.append(f"{L}: read_call_A {len(A[L])} signs, positional {len(signs)} signs; family alignment matches {len(match)}; word-'a' joins {n_wa}; "
                   f"unmatched {len(A[L]) - n_ok}; A families {' '.join(a_fam)} | positional {' '.join(s_fam)}")
        if n_ok != len(A[L]): rep.append(f"{L}: not fully joined -> not written"); continue
        for p, k, src in joined:
            prev = "edge" if k == 0 else items[k - 1][3]; nxt = "edge" if k == len(items) - 1 else items[k + 1][3]
            out.append(f"{L}\t{p}\t{dec[(L, p)]}\t{items[k][1]}\t{items[k][2]}\t{prev}\t{nxt}\t{src}")
    open(f"{HERE}/f61_positions_L07L08.tsv", "w").write("\n".join(out) + "\n")
    base = [l.rstrip("\n") for l in open(f"{HERE}/f61_positions.tsv")]
    allrows = [base[0] + "\tsrc"] + [l + "\tsign" for l in base[1:]] + out[1:]
    open(f"{HERE}/f61_positions_all.tsv", "w").write("\n".join(allrows) + "\n")
    j = [l.split("\t") for l in allrows[1:]]
    for cls in ("CA", "C6", "PHI", "C43", "LOOPBAR", "ZHOOK"):
        c = [r for r in j if r[2] == cls]; b = sum(1 for r in c if "word" in (r[5], r[6]))
        rep.append(f"{cls}: {len(c)} positioned on six lines, {b} next to a clear word")
    txt = "\n".join(rep) + "\n"; p = f"{HERE}/f61positions_join2_result.txt"
    if "--check" in sys.argv:
        ok = os.path.exists(p) and open(p).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(p, "w").write(txt); print(txt, end="")
if __name__ == "__main__": main()
