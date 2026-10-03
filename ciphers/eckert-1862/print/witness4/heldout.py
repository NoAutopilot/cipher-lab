#!/usr/bin/env python3
"""GAPS191, 3 Oct 2026: leave-one-telegram-out check on witnesses.tsv. Each witness is predicted from the other
witnesses of the same code word: same slot class (signature/address vs body) first, then the nearest date. Control:
the printed meanings shuffled across all rows (shuffled pairing), same prediction rule; the pairing is exactly what
the shuffle changes, so the control can differ from the real run. Usage: heldout.py witnesses.tsv [--shuffles 2000]"""
import csv, sys, random, datetime
rows = list(csv.DictReader(open(sys.argv[1]), delimiter='\t')); S = int(sys.argv[sys.argv.index('--shuffles') + 1]) if '--shuffles' in sys.argv else 2000
d = lambda s: datetime.datetime.strptime(s + ' 1862', '%d %b %Y')
cls = lambda r: 'name' if r['slot'] in ('signature', 'address') else 'body'
def score(mean):
    hits = 0; per = {}
    for i, r in enumerate(rows):
        oth = [j for j, o in enumerate(rows) if j != i and o['code_word'] == r['code_word'] and not (o['pointer'] == r['pointer'] and o['pointer'] != '-')]
        if not oth: continue
        oth.sort(key=lambda j: (cls(rows[j]) != cls(r), abs((d(rows[j]['date_1862']) - d(r['date_1862'])).days)))
        h = mean[oth[0]] == mean[i]; hits += h; per.setdefault(r['code_word'], [0, 0]); per[r['code_word']][0] += h; per[r['code_word']][1] += 1
    return hits, per
real = [r['printed'] for r in rows]; h, per = score(real)
rnd = random.Random(1); ctrl = []
for _ in range(S):
    m = real[:]; rnd.shuffle(m); ctrl.append(score(m)[0])
ctrl.sort(); n = sum(v[1] for v in per.values())
print('real', h, 'of', n, {k: '%d/%d' % tuple(v) for k, v in per.items()})
print('shuffled-pairing control: mean %.2f p95 %d p99 %d max %d (%d shuffles)' % (sum(ctrl) / S, ctrl[int(.95 * S)], ctrl[int(.99 * S)], ctrl[-1], S))
