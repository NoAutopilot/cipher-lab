#!/usr/bin/env python3
"""score.py -- GAPS14 (2 Oct 2026): score the blind letterform sorts against the pre-registered gate (PREREG.md).
Inputs: tile_key.tsv (tile -> id), sorts passA.tsv, passB.tsv, recon.tsv (tile -> group A|B). Ids: T36* = code 36,
Kc* = known c, Ke* = known e. Prints, per sort: group naming, known-answer accuracy with per-class counts, where the
four 36 tiles fall, and the 20-seed label-shuffle control; then the gate verdict on the reconciled sort. Exit 0 always.
Usage: python3 score.py [--seeds 20]
"""
import argparse, csv, os, random
H = os.path.dirname(os.path.abspath(__file__))
ap = argparse.ArgumentParser(); ap.add_argument('--seeds', type=int, default=20); a = ap.parse_args()
key = {r['tile']: r['id'] for r in csv.DictReader(open(os.path.join(H, 'tile_key.tsv')), delimiter='\t')}
def load(f): return {r['tile']: r['group'].strip().upper() for r in csv.DictReader(open(os.path.join(H, f)), delimiter='\t')}
def lab(i): return 'c' if i.startswith('Kc') else ('e' if i.startswith('Ke') else '36')
def acc(sort, labels):
    known = [t for t in labels if labels[t] in 'ce']
    ge = [sort[t] for t in known if labels[t] == 'e']; eg = max(set(ge), key=ge.count) if ge else 'A'
    right = sum((sort[t] == eg) == (labels[t] == 'e') for t in known)
    return right / len(known), eg
res = {}
for f in ('passA.tsv', 'passB.tsv', 'recon.tsv'):
    if not os.path.exists(os.path.join(H, f)): continue
    s = load(f); labels = {t: lab(key[t]) for t in key}
    ac, eg = acc(s, labels)
    cr = sum(s[t] != eg for t in key if labels[t] == 'c'); er = sum(s[t] == eg for t in key if labels[t] == 'e')
    g36 = [('e' if s[t] == eg else 'c') for t in sorted(key, key=lambda t: key[t]) if labels[t] == '36']
    known = [t for t in key if labels[t] in 'ce']; vals = [labels[t] for t in known]; null = []
    for seed in range(a.seeds):
        v = vals[:]; random.Random(seed).shuffle(v); null.append(acc(s, dict(zip(known, v)))[0])
    null.sort(); p95 = null[int(0.95 * (len(null) - 1))]
    print('%s: e group=%s; known-answer %.3f (c %d/2, e %d/8); 36 tiles (T36a..d = L04,L06,L10,L14) -> %s; '
          'shuffle 20 seeds mean %.3f p95 %.3f max %.3f, %d/20 >= target'
          % (f, eg, ac, cr, er, ' '.join(g36), sum(null) / len(null), p95, null[-1], sum(x >= ac for x in null)))
    res[f] = (ac, cr, p95, g36)
if 'recon.tsv' in res:
    ac, cr, p95, g36 = res['recon.tsv']
    ok = ac >= 0.9 and cr == 2 and ac > p95 and len(set(g36)) == 1
    print('GATE (reconciled):', 'PASS -> 36 = %s at C' % g36[0] if ok else 'FAIL -> 36 stays M',
          '| acc>=0.90 %s, c 2/2 %s, >p95 %s, 36 one group %s' % (ac >= 0.9, cr == 2, ac > p95, len(set(g36)) == 1))
