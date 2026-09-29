#!/usr/bin/env python3
"""H420 rescore (runner 15, 29 Sept 2026), script-only: the f.108r overlay under key v8 with scripts/f108r_positions_corrections.tsv applied (and
with H419's BETA m/z beside it), H417's scorer and permuted keys.  python3 h420_rescore.py [--check]"""
import csv, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); T = os.path.abspath(f"{HERE}/.."); CHECK = "--check" in sys.argv; sys.argv = sys.argv[:1]; sys.path.insert(0, HERE)
import h417_column_closure as q
def main():
    lines = q.split_lines(q.load_read()); lines.update(q.f108_lines()); q.relabel(lines)
    s108 = [(s, "F108_" + ("L02" if s == "T1" else "L03"), m) for s, _, m, _ in (l.rstrip("\n").split("\t") for l in open(f"{T}/scripts/tomokiyo_spans_3983.tsv") if l[0] == "T")]
    corr = [r for r in csv.DictReader((l for l in open(f"{T}/scripts/f108r_positions_corrections.tsv") if not l.startswith("#")), delimiter="\t")]
    kA = q.b8.load_key_v8(ebr="A"); out = []
    for tag, k, fix in (("v8", kA, False), ("v8 + f108r correction", kA, True), ("v8 BETA m/z + f108r correction", dict(kA, BETA=("m", "z")), True)):
        ll = {x: list(v) for x, v in lines.items()}
        if fix:
            for r in corr: ll["F108_" + r["line"]][int(r["pos"]) - 1] = r["class"]
        mt, tot, p95, ge = q.score(k, s108, ll); out.append(f"{tag}: f.108r overlay {mt}/{tot} = {mt/tot:.3f}; own permuted p95 {p95:.3f}; >= key {ge}/2000")
    txt = "\n".join(out) + "\n"; p = f"{HERE}/h420_rescore_result.txt"
    if CHECK:
        ok = os.path.exists(p) and open(p).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(p, "w").write(txt); print(txt, end="")
if __name__ == "__main__": main()
