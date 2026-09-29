#!/usr/bin/env python3
"""H196 (runner 7, 29 Sept 2026): a TEST key, not a merge -- key v5 (build_key_v5.load_key_v5) with 4TRI narrowed to c/p, the letters the 4-family
bowl sign carries on fr.3984 f.176v/f.176r (H193, period decipherment) and at Tomokiyo's f.61 positions (H194). Scored exactly as build_key_v5's
repro(): f.61 five known spans and the f.108r overlay (EBR form A), v5 vs the test key, 2000 permuted keys (seed 20260929); and the f.61 meter
(f61_decode_period_v4_frac0.1_sbs.tsv) with 4TRI tokens moved to c/p. Narrowing can only remove letters, so a known-letter count equal to v5's means
no contradiction with his letters wherever 4TRI occurs.  python3 h196_4tri_cp.py [--check]"""
import csv, os, random, sys
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); S = os.path.abspath(f"{HERE}/../scripts"); sys.path.insert(0, HERE); sys.path.insert(0, S)
import build_key_v5 as K
from f61crib import align, load_read, load_spans
from f61crib4 import split_lines
from f61joint import f108_lines
from sbs_relabel import relabel
def main():
    k5 = K.load_key_v5(); k5A = K.load_key_v5(ebr="A"); t = dict(k5); tA = dict(k5A); t["4TRI"] = ("c", "p"); tA["4TRI"] = ("c", "p")
    lines = split_lines(load_read()); lines.update(f108_lines()); relabel(lines)
    s61 = load_spans(); s108 = [(s, "F108_" + ("L02" if s == "T1" else "L03"), m) for s, _, m, _ in (l.rstrip("\n").split("\t") for l in open(f"{S}/tomokiyo_spans_3983.tsv") if l[0] == "T")]
    def sc(key, spans):
        mt = tot = 0
        for s, l, m in spans:
            mm = m.translate(K.FOLD); mt += align(mm, lines[l], key)[0]; tot += sum(1 for ch in mm if ch != "-")
        return mt, tot
    out = [f"v5 4TRI = {'/'.join(k5['4TRI'])}; test key 4TRI = c/p"]
    for tag, spans, a, b in (("f.61 five spans", s61, k5, t), ("f.108r overlay (EBR form A)", s108, k5A, tA)):
        for name, k in (("v5", a), ("test", b)):
            mt, tot = sc(k, spans); labs = sorted(k); vals = [k[x] for x in labs]; rng = random.Random(20260929); cs = []
            for _ in range(2000):
                v = list(vals); rng.shuffle(v); cs.append(sc(dict(zip(labs, v)), spans)[0])
            cs.sort(); out.append(f"{tag}: {name} {mt}/{tot} = {mt/tot:.3f}; 2000 permuted mean {sum(cs)/2000/tot:.3f} p95 {cs[1899]/tot:.3f} max {cs[-1]/tot:.3f}; >= key {sum(x >= mt for x in cs)}/2000")
    d = list(csv.DictReader(open(f"{HERE}/f61_decode_period_v4_frac0.1_sbs.tsv"), delimiter="\t"))
    n4 = Counter(r["period_letters"] for r in d if r["class"] == "4TRI")
    out.append(f"f.61 4TRI tokens: {sum(n4.values())} (v4 letters {dict(n4)}) -> c/p two-way under the test key")
    txt = "\n".join(out) + "\n"; p = f"{HERE}/h196_4tri_cp_result.txt"
    if "--check" in sys.argv:
        ok = os.path.exists(p) and open(p).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(p, "w").write(txt); print(txt, end="")
if __name__ == "__main__": main()
