#!/usr/bin/env python3
"""H219 (runner 8 session_011Taenrv3JSdk7VjpiBjids, 29 Sept 2026), script-only, written before the run: a TEST key, not a merge. On the known-span lines
the reader codes coincide with shape (H194: every f.61 4TRI a bowl, every C43/4STEM/4PI none; H202: f.108r L02-L03 4TRI 3 bowl / 1 none, others none),
so the shape rule (bowl c/p, no bowl a/n) is, at code level there, 4TRI c/p, C43 a/n, 4STEM a/n (4PI and HASH4 unchanged: no HASH4 on any span line).
Test key = v5 with those three cells; scored as h196_4tri_cp.py (build_key_v5's scorer, f.61 five spans and f.108r overlay, EBR form A for f.108r,
2000 permuted keys, seed 20260929). The one known exception (H202 S14: a no-bowl 4TRI at overlay letter c, which the shape rule reads a/n) is reported
beside, as a one-letter loss the code-level score cannot show. Gate for handing the shape rule to a verifier as a v6 candidate: no loss on the f.61
spans and at most that one on f.108r.  python3 h219_shape_testkey.py [--check]"""
import os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__)); S = os.path.abspath(f"{HERE}/../scripts"); sys.path.insert(0, HERE); sys.path.insert(0, S)
import build_key_v5 as K
from f61crib import align, load_read, load_spans
from f61crib4 import split_lines
from f61joint import f108_lines
from sbs_relabel import relabel
def main():
    k5 = K.load_key_v5(); k5A = K.load_key_v5(ebr="A"); cells = {"4TRI": ("c", "p"), "C43": ("a", "n"), "4STEM": ("a", "n")}
    t = dict(k5, **cells); tA = dict(k5A, **cells)
    lines = split_lines(load_read()); lines.update(f108_lines()); relabel(lines)
    s61 = load_spans(); s108 = [(s, "F108_" + ("L02" if s == "T1" else "L03"), m) for s, _, m, _ in (l.rstrip("\n").split("\t") for l in open(f"{S}/tomokiyo_spans_3983.tsv") if l[0] == "T")]
    def sc(key, spans):
        mt = tot = 0
        for s, l, m in spans:
            mm = m.translate(K.FOLD); mt += align(mm, lines[l], key)[0]; tot += sum(1 for ch in mm if ch != "-")
        return mt, tot
    out = ["v5 cells: " + ", ".join(f"{c} {'/'.join(k5[c])}" for c in cells) + "; test key: 4TRI c/p, C43 a/n, 4STEM a/n"]
    res = {}
    for tag, spans, a, b in (("f.61 five spans", s61, k5, t), ("f.108r overlay (EBR form A)", s108, k5A, tA)):
        for name, k in (("v5", a), ("test", b)):
            mt, tot = sc(k, spans); res[(tag, name)] = mt; labs = sorted(k); vals = [k[x] for x in labs]; rng = random.Random(20260929); cs = []
            for _ in range(2000):
                v = list(vals); rng.shuffle(v); cs.append(sc(dict(zip(labs, v)), spans)[0])
            cs.sort(); out.append(f"{tag}: {name} {mt}/{tot} = {mt/tot:.3f}; 2000 permuted p95 {cs[1899]/tot:.3f} max {cs[-1]/tot:.3f}; >= key {sum(x >= mt for x in cs)}/2000")
    out.append("known exception outside the code-level score: f.108r overlay S14 (H202), a no-bowl 4TRI at letter c -> the shape rule reads a/n: -1")
    l61 = res[("f.61 five spans", "v5")] - res[("f.61 five spans", "test")]; l108 = res[("f.108r overlay (EBR form A)", "v5")] - res[("f.108r overlay (EBR form A)", "test")] + 1
    out.append(f"gate: loss on f.61 spans {l61} (need 0), on f.108r {l108} including S14 (need <= 1) -> " + ("PASS: hand to a verifier as a v6 candidate" if l61 == 0 and l108 <= 1 else "FAIL"))
    txt = "\n".join(out) + "\n"; p = f"{HERE}/h219_shape_testkey_result.txt"
    if "--check" in sys.argv:
        ok = os.path.exists(p) and open(p).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(p, "w").write(txt); print(txt, end="")
if __name__ == "__main__": main()
