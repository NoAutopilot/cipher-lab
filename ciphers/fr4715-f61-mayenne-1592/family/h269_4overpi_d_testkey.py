#!/usr/bin/env python3
"""H269 (runner 10 session_0148wt8Aokh6aZEdJsXzYiZX, 29 Sept 2026), script-only, H240's design under key v6's f.61 reading (build_key_v6.load_key_v6(f61=True)).
H268: Tomokiyo's S5 'melente-noit' is French only as 'me l'entendoit', which reads L11 8 (4STEM, cell a/n) as n and L11 9 (the 4-over-Pi, his n) as d.
Test keys: v6 (4PI a/d/n/q pooled, as loaded for f.61) vs 4-over-Pi = d (4PI: d) vs 4-over-Pi = a/n (H240/H245's cell), scored on the five known spans
(a) against the published markup (tomokiyo_spans.tsv) and (b) with S5 rewritten as the H268 witness 'melentendoit' (his dash at 4STEM filled with n,
his n at the 4-over-Pi replaced by d; every other span unchanged). build_key_v5's scorer (f61crib.align, j/v/y folded), 2000 permuted keys per cell
(seed 20260929); --spans not needed: witness (b) is read from scripts/tomokiyo_spans_witness.tsv (H277). Descriptive: (a) says what the published letters support, (b) what the French witness supports; which witness the key follows is the
verifier's call. No merge.  python3 h269_4overpi_d_testkey.py [--check]"""
import os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__)); S = os.path.abspath(f"{HERE}/../scripts"); sys.path.insert(0, HERE); sys.path.insert(0, S)
import build_key_v5 as K
from build_key_v6 import load_key_v6
from f61crib import align, load_read, load_spans
from f61crib4 import split_lines
from sbs_relabel import relabel
def main():
    k6 = load_key_v6(f61=True); lines = split_lines(load_read()); relabel(lines)
    pub = load_spans(); wit = load_spans(f"{S}/tomokiyo_spans_witness.tsv")   # H277: the witness file replaces the inline rewrite
    assert wit == [(s, l, "melentendoit" if s == "S5" else m) for s, l, m in pub], "witness file differs from the published spans beyond S5"
    def sc(key, spans):
        mt = tot = 0
        for s, l, m in spans:
            mm = m.translate(K.FOLD); mt += align(mm, lines[l], key)[0]; tot += sum(1 for ch in mm if ch != "-")
        return mt, tot
    out = [f"v6 f.61 reading: 4PI {'/'.join(k6['4PI'])}, 4STEM {'/'.join(k6['4STEM'])}"]
    keys = (("v6", k6), ("4-over-Pi = d", dict(k6, **{"4PI": ("d",)})), ("4-over-Pi = a/n", dict(k6, **{"4PI": ("a", "n")})))
    for tag, spans in (("(a) published markup", pub), ("(b) S5 as 'melentendoit'", wit)):
        for name, k in keys:
            mt, tot = sc(k, spans); labs = sorted(k); vals = [k[x] for x in labs]; rng = random.Random(20260929); cs = []
            for _ in range(2000):
                v = list(vals); rng.shuffle(v); cs.append(sc(dict(zip(labs, v)), spans)[0])
            cs.sort(); out.append(f"{tag}: {name} {mt}/{tot} = {mt/tot:.3f}; permuted p95 {cs[1899]/tot:.3f} max {cs[-1]/tot:.3f}; >= key {sum(x >= mt for x in cs)}/2000")
    txt = "\n".join(out) + "\n"; p = f"{HERE}/h269_4overpi_d_testkey_result.txt"
    if "--check" in sys.argv:
        ok = os.path.exists(p) and open(p).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(p, "w").write(txt); print(txt, end="")
if __name__ == "__main__": main()
