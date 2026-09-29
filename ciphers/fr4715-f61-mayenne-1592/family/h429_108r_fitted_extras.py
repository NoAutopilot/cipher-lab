#!/usr/bin/env python3
"""H429 (runner 16 session_01Vtwc6CEJD2BSnYdzzY4f8W, 29 Sept 2026), script-only, descriptive: the f.108r overlay letters that key v8 catches only
through a fitted letter outside the table column (H417: the 'column' key lost six) -- per token, the sequence class (corrections applied), pass A's
code, confidence and note, pass B's code at the same position, the overlay letter, v8's cell and the column key's cell (h417.column). For the
verifier: is a shape test (bracket forms, 4TRI vs the qui sign) warranted before any call?  No key change.  python3 h429_108r_fitted_extras.py [--check]"""
import csv, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); T = os.path.abspath(f"{HERE}/.."); CHECK = "--check" in sys.argv; sys.argv = sys.argv[:1]; sys.path.insert(0, HERE); sys.path.insert(0, f"{T}/scripts")
import h417_column_closure as q, build_key_v8 as b8, build_key_v7 as b
from f61crib import align
def rd(f): return list(csv.DictReader((l for l in open(f) if not l.startswith("#")), delimiter="\t"))
def main():
    lines = q.split_lines(q.load_read()); lines.update(q.f108_lines()); q.relabel(lines)
    for r in rd(f"{T}/scripts/f108r_positions_corrections.tsv"): lines["F108_" + r["line"]][int(r["pos"]) - 1] = r["class"]
    A = {}; B = {}
    for src, D in (("A", A), ("B", B)):
        for r in rd(f"{T}/scripts/pass108{src}_classes.tsv"): D[(r["line"], int(r["pos"]))] = r
    kA = b8.load_key_v8(ebr="A"); kc = q.column(kA, q.mass()); out = ["line\tpos\tclass\tpassA\tconfA\tpassB\toverlay\tv8_cell\tcolumn_cell\tnoteA"]
    for s, _, m, _ in (l.rstrip("\n").split("\t") for l in open(f"{T}/scripts/tomokiyo_spans_3983.tsv") if l[0] == "T"):
        row = "L02" if s == "T1" else "L03"; seq = lines["F108_" + row]; mm = m.translate(b.FOLD)
        _, pv = align(mm, seq, kA); _, pc = align(mm, seq, kc)
        hv = {j: mm[i] for i, j in pv if mm[i] in kA.get(seq[j], ())}; hc = {j for i, j in pc if mm[i] in kc.get(seq[j], ())}
        for j in sorted(set(hv) - hc):
            a = A.get((row, j + 1), {}); bb = B.get((row, j + 1), {})
            out.append(f"{row}\t{j+1}\t{seq[j]}\t{a.get('sign','')}\t{a.get('conf','')}\t{bb.get('sign','')}\t{hv[j]}\t{'/'.join(kA.get(seq[j], ()))}\t{'/'.join(kc.get(seq[j], ()))}\t{a.get('note','')}")
    out.append(f"# {len(out) - 1} overlay letters caught by key v8 and not by the column key")
    txt = "\n".join(out) + "\n"; p = f"{HERE}/h429_108r_fitted_extras_result.tsv"
    if CHECK:
        ok = os.path.exists(p) and open(p).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(p, "w").write(txt); print(txt, end="")
if __name__ == "__main__": main()
