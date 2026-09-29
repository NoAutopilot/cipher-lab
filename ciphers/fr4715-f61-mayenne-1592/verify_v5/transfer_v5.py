#!/usr/bin/env python3
"""VERIFY-F61-V5 (29 Sept 2026): does each value that key_period_f176.tsv proposes carry over from Desportes's hand (fr.3984 f.176r)
to the Mayenne hands, against shuffled-value controls?
(a) Known letters (Tomokiyo's five f.61r spans, 55 letters; his f.108r overlay, 84): each span is aligned with key v4 as the f.61 tests
    use it (--collapse-ebr --min 2 --frac 0.1, --sbs relabel) but with class X LEFT OUT (so X's positions are set by its neighbours,
    never by the value under test); his letter opposite every X sign is collected (folded: j->i, v->u, y->i). Hits = letters in the
    proposed cell; control = 200 random two-letter cells drawn from the letter frequency of f.176r's own decipherment (seed 29):
    p = share of controls with hits >= the proposed cell's. v4's own set is reported beside it.
(b) f.108v (no read gloss): the H127 sequence gain (scripts/f61beam_seqgain.py) with the 14-cell map and X set to the proposed cell,
    ranked against X set to each of the 11 Tomokiyo cells and 40 random letter pairs (seed 29), and against X dropped.
Writes transfer_v5_result.txt; --check fails when stale."""
import os, random, sys
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); F = os.path.abspath(f"{HERE}/../family"); S = os.path.abspath(f"{HERE}/../scripts")
CHECK = "--check" in sys.argv
sys.argv = [sys.argv[0], "--key", f"{F}/key_period_v4.tsv", "--collapse-ebr", "--min", "2", "--frac", "0.1", "--sbs"]
sys.path.insert(0, F); sys.path.insert(0, S)
import test_period_key as T, h170_gate as g
from f61crib import align, load_read, load_spans
from f61crib4 import split_lines
from f61joint import f108_lines
from sbs_relabel import relabel
PROP = {"VBAR_A": "gt", "EBR": "li", "HASH4": "dq", "4STEM": "cp", "DBL": "bo", "SBS": "bo", "ZHOOK": "ix", "BETA": "mz", "C43": "an", "4PI": "cp"}
FOLD = str.maketrans("jvy", "iui")
def main():
    key = T.load_key(); lines = split_lines(load_read()); lines.update(f108_lines()); relabel(lines)
    s61 = load_spans()
    s108 = [(s, "F108_" + ("L02" if s == "T1" else "L03"), m) for s, _, m, _ in (l.rstrip("\n").split("\t") for l in open(f"{S}/tomokiyo_spans_3983.tsv") if l[0] == "T")]
    import glob
    clear = "".join(g.fold(r["text"]) for f in sorted(glob.glob(f"{F}/passes/f177r_clearA_*.tsv")) for r in g.rd(f))
    freq = Counter(clear); letters = sorted(freq); wts = [freq[x] for x in letters]
    rng = random.Random(29); ctrl = []
    while len(ctrl) < 200:
        a, b = rng.choices(letters, wts, k=2)
        if a != b: ctrl.append(a + b)
    out = ["# transfer_v5.py (VERIFY-F61-V5): (a) Tomokiyo's letters at class X's positions, X left out of the aligning key", "",
           "leaf\tclass\tn pos\this letters there\tproposed cell\thits\tv4 set\thits v4\t200 random cells: mean hits / p(>= proposed)"]
    for tag, spans in (("f.61", s61), ("f.108r", s108)):
        for X in PROP:
            k2 = {c: v for c, v in key.items() if c != X}; got = []
            for s, l, m in spans:
                for i, j in align(m, lines[l], k2)[1]:
                    if lines[l][j] == X and m[i] != "-": got.append(m[i].translate(FOLD))
            if not got: continue
            C = Counter(got); hp = sum(C[x] for x in PROP[X]); v4 = "".join(key.get(X, ())); hv = sum(C[x] for x in v4.translate(FOLD))
            hc = [sum(C[x] for x in c) for c in ctrl]; p = sum(h >= hp for h in hc) / len(hc)
            out.append(f"{tag}\t{X}\t{len(got)}\t{' '.join(f'{x}{n}' for x, n in C.most_common())}\t{'/'.join(PROP[X])}\t{hp}\t{'/'.join(key.get(X, ())) or '-'}\t{hv}\t{sum(hc)/len(hc):.2f} / {p:.3f}")
    # (b) f.108v sequence gain
    sys.argv = sys.argv[:1]; import f61beam_seqgain as G
    Cm = G.J.cells(); L = G.J.lines("f108v"); SH = G.shuffles(L); n108v = Counter(x for s in L.values() for x in s)
    out += ["", "# (b) f.108v sequence gain (14-cell map; X varied); rank 1 = best", "class\tsigns on f.108v\tmap value\tproposed\tgain proposed\trank among 11 Tomokiyo cells + 40 random pairs (51)\tgain X dropped"]
    rp = random.Random(29); rnd = []
    while len(rnd) < 40:
        a, b = rp.sample("abcdefghilmnopqrstuxz", 2); rnd.append(a + b)
    cells = ["an", "bo", "cp", "dq", "er", "fs", "gt", "hu", "ix", "li", "mz"]
    fmtc = lambda c: {"li": "l/y"}.get(c, "/".join(c))
    for X, cls in (("VBAR_A", "VBAR_A"), ("EBR_B", "EBR_B"), ("HASH4", "HASH4"), ("4STEM", "4STEM"), ("SBS", "SBS"), ("ZHOOK", "ZHOOK"), ("BETA", "BETA")):
        if not n108v[cls]: continue
        prop = PROP.get(X, PROP.get("EBR")) if X != "EBR_B" else "li"
        gp = G.gain(L, SH, dict(Cm, **{cls: fmtc(prop)})); alts = [G.gain(L, SH, dict(Cm, **{cls: fmtc(c)})) for c in cells + rnd]
        rank = 1 + sum(a > gp for a in alts if True) - 1  # proposed itself is among the 11 cells: count strictly better
        gd = G.gain(L, SH, {k: v for k, v in Cm.items() if k != cls})
        out.append(f"{cls}\t{n108v[cls]}\t{Cm.get(cls, '-')}\t{fmtc(prop)}\t{gp:.4f}\t{1 + sum(a > gp for a in alts)}\t{gd:.4f}")
    txt = "\n".join(out) + "\n"; path = f"{HERE}/transfer_v5_result.txt"
    if CHECK: sys.exit(0 if open(path).read() == txt else "STALE")
    open(path, "w").write(txt); print(txt)
if __name__ == "__main__": main()
