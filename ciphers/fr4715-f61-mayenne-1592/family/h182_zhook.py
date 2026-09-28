#!/usr/bin/env python3
"""H182 (runner 6, 28 Sept 2026): Tomokiyo's letters at every ZHOOK position of f.61r (five spans) and f.108r (overlay), under the
alignment of the test key key_period_v4n176z.tsv (= key_period_v4n176.tsv + ZHOOK i/x from fr.3984 f.176r's period decipherment,
H177b: agreed ZHOOK i 23, x 3 of 46). Descriptive for the verifier; writes h182_zhook_result.txt; --check fails if stale."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.abspath(f"{HERE}/../scripts"))
sys.argv[1:1] = ["--key", "key_period_v4n176z.tsv", "--collapse-ebr", "--min", "2", "--frac", "0.1", "--sbs"]
import test_period_key as T
from f61crib import align, load_read, load_spans
from f61crib4 import split_lines
from f61joint import f108_lines
from sbs_relabel import relabel
key = T.load_key(); lines = split_lines(load_read()); lines.update(f108_lines()); relabel(lines)
s108 = [(s, "F108_" + ("L02" if s == "T1" else "L03"), m) for s, _, m, _ in (l.rstrip("\n").split("\t") for l in open(f"{HERE}/../scripts/tomokiyo_spans_3983.tsv") if l[0] == "T")]
out = ["span\tline\tpos\ttomokiyo\ti_or_j"]; n = k = 0
for s, l, m in load_spans() + s108:
    for i, j in align(m, lines[l], key)[1]:
        if lines[l][j] == "ZHOOK": n += 1; ok = m[i] in "ij"; k += ok; out.append(f"{s}\t{l}\t{j + 1}\t{m[i]}\t{'yes' if ok else 'NO'}")
out.append(f"i or j at {k}/{n} ZHOOK positions")
txt = "\n".join(out) + "\n"; res = f"{HERE}/h182_zhook_result.txt"
if "--check" in sys.argv:
    ok = open(res).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
open(res, "w").write(txt); print(txt, end="")
