#!/usr/bin/env python3
"""H240 (runner 9 session_012NTadgrCBftz3oRtgw5jFu, 29 Sept 2026), script-only, H219's design, written before the run. H233/H239: the readers' code 4PI
is the 4-head hash on f.101r and f.108r (period d/q: f.108r overlay d 4, p 1) but a 4 over a Pi on f.61 (no hash; a no-bowl 4 by H193's question). And
Tomokiyo's span S5 reads f.61's L11 9 4PI as n (h191 table). So the test keys split 4PI by leaf, by shape:
 f.108r overlay: 4PI d/q (the 4-head) vs v5's d/a/q/n;  f.61 spans: 4PI a/n (the no-bowl 4, H194/H219's cell) vs v5 d/a/q/n vs unread (H234's choice).
Scored with build_key_v5's scorer (f61crib.align), 2000 permuted keys (seed 20260929), EBR form A for f.108r. Pre-stated gate: no loss on f.61's spans
under 4PI a/n, at most one on f.108r's overlay under 4PI d/q (the overlay's p). Descriptive, for the verifier; no merge.  python3 h240_4head_testkey.py [--check]"""
import os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__)); S = os.path.abspath(f"{HERE}/../scripts"); sys.path.insert(0, HERE); sys.path.insert(0, S)
import build_key_v5 as K
from f61crib import align, load_read, load_spans
from f61crib4 import split_lines
from f61joint import f108_lines
from sbs_relabel import relabel
def main():
    k5 = K.load_key_v5(); k5A = K.load_key_v5(ebr="A")
    lines = split_lines(load_read()); lines.update(f108_lines()); relabel(lines)
    s61 = load_spans(); s108 = [(s, "F108_" + ("L02" if s == "T1" else "L03"), m) for s, _, m, _ in (l.rstrip("\n").split("\t") for l in open(f"{S}/tomokiyo_spans_3983.tsv") if l[0] == "T")]
    def sc(key, spans):
        mt = tot = 0
        for s, l, m in spans:
            mm = m.translate(K.FOLD); mt += align(mm, lines[l], key)[0]; tot += sum(1 for ch in mm if ch != "-")
        return mt, tot
    out = [f"v5 4PI cell: {'/'.join(k5['4PI'])}"]; res = {}
    for tag, spans, variants in (("f.61 five spans", s61, (("v5", k5), ("4PI a/n", dict(k5, **{"4PI": ("a", "n")})), ("4PI unread", {k: v for k, v in k5.items() if k != "4PI"}))),
                                 ("f.108r overlay (EBR form A)", s108, (("v5", k5A), ("4PI d/q", dict(k5A, **{"4PI": ("d", "q")}))))):
        for name, k in variants:
            mt, tot = sc(k, spans); res[(tag, name)] = mt; labs = sorted(k); vals = [k[x] for x in labs]; rng = random.Random(20260929); cs = []
            for _ in range(2000):
                v = list(vals); rng.shuffle(v); cs.append(sc(dict(zip(labs, v)), spans)[0])
            cs.sort(); out.append(f"{tag}: {name} {mt}/{tot} = {mt/tot:.3f}; permuted p95 {cs[1899]/tot:.3f} max {cs[-1]/tot:.3f}; >= key {sum(x >= mt for x in cs)}/2000")
    l61 = res[("f.61 five spans", "v5")] - res[("f.61 five spans", "4PI a/n")]; l108 = res[("f.108r overlay (EBR form A)", "v5")] - res[("f.108r overlay (EBR form A)", "4PI d/q")]
    lu = res[("f.61 five spans", "v5")] - res[("f.61 five spans", "4PI unread")]
    out.append(f"gate: f.61 loss under 4PI a/n {l61} (need 0), f.108r loss under 4PI d/q {l108} (need <= 1) -> " + ("PASS" if l61 <= 0 and l108 <= 1 else "FAIL") + f"; f.61 loss if 4PI left unread {lu}")
    txt = "\n".join(out) + "\n"; p = f"{HERE}/h240_4head_testkey_result.txt"
    if "--check" in sys.argv:
        ok = os.path.exists(p) and open(p).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(p, "w").write(txt); print(txt, end="")
if __name__ == "__main__": main()
