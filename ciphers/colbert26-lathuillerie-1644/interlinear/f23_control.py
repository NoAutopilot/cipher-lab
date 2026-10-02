#!/usr/bin/env python3
"""A2-COL2, 2 Oct 2026: shuffled-gloss control for the f.23 (canvas 26) interlinear alignment.
Real: f23_pairs.tsv (two-digit codes renumbered 100+code so every code may take a chunk) aligned by
tools/interlinear_align.py with FLAGS below. Control: the same cipher runs with the gloss phrases dealt out in a
random derangement (no pair keeps its own gloss), same flags, 50 seeds. Statistic: tokens whose chunk agrees
with their code's majority reading over >=2 occurrences ('agrees'), total and excluding any seeded codes.
The control changes which gloss a cipher run meets, which is what the statistic depends on, so it can fail
differently from the real alignment. Usage: f23_control.py [--prior SEED.tsv]  (no prior = flat start).
Deterministic (SEED below); prints both numbers and the control's mean/p95/max."""
import csv, random, subprocess, sys, tempfile, os
SEED, N = 20261002, 50
HERE = os.path.dirname(os.path.abspath(__file__))
TOOL = os.path.join(HERE, '../../../tools/interlinear_align.py')
FLAGS = ['--floor', '100', '--keep-fs', '--max-chunk', '6']
seeded = set()
if '--prior' in sys.argv:
    pr = sys.argv[sys.argv.index('--prior') + 1]
    FLAGS += ['--prior', os.path.abspath(pr), '--word-prior']
    seeded = {r['code'] for r in csv.DictReader(open(pr), delimiter='\t')}

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

pairs = list(csv.DictReader(open(os.path.join(HERE, 'f23_pairs.tsv')), delimiter='\t'))
real = score(pairs)
rng = random.Random(SEED); ctl = []
for _ in range(N):
    while True:
        perm = list(range(len(pairs))); rng.shuffle(perm)
        if all(i != j for i, j in enumerate(perm)): break
    sh = [dict(p, plain_line=pairs[j]['plain_line'], plain_raw=pairs[j]['plain_raw']) for p, j in zip(pairs, perm)]
    ctl.append(score(sh))
print('flags\t' + ' '.join(os.path.basename(x) for x in FLAGS))
for k, name in ((0, 'agrees_all'), (1, 'agrees_unseeded')):
    v = sorted(c[k] for c in ctl)
    print('%s\treal %d\tcontrol mean %.1f p95 %d max %d\treal>max %s' % (name, real[k], sum(v)/N, v[int(0.95*N)-1], v[-1], real[k] > v[-1]))
