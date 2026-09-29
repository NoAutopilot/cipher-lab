#!/usr/bin/env python3
"""H417 (runner 15 session_01BDhspZ38TdrrXYSvLPTpjc, 29 Sept 2026), script-only, written before running: the published table's column structure
(eleven columns a/n b/o c/p d/q e/r f/s g/t h/u i/x l/y m/z, each ONE symbol except a/n and e/r, keys/key_mayenne_1592.tsv) as a constraint on key v8.
 v8      -- key v8 as loaded (f.61 reading key for f.61, pooled EBR form A for f.108r, as build_key_v7's checks).
 closed  -- every cell widened to whole columns (each letter brings its column partner), then folded (j=i, v=u, y=i as the scorer folds).
 column  -- each class whose cell spans more than one column is replaced by the single column carrying the most period-letter mass for that class in
            key_period_v8.tsv (all leaves pooled, '-' rows ignored); other cells as v8.
Scored: f.61's five spans with scripts/f61_positions_corrections.tsv applied (h408's sequence) and the f.108r overlay, each against 2000 permuted keys
of the variant itself (seed 20260929, labels shuffled as build_key_v7). Descriptive, pre-stated: a variant 'fits the known answers as well' iff its
count is >= v8's and its margin over its own permuted p95 is >= v8's margin. No key change.   python3 h417_column_closure.py [--check]"""
import csv, os, random, sys
from collections import defaultdict
HERE = os.path.dirname(os.path.abspath(__file__)); S = os.path.abspath(f"{HERE}/../scripts"); CHECK = "--check" in sys.argv; sys.argv = sys.argv[:1]
sys.path.insert(0, HERE); sys.path.insert(0, S)
import build_key_v7 as b, build_key_v8 as b8, h408_span_miss_apply as h8
from f61crib import align, load_read, load_spans
from f61crib4 import split_lines
from f61joint import f108_lines
from sbs_relabel import relabel
COLS = ["an", "bo", "cp", "dq", "er", "fs", "gt", "hu", "ix", "ly", "mz"]; COL = {c: col for col in COLS for c in col}
FOLD = {"j": "i", "v": "u", "y": "i"}
def fold(s): return tuple(sorted({FOLD.get(c, c) for c in s}))
def closed(k): return {c: fold({x for l in v for x in COL.get(l, l)}) for c, v in k.items()}
def mass():
    m = defaultdict(lambda: defaultdict(int))
    for r in csv.reader(l for l in open(f"{HERE}/key_period_v8.tsv") if not l.startswith("#")):
        pass
    for line in open(f"{HERE}/key_period_v8.tsv"):
        if line.startswith("#") or line.startswith("class\t"): continue
        f = line.rstrip("\n").split("\t")
        if len(f) >= 3 and f[1] in COL and f[2].isdigit(): m[f[0]][COL[f[1]]] += int(f[2])
    return m
def column(k, M):
    out = {}
    for c, v in k.items():
        cols = {COL.get(l, l) for l in v}
        if len(cols) > 1 and M.get(c): out[c] = fold(max(M[c].items(), key=lambda x: x[1])[0])
        else: out[c] = v
    return out
def score(k, spans, ll):
    def sc(kk): return sum(align(m.translate(b.FOLD), ll[l], kk)[0] for s, l, m in spans)
    mt = sc(k); tot = sum(sum(1 for ch in m.translate(b.FOLD) if ch != "-") for s, l, m in spans)
    labs = sorted(k); vals = [k[x] for x in labs]; rng = random.Random(20260929); cs = []
    for _ in range(2000):
        v = list(vals); rng.shuffle(v); cs.append(sc(dict(zip(labs, v))))
    cs.sort(); return mt, tot, cs[1899] / tot, sum(x >= mt for x in cs)
def main():
    lines = split_lines(load_read()); lines.update(f108_lines()); relabel(lines)
    l61 = h8.apply_seq(b.f61_relabel({x: list(v) for x, v in lines.items()}))
    s61 = load_spans(); s108 = [(s, "F108_" + ("L02" if s == "T1" else "L03"), m) for s, _, m, _ in (l.rstrip("\n").split("\t") for l in open(f"{S}/tomokiyo_spans_3983.tsv") if l[0] == "T")]
    M = mass(); kf = b8.load_key_v8(f61=True); kA = b8.load_key_v8(ebr="A"); out = []
    ch = {c: (kA[c], column(kA, M)[c]) for c in kA if column(kA, M)[c] != kA[c]}
    out.append("column variant changes (pooled, form A): " + "; ".join(f"{c} {'/'.join(a)} -> {'/'.join(z)}" for c, (a, z) in sorted(ch.items())))
    res = {}
    for tag, f in (("v8", lambda k: k), ("closed", closed), ("column", lambda k: column(k, M))):
        for leaf, k, sp, ll in (("f.61 spans (corrected)", kf, s61, l61), ("f.108r overlay", kA, s108, lines)):
            mt, tot, p95, ge = score(f(k), sp, ll); res[(tag, leaf)] = (mt, mt / tot - p95)
            out.append(f"{tag:6s} {leaf}: {mt}/{tot} = {mt/tot:.3f}; own permuted p95 {p95:.3f}; margin {mt/tot - p95:+.3f}; >= key {ge}/2000")
    for tag in ("closed", "column"):
        ok = all(res[(tag, l)][0] >= res[("v8", l)][0] and res[(tag, l)][1] >= res[("v8", l)][1] for l in ("f.61 spans (corrected)", "f.108r overlay"))
        out.append(f"read-out {tag}: " + ("fits the known answers as well as v8 (count and margin, both leaves)" if ok else "does not fit as well as v8 on at least one leaf (count or margin)"))
    txt = "\n".join(out) + "\n"; p = f"{HERE}/h417_column_closure_result.txt"
    if CHECK:
        ok = os.path.exists(p) and open(p).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(p, "w").write(txt); print(txt, end="")
if __name__ == "__main__": main()
