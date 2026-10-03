#!/usr/bin/env python3
"""BIR-ROUND2 (3 Oct 2026, account-3 worker): round-2 lattice on the M tokens, fixed before any crop or score.
Run from this folder: python3 prereg_round2.py -> r2_<leaf>_topk.tsv (new base lattice), r2_<leaf>_lam4.decode.tsv,
r2positions.tsv (hidden truth), r2blind_<leaf>.tsv / r2orient_<leaf>.txt (reader files).
Base per leaf (PREREG-ROUND2.md):
  * the 24 A1-BIR-VERIFY S positions (../verify/exceptions_*.tsv) pinned to their key-implied sign (single candidate);
  * H positions (base conf H: f.117r/f.168 top-1 prior >= 0.85 as build_decode.py; f.144r the committed conf) pinned to top-1;
  * M positions keep the TX-DECODE lattice candidates (the two readers' signs and alts) plus the top-2 confusion_1572.tsv
    partners of the top-1 sign (tools/lookalike_pass.py pairs) where absent, at score 0.03, renormalised, top 5 kept.
tools/key_decode_lattice.py viterbi at lam 4, beam 64 (round 1's settings). Changed positions not already asked in
A1-BIR-EYE / A1-BIR-VERIFY are the round-2 'changed' questions (top-1 vs key-implied). 'mdecoy': unchanged M positions,
not asked before, alt/top-1 ratio >= 0.3, seeded sample (seed 20261005) of the same count (or all if fewer)."""
import csv, random, sys
sys.path.insert(0, '../../../../../../tools'); import key_decode_lattice as K
from judge_plaintext import LANG_CORPORA, NgramModel, read_corpus
H = '../../../'; T = '../../'
KEY = K.read_key(H + 'key_1572_sheet.tsv'); NB = K.read_confusion(H + 'confusion_1572.tsv')
LEAVES = [('f117', 'fr'), ('f168', 'it16dip'), ('f144r', 'it16dip')]; THR = 0.3; ADD = 0.03
rng = random.Random(20261005)
asked = set()
for p in csv.DictReader(open('../positions.tsv'), delimiter='\t'):
    asked.add((p['leaf'], p['passage'], p['pos']))
for p in csv.DictReader(open('../verify/vpositions.tsv'), delimiter='\t'):
    asked.add((p['leaf'], p['passage'], p['pos']))

def base(L):
    lat = K.read_topk(T + L + '_topk.tsv')
    dec = {(r['line'], int(r['pos'])): r for r in csv.DictReader(open(T + L + '_lam4.decode.tsv'), delimiter='\t')}
    pin = {}
    for r in csv.DictReader(open(f'../verify/exceptions_{L}.tsv'), delimiter='\t'):
        pin[(r['line'], int(r['pos']))] = r['reason'].split('->')[1].split(' ')[0]
    if L == 'f144r':
        conf = {(r['line'].split('_', 1)[1], int(r['pos'])): r['conf'] for r in csv.DictReader(open(H + 'ciphertext_f144r.tsv'), delimiter='\t')}
    else:
        conf = {k: ('H' if float(r['prior']) >= 0.85 else 'M') for k, r in dec.items()}
    out, kind = [], {}
    for k, c in lat:
        t1 = max(c.items(), key=lambda kv: kv[1])[0]
        if k in pin:
            out.append((k, {pin[k]: 1.0})); kind[k] = 'S'
        elif conf.get(k, 'M') == 'H':
            out.append((k, {t1: 1.0})); kind[k] = 'H'
        else:
            c2 = dict(c)
            for b, _ in sorted(NB.get(t1, {}).items(), key=lambda kv: -kv[1])[:2]:
                c2.setdefault(b, ADD)
            c2 = dict(sorted(c2.items(), key=lambda kv: -kv[1])[:5]); s = sum(c2.values())
            out.append((k, {a: v / s for a, v in c2.items()})); kind[k] = 'M'
    return out, kind

rows = []
for L, g in LEAVES:
    lat, kind = base(L)
    with open(f'r2_{L}_topk.tsv', 'w') as f:
        f.write('line\tpos\tcand\tscore\tbase\n')
        for k, c in lat:
            for a, v in sorted(c.items(), key=lambda kv: -kv[1]):
                f.write(f'{k[0]}\t{k[1]}\t{a}\t{v:.4f}\t{kind[k]}\n')
    m = NgramModel([read_corpus(p) for p in LANG_CORPORA[g]]); lm = K.LM(m)
    seq, _ = K.viterbi(lat, KEY, lm, 4.0, 64); t1 = K.top1(lat)
    with open(f'r2_{L}_lam4.decode.tsv', 'w') as f:
        f.write('line\tpos\tbase\ttop1\tchosen\tvalue\tprior\tchanged\n')
        for (k, c), a, b in zip(lat, t1, seq):
            f.write(f"{k[0]}\t{k[1]}\t{kind[k]}\t{a}\t{b}\t{KEY.get(b, '?')}\t{c.get(b, 0):.3f}\t{int(a != b)}\n")
    ch = [(k, a, b, c) for (k, c), a, b in zip(lat, t1, seq) if a != b]
    new = [x for x in ch if (L, x[0][0], str(x[0][1])) not in asked]
    pool = []
    for (k, c), a, b in zip(lat, t1, seq):
        if a != b or kind[k] != 'M' or (L, k[0], str(k[1])) in asked:
            continue
        alt = sorted(((v, s) for s, v in c.items() if s != a), reverse=True)
        if alt and alt[0][0] / c[a] >= THR:
            pool.append((k, a, alt[0][1], alt[0][0] / c[a]))
    items = []
    for k, a, b, c in new:
        pair = [a, b]; rng.shuffle(pair)
        items.append(dict(kind='changed', passage=k[0], pos=k[1], A=pair[0], B=pair[1], original=a, other=b,
                          ratio=round(c.get(b, 0) / c[a], 4)))
    for k, a, b, r in rng.sample(pool, min(len(new), len(pool))):
        pair = [a, b]; rng.shuffle(pair)
        items.append(dict(kind='mdecoy', passage=k[0], pos=k[1], A=pair[0], B=pair[1], original=a, other=b, ratio=round(r, 4)))
    rng.shuffle(items)
    for i, it in enumerate(items, 1):
        it.update(leaf=L, qid=f'r{L}-{i:02d}'); rows.append(it)
    print(L, 'M', sum(v == 'M' for v in kind.values()), 'changed', len(ch), 'new', len(new), 'already-asked', len(ch) - len(new),
          'mdecoy', sum(it['kind'] == 'mdecoy' for it in items), 'pool', len(pool))
    q = {(it['passage'], it['pos']): it['qid'] for it in items}
    with open(f'r2blind_{L}.tsv', 'w') as f:
        f.write('qid\tpassage\tpos\tA\tB\n')
        for it in sorted(items, key=lambda it: it['qid']):
            f.write(f"{it['qid']}\t{it['passage']}\t{it['pos']}\t{it['A']}\t{it['B']}\n")
    with open(f'r2orient_{L}.txt', 'w') as f:
        cur = None
        for (k, c), a in zip(lat, t1):
            if k[0] != cur:
                f.write(('\n' if cur else '') + k[0] + ':'); cur = k[0]
            f.write(' ' + (f'[{q[k]}]' if k in q else a))
        f.write('\n')
cols = ['leaf', 'qid', 'kind', 'passage', 'pos', 'A', 'B', 'original', 'other', 'ratio']
with open('r2positions.tsv', 'w') as f:
    w = csv.DictWriter(f, cols, delimiter='\t', extrasaction='ignore'); w.writeheader(); w.writerows(rows)
