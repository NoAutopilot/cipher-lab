#!/usr/bin/env python3
"""D2B-MATF110 scorer (5 Oct 2026): aligns blind passes A/B of f.110 lines 1-6 against Bourdeau's f110-1..6
(ciphertext.txt) and evaluates the gates pre-registered in f110crops/PREREG.md (G0 known-answer, G1 label collapse with
specificity, G2 crib from openings/openings_alignment.tsv). Usage: python3 f110crops/score.py  (run from the target dir)."""
import collections, glob, json, os, sys
D = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(D)
key = {}
for l in open(os.path.join(T, 'key.tsv')).read().splitlines()[1:]:
    p = l.split('\t'); key[p[0]] = p[1]
keyed = lambda x: x in key and key[x] != '+'
bour = {}
for l in open(os.path.join(T, 'ciphertext.txt')):
    p = l.rstrip('\n').split('\t')
    if p[0].startswith('f110-'): bour[int(p[0][5:])] = p[1].split()
def load(pfx):
    out = {}
    for f in sorted(glob.glob(os.path.join(D, pfx + '_L*.tsv'))):
        for l in open(f).read().splitlines()[1:]:
            p = l.split('\t')
            if len(p) >= 2 and p[0].strip():
                try: out[int(p[0])] = p[1].split()
                except ValueError: pass
    return out
def nw(a, b):
    n, m = len(a), len(b); S = [[0]*(m+1) for _ in range(n+1)]
    for i in range(n+1): S[i][0] = i
    for j in range(m+1): S[0][j] = j
    for i in range(1, n+1):
        for j in range(1, m+1):
            S[i][j] = min(S[i-1][j]+1, S[i][j-1]+1, S[i-1][j-1]+(0 if a[i-1]==b[j-1] else 1))
    i, j, pairs = n, m, []
    while i > 0 and j > 0:
        if S[i][j] == S[i-1][j-1]+(0 if a[i-1]==b[j-1] else 1): pairs.append((i-1, j-1)); i -= 1; j -= 1
        elif S[i][j] == S[i-1][j]+1: i -= 1
        else: j -= 1
    return pairs[::-1], S[n][m]
crib = {}
for l in open(os.path.join(T, 'openings/openings_alignment.tsv')).read().splitlines()[1:]:
    p = l.split('\t')
    if p[1].startswith('f110-') and p[2].isdigit() and p[6] not in ('', '-'):
        crib[(int(p[1][5:]), int(p[2])-1)] = p[6]
TARGETS = ['BOX', 'z', 'w', 'T', '4', 'U', 'p', 'v', 'y', '1']
res = {}
passes = {k: load('pass' + k) for k in 'AB'}
for k, P in passes.items():
    al = []  # (line, bpos, bourdeau label, pass label)
    # image lines are matched to the Bourdeau line (f110-1..8) with the lowest normalised edit distance
    # (the crop centres drifted: image line 5 = f110-4, 6 = f110-5); a Bourdeau line keeps its best pass line only
    best = {}
    for il in sorted(P):
        cands = [(nw(bour[b], P[il])[1] / max(len(bour[b]), len(P[il])), b) for b in range(1, 9)]
        d, b = min(cands)
        if b not in best or d < best[b][0]: best[b] = (d, il)
    res.setdefault('map', {})[k] = {il: [b, round(d, 3)] for b, (d, il) in best.items()}
    for b, (d, il) in sorted(best.items()):
        if d > 0.8: continue  # no real match (crop off a line)
        pairs, _ = nw(bour[b], P[il])
        al += [(b, i, bour[b][i], P[il][j]) for i, j in pairs]
    kp = [r for r in al if keyed(r[2])]
    g0 = sum(r[2] == r[3] for r in kp) / max(1, len(kp))
    same_val = sum(keyed(r[3]) and key[r[3]] == key[r[2]] for r in kp) / max(1, len(kp))
    labs = {}
    for L in TARGETS:
        inst = [r for r in al if r[2] == L]
        if not inst: continue
        c = collections.Counter(r[3] for r in inst)
        rest = [r for r in al if r[2] != L]
        rc = collections.Counter(r[3] for r in rest)
        top = c.most_common(3)
        labs[L] = {'n': len(inst), 'top': top,
                   'spec': {K: round((v/len(inst)) / max(1e-9, rc[K]/max(1, len(rest))), 2) for K, v in top}}
    res[k] = {'lines': sorted(P), 'aligned': len(al), 'keyed_aligned': len(kp), 'G0_exact': round(g0, 3),
              'same_value': round(same_val, 3), 'labels': labs, '_al': al}
# pass-to-pass agreement on Bourdeau positions both aligned
if 'A' in res and 'B' in res:
    a = {(r[0], r[1]): r[3] for r in res['A']['_al']}; b = {(r[0], r[1]): r[3] for r in res['B']['_al']}
    both = set(a) & set(b); agree = sum(a[x] == b[x] for x in both) / max(1, len(both))
    res['AB'] = {'both_aligned': len(both), 'agree': round(agree, 3)}
    g1 = {}
    for L in TARGETS:
        pos = [x for x in both if dict(((r[0], r[1]), r[2]) for r in res['A']['_al'])[x] == L]
        if len(pos) < 4: g1[L] = {'n': len(pos), 'verdict': 'too few (<4)'}; continue
        ca = collections.Counter(a[x] for x in pos); cb = collections.Counter(b[x] for x in pos)
        Ka, na = ca.most_common(1)[0]; Kb, nb = cb.most_common(1)[0]
        ok = Ka == Kb and keyed(Ka) and na/len(pos) >= .6 and nb/len(pos) >= .6 \
            and res['A']['labels'][L]['spec'].get(Ka, 0) >= 3 and res['B']['labels'][L]['spec'].get(Kb, 0) >= 3
        cr = [(crib[x], key.get(Ka)) for x in pos if x in crib]
        g2 = sum(1 for c, v in cr if v and c in v.split('|'))
        g1[L] = {'n': len(pos), 'A_top': [Ka, na], 'B_top': [Kb, nb], 'G1': ok,
                 'G2': f'{g2}/{len(cr)}' if cr else 'no data'}
    res['G1'] = g1
for k in 'AB':
    if k in res: res[k].pop('_al')
print(json.dumps(res, indent=1, ensure_ascii=False))
