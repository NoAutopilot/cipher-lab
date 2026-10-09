#!/usr/bin/env python3
"""LAG-MARKS (9 Oct 2026): one-reader marks-kept error of the la-garde-1577 transcription, from the split cells settled
from the image. Inputs: lag_marks_cells.tsv (every literal split between pass A and its witness, lag_marks_cells.py) and
lag_marks_look.tsv (the settled reading per distinct cell: a fresh look C, or v2's H grade where WC-LAGARDE already
settled the cell from the image). For each comparison (A vs L1, A vs B) a reader is charged one error at every split
cell where its sign differs from the settled sign. Cells where A and its witness agree are assumed right (a shared
misreading is invisible here, so this is a LOWER bound on one reader's error); split cells whose look was `doubt` are
reported three ways: dropped (central), charged to both readers (upper), and charged to neither (lower).
  python3 lag_marks.py [--check]    writes lag_marks.tsv; --check exits 1 if stale."""
import os, sys, collections
HERE = os.path.dirname(os.path.abspath(__file__))
rd = lambda f: [l.split("\t") for l in open(os.path.join(HERE, f), encoding="utf-8").read().splitlines()[1:] if l.strip()]
cells = rd("lag_marks_cells.tsv")
look = {(r[0], r[1]): r for r in rd("lag_marks_look.tsv")}   # unit tag (6179/6467), line.pos -> row
N = {}   # aligned comparisons per unit, from lag_err.tsv (LAG-ERR)
for r in rd("lag_err.tsv"):
    if not r[0].startswith(("TOTAL", "6179 A-vs", "6467 A-vs")):
        N[r[0]] = int(r[1])
acc = collections.defaultdict(lambda: collections.Counter())
detail = []
for unit, cell, a_sign, w_sign, kind, *_ in cells:
    tag = unit.split()[0]
    lk = look.get((tag, cell))
    if lk is None:
        sys.exit(f"no settled reading for {tag} {cell}")
    settled, conf = lk[2], lk[3]
    a_err, w_err = a_sign != settled, w_sign != settled
    key = unit
    c = acc[key]
    c["split"] += 1
    if conf == "doubt":
        c["doubt"] += 1
        c["A_doubt"] += a_err; c["W_doubt"] += w_err
    else:
        c["A_err"] += a_err; c["W_err"] += w_err
        c["both_wrong"] += a_err and w_err
    detail.append((unit, cell, a_sign, w_sign, settled, conf, "A" * a_err + "W" * w_err or "-"))
lines = ["comparison\tn_aligned\tsplit\tdoubt\tA_err\tW_err\tA_rate_central\tW_rate_central\tmean_reader_central\tmean_reader_lower\tmean_reader_upper"]
def row(name, n, c):
    nd = n - c["doubt"]
    ac, wc = c["A_err"] / nd, c["W_err"] / nd
    lo = (c["A_err"] + c["W_err"]) / 2 / n
    up = (c["A_err"] + c["W_err"] + 2 * c["doubt"]) / 2 / n
    return f"{name}\t{n}\t{c['split']}\t{c['doubt']}\t{c['A_err']}\t{c['W_err']}\t{ac:.3f}\t{wc:.3f}\t{(ac+wc)/2:.3f}\t{lo:.3f}\t{up:.3f}"
tot = collections.defaultdict(collections.Counter); totn = collections.Counter()
for name, n in N.items():
    c = acc[name]
    lines.append(row(name, n, c))
    for k in ("A-vs-B", "A-vs-L1", "pooled"):
        if k == "pooled" or name.endswith(k):
            tot[k].update(c); totn[k] += n
for k in ("A-vs-B", "A-vs-L1", "pooled"):
    lines.append(row("TOTAL " + k, totn[k], tot[k]))
out = "\n".join(lines) + "\n\nunit\tcell\tA\twitness\tsettled\tlook\twrong\n" + "".join("\t".join(d) + "\n" for d in detail)
p = os.path.join(HERE, "lag_marks.tsv")
if "--check" in sys.argv:
    sys.exit(0 if os.path.exists(p) and open(p, encoding="utf-8").read() == out else 1)
open(p, "w", encoding="utf-8").write(out)
print("\n".join(lines))
