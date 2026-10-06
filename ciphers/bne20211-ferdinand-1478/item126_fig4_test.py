#!/usr/bin/env python3
"""Test Tomokiyo 2018 Fig. 4's syllable numerals on BNE MSS/20211/126 against the leaf's own interlinear period
decipherment (LANE-PRIV1, 6 Oct 2026). Rule fixed before the first run: statistic = share of numeral tokens whose Fig. 4
syllable occurs in the letters of the same line's gloss, lines with >= 8 gloss letters read; control = the Fig. 4
syllables shuffled over its codes, 2000 draws (seed 1); gate = real > shuffled p99. One run per pass (A, B), each blind.

  python3 item126_fig4_test.py KEY.tsv [item126_passes.tsv]
KEY.tsv (code, value, ...) is Tomokiyo's table, kept in the private repository (author's work, not redistributed here).
"""
import collections, os, random, re, sys

key_path = sys.argv[1]
passes = sys.argv[2] if len(sys.argv) > 2 else os.path.join(os.path.dirname(os.path.abspath(__file__)), 'item126_passes.tsv')
key = {}
for line in open(key_path).read().split('\n')[1:]:
    if line:
        c, v = line.split('\t')[:2]
        key[c] = v
rows = [l.rstrip('\n').split('\t') for l in open(passes) if not l.startswith('#')][1:]


def stat(k, G, C):
    hit = tot = 0
    for ln in C:
        g = re.sub('[^a-z]', '', G[ln].lower())
        if len(g) < 8:
            continue
        for t in C[ln]:
            if t in k:
                tot += 1
                hit += k[t] in g
    return hit, tot


for p in ('A', 'B'):
    G, C = collections.defaultdict(str), collections.defaultdict(list)
    for pas, ln, seg, kind, txt in rows:
        if pas != p or ln == 'V12':      # V12 is the clear closing, not cipher
            continue
        if kind == 'G':
            G[ln] += ' ' + txt
        elif kind == 'C':
            C[ln] += [t for t in txt.split() if t.isdigit()]
    h, t = stat(key, G, C)
    real = h / max(t, 1)
    codes, vals = list(key), list(key.values())
    rnd, null = random.Random(1), []
    for _ in range(2000):
        rnd.shuffle(vals)
        a, b = stat(dict(zip(codes, vals)), G, C)
        null.append(a / max(b, 1))
    null.sort()
    p99 = null[int(0.99 * len(null))]
    print(f'pass {p}: numeral tokens tested {t}, hits {h}; real {real:.3f}  shuffled mean {sum(null) / len(null):.3f}  '
          f'p99 {p99:.3f}  GATE {"PASS" if real > p99 else "FAIL"}')
