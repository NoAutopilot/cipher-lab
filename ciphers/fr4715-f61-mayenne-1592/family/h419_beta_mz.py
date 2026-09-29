#!/usr/bin/env python3
"""H419 (runner 15 session_01BDhspZ38TdrrXYSvLPTpjc, 29 Sept 2026), script-only, written before running: key v8 with the single cell BETA m/s ->
m/z (the table's m/z column; H416: the 'z' of 'commoditez' at a BETA on f.108r), scored as H417 (f.61 spans corrected, f.108r overlay, own 2000
permuted keys). Pre-stated: 'BETA m/z is supported' iff both counts >= v8's and both margins >= v8's. No key change.  [--check]"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); CHECK = "--check" in sys.argv; sys.argv = sys.argv[:1]; sys.path.insert(0, HERE)
import h417_column_closure as q
def main():
    lines = q.split_lines(q.load_read()); lines.update(q.f108_lines()); q.relabel(lines)
    l61 = q.h8.apply_seq(q.b.f61_relabel({x: list(v) for x, v in lines.items()}))
    s61 = q.load_spans(); s108 = [(s, "F108_" + ("L02" if s == "T1" else "L03"), m) for s, _, m, _ in (l.rstrip("\n").split("\t") for l in open(f"{q.S}/tomokiyo_spans_3983.tsv") if l[0] == "T")]
    kf = q.b8.load_key_v8(f61=True); kA = q.b8.load_key_v8(ebr="A"); out = []; res = {}
    for tag, f in (("v8", lambda k: k), ("BETA m/z", lambda k: dict(k, BETA=("m", "z")))):
        for leaf, k, sp, ll in (("f.61 spans (corrected)", kf, s61, l61), ("f.108r overlay", kA, s108, lines)):
            mt, tot, p95, ge = q.score(f(k), sp, ll); res[(tag, leaf)] = (mt, mt / tot - p95)
            out.append(f"{tag:8s} {leaf}: {mt}/{tot} = {mt/tot:.3f}; own permuted p95 {p95:.3f}; margin {mt/tot - p95:+.3f}; >= key {ge}/2000")
    ok = all(res[("BETA m/z", l)][0] >= res[("v8", l)][0] and res[("BETA m/z", l)][1] >= res[("v8", l)][1] for l in ("f.61 spans (corrected)", "f.108r overlay"))
    out.append("read-out: " + ("BETA m/z is supported" if ok else "BETA m/z is not supported on both leaves"))
    txt = "\n".join(out) + "\n"; p = f"{HERE}/h419_beta_mz_result.txt"
    if CHECK:
        ok2 = os.path.exists(p) and open(p).read() == txt; print("check", "OK" if ok2 else "STALE"); sys.exit(0 if ok2 else 1)
    open(p, "w").write(txt); print(txt, end="")
if __name__ == "__main__": main()
