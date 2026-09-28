#!/usr/bin/env python3
"""VERIFY-F61-V4 step 1 (28 Sept 2026): re-run family/test_period_key.py's scoring for key_period_v4.tsv
(--collapse-ebr --min 2 --frac 0.1 --sbs) with FRESH permutation seeds (the committed run used seed 1, 200 perms).
Imports test_period_key's own functions unchanged; only the seed and N differ. Writes verify_v4/repro_result.txt.
  python3 verify_v4/repro.py [--check]
"""
import os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__)); FAM = os.path.abspath(f"{HERE}/../family")
sys.argv = [sys.argv[0], "--key", f"{FAM}/key_period_v4.tsv", "--collapse-ebr", "--min", "2", "--frac", "0.1", "--sbs"] + (["--check"] if "--check" in sys.argv else [])
sys.path.insert(0, FAM)
import test_period_key as T
from sbs_relabel import relabel
key = T.load_key(); lines = T.split_lines(T.load_read()); lines.update(T.f108_lines()); relabel(lines)
spans = T.load_spans()
mt, tot = T.score(key, lines, spans)
out = [f"key v4 ({len(key)} classes): f.61 five spans {mt}/{tot} = {mt/tot:.3f}"]
labs = sorted(key); vals = [key[l] for l in labs]
for seed, N in ((20260928, 2000), (7331, 2000)):
    rng = random.Random(seed); cs = []
    for _ in range(N):
        v = list(vals); rng.shuffle(v); cs.append(T.score(dict(zip(labs, v)), lines, spans)[0])
    cs.sort()
    out.append(f"seed {seed}, {N} permuted keys: mean {sum(cs)/N/tot:.3f} p95 {cs[int(.95*N)-1]/tot:.3f} p99 {cs[int(.99*N)-1]/tot:.3f} max {cs[-1]/tot:.3f}; >= key {sum(c >= mt for c in cs)}/{N}")
txt = "\n".join(out) + "\n"; path = f"{HERE}/repro_result.txt"
if "--check" in sys.argv: ok = os.path.exists(path) and open(path).read() == txt; print("fresh" if ok else "STALE"); sys.exit(0 if ok else 1)
open(path, "w").write(txt); print(txt, end="")
