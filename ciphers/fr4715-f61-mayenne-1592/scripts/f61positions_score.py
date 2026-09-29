#!/usr/bin/env python3
"""H253 (runner 9 session_012NTadgrCBftz3oRtgw5jFu, 29 Sept 2026): join the blind positional read (h253_reply1.tsv, h253_reply2.tsv) to read_call_A's sign order.
A line is joined only where the positional read lists the same number of signs as read_call_A (after dropping items described as a dot / punctuation);
other lines are reported and left out. Writes f61_positions.tsv (line, pos, class from the decode, segment, x in sheet px, previous item and next item
kinds: sign / word / edge) and f61positions_result.txt.  [--check]"""
import csv, os, sys
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); F = os.path.abspath(f"{HERE}/../family")
def main():
    rows = [l.rstrip("\n").split("\t") for f in ("h253_reply1.tsv", "h253_reply2.tsv") for l in open(f"{HERE}/{f}") if l[0] == "L"]
    rows = [r for r in rows if not (r[3] == "sign" and ("dot" in r[4] or "punctuation" in r[4]))]
    A = Counter(r["line"] for r in csv.DictReader(open(f"{HERE}/read_call_A.tsv"), delimiter="\t"))
    dec = {(r["line"], int(r["pos"])): r["class"] for r in csv.DictReader(open(f"{F}/f61_decode_period_v4_frac0.1_sbs.tsv"), delimiter="\t")}
    out = ["line\tpos\tclass\tsegment\tx\tprev\tnext"]; rep = []
    for L in sorted(A):
        items = [r for r in rows if r[0][:3] == L]; signs = [k for k, r in enumerate(items) if r[3] == "sign"]
        if len(signs) != A[L]: rep.append(f"{L}: positional signs {len(signs)} vs read_call_A {A[L]} -> not joined"); continue
        rep.append(f"{L}: {len(signs)} signs joined")
        for p, k in enumerate(signs, 1):
            prev = "edge" if k == 0 else items[k - 1][3]; nxt = "edge" if k == len(items) - 1 else items[k + 1][3]
            out.append(f"{L}\t{p}\t{dec.get((L, p), '?')}\t{items[k][1]}\t{items[k][2]}\t{prev}\t{nxt}")
    j = [l.split("\t") for l in out[1:]]
    for cls in ("C6", "CA", "PHI", "C43"):
        c = [r for r in j if r[2] == cls]; b = sum(1 for r in c if "word" in (r[5], r[6]))
        rep.append(f"{cls}: {len(c)} joined, {b} next to a clear word")
    open(f"{HERE}/f61_positions.tsv", "w").write("\n".join(out) + "\n"); txt = "\n".join(rep) + "\n"; p = f"{HERE}/f61positions_result.txt"
    if "--check" in sys.argv:
        ok = os.path.exists(p) and open(p).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(p, "w").write(txt); print(txt, end="")
if __name__ == "__main__": main()
