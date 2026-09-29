#!/usr/bin/env python3
"""H188 (runner 7, 29 Sept 2026), script-only: TEST keys, not merges -- key v5 plus, one at a time and together, the Desportes-hand leans the
verifier left open: 4TRI c/p (H193/H194), HASH4 d/q (f.176r d 0.51, f.176v d 0.43; H192), BETA m (0.40 / 0.74). CROSS s is left out (untestable in
f.61's hand, H197). Scored as build_key_v5's repro (f.61 five spans; f.108r overlay, EBR form A), 2000 permuted keys each, seed 20260929.
A narrowing can only remove letters: a count below v5's lists a contradiction with Tomokiyo's letters.  python3 h188_v5_plus.py [--check]"""
import os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__)); S = os.path.abspath(f"{HERE}/../scripts"); sys.path.insert(0, HERE); sys.path.insert(0, S)
import build_key_v5 as K
from f61crib import align, load_read, load_spans
from f61crib4 import split_lines
from f61joint import f108_lines
from sbs_relabel import relabel
NARROW = {"4TRI c/p": {"4TRI": ("c", "p")}, "HASH4 d/q": {"HASH4": ("d", "q")}, "BETA m": {"BETA": ("m",)}}
NARROW["all three"] = {k: v for d in NARROW.values() for k, v in d.items()}
def main():
    k5 = K.load_key_v5(); k5A = K.load_key_v5(ebr="A")
    lines = split_lines(load_read()); lines.update(f108_lines()); relabel(lines)
    s61 = load_spans(); s108 = [(s, "F108_" + ("L02" if s == "T1" else "L03"), m) for s, _, m, _ in (l.rstrip("\n").split("\t") for l in open(f"{S}/tomokiyo_spans_3983.tsv") if l[0] == "T")]
    def sc(key, spans):
        mt = tot = 0
        for s, l, m in spans:
            mm = m.translate(K.FOLD); mt += align(mm, lines[l], key)[0]; tot += sum(1 for ch in mm if ch != "-")
        return mt, tot
    out = ["v5 cells: " + "; ".join(f"{c} {'/'.join(k5.get(c, ('-',)))}" for c in ("4TRI", "HASH4", "BETA"))]
    for name, nar in [("v5", {})] + list(NARROW.items()):
        row = [name]
        for spans, base in ((s61, k5), (s108, k5A)):
            k = dict(base, **nar); mt, tot = sc(k, spans); labs = sorted(k); vals = [k[x] for x in labs]; rng = random.Random(20260929); cs = []
            for _ in range(2000):
                v = list(vals); rng.shuffle(v); cs.append(sc(dict(zip(labs, v)), spans)[0])
            cs.sort(); row.append(f"{mt}/{tot} (p95 {cs[1899]/tot:.3f}, >= key {sum(x >= mt for x in cs)}/2000)")
        out.append(f"{row[0]}: f.61 five spans {row[1]}; f.108r overlay {row[2]}")
    txt = "\n".join(out) + "\n"; p = f"{HERE}/h188_v5_plus_result.txt"
    if "--check" in sys.argv:
        ok = os.path.exists(p) and open(p).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(p, "w").write(txt); print(txt, end="")
if __name__ == "__main__": main()
