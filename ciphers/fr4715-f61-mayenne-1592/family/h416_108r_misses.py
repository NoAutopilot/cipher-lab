#!/usr/bin/env python3
"""H416 (runner 15 session_01BDhspZ38TdrrXYSvLPTpjc, 29 Sept 2026), script-only: the f.108r overlay letters (f.61's hand; Tomokiyo's reprint of the
period gloss, scripts/tomokiyo_spans_3983.tsv) that key v8 (pooled, EBR form A, as build_key_v7's check) misses, with the reader code and cell at
each, via build_key_v7's own alignment.  python3 h416_108r_misses.py [--check]"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); S = os.path.abspath(f"{HERE}/../scripts"); CHECK = "--check" in sys.argv; sys.argv = sys.argv[:1]
sys.path.insert(0, HERE); sys.path.insert(0, S)
import build_key_v7 as b, build_key_v8 as b8
from f61crib import align, load_read
from f61crib4 import split_lines
from f61joint import f108_lines
from sbs_relabel import relabel
def main():
    k = b8.load_key_v8(ebr="A"); lines = split_lines(load_read()); lines.update(f108_lines()); relabel(lines); out = []; tot = hit = 0
    for s, _, m, _ in (l.rstrip("\n").split("\t") for l in open(f"{S}/tomokiyo_spans_3983.tsv") if l[0] == "T"):
        l = "F108_" + ("L02" if s == "T1" else "L03"); mm = m.translate(b.FOLD); n, pairs = align(mm, lines[l], k); seq = lines[l]; pd = dict(pairs); tot += len(mm); hit += n
        for i, ch in enumerate(mm):
            j = pd.get(i)
            if not (j is not None and ch in k.get(seq[j], ())):
                out.append(f"{s}\t{l}\tletter {i + 1} '{ch}'\t" + (f"sign {j + 1} {seq[j]} cell {'/'.join(k.get(seq[j], ())) or '-'}" if j is not None else "no sign paired"))
    txt = f"f.108r overlay under key v8 (pooled, EBR form A): {hit}/{tot}; misses:\n" + "\n".join(out) + "\n"; p = f"{HERE}/h416_108r_misses_result.txt"
    if CHECK:
        ok = os.path.exists(p) and open(p).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(p, "w").write(txt); print(txt, end="")
if __name__ == "__main__": main()
