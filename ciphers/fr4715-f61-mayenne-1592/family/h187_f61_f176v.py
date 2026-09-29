#!/usr/bin/env python3
"""H187 (runner 7, 29 Sept 2026): at f.61r's own positions inside Tomokiyo's five spans, compare each class's letters from fr.3984 f.176v's
period decipherment (key_period_f176v.tsv, H177f: letters with share >= 0.15 of the class's agreed columns) with his letter at the same
position, via the F61-CAL DP alignment under key_period_v4n176.tsv (the H181 set-up). Null: 1000 permutations of the letter sets across the
compared classes (seed 187), p95 of the total agreement. Descriptive, for the verifier; his letters come from his own table, and f.61's
classes are f.61's readers' classes (H178b's ZHOOK tile link across hands FAILED).  python3 h187_f61_f176v.py [--check]"""
import os, random, sys
from collections import Counter, defaultdict
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.abspath(f"{HERE}/../scripts"))
sys.argv[1:1] = ["--key", "key_period_v4n176.tsv", "--collapse-ebr", "--min", "2", "--frac", "0.1", "--sbs"]
import test_period_key as T, h170_gate as g
from f61crib import align, load_read, load_spans
from f61crib4 import split_lines
from sbs_relabel import relabel
cnt = defaultdict(Counter)
for r in g.rd(f"{HERE}/key_period_f176v.tsv"): cnt[r["class"]][r["letter"]] += int(r["n"])
V = {c: {x for x, n in C.items() if n >= 0.15 * sum(C.values())} for c, C in cnt.items() if sum(C.values()) >= 10}
key = T.load_key(); lines = split_lines(load_read()); relabel(lines); pos = []
for s, l, m in load_spans():
    for i, j in align(m, lines[l], key)[1]:
        c = lines[l][j]
        if c in V and m[i].isalpha(): pos.append((s, l, j + 1, c, m[i]))
out = ["span\tline\tpos\tclass\tf176v_letters\ttomokiyo\tagree"]; per = defaultdict(lambda: [0, 0])
for s, l, j, c, t in pos:
    ok = t in V[c]; per[c][0] += ok; per[c][1] += 1; out.append(f"{s}\t{l}\t{j}\t{c}\t{'/'.join(sorted(V[c]))}\t{t}\t{'yes' if ok else 'NO'}")
tot = sum(a for a, n in per.values()); N = sum(n for a, n in per.values())
cls = sorted(per); rng = random.Random(187); null = []
for _ in range(1000):
    sets = [V[c] for c in cls]; rng.shuffle(sets); M = dict(zip(cls, sets)); null.append(sum(t in M[c] for _, _, _, c, t in pos))
null.sort(); out += ["", "class\tf176v letters\tagree/n"] + [f"{c}\t{'/'.join(sorted(V[c]))}\t{per[c][0]}/{per[c][1]}" for c in cls]
out.append(f"total {tot}/{N}; null (letter sets permuted across these classes) mean {sum(null) / len(null):.1f}, p95 {null[949]}, max {null[-1]}")
txt = "\n".join(out) + "\n"; res = f"{HERE}/h187_f61_f176v_result.txt"
if "--check" in sys.argv:
    ok = open(res).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
open(res, "w").write(txt); print("\n".join(out[out.index(""):]))
