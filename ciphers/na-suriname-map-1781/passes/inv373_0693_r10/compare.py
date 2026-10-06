#!/usr/bin/env python3
"""R10-SUR693: test the inv. 373 scan 0692-0693 cipher/gloss pairs against the map key (PREREG.md).
Reads align_words.tsv and ../../key_period_codes_nieuw.tsv (and ../../key.tsv for the C-grade map key); writes
compare.out (summary, gate), sign_table.tsv (per code), candidates_0693.tsv (values this pair suggests). No key edit.
Run from anywhere: python3 compare.py"""
import os, random, collections
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.join(H, '..', '..')
def load(p, ci=1):
    d = {}
    for l in open(p, encoding='utf-8'):
        if l.startswith('#') or l.startswith('code\t') or not l.strip(): continue
        f = l.rstrip('\n').split('\t'); d[f[0]] = (f[ci], f[2] if len(f) > 2 else '')
    return d
nieuw = load(os.path.join(T, 'key_period_codes_nieuw.tsv')); mapc = load(os.path.join(T, 'key.tsv'))
EQ = {'j': 'i', 'y': 'i', 'ij': 'i', 'u': 'v'}
def norm(c): return EQ.get(c, c)
def letters(w):
    out, i = [], 0
    while i < len(w):
        if w[i:i+2] == 'ij': out.append('ij'); i += 2
        else: out.append(w[i]); i += 1
    return out
pairs = []  # (code, letter, rv, line, word)
for l in open(os.path.join(H, 'align_words.tsv'), encoding='utf-8'):
    if l.startswith('#') or l.startswith('line\t'): continue
    f = l.rstrip('\n').split('\t')
    if f[3] != 'aligned': continue
    s, p = f[2].split(), letters(f[1])
    assert len(s) == len(p), (f[1], s)
    pairs += [(c, x, f[4] == '1', f[0], f[1]) for c, x in zip(s, p)]
def agrees(code, letter, key):
    v = key[code][0]
    return any(norm(a) == norm(letter) for a in v.split('|'))
def stat(pp, key=nieuw):
    k = [(c, x) for c, x, *_ in pp if c in key]
    return (sum(agrees(c, x, key) for c, x in k) / len(k) if k else 0.0), len(k)
out = []
for label, pp in (('all aligned', pairs), ('rv=1 rows dropped', [p for p in pairs if not p[2]])):
    real, n = stat(pp)
    rnd = random.Random(693); xs = [p[1] for p in pp]; ctl = []
    for _ in range(1000):
        rnd.shuffle(xs); ctl.append(stat([(p[0], x) for p, x in zip(pp, xs)])[0])
    ctl.sort(); p99 = ctl[989]; mean = sum(ctl) / len(ctl)
    gate = 'SAME SYSTEM' if real >= 0.60 and real > p99 else 'not shown'
    out.append(f'{label}: positions {len(pp)}, keyed in nieuw {n}, agree {real:.3f}; control mean {mean:.3f} p99 {p99:.3f} -> {gate}')
    rm, nm = stat(pp, mapc)
    out.append(f'  vs key.tsv (map C key): keyed {nm}, agree {rm:.3f}')
tab = collections.defaultdict(lambda: collections.Counter())
for c, x, *_ in pairs: tab[c][norm(x) if x != 'ij' else 'i'] += 1
rows = ['code\tnieuw_value\tnieuw_grade\tkeytsv_value\tletters_seen\tagree\tconflict\tverdict']
cands = ['code\tsuggested\tcount\tnieuw_value\tnieuw_grade\tnote']
for c in sorted(tab):
    seen = tab[c]; nv, ng = nieuw.get(c, ('', '')); kv = mapc.get(c, ('', ''))[0]
    a = sum(n for x, n in seen.items() if nv and any(norm(v) == x for v in nv.split('|')))
    tot = sum(seen.values()); conf = tot - a if nv else 0
    verdict = ('unkeyed' if not nv else 'agree' if conf == 0 else 'conflict' if a == 0 else 'mixed')
    rows.append(f"{c}\t{nv}\t{ng}\t{kv}\t{' '.join(f'{x}:{n}' for x, n in seen.most_common())}\t{a}\t{conf}\t{verdict}")
    top, n = seen.most_common(1)[0]
    if verdict in ('unkeyed', 'conflict', 'mixed') or ng == 'M':
        cands.append(f'{c}\t{top}\t{n}\t{nv}\t{ng}\t{verdict}; all: ' + ' '.join(f'{x}:{k}' for x, k in seen.most_common()))
open(os.path.join(H, 'sign_table.tsv'), 'w').write('\n'.join(rows) + '\n')
open(os.path.join(H, 'candidates_0693.tsv'), 'w').write('# candidate values from the 0692-0693 gloss pair, for a verifier; NOT applied to any key\n' + '\n'.join(cands) + '\n')
open(os.path.join(H, 'compare.out'), 'w').write('\n'.join(out) + '\n'); print('\n'.join(out))
