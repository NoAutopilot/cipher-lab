"""MERCY-GAP gate (PREREG-MERCY-GAP.md): LOO threshold on g_norm, positives = six glued clusters, negatives = ordinary
between-token gaps; 20 label-shuffled controls. Targets are never read here."""
import csv, random, numpy as np
D = 'ciphers/espagnol142-mercy-1648/mercygap/'
POS = {('r16', 21), ('r17', 10), ('r17', 21), ('r20', 15), ('r23', 1), ('r24', 4)}
TGT = {('r20', 6), ('r18', 5), ('r24', 14)}
FLAG = {('r19', 7), ('r20', 4), ('r22', 2), ('r22', 6), ('r22', 10), ('r24', 20)}
rows = list(csv.DictReader(open(D + 'gaps.tsv'), delimiter='\t'))
pos, neg, intra = [], [], []
for r in rows:
    k = (r['row'], int(r['pos1'])); g = float(r['g_norm'])
    if r['kind'] == 'intra': intra.append(g); continue
    if k in TGT or k in FLAG: continue
    (pos if k in POS else neg).append(g)
assert len(pos) == 6, len(pos)

def thresh(p, n):
    """t maximizing balanced accuracy (glued: g < t); ties -> midpoint of the widest tie run."""
    vals = sorted(set(p + n)); cands = [vals[0] - 1e-3] + [(a + b) / 2 for a, b in zip(vals, vals[1:])] + [vals[-1] + 1e-3]
    sc = [(np.mean([x < t for x in p]) + np.mean([x >= t for x in n])) / 2 for t in cands]
    best = max(sc); ix = [i for i, s in enumerate(sc) if s == best]
    return (cands[ix[0]] + cands[ix[-1]]) / 2

def loo(p, n):
    hp = [x < thresh(p[:i] + p[i + 1:], n) for i, x in enumerate(p)]
    hn = [x >= thresh(p, n[:i] + n[i + 1:]) for i, x in enumerate(n)]
    return all(hp), sum(hp), np.mean(hn), (all(hp) and np.mean(hn) >= 0.9)

if __name__ == '__main__':
    print('positives', len(pos), sorted(pos)); print('negatives', len(neg), 'min %.3f p10 %.3f median %.3f' %
          (min(neg), np.percentile(neg, 10), np.median(neg)))
    print('negatives sorted low end', sorted(neg)[:8])
    a, hp, hn, ok = loo(pos, neg)
    print('REAL LOO: positives on glued side %d/6, negatives on split side %.3f -> %s' % (hp, hn, 'PASS' if ok else 'FAIL'))
    t = thresh(pos, neg); print('full-data threshold t = %.3f' % t)
    allv = pos + neg; fails = 0
    for s in range(20):
        random.seed(s); lab = [1] * len(pos) + [0] * len(neg); random.shuffle(lab)
        p = [v for v, l in zip(allv, lab) if l]; n = [v for v, l in zip(allv, lab) if not l]
        _, php, phn, pok = loo(p, n); fails += (not pok)
        print('  shuffle seed %d: %d/6, %.3f -> %s' % (s, php, phn, 'PASS' if pok else 'FAIL'))
    print('CONTROL: shuffled labels fail the gate in %d/20 (needs >= 19) -> %s' % (fails, 'PASS' if fails >= 19 else 'FAIL'))
    print('DIAGNOSTIC intra-code gaps: n %d, median %.3f, max %.3f; positives max %.3f' % (len(intra), np.median(intra), max(intra), max(pos)))
    di = [x for x in intra]; a2, hp2, hn2, ok2 = loo(pos, di) if False else (None, None, None, None)
