#!/usr/bin/env python3
"""A2-COL, 2 Oct 2026: shuffled-gloss control for the f.24 (canvas 27) interlinear alignment.
Real: f24_pairs.tsv aligned by tools/interlinear_align.py (--floor 100 --keep-fs --max-chunk 6
--prior seed_prior.tsv --word-prior). Control: the same cipher lines with the gloss lines dealt out
in a random derangement (no line keeps its own gloss), same flags, 50 seeds. Statistic: tokens whose
chunk agrees with their code's majority reading over >=2 occurrences ('agrees'), total and excluding
the three seeded codes (83 de, 92 comte, 31 que). The control changes which gloss a cipher line
meets, which is exactly what the agreement statistic depends on, so it can fail differently.
Deterministic (SEED below); prints both numbers and the control's mean/p95/max."""
import csv, random, subprocess, sys, tempfile, os
SEED, N = 20261002, 50
HERE = os.path.dirname(os.path.abspath(__file__))
TOOL = os.path.join(HERE, '../../../tools/interlinear_align.py')
FLAGS = ['--floor', '100', '--keep-fs', '--max-chunk', '6', '--prior', os.path.join(HERE, 'seed_prior.tsv'), '--word-prior']
seeded = {r['code'] for r in csv.DictReader(open(os.path.join(HERE, 'seed_prior.tsv')), delimiter='\t')}

def score(pairs):
    with tempfile.TemporaryDirectory() as d:
        p = os.path.join(d, 'p.tsv')
        with open(p, 'w') as f:
            w = csv.DictWriter(f, fieldnames=list(pairs[0].keys()), delimiter='\t', lineterminator='\n')
            w.writeheader(); w.writerows(pairs)
        subprocess.run([sys.executable, TOOL, 'align', p, d + '/a.tsv', d + '/k.tsv'] + FLAGS, check=True, capture_output=True)
        rows = list(csv.DictReader(open(d + '/a.tsv'), delimiter='\t'))
    tot = sum(r['status'] == 'agrees' for r in rows)
    uns = sum(r['status'] == 'agrees' and r['value'] not in seeded for r in rows)
    return tot, uns

pairs = list(csv.DictReader(open(os.path.join(HERE, 'f24_pairs.tsv')), delimiter='\t'))
real = score(pairs)
rng = random.Random(SEED); ctl = []
for _ in range(N):
    while True:
        perm = list(range(len(pairs))); rng.shuffle(perm)
        if all(i != j for i, j in enumerate(perm)): break
    sh = [dict(p, plain_line=pairs[j]['plain_line'], plain_raw=pairs[j]['plain_raw']) for p, j in zip(pairs, perm)]
    ctl.append(score(sh))
for k, name in ((0, 'agrees_all'), (1, 'agrees_unseeded')):
    v = sorted(c[k] for c in ctl)
    print('%s\treal %d\tcontrol mean %.1f p95 %d max %d\treal>max %s' % (name, real[k], sum(v)/N, v[int(0.95*N)-1], v[-1], real[k] > v[-1]))
