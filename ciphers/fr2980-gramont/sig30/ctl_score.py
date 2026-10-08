#!/usr/bin/env python3
"""SIG-GRA30 control scorer: per-row keyed-sign agreement on fr.3040 f.18r L11-L21 (rows f18rB_L01..L11), aligning the
whole block to N8-GRA2's print span S1 with N8-GRA2's registered decode/align_agree (unchanged), then counting agreement
on the tokens of each row. A row file given with --replace substitutes those rows before the whole-block alignment.

  python3 sig30/ctl_score.py BASE.tsv [--replace ROWS.tsv]     prints row, keyed, agree, rate
"""
import sys, collections
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "n8gra2")); sys.path.insert(0, str(HERE.parent / "n8gra3"))
import score as S, score3 as S3

def rows(p):
    d = collections.OrderedDict()
    for ln in Path(p).read_text().splitlines()[1:]:
        f = ln.split("\t")
        if len(f) == 2: d[f[0]] = f[1].split()
    return d

def per_row(block):
    key = S.load_key(); pr = S3.SEGS["S1"]
    toks, own = [], []
    for r, tt in block.items():
        for t in tt: toks.append(t); own.append(r)
    dec = S.decode(toks, key)
    ag, kn, al = S.align_agree(dec, pr)
    res = collections.OrderedDict((r, [0, 0]) for r in block)
    for (t, v), a, r in zip(dec, al, own):
        if v: res[r][0] += 1; res[r][1] += (a == v)
    return ag, kn, res

if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"): print(__doc__); sys.exit(0)
    b = rows(sys.argv[1])
    if "--replace" in sys.argv:
        for r, tt in rows(sys.argv[sys.argv.index("--replace") + 1]).items(): b[r] = tt
    ag, kn, res = per_row(b)
    print(f"block\t{kn}\t{round(ag*kn)}\t{ag:.3f}")
    for r, (k, a) in res.items(): print(f"{r}\t{k}\t{a}\t{(a/k if k else 0):.3f}")
