#!/usr/bin/env python3
"""H427 (runner 16, 29 Sept 2026), script-only, descriptive: H423's chooser and unigram rule per pair and per leaf with 95% Wilson
intervals, marking pairs where the chooser is below the unigram rule -- which cells a context chooser must not be trusted on.
No gate, no f.61 letter (f.61 rows are its hidden-span known cells only).  python3 h427_ctx_perpair.py [--check]"""
import math, os, sys
from collections import defaultdict
HERE = os.path.dirname(os.path.abspath(__file__)); CHECK = "--check" in sys.argv; sys.argv = sys.argv[:1]; sys.path.insert(0, HERE)
import h423_ctx_chooser as c
def wilson(k, n, z=1.96):
    if n == 0: return (0, 0)
    p = k / n; d = 1 + z * z / n; m = (p + z * z / (2 * n)) / d; h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d; return (m - h, m + h)
def main():
    out = ["leaf\tpair\tN\tchooser\tchooser_95\tunigram\tunigram_95\tflag"]
    for n, fn in c.LEAVES.items():
        segs = fn(); ok, _ = c.run(segs); bp = defaultdict(lambda: [0, 0, 0])
        for (si, i), a in ok.items():
            x = segs[si][i]; p = "/".join(x["c"]); bp[p][0] += 1; bp[p][1] += a; bp[p][2] += max(x["c"], key=c.uni) == x["t"]
        for p, (N, k, u) in sorted(bp.items(), key=lambda kv: -kv[1][0]):
            lo, hi = wilson(k, N); ulo, uhi = wilson(u, N)
            out.append(f"{n}\t{p}\t{N}\t{k/N:.3f}\t{lo:.2f}-{hi:.2f}\t{u/N:.3f}\t{ulo:.2f}-{uhi:.2f}\t{'BELOW unigram' if k < u else ('above' if k > u else 'tie')}")
    txt = "\n".join(out) + "\n"; p = f"{HERE}/h427_ctx_perpair_result.tsv"
    if CHECK:
        ok = os.path.exists(p) and open(p).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(p, "w").write(txt); print(txt, end="")
if __name__ == "__main__": main()
