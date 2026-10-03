#!/usr/bin/env python3
"""FT4c, 3 Oct 2026: with the gate's best pin set (22 de, 66 r, 501 et) fixed on f.216v/f.217r, list for each repeated
free code every chunk that admits an exact-coverage segmentation (repeats otherwise relaxed), and for each pinned
occurrence the slip positions it can take. A code with one surviving chunk is forced in the relaxed model, hence in
every fully consistent segmentation too. Reads ciphertext_f216v.txt, slip_f217r.txt; maxlen 12 as the gate."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gate_pair as g
from collections import Counter
T = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
toks, text = g.load(os.path.join(T, 'ciphertext_f216v.txt'), os.path.join(T, 'slip_f217r.txt'))
sc = g.Scorer(text, 12)
pins = {'22': 'de', '66': 'r', '501': 'et'}
cnt = Counter(toks)
subs = {text[i:i + l] for l in range(1, 13) for i in range(len(text) - l + 1)}
for t in sorted((t for t, c in cnt.items() if c > 1 and t not in pins), key=lambda t: -cnt[t]):
    cs = sorted(s for s in subs if bin(sc.smask(s)).count('1') >= cnt[t] and sc.feasible(toks, dict(pins, **{t: s})))
    print(t, 'x%d' % cnt[t], len(cs), cs[:12])
