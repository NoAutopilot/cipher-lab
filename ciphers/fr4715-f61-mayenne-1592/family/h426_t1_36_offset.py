#!/usr/bin/env python3
"""H426 (runner 16, 29 Sept 2026), script-only: is f.108r T1/36 (INF, confirmed three times by H418/H420) under the overlay 'e' an alignment
offset or a genuine INF-e conflict?  T1 has 39 signs (F108_L02, corrections applied) and 39 overlay letters; report f61crib.align's
matches, whether any gap is used, and the match count in the window T1/30-39 for the overlay shifted by -2..+2 against the signs
(key v8 ebr A, the H420/H423 key).  python3 h426_t1_36_offset.py [--check]"""
import csv, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); T = os.path.abspath(f"{HERE}/.."); CHECK = "--check" in sys.argv; sys.argv = sys.argv[:1]
sys.path.insert(0, HERE); sys.path.insert(0, f"{T}/scripts")
import h417_column_closure as q, build_key_v8 as b8, h423_ctx_chooser as c
from f61crib import align
def main():
    lines = q.split_lines(q.load_read()); lines.update(q.f108_lines()); q.relabel(lines)
    for r in csv.DictReader((l for l in open(f"{T}/scripts/f108r_positions_corrections.tsv") if not l.startswith("#")), delimiter="\t"):
        lines["F108_" + r["line"]][int(r["pos"]) - 1] = r["class"]
    kk = {x: c.cell(v) for x, v in b8.load_key_v8(ebr="A").items()}
    seq = lines["F108_L02"]; mm = "".join(c.fl(x) for x in "satisfaireungseulauprejudicedeplusieurs")
    m, pairs = align(mm, seq, kk); gaps = len(seq) + len(mm) - 2 * len(pairs)
    miss = [f"T1/{j+1} {seq[j]} under '{mm[i]}'" for i, j in pairs if mm[i] not in kk.get(seq[j], ())]
    out = [f"T1: {len(seq)} signs, {len(mm)} overlay letters; align matched {m}, pairs {len(pairs)}, gap moves {gaps}; misses: {'; '.join(miss)}"]
    for sh in (-2, -1, 0, 1, 2):
        hit = sum(1 for j in range(29, 39) if 0 <= j + sh < len(mm) and mm[j + sh] in kk.get(seq[j], ()))
        out.append(f"window T1/30-39, overlay shifted {sh:+d}: {hit}/10 signs carry their overlay letter")
    out.append("reading: " + ("no offset -- the unshifted one-to-one alignment is the only one that fits the window; T1/36 is a genuine INF-e conflict (the overlay truth is left as it is)"
                              if gaps == 0 and all(sh == 0 or sum(1 for j in range(29, 39) if 0 <= j + sh < len(mm) and mm[j + sh] in kk.get(seq[j], ())) < 9 for sh in (-2, -1, 1, 2)) else "an offset is possible; see the counts"))
    txt = "\n".join(out) + "\n"; p = f"{HERE}/h426_t1_36_offset_result.txt"
    if CHECK:
        ok = os.path.exists(p) and open(p).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(p, "w").write(txt); print(txt, end="")
if __name__ == "__main__": main()
