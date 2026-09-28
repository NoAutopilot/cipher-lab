#!/usr/bin/env python3
"""F61-BEAM-MARGIN-14 (campaign step H126, 28 Sept 2026, runner 5 session_01RbeePKZVn83gNfES8yFmhe), script-only. H117's
margin calibration, under the 14-cell pairs where the beam's choices are 0.856 right (H116/H121), on both known texts:
f.61 span lines (folds S1, S2, S3, S4a+S4b, S5) and Tomokiyo's f.108r overlay lines (folds T1, T2) -- seven folds.
Margin at a covered position = best beam path score of its line minus the best path with that position forced to the
pair's other letter. Known positions = aligned markup letters inside the pair (f61crib.align, as H116/H121).
tau(train) = smallest margin at which the training positions with margin >= tau are >= 90% right (>= 5 of them), else none.
GATE H126 (pre-registered): pooled held-out accuracy of positions with margin >= tau >= 0.90 on >= 20 positions.
  -> scripts/f61beam_margin14_result.txt, scripts/f61beam_margin14_positions.tsv [--check]"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ARGS = sys.argv[1:]; sys.argv = sys.argv[:1]
import f61beam_margin as BM
import f61beam_known as K
from f61crib import load_spans, align
J, jp = K.J, K.jp
def known_positions(L, spans, C):
    key = {c: tuple(v.split("/")) for c, v in C.items()}; P = {}
    for s, line, markup in spans:
        for i, j in align(markup, L[line], key)[1]:
            if markup[i] != "-": P[(line, j)] = (s, jp.fold(markup[i]))
    return P
def rows(L, C, P):
    out = []
    for line, seq in L.items():
        idx = [k for k, c in enumerate(seq) if c in C]; sets = [tuple(jp.fold(x) for x in C[seq[k]].split("/")) for k in idx]
        s, v = BM.best(sets)
        for i, k in enumerate(idx):
            if (line, k) not in P: continue
            sp, tr = P[(line, k)]
            if tr not in sets[i]: continue
            alt = BM.best(sets[:i] + [tuple(c for c in sets[i] if c != s[i])] + sets[i + 1:])[1]
            out.append((line, k + 1, "/".join(sets[i]), s[i], round(v - alt, 4), sp, "", tr))
    return out
def main():
    C = J.cells()
    L61, sp61 = J.lines("known_h51"), load_spans(); L108, sp108 = K.load108()
    R = rows(L61, C, known_positions(L61, sp61, C)) + rows(L108, C, known_positions(L108, sp108, C))
    R = [(a, b, c, d, e, f, h) for a, b, c, d, e, f, _, h in R]   # BM.tau reads p[3] beam, p[4] margin, p[6] true
    folds = [("S1",), ("S2",), ("S3",), ("S4a", "S4b"), ("S5",), ("T1",), ("T2",)]
    out = [f"known positions {len(R)}; beam right {sum(p[3] == p[6] for p in R)}/{len(R)}"]; hr = hn = 0
    for f in folds:
        tr = [p for p in R if p[5] not in f]; te = [p for p in R if p[5] in f]; t = BM.tau(tr)
        if t is None: out.append(f"fold {'+'.join(f)}: no tau; held-out {len(te)} not scored"); continue
        a = [p for p in te if p[4] >= t]; r = sum(p[3] == p[6] for p in a); hr += r; hn += len(a)
        out.append(f"fold {'+'.join(f)}: tau {t:.3f}; held-out above tau {r}/{len(a)} (of {len(te)}, {sum(p[3] == p[6] for p in te)} right overall)")
    ok = hn >= 20 and hr / hn >= 0.90
    out.append(f"GATE H126 (pooled held-out >= 0.90 on >= 20): {hr}/{hn}" + (f" = {hr / hn:.3f}" if hn else "") + f" -> {'PASS' if ok else 'FAIL'}")
    if ok: out.append(f"tau from all known positions: {BM.tau(R):.3f}")
    txt = "\n".join(out) + "\n"; tsv = "line\tpos\tpair\tbeam\tmargin\tspan\ttrue\n" + "".join("\t".join(map(str, p[:7])) + "\n" for p in R)
    rp, tp = f"{HERE}/f61beam_margin14_result.txt", f"{HERE}/f61beam_margin14_positions.tsv"
    if "--check" in ARGS:
        good = os.path.exists(rp) and open(rp).read() == txt and open(tp).read() == tsv; print("fresh" if good else "STALE"); sys.exit(0 if good else 1)
    open(rp, "w").write(txt); open(tp, "w").write(tsv); print(txt, end="")
if __name__ == "__main__": main()
