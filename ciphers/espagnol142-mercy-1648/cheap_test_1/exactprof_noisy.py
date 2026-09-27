#!/usr/bin/env python3
"""Exact-profile control with injected transcription error (campaign espagnol142-mercy-1648 H1, 27 Sept 2026).

Builds the same exact-profile control as `tools/homophonic_anneal.py --control PLAIN --profile CIPHER.tsv --seed S`
(same seed -> same window, same key, same homophone draws), then replaces a share --noise of the positions with a
sign drawn from the profile's own occurrence distribution (a misread digit that looks like another code), writes the
noisy sequence as a long-format TSV for target-mode annealing, and the clean plaintext beside it so recovery can be
scored. CLAUDE.md rule 3 (SALV-DIAG): a control's error level must bracket the target's measured transcription
error (4.7 percent two-pass disagreement, Y6; 5 percent blind re-check, R7-MEYE) before a miss on the target is read.

  python3 ciphers/espagnol142-mercy-1648/cheap_test_1/exactprof_noisy.py --control PLAIN.txt --profile cipher_codes.tsv \
      --seed 1 --noise 0.05 --out /tmp/noisy.tsv
  python3 tools/homophonic_anneal.py /tmp/noisy.tsv --skip NONE --corpus ... --seed 1 --out r.json
  python3 ciphers/espagnol142-mercy-1648/cheap_test_1/exactprof_noisy.py --score r.json --plain /tmp/noisy.tsv.plain
"""
import argparse, json, os, random, sys
from collections import Counter
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "tools"))
import homophonic_anneal as ha

ap = argparse.ArgumentParser()
ap.add_argument("--control"); ap.add_argument("--profile"); ap.add_argument("--seed", type=int, default=1)
ap.add_argument("--noise", type=float, default=0.05); ap.add_argument("--out")
ap.add_argument("--score"); ap.add_argument("--plain")
a = ap.parse_args()
if a.score:
    o = json.load(open(a.score)); p = open(a.plain).read().strip()
    ok = sum(1 for x, y in zip(o["decoded"], p) if x == y)
    print(f"score {o['score']:.1f} recovery {ok}/{len(p)} = {ok/len(p):.1%} restarts {o['restart_scores']}")
    sys.exit()
prof = ha.load_profile(a.profile, {"NONE"})
seq, p, truth, start = ha.make_profile_control(open(a.control, encoding="utf-8").read(), prof, a.seed)
rng = random.Random(a.seed + 7000)
signs = sorted(Counter(seq).items())
pool = [s for s, c in signs for _ in range(c)]
n = int(round(a.noise * len(seq)))
for i in rng.sample(range(len(seq)), n):
    seq[i] = rng.choice(pool)
with open(a.out, "w") as f:
    f.write("line\tposition\tsign\n")
    for i, s in enumerate(seq):
        f.write(f"l1\t{i+1}\t{s}\n")
open(a.out + ".plain", "w").write(p)
print(f"window {start} N={len(seq)} K={len(set(seq))} noisy positions {n} ({a.noise:.0%})")
